import asyncio
from datetime import datetime
from homeassistant.helpers.event import async_track_time_change
from homeassistant.util import dt as dt_util
from .const import (
    CONF_START_HOUR,
    CONF_END_HOUR,
    CONF_PLAYER_DEVICE,
    CONF_PLAYER_TYPE,
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
from .player_alexa import AlexaPlayer
from .player_google import GooglePlayer
from .languages import (
    PL_HOUR_NAMES,
    CS_HOUR_NAMES_EXACT,
    CS_HOUR_NAMES_HALF,
    SK_HOUR_NAMES_EXACT,
    SK_HOUR_NAMES_HALF,
)


def _create_player(hass, player_entity_id: str, player_type: str):
    """Factory: crea il player corretto in base al tipo scelto."""
    if player_type == "google":
        return GooglePlayer(hass, player_entity_id)
    elif player_type == "alexa":
        return AlexaPlayer(hass, player_entity_id)
    else:
        return AlexaPlayer(hass, player_entity_id)


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
        self.announce_half_hours = config.get(CONF_ANNOUNCE_HALF_HOURS, DEFAULT_ANNOUNCE_HALF_HOURS)
        self.voice_announcement = config.get(CONF_VOICE_ANNOUNCEMENT, DEFAULT_VOICE_ANNOUNCEMENT)
        player_type = config.get(CONF_PLAYER_TYPE, "alexa")
        self._player = _create_player(self.hass, self.player, player_type)

    def update_config(self):
        """Update configuration when options change."""
        self._load_config()

    def _normalize_language(self) -> str:
        """Normalize HA language code to 2-char ISO code (e.g. 'en-GB' -> 'en')."""
        lang = self.hass.config.language or "en"
        return lang[:2].lower()

    async def async_start(self):
        """Sincronizza il timer esattamente all'inizio di ogni minuto."""
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
        if minute == 30 and not self.announce_half_hours:
            return
        if hour < self.start_hour or hour > self.end_hour:
            return
        if hour == self.end_hour and minute > 0:
            return
        text = self._build_text(hour, minute)
        await self._speak(text, hour, minute)

    def _build_text(self, hour: int, minute: int) -> str:
        """Build announcement text using translations."""
        language = self._normalize_language()
        translations = self._get_translations(language)

        # --- Tedesco: halb = riferimento all'ora successiva ---
        if language == "de" and minute == 30:
            next_hour = (hour + 1) % 24
            return translations.get("hour_and_half", "Es ist halb {next_hour}").format(next_hour=next_hour)

        # --- Spagnolo: singolare per l'1 e le 13 ---
        if language == "es" and (hour == 1 or hour == 13):
            if minute == 30:
                return "Es la una y media"
            else:
                return "Es la una"

        # --- Italiano ---
        if language == "it":
            hour_text = "una" if hour == 1 else str(hour)
            if minute == 30:
                return f"Ore {hour_text} e trenta"
            else:
                return f"Ore {hour_text}"

        # --- Polacco: wpół do = riferimento all'ora successiva ---
        if language == "pl":
            if minute == 30:
                next_hour = (hour + 1) % 24
                next_name = PL_HOUR_NAMES.get(next_hour, str(next_hour))
                return f"Wpół do {next_name}"
            else:
                return f"Jest {PL_HOUR_NAMES.get(hour, str(hour))}"

        # --- Ceco: půl = riferimento all'ora successiva in genitivo ---
        if language == "cs":
            if minute == 30:
                next_hour = (hour + 1) % 24
                next_name = CS_HOUR_NAMES_HALF.get(next_hour, str(next_hour))
                return f"Půl {next_name}"
            else:
                return f"Je {CS_HOUR_NAMES_EXACT.get(hour, str(hour))}"

        # --- Slovacco: pol = riferimento all'ora successiva in genitivo ---
        if language == "sk":
            if minute == 30:
                next_hour = (hour + 1) % 24
                next_name = SK_HOUR_NAMES_HALF.get(next_hour, str(next_hour))
                return f"Pol {next_name}"
            else:
                return f"Je {SK_HOUR_NAMES_EXACT.get(hour, str(hour))}"

        # --- Tutti gli altri casi (inglese, francese, ecc.) ---
        if minute == 30:
            return translations.get("hour_and_half", "It's {hour} thirty").format(hour=hour)
        else:
            return translations.get("hour", "It's {hour} o'clock").format(hour=hour)

    def _get_translations(self, language: str) -> dict:
        """Get translations for the given language."""
        fallback = {
            "hour": "It's {hour} o'clock",
            "hour_and_half": "It's {hour} thirty",
            "hour_exact": "It's {hour} o'clock exactly",
            "hour_and_minutes": "It's {hour} {minutes}"
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
            },
            "pl": {
                "hour": "Jest {hour}",
                "hour_and_half": "Wpół do {next_hour}",
                "hour_exact": "Jest dokładnie {hour}",
                "hour_and_minutes": "Jest {hour} i {minutes}"
            },
            "cs": {
                "hour": "Je {hour}",
                "hour_and_half": "Půl {next_hour}",
                "hour_exact": "Je přesně {hour}",
                "hour_and_minutes": "Je {hour} a {minutes} minut"
            },
            "sk": {
                "hour": "Je {hour}",
                "hour_and_half": "Pol {next_hour}",
                "hour_exact": "Je presne {hour}",
                "hour_and_minutes": "Je {hour} a {minutes} minút"
            },
        }
        return translations.get(language, fallback)

    async def _play_chime(self, hour: int = None, minute: int = None):
        """Play chime sound."""
        if self.tower_clock and hour == 12 and minute == 0:
            westminster_url = PRESET_CHIMES["westminster"]["url"]
            await self._player.play_chime(westminster_url)
            return
        if self.preset_chime and self.preset_chime != "custom":
            chime_info = PRESET_CHIMES.get(self.preset_chime)
            if chime_info and chime_info["url"]:
                await self._player.play_chime(chime_info["url"])
                return
        elif self.preset_chime == "custom" and self.custom_chime_path and self.custom_chime_path.strip():
            await self._player.play_chime(self.custom_chime_path.strip())
            return
        await self._player.play_default_chime()

    async def _speak(self, text: str, hour: int = None, minute: int = None):
        if self.use_chime:
            await self._play_chime(hour, minute)
            await asyncio.sleep(1.2)
        if self.voice_announcement:
            await self._player.speak(text)

    async def async_test_announcement(self):
        """Test immediato dell'annuncio con orario completo."""
        now = dt_util.now()
        hour = now.hour
        minute = now.minute
        language = self._normalize_language()

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

        elif language == "pl":
            if minute == 0:
                text = f"Jest dokładnie {PL_HOUR_NAMES.get(hour, str(hour))}"
            else:
                text = f"Jest {PL_HOUR_NAMES.get(hour, str(hour))} i {minute:02d}"

        elif language == "cs":
            if minute == 0:
                text = f"Je přesně {CS_HOUR_NAMES_EXACT.get(hour, str(hour))}"
            else:
                text = f"Je {CS_HOUR_NAMES_EXACT.get(hour, str(hour))} a {minute:02d} minut"

        elif language == "sk":
            if minute == 0:
                text = f"Je presne {SK_HOUR_NAMES_EXACT.get(hour, str(hour))}"
            else:
                text = f"Je {SK_HOUR_NAMES_EXACT.get(hour, str(hour))} a {minute:02d} minút"

        else:
            translations = self._get_translations(language)
            if minute == 0:
                text = translations.get("hour_exact", "It's {hour} o'clock exactly").format(hour=hour)
            else:
                text = translations.get("hour_and_minutes", "It's {hour} {minutes}").format(hour=hour, minutes=f"{minute:02d}")

        await self._speak(text)
