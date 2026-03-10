from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.helpers import config_validation as cv
from .const import DOMAIN
from .pendulum import DigitalPendulum
from . import config_flow

CONFIG_SCHEMA = cv.config_entry_only_config_schema(DOMAIN)
PLATFORMS = ["switch", "button", "binary_sensor"]

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the Digital Pendulum component."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Digital Pendulum from a config entry."""
    pendulum = DigitalPendulum(hass, entry)
    await pendulum.async_start()
    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = pendulum

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    async def handle_test_announcement(call: ServiceCall):
        """Handle the test announcement service call."""
        await pendulum.async_test_announcement()

    hass.services.async_register(
        DOMAIN,
        "test_announcement",
        handle_test_announcement,
    )

    entry.async_on_unload(entry.add_update_listener(update_listener))
    return True

async def update_listener(hass: HomeAssistant, entry: ConfigEntry):
    """Handle options update."""
    pendulum = hass.data[DOMAIN][entry.entry_id]
    pendulum.update_config()

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    hass.services.async_remove(DOMAIN, "test_announcement")
    await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    pendulum = hass.data[DOMAIN].pop(entry.entry_id)
    await pendulum.async_stop()
    return True



