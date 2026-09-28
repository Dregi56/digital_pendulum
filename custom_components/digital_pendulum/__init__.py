import voluptuous as vol

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import ATTR_ENTITY_ID
from homeassistant.core import HomeAssistant, ServiceCall, callback
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers import entity_registry as er
from .const import DOMAIN
from .pendulum import DigitalPendulum
from . import config_flow

CONFIG_SCHEMA = cv.config_entry_only_config_schema(DOMAIN)
PLATFORMS = ["switch", "button", "binary_sensor"]

SERVICE_TEST_ANNOUNCEMENT = "test_announcement"
SERVICE_TEST_ANNOUNCEMENT_SCHEMA = vol.Schema(
    {vol.Optional(ATTR_ENTITY_ID): cv.entity_ids}
)


@callback
def _resolve_pendulums(hass: HomeAssistant, entity_ids: list[str] | None) -> list[DigitalPendulum]:
    """Return the pendulums targeted by a service call.

    Without entity_id every loaded pendulum is returned; otherwise only the
    pendulums owning the given entities (switch, button or binary_sensor).
    """
    pendulums: dict[str, DigitalPendulum] = hass.data.get(DOMAIN, {})
    if not entity_ids:
        return list(pendulums.values())

    registry = er.async_get(hass)
    selected: dict[str, DigitalPendulum] = {}
    for entity_id in entity_ids:
        entity = registry.async_get(entity_id)
        if entity is None or entity.config_entry_id not in pendulums:
            continue
        selected[entity.config_entry_id] = pendulums[entity.config_entry_id]
    return list(selected.values())


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the Digital Pendulum component."""
    hass.data.setdefault(DOMAIN, {})

    async def handle_test_announcement(call: ServiceCall):
        """Handle the test announcement service call."""
        for pendulum in _resolve_pendulums(hass, call.data.get(ATTR_ENTITY_ID)):
            await pendulum.async_test_announcement()

    # Registered once for the whole integration, so that several clocks
    # (one per speaker) can coexist and unloading one does not remove it.
    hass.services.async_register(
        DOMAIN,
        SERVICE_TEST_ANNOUNCEMENT,
        handle_test_announcement,
        schema=SERVICE_TEST_ANNOUNCEMENT_SCHEMA,
    )
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Digital Pendulum from a config entry."""
    pendulum = DigitalPendulum(hass, entry)
    await pendulum.async_start()
    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = pendulum

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    entry.async_on_unload(entry.add_update_listener(update_listener))
    return True

async def update_listener(hass: HomeAssistant, entry: ConfigEntry):
    """Handle options update."""
    pendulum = hass.data[DOMAIN][entry.entry_id]
    pendulum.update_config()

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        pendulum = hass.data[DOMAIN].pop(entry.entry_id)
        await pendulum.async_stop()
    return unload_ok
