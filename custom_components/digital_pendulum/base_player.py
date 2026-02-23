from abc import ABC, abstractmethod

class BasePlayer(ABC):
    """Classe base astratta per tutti i player."""

    def __init__(self, hass, player_entity_id):
        self.hass = hass
        self.player = player_entity_id

    @abstractmethod
    async def play_chime(self, chime_url: str):
        """Suona il chime dal URL fornito."""
        pass

    @abstractmethod
    async def play_default_chime(self):
        """Suona il chime di default."""
        pass

    @abstractmethod
    async def speak(self, text: str):
        """Annuncio vocale del testo."""
        pass
