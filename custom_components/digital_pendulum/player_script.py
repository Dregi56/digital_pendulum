import logging

from .player_base import BasePlayer

_LOGGER = logging.getLogger(__name__)


class ScriptPlayer(BasePlayer):
    """Player that delegates chimes and announcements to a user script.

    For every chime the script is started with the variable ``chime_url``
    (the sound URL, or an empty string for the default chime); for every
    announcement with ``message`` (the localized text built by Digital
    Pendulum) and ``language``. The script decides how and where to play
    them: several speakers, a TTS engine of choice, a notification
    integration, extra conditions, and so on.

    Use ``mode: queued`` in the script so that chime and announcement are
    always played in order.
    """

    async def play_chime(self, chime_url: str):
        await self._run({"chime_url": chime_url})

    async def play_default_chime(self):
        await self._run({"chime_url": ""})

    async def speak(self, text: str, language: str = "en"):
        await self._run({"message": text, "language": language})

    async def _run(self, variables: dict):
        try:
            # script.turn_on returns as soon as the script has started, so
            # blocking=True does not wait for the script to finish; it only
            # makes errors (e.g. missing script) visible here.
            await self.hass.services.async_call(
                "script",
                "turn_on",
                {"entity_id": self.player, "variables": variables},
                blocking=True,
            )
        except Exception as err:
            _LOGGER.error(
                "Digital Pendulum: error running script '%s': %s",
                self.player,
                err,
            )
