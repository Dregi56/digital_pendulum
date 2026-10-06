"""Tests for the announcement style option in the config and options flows."""

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResultType
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.digital_pendulum.const import (
    CONF_ANNOUNCEMENT_STYLE,
    CONF_PLAYER_DEVICE,
    CONF_PLAYER_TYPE,
    DOMAIN,
)


async def test_user_flow_defaults_to_classic_style(hass: HomeAssistant) -> None:
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    assert result["type"] is FlowResultType.FORM
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        {CONF_PLAYER_TYPE: "alexa", CONF_PLAYER_DEVICE: "media_player.x"},
    )
    assert result["type"] is FlowResultType.CREATE_ENTRY
    assert result["data"][CONF_ANNOUNCEMENT_STYLE] == "classic"


async def test_options_flow_sets_colloquial_style(hass: HomeAssistant) -> None:
    entry = MockConfigEntry(
        domain=DOMAIN,
        data={CONF_PLAYER_TYPE: "alexa", CONF_PLAYER_DEVICE: "media_player.x"},
    )
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    result = await hass.config_entries.options.async_init(entry.entry_id)
    assert result["type"] is FlowResultType.FORM
    result = await hass.config_entries.options.async_configure(
        result["flow_id"],
        {
            CONF_PLAYER_TYPE: "alexa",
            CONF_PLAYER_DEVICE: "media_player.x",
            CONF_ANNOUNCEMENT_STYLE: "colloquial",
        },
    )
    assert result["type"] is FlowResultType.CREATE_ENTRY
    await hass.async_block_till_done()
    assert entry.options[CONF_ANNOUNCEMENT_STYLE] == "colloquial"
    assert hass.data[DOMAIN][entry.entry_id].announcement_style == "colloquial"
