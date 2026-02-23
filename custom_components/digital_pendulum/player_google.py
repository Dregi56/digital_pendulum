from .base_player import BasePlayer

class GooglePlayer(BasePlayer):
    """Player per dispositivi Google Home/Assistant."""

    async def play_default_chime(self):
        # Google non ha un sistema di "announce" nativo
        # Usa TTS con un breve silenzio o nulla
        pass

    async def play_chime(self, chime_url: str):
        try:
            await self.hass.services.async_call(
                "media_player",
                "play_media",
                {
                    "entity_id": self.player,
                    "media_content_id": chime_url,
                    "media_content_type": "music",
                },
                blocking=False,
            )
        except Exception:
            await self.play_default_chime()

    async def speak(self, text: str):
        await self.hass.services.async_call(
            "tts",
            "google_translate_say",
            {
                "entity_id": self.player,
                "message": text,
            },
            blocking=False,
        )
