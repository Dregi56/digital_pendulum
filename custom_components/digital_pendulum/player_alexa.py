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
            blocking=True,
        )

    async def play_chime(self, chime_url: str):
        # blocking=True is required for the fallback below to work: with
        # blocking=False the error is raised later inside the HA core, after
        # this except clause has already exited (same as GooglePlayer).
        try:
            await self.hass.services.async_call(
                "notify",
                "alexa_media",
                {
                    "target": self.player,
                    "message": f"<audio src='{chime_url}'/>",
                    "data": {"type": "tts"},
                },
                blocking=True,
            )
        except Exception:
            await self.play_default_chime()

    async def speak(self, text: str, language: str = "en"):
        """Alexa usa la lingua del dispositivo fisico, il parametro language viene ignorato."""
        await self.hass.services.async_call(
            "notify",
            "alexa_media",
            {
                "target": self.player,
                "message": text,
                "data": {"type": "tts"},
            },
            blocking=True,
        )
