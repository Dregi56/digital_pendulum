from homeassistant.components.binary_sensor import (
    BinarySensorEntity,
    BinarySensorDeviceClass,
)
from homeassistant.helpers.entity import EntityCategory
from .const import DOMAIN


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up the Digital Pendulum binary sensor."""
    pendulum = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([DigitalPendulumStatusSensor(pendulum, entry)])


class DigitalPendulumStatusSensor(BinarySensorEntity):
    """Binary sensor che mostra problemi di configurazione o stato."""
    
    _attr_has_entity_name = True
    _attr_name = "Status Warning"
    _attr_device_class = BinarySensorDeviceClass.PROBLEM
    _attr_entity_category = EntityCategory.DIAGNOSTIC

    def __init__(self, pendulum, entry):
        self.pendulum = pendulum
        self.entry = entry
        self._attr_unique_id = f"{entry.entry_id}_status_warning"
        self._attr_device_info = {
            "identifiers": {(DOMAIN, entry.entry_id)},
            "name": "Digital Pendulum",
            "manufacturer": "Custom",
            "model": "Digital Pendulum",
        }

    @property
    def is_on(self):
        """Return True if there are actual problems."""
        # Switching the clock off is a user choice, not a problem: it is
        # still reported in the attributes ("Integration disabled").

        # Problema 1: player non disponibile
        player_state = self.hass.states.get(self.pendulum.player)
        if not player_state or player_state.state == "unavailable":
            return True
        
        # Problema 2: orari configurati male. start > end is a valid range
        # across midnight (e.g. 22 -> 7); only start == end is ambiguous.
        if self.pendulum.start_hour == self.pendulum.end_hour:
            return True
        
        # Nessun problema
        return False

    @property
    def icon(self):
        """Return icon based on state."""
        if self.is_on:  # Problema rilevato
            return "mdi:alert-circle"
        return "mdi:check-circle"

    @property
    def extra_state_attributes(self):
        """Return warnings and diagnostic info."""
        warnings = []
        
        # Controlla integrazione
        if not self.pendulum.enabled:
            warnings.append("Integration disabled")
        
        # Controlla player
        player_state = self.hass.states.get(self.pendulum.player)
        if not player_state:
            warnings.append("Player device not found")
        elif player_state.state == "unavailable":
            warnings.append("Player device offline")
        
        # Controlla orari
        if self.pendulum.start_hour == self.pendulum.end_hour:
            warnings.append("Invalid time range (start == end)")
        
        return {
            "warnings": warnings if warnings else ["No issues"],
            "integration_enabled": self.pendulum.enabled,
            "player_available": player_state.state if player_state else "unknown",
            "start_hour": self.pendulum.start_hour,
            "end_hour": self.pendulum.end_hour,
        }
