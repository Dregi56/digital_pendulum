from .player_base import BasePlayer

class AlexaPlayer(BasePlayer):
    """Player per dispositivi Alexa tramite alexa_media_player."""

    async def play_default_chime(self):
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

    async def play_chime(self, chime_url: str):
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
            await self.play_default_chime()

    async def speak(self, text: str):
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
