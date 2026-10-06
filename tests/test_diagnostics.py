"""Tests for the diagnostics."""

from homeassistant.core import HomeAssistant
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.digital_pendulum.const import (
    CONF_LANGUAGE,
    CONF_PLAYER_DEVICE,
    CONF_PLAYER_TYPE,
    DOMAIN,
)
from custom_components.digital_pendulum.diagnostics import (
    async_get_config_entry_diagnostics,
)


async def test_diagnostics(hass: HomeAssistant) -> None:
    hass.states.async_set(
        "media_player.kitchen", "idle", {"friendly_name": "Kitchen", "volume_level": 0.4}
    )
    entry = MockConfigEntry(
        domain=DOMAIN,
        title="Digital Pendulum",
        data={
            CONF_PLAYER_TYPE: "alexa",
            CONF_PLAYER_DEVICE: "media_player.kitchen",
            CONF_LANGUAGE: "it",
        },
    )
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    result = await async_get_config_entry_diagnostics(hass, entry)

    assert result["entry"]["data"][CONF_PLAYER_DEVICE] == "media_player.kitchen"
    runtime = result["runtime"]
    assert runtime["player_class"] == "AlexaPlayer"
    assert runtime["player_state"] == "idle"
    assert runtime["player_attributes"] == {"friendly_name": "Kitchen", "volume_level": 0.4}
    assert runtime["announcement_language"] == "it"
    assert runtime["announcement_style"] == "classic"
    assert runtime["enabled"] is True


async def test_diagnostics_entry_not_loaded(hass: HomeAssistant) -> None:
    entry = MockConfigEntry(
        domain=DOMAIN,
        data={CONF_PLAYER_TYPE: "alexa", CONF_PLAYER_DEVICE: "media_player.kitchen"},
    )
    entry.add_to_hass(hass)

    result = await async_get_config_entry_diagnostics(hass, entry)

    assert result["runtime"] == "not loaded"
