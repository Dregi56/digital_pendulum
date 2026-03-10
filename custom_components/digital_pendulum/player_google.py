from .player_base import BasePlayer

class GooglePlayer(BasePlayer):
    async def play_default_chime(self):
        pass

    async def play_chime(self, chime_url: str):
        try:
            await self.hass.services.async_call(
                "media_player",
                "play_media",
                {
                    "entity_id": self.player,
                    "media_content_id": chime_url,
                    "media_content_type": "audio/mp3",
                },
                blocking=True,
            )
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

    async def speak(self, text: str):
        language = self.hass.config.language or "en"
        tts_entity = self._find_tts_entity()

        if tts_entity:
            await self.hass.services.async_call(
                "tts",
                "speak",
                {
                    "entity_id": tts_entity,
                    "media_player_entity_id": self.player,
                    "message": text,
                    "language": language,
                },
                blocking=False,
            )
        else:
            await self.hass.services.async_call(
                "tts",
                "google_translate_say",
                {
                    "entity_id": self.player,
                    "message": text,
                    "language": language,
                },
                blocking=False,
            )
