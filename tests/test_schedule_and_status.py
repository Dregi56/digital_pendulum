"""Tests for the active time range and the status sensor."""

import pytest
from homeassistant.core import HomeAssistant
from homeassistant.helpers import entity_registry as er
from homeassistant.setup import async_setup_component
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.digital_pendulum.const import (
    CONF_END_HOUR,
    CONF_PLAYER_DEVICE,
    CONF_PLAYER_TYPE,
    CONF_START_HOUR,
    DOMAIN,
)
from custom_components.digital_pendulum.pendulum import DigitalPendulum


def _pendulum(hass: HomeAssistant, start: int, end: int) -> DigitalPendulum:
    entry = MockConfigEntry(
        domain=DOMAIN,
        data={
            CONF_PLAYER_TYPE: "alexa",
            CONF_PLAYER_DEVICE: "media_player.x",
            CONF_START_HOUR: start,
            CONF_END_HOUR: end,
        },
    )
    return DigitalPendulum(hass, entry)


@pytest.mark.parametrize(
    ("start", "end", "hour", "minute", "expected"),
    [
        # Same-day range: unchanged behaviour
        (8, 22, 7, 30, False),
        (8, 22, 8, 0, True),
        (8, 22, 15, 30, True),
        (8, 22, 22, 0, True),
        (8, 22, 22, 30, False),
        (8, 22, 23, 0, False),
        # Range across midnight
        (22, 7, 21, 30, False),
        (22, 7, 22, 0, True),
        (22, 7, 23, 30, True),
        (22, 7, 0, 0, True),
        (22, 7, 3, 30, True),
        (22, 7, 7, 0, True),
        (22, 7, 7, 30, False),
        (22, 7, 12, 0, False),
    ],
)
def test_in_active_hours(hass, start, end, hour, minute, expected) -> None:
    assert _pendulum(hass, start, end)._in_active_hours(hour, minute) is expected


async def _setup(hass: HomeAssistant, start: int = 8, end: int = 22) -> MockConfigEntry:
    hass.states.async_set("media_player.x", "idle")
    entry = MockConfigEntry(
        domain=DOMAIN,
        data={
            CONF_PLAYER_TYPE: "alexa",
            CONF_PLAYER_DEVICE: "media_player.x",
            CONF_START_HOUR: start,
            CONF_END_HOUR: end,
        },
    )
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()
    return entry


def _status(hass: HomeAssistant, entry: MockConfigEntry):
    entity_id = er.async_get(hass).async_get_entity_id(
        "binary_sensor", DOMAIN, f"{entry.entry_id}_status_warning"
    )
    return hass.states.get(entity_id)


async def test_switched_off_is_not_a_problem(hass: HomeAssistant) -> None:
    entry = await _setup(hass)
    switch = er.async_get(hass).async_get_entity_id(
        "switch", DOMAIN, f"{entry.entry_id}_enabled"
    )
    await hass.services.async_call("switch", "turn_off", {"entity_id": switch}, blocking=True)
    assert hass.data[DOMAIN][entry.entry_id].enabled is False

    # The sensor is polled: refresh it before reading the state.
    assert await async_setup_component(hass, "homeassistant", {})
    entity_id = _status(hass, entry).entity_id
    await hass.services.async_call(
        "homeassistant", "update_entity", {"entity_id": entity_id}, blocking=True
    )
    state = hass.states.get(entity_id)
    assert state.state == "off"
    assert "Integration disabled" in state.attributes["warnings"]


async def test_overnight_range_is_not_a_problem(hass: HomeAssistant) -> None:
    entry = await _setup(hass, start=22, end=7)
    state = _status(hass, entry)
    assert state.state == "off"


async def test_same_start_and_end_is_a_problem(hass: HomeAssistant) -> None:
    entry = await _setup(hass, start=8, end=8)
    state = _status(hass, entry)
    assert state.state == "on"
    assert "Invalid time range (start == end)" in state.attributes["warnings"]


async def test_unavailable_player_is_a_problem(hass: HomeAssistant) -> None:
    hass.states.async_set("media_player.x", "unavailable")
    entry = MockConfigEntry(
        domain=DOMAIN,
        data={CONF_PLAYER_TYPE: "alexa", CONF_PLAYER_DEVICE: "media_player.x"},
    )
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()
    state = _status(hass, entry)
    assert state.state == "on"
    assert "Player device offline" in state.attributes["warnings"]
