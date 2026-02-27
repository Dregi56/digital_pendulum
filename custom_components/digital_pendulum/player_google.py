from .player_base import BasePlayer

class GooglePlayer(BasePlayer):
    """
    Player per dispositivi Google Home / Nest / Chromecast.
    Usa Google Cast (integrazione nativa HA).
    """

    async def play_default_chime(self):
        """Google Cast non ha un announce nativo, non fa nulla."""
        pass

    async def play_chime(self, chime_url: str):
        """Riproduce audio tramite media_player standard."""
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

    async def speak(self, text: str):
        """TTS universale - funziona con qualsiasi motore TTS configurato in HA."""
        await self.hass.services.async_call(
            "tts",
            "speak",
            {
                "media_player_entity_id": self.player,
                "message": text,
                "language": self.hass.config.language,
            },
            blocking=False,
        )
