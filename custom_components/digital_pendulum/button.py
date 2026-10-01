from homeassistant.components.button import ButtonEntity
from homeassistant.helpers.entity import EntityCategory

from .const import DOMAIN


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up the Digital Pendulum button."""
    pendulum = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([DigitalPendulumTestButton(pendulum, entry)])


class DigitalPendulumTestButton(ButtonEntity):
    """Pulsante per testare l'annuncio del pendolo."""

    _attr_has_entity_name = True
    _attr_translation_key = "test_announcement"
    _attr_icon = "mdi:bell-ring"
    _attr_entity_category = EntityCategory.DIAGNOSTIC

    def __init__(self, pendulum, entry):
        self.pendulum = pendulum
        self.entry = entry
        self._attr_unique_id = f"{entry.entry_id}_test_button"
        self._attr_device_info = {
            "identifiers": {(DOMAIN, entry.entry_id)},
            "name": "Digital Pendulum",
            "manufacturer": "Custom",
            "model": "Digital Pendulum",
        }

    async def async_press(self):
        """Handle button press."""
        await self.pendulum.async_test_announcement()