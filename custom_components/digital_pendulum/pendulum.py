import asyncio
import os
from datetime import datetime, timedelta
from homeassistant.helpers.event import async_track_time_change
from homeassistant.util import dt as dt_util
from .const import (
    CONF_START_HOUR,
    CONF_END_HOUR,
    CONF_PLAYER_DEVICE,
    CONF_ENABLED,
    CONF_USE_CHIME,
    CONF_CUSTOM_CHIME_PATH,
    CONF_PRESET_CHIME,
    CONF_TOWER_CLOCK,
    CONF_ANNOUNCE_HALF_HOURS,
    CONF_VOICE_ANNOUNCEMENT,
    DEFAULT_START_HOUR,
    DEFAULT_END_HOUR,
    DEFAULT_ENABLED,
    DEFAULT_USE_CHIME,
    DEFAULT_CUSTOM_CHIME_PATH,
    DEFAULT_PRESET_CHIME,
    DEFAULT_TOWER_CLOCK,
    DEFAULT_ANNOUNCE_HALF_HOURS,
    DEFAULT_VOICE_ANNOUNCEMENT,
    PRESET_CHIMES,
    DOMAIN, 
)


class DigitalPendulum:
    def __init__(self, hass, entry):
        self.hass = hass
        self.entry = entry
        self._unsub_timer = None
        self._load_config()

    def _load_config(self):
        """Load configuration from entry (options or data)."""
        config = self.entry.options or self.entry.data
        
        self.start_hour = config.get(CONF_START_HOUR, DEFAULT_START_HOUR)
        self.end_hour = config.get(CONF_END_HOUR, DEFAULT_END_HOUR)
        self.player = config.get(CONF_PLAYER_DEVICE)
        self.enabled = config.get(CONF_ENABLED, DEFAULT_ENABLED)
        self.use_chime = config.get(CONF_USE_CHIME, DEFAULT_USE_CHIME)
        self.preset_chime = config.get(CONF_PRESET_CHIME, DEFAULT_PRESET_CHIME)
        self.custom_chime_path = config.get(CONF_CUSTOM_CHIME_PATH, DEFAULT_CUSTOM_CHIME_PATH)
        self.tower_clock = config.get(CONF_TOWER_CLOCK, DEFAULT_TOWER_CLOCK)
        # NUOVE OPZIONI
        self.announce_half_hours = config.get(CONF_ANNOUNCE_HALF_HOURS, DEFAULT_ANNOUNCE_HALF_HOURS)
        self.voice_announcement = config.get(CONF_VOICE_ANNOUNCEMENT, DEFAULT_VOICE_ANNOUNCEMENT)

    def update_config(self):
        """Update configuration when options change."""
        self._load_config()

    async def async_start(self):
        # Sincronizza il timer esattamente all'inizio di ogni minuto (secondo=0)
        self._unsub_timer = async_track_time_change(
            self.hass,
            self._time_tick,
            second=0,
        )

    async def async_stop(self):
        if self._unsub_timer:
            self._unsub_timer()
            self._unsub_timer = None

    async def _time_tick(self, now: datetime):
        if not self.enabled:
            return
        
        local_time = dt_util.as_local(now)
        
        hour = local_time.hour
        minute = local_time.minute
        
        if minute not in (0, 30):
            return
        
        # NUOVA LOGICA: Salta le mezz'ore se disabilitate
        if minute == 30 and not self.announce_half_hours:
            return
        
        # Controllo orario migliorato: se siamo all'ora di fine, accetta solo i minuti :00
        if hour < self.start_hour or hour > self.end_hour:
            return
        if hour == self.end_hour and minute > 0:
            return
        
        text = self._build_text(hour, minute)
        await self._speak(text, hour, minute)

    def _build_text(self, hour: int, minute: int) -> str:
        """Build announcement text using translations."""
        language = self.hass.config.language
        translations = self._get_translations(language)
        
        # Gestione speciale per tedesco (halb = mezza)
        if language == "de" and minute == 30:
            next_hour = (hour + 1) % 24
            return translations.get("hour_and_half", "Es ist halb {next_hour}").format(next_hour=next_hour)
        
        # Gestione speciale per spagnolo (singolare per l'1)
        if language == "es" and (hour == 1 or hour == 13):
            if minute == 30:
                return "Es la una y media"
            else:
                return "Es la una"
        
        # Gestione speciale per italiano: converti solo 1 in "una"
        if language == "it":
            hour_text = "una" if hour == 1 else str(hour)
            if minute == 30:
                return f"Ore {hour_text} e trenta"
            else:
                return f"Ore {hour_text}"
        
        # Tutti gli altri casi (inglese, francese, ecc.)
        if minute == 30:
            return translations.get("hour_and_half", f"Ore {hour} e trenta").format(hour=hour)
        else:
            return translations.get("hour", f"Ore {hour}").format(hour=hour)

    def _get_translations(self, language: str) -> dict:
        """Get translations for the given language."""
        fallback = {
            "hour": "Ore {hour}",
            "hour_and_half": "Ore {hour} e trenta",
            "hour_exact": "Ore {hour} in punto",
            "hour_and_minutes": "Ore {hour} e {minutes}"
        }
        
        translations = {
            "it": {
                "hour": "Ore {hour}",
                "hour_and_half": "Ore {hour} e trenta",
                "hour_exact": "Ore {hour} in punto",
                "hour_and_minutes": "Ore {hour} e {minutes}"
            },
            "en": {
                "hour": "It's {hour} o'clock",
                "hour_and_half": "It's {hour} thirty",
                "hour_exact": "It's {hour} o'clock exactly",
                "hour_and_minutes": "It's {hour} {minutes}"
            },
            "fr": {
                "hour": "Il est {hour} heures",
                "hour_and_half": "Il est {hour} heures trente",
                "hour_exact": "Il est {hour} heures pile",
                "hour_and_minutes": "Il est {hour} heures {minutes}"
            },
            "de": {
                "hour": "Es ist {hour} Uhr",
                "hour_and_half": "Es ist halb {next_hour}",
                "hour_exact": "Es ist genau {hour} Uhr",
                "hour_and_minutes": "Es ist {hour} Uhr {minutes}"
            },
            "es": {
                "hour": "Son las {hour}",
                "hour_and_half": "Son las {hour} y media",
                "hour_exact": "Son las {hour} en punto",
                "hour_and_minutes": "Son las {hour} y {minutes}"
            }
        }
        
        return translations.get(language, fallback)

    async def _play_chime(self, hour: int = None, minute: int = None):
        """Play chime sound (custom, default, or Westminster for tower clock)."""
        # Se tower_clock è attivo e sono le 12:00, suona Westminster
        if self.tower_clock and hour == 12 and minute == 0:
            await self._play_westminster()
            return
        
        # Altrimenti comportamento normale
        # Determina se usare suono personalizzato o default
        if self.preset_chime or self.custom_chime_path:
            await self._play_custom_chime()
        else:
            await self._play_default_chime()

    async def _play_default_chime(self):
        """Play default announce chime."""
        await self.hass.services.async_call(
            "notify",
            "alexa_media",
            {
                "target": self.player,
                "data": {"type": "announce"},
                "message": " ",
            },
            blocking=False,
        )

    async def _play_westminster(self):
        """Play Westminster chime for tower clock at 12:00."""
        westminster_url = "https://raw.githubusercontent.com/Dregi56/digital_pendulum/main/sounds/westminster.mp3"
        
        try:
            await self.hass.services.async_call(
                "notify",
                "alexa_media",
                {
                    "target": self.player,
                    "message": f"<audio src='{westminster_url}'/>",
                    "data": {"type": "tts"},
                },
                blocking=False,
            )
        except Exception:
            # Se fallisce, usa suono default
            await self._play_default_chime()

    async def _play_custom_chime(self):
        """Play custom audio file or preset chime."""
        
        # Determina quale URL usare
        chime_url = None
        
        # Se ha selezionato un preset (non "custom")
        if self.preset_chime and self.preset_chime != "custom":
            chime_info = PRESET_CHIMES.get(self.preset_chime)
            if chime_info and chime_info["url"]:
                chime_url = chime_info["url"]
        
        # Altrimenti usa custom path se "custom" è selezionato
        elif self.preset_chime == "custom" and self.custom_chime_path and self.custom_chime_path.strip():
            chime_url = self.custom_chime_path.strip()
        
        # Se non ha URL valido, usa default
        if not chime_url:
            await self._play_default_chime()
            return
        
        # Riproduci tramite TTS con SSML (come nel tuo script)
        try:
            await self.hass.services.async_call(
                "notify",
                "alexa_media",
                {
                    "target": self.player,
                    "message": f"<audio src='{chime_url}'/>",
                    "data": {"type": "tts"},
                },
                blocking=False,
            )
        except Exception:
            # Se fallisce, usa suono default
            await self._play_default_chime()

    async def _speak(self, text: str, hour: int = None, minute: int = None):
        if self.use_chime:
            await self._play_chime(hour, minute)
            await asyncio.sleep(1.2)
        
        # NUOVA LOGICA: Annuncio vocale solo se abilitato
        if self.voice_announcement:
            await self.hass.services.async_call(
                "notify",
                "alexa_media",
                {
                    "target": self.player,
                    "message": text,
                    "data": {"type": "tts"},
                },
                blocking=False,
            )

    async def async_test_announcement(self):
        """Test immediato dell'annuncio con orario completo."""
        now = dt_util.now()
        hour = now.hour
        minute = now.minute
        
        language = self.hass.config.language
        
        if language == "it":
            hour_text = "una" if hour == 1 else str(hour)
            if minute == 0:
                text = f"Ore {hour_text} in punto"
            else:
                text = f"Ore {hour_text} e {minute:02d}"
        elif language == "es" and (hour == 1 or hour == 13):
            if minute == 0:
                text = "Es la una en punto"
            else:
                text = f"Es la una y {minute:02d}"
        else:
            translations = self._get_translations(language)
            if minute == 0:
                text = translations.get("hour_exact", f"Ore {hour} in punto").format(hour=hour)
            else:
                text = translations.get("hour_and_minutes", f"Ore {hour} e {minute:02d}").format(hour=hour, minutes=f"{minute:02d}")
        
        await self._speak(text)
