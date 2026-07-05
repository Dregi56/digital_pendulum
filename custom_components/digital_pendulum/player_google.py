import logging
import voluptuous as vol
from .player_base import BasePlayer

_LOGGER = logging.getLogger(__name__)
DEFAULT_TTS_LANGUAGE = "en"
CLOUD_TTS_LANGUAGE_MAP = {
    "en": "en-US",
    "it": "it-IT",
    "de": "de-DE",
    "es": "es-ES",
    "fr": "fr-FR",
    "pt": "pt-PT",
    "pl": "pl-PL",
    "cs": "cs-CZ",
    "sk": "sk-SK",
}


class GooglePlayer(BasePlayer):
    def _tts_language_for_service(self, tts_entity: str | None, language: str) -> str | None:
        is_cloud_tts = tts_entity == "tts.home_assistant_cloud"
        if language == "auto":
            if is_cloud_tts:
                return None
            hass_lang = self.hass.config.language or DEFAULT_TTS_LANGUAGE
            return hass_lang[:2].lower()
        if is_cloud_tts:
            return CLOUD_TTS_LANGUAGE_MAP.get(language, language)
        return language

    async def play_default_chime(self):
        pass

    async def play_chime(self, chime_url: str):
        base_data = {
            "entity_id": self.player,
            "media_content_id": chime_url,
            "media_content_type": "audio/mp3",
        }
        try:
            # Alcuni media_player (es. Google Cast/Sonos) supportano "announce"
            # per non interrompere la riproduzione in corso. Non tutte le
            # integrazioni (es. Apple TV/HomePod) lo accettano: in quel caso
            # voluptuous solleva MultipleInvalid e ripieghiamo senza il flag.
            await self.hass.services.async_call(
                "media_player",
                "play_media",
                {**base_data, "announce": True},
                blocking=True,
            )
        except vol.Invalid:
            _LOGGER.debug(
                "Digital Pendulum: 'announce' non supportato da '%s', ritento senza",
                self.player,
            )
            try:
                await self.hass.services.async_call(
                    "media_player",
                    "play_media",
                    base_data,
                    blocking=True,
                )
            except Exception:
                await self.play_default_chime()
        except Exception:
            await self.play_default_chime()

    def _find_tts_entity(self) -> str | None:
        preferred = [
            "tts.home_assistant_cloud",
            "tts.google_translate_en_com",
            "tts.google_translate",
        ]
        for entity_id in preferred:
            if self.hass.states.get(entity_id) is not None:
                return entity_id
        for state in self.hass.states.async_all("tts"):
            return state.entity_id
        return None

    async def speak(self, text: str, language: str = DEFAULT_TTS_LANGUAGE):
        """Annuncio vocale nella lingua specificata."""
        tts_entity = self._find_tts_entity()
        service_language = self._tts_language_for_service(tts_entity, language)
        if tts_entity:
            base_data = {
                "entity_id": tts_entity,
                "media_player_entity_id": self.player,
                "message": text,
            }
            if service_language:
                base_data["language"] = service_language
            try:
                await self.hass.services.async_call(
                    "tts",
                    "speak",
                    {**base_data, "announce": True},
                    blocking=False,
                )
            except vol.Invalid:
                _LOGGER.debug(
                    "Digital Pendulum: 'announce' non supportato da '%s', ritento senza",
                    self.player,
                )
                await self.hass.services.async_call(
                    "tts",
                    "speak",
                    base_data,
                    blocking=False,
                )
        else:
            await self.hass.services.async_call(
                "tts",
                "google_translate_say",
                {
                    "entity_id": self.player,
                    "message": text,
                    "language": service_language,
                },
                blocking=False,
            )
