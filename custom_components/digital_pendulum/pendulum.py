import asyncio
from datetime import datetime
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
)

# ==========================================================
# 🔥 VOLUME TEMPORANEO TEST (0.0 → 1.0)
# ==========================================================
TEST_TTS_VOLUME = 0.7
# ==========================================================


class DigitalPendulum:
    def __init__(self, hass, entry):
        self.hass = hass
        self.entry = entry
        self._unsub_timer = None
        self._load_config()

    def _load_config(self):
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

        # 🔥 Volume temporaneo (test)
        self.tts_volume = TEST_TTS_VOLUME
        if self.tts_volume is not None:
            self.tts_volume = max(0.0, min(1.0, float(self.tts_volume)))

    def update_config(self):
        self._load_config()

    async def async_start(self):
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
        language = self.hass.config.language

        if language == "it":
            hour_text = "una" if hour == 1 else str(hour)
            if minute == 0:
                return f"Ore {hour_text}"
            return f"Ore {hour_text} e trenta"

        if minute == 30:
            return f"It's {hour} thirty"
        return f"It's {hour} o'clock"

    async def _play_chime(self, hour: int = None, minute: int = None):
        await self.hass.services.async_call(
            "notify",
            "alexa_media",
            {
                "target": [self.player],
                "data": {"type": "announce"},
                "message": " ",
            },
            blocking=False,
        )

    async def _speak(self, text: str, hour: int = None, minute: int = None):
        if self.use_chime:
            await self._play_chime(hour, minute)
            await asyncio.sleep(1.2)

        if not self.voice_announcement:
            return

        data_payload = {
            "type": "tts",
        }

        # 🔥 Volume temporaneo senza beep
        if self.tts_volume is not None:
            data_payload["volume"] = self.tts_volume

        # Garantiamo che target sia lista
        targets = [self.player] if isinstance(self.player, str) else self.player

        await self.hass.services.async_call(
            "notify",
            "alexa_media",
            {
                "target": targets,
                "message": text,
                "data": data_payload,
            },
            blocking=False,
        )

    async def async_test_announcement(self):
        now = dt_util.now()
        hour = now.hour
        minute = now.minute
        text = f"Ora sono le {hour}:{minute:02d}"
        await self._speak(text)




