"""Tests for the counted strikes option."""

from pathlib import Path
from unittest.mock import patch

import pytest
from homeassistant.core import HomeAssistant, ServiceCall
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.digital_pendulum.const import (
    CONF_AFTER_CHIME_DELAY,
    CONF_COUNT_STRIKES,
    CONF_PLAYER_DEVICE,
    CONF_PLAYER_TYPE,
    CONF_TOWER_CLOCK,
    DOMAIN,
    PRESET_CHIMES,
    STRIKE_INTERVAL,
    STRIKES_URL,
)
from custom_components.digital_pendulum.pendulum import DigitalPendulum

SOUNDS = Path(__file__).parent.parent / "sounds" / "strikes"
DELAY = 1.2


async def _setup(hass: HomeAssistant, **options) -> tuple[DigitalPendulum, list, list]:
    """Clock with the Script player, recording chime URLs and waits."""
    chimes: list[str] = []

    async def fake_turn_on(call: ServiceCall) -> None:
        variables = call.data["variables"]
        if "chime_url" in variables:
            chimes.append(variables["chime_url"])

    hass.services.async_register("script", "turn_on", fake_turn_on)
    entry = MockConfigEntry(
        domain=DOMAIN,
        data={
            CONF_PLAYER_TYPE: "script",
            CONF_PLAYER_DEVICE: "script.clock",
            CONF_AFTER_CHIME_DELAY: DELAY,
            **options,
        },
    )
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()
    return hass.data[DOMAIN][entry.entry_id], chimes, []


async def _announce(pendulum: DigitalPendulum, hour: int, minute: int, waits: list) -> None:
    async def fake_sleep(seconds: float) -> None:
        waits.append(seconds)

    with patch("custom_components.digital_pendulum.pendulum.asyncio.sleep", fake_sleep):
        await pendulum._speak(pendulum._build_text(hour, minute), hour, minute)


def _strikes(count: int) -> str:
    return STRIKES_URL.format(count=count)


@pytest.mark.parametrize(("hour", "count"), [(0, 12), (1, 1), (3, 3), (12, 12), (13, 1), (15, 3), (23, 11)])
async def test_strikes_on_the_hour(hass: HomeAssistant, hour: int, count: int) -> None:
    pendulum, chimes, waits = await _setup(hass, **{CONF_COUNT_STRIKES: True})
    await _announce(pendulum, hour, 0, waits)
    assert chimes == [_strikes(count)]
    assert waits == [pytest.approx((count - 1) * STRIKE_INTERVAL + DELAY)]


async def test_no_strikes_at_half_past(hass: HomeAssistant) -> None:
    pendulum, chimes, waits = await _setup(hass, **{CONF_COUNT_STRIKES: True})
    await _announce(pendulum, 15, 30, waits)
    assert chimes == [PRESET_CHIMES["church-bell"]["url"]]
    assert waits == [DELAY]


async def test_option_off_keeps_single_chime(hass: HomeAssistant) -> None:
    pendulum, chimes, waits = await _setup(hass)
    await _announce(pendulum, 15, 0, waits)
    assert chimes == [PRESET_CHIMES["church-bell"]["url"]]
    assert waits == [DELAY]


async def test_tower_clock_plays_westminster_then_twelve_strikes(hass: HomeAssistant) -> None:
    pendulum, chimes, waits = await _setup(
        hass, **{CONF_COUNT_STRIKES: True, CONF_TOWER_CLOCK: True}
    )
    await _announce(pendulum, 12, 0, waits)
    assert chimes == [PRESET_CHIMES["westminster"]["url"], _strikes(12)]
    assert waits == [20.0, pytest.approx(11 * STRIKE_INTERVAL + DELAY)]


async def test_tower_clock_without_strikes_is_unchanged(hass: HomeAssistant) -> None:
    pendulum, chimes, waits = await _setup(hass, **{CONF_TOWER_CLOCK: True})
    await _announce(pendulum, 12, 0, waits)
    assert chimes == [PRESET_CHIMES["westminster"]["url"]]
    assert waits == [20.0]


def test_all_strike_files_exist() -> None:
    for count in range(1, 13):
        assert (SOUNDS / f"strike_{count}.mp3").is_file()
        assert STRIKES_URL.format(count=count).endswith(f"sounds/strikes/strike_{count}.mp3")
