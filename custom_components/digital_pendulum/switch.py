from homeassistant.components.switch import SwitchEntity
from homeassistant.helpers.entity import EntityCategory
from homeassistant.helpers.restore_state import RestoreEntity

from .const import DOMAIN


async def async_setup_entry(hass, entry, async_add_entities):
    pendulum = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([DigitalPendulumSwitch(pendulum, entry)])


class DigitalPendulumSwitch(SwitchEntity, RestoreEntity):
    """Switch per abilitare/disabilitare il pendolo digitale."""

    _attr_has_entity_name = True
    _attr_name = "Enabled"
    _attr_icon = "mdi:clock-outline"
    _attr_entity_category = EntityCategory.CONFIG

    def __init__(self, pendulum, entry):
        self.pendulum = pendulum
        self.entry = entry
        self._attr_unique_id = f"{entry.entry_id}_enabled"
        self._attr_device_info = {
            "identifiers": {(DOMAIN, entry.entry_id)},
            "name": "Digital Pendulum",
            "manufacturer": "Custom",
            "model": "Digital Pendulum",
        }

    async def async_added_to_hass(self):
        """Ripristina lo stato precedente."""
        await super().async_added_to_hass()
        last_state = await self.async_get_last_state()
        if last_state is not None:
            self.pendulum.enabled = last_state.state == "on"
        self.async_on_remove(
            self.pendulum.async_add_listener(self.async_write_ha_state)
        )

    @property
    def is_on(self):
        return self.pendulum.enabled

    async def async_turn_on(self, **kwargs):
        self.pendulum.enabled = True
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs):
        self.pendulum.enabled = False
        self.async_write_ha_state()