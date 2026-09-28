"""Tests for Digital Pendulum setup, service and options handling."""

from unittest.mock import patch

from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers import entity_registry as er
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.digital_pendulum.const import (
    CONF_ENABLED,
    CONF_PLAYER_DEVICE,
    CONF_PLAYER_TYPE,
    DOMAIN,
)
from custom_components.digital_pendulum.pendulum import DigitalPendulum


async def _setup_entry(hass: HomeAssistant, player: str, **extra) -> MockConfigEntry:
    entry = MockConfigEntry(
        domain=DOMAIN,
        title=player,
        data={CONF_PLAYER_TYPE: "alexa", CONF_PLAYER_DEVICE: player, **extra},
    )
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()
    return entry


def _entity_id(hass: HomeAssistant, domain: str, unique_id: str) -> str:
    entity_id = er.async_get(hass).async_get_entity_id(domain, DOMAIN, unique_id)
    assert entity_id is not None
    return entity_id


async def test_service_targets_requested_instance(hass: HomeAssistant) -> None:
    """The test service must announce on the instance owning the given entity."""
    entry_1 = await _setup_entry(hass, "media_player.kitchen")
    await _setup_entry(hass, "media_player.bedroom")
    button_1 = _entity_id(hass, "button", f"{entry_1.entry_id}_test_button")

    with patch.object(
        DigitalPendulum, "async_test_announcement", autospec=True
    ) as mock_test:
        await hass.services.async_call(
            DOMAIN, "test_announcement", {"entity_id": button_1}, blocking=True
        )

    assert [call.args[0].player for call in mock_test.call_args_list] == [
        "media_player.kitchen"
    ]


async def test_service_without_target_announces_on_all(hass: HomeAssistant) -> None:
    """Without entity_id every configured clock is tested."""
    await _setup_entry(hass, "media_player.kitchen")
    await _setup_entry(hass, "media_player.bedroom")

    with patch.object(
        DigitalPendulum, "async_test_announcement", autospec=True
    ) as mock_test:
        await hass.services.async_call(DOMAIN, "test_announcement", {}, blocking=True)

    assert sorted(call.args[0].player for call in mock_test.call_args_list) == [
        "media_player.bedroom",
        "media_player.kitchen",
    ]


async def test_unloading_one_instance_keeps_service(hass: HomeAssistant) -> None:
    """Removing one clock must not remove the service used by the others."""
    await _setup_entry(hass, "media_player.kitchen")
    entry_2 = await _setup_entry(hass, "media_player.bedroom")

    assert await hass.config_entries.async_unload(entry_2.entry_id)
    await hass.async_block_till_done()
    assert hass.services.has_service(DOMAIN, "test_announcement")

    with patch.object(
        DigitalPendulum, "async_test_announcement", autospec=True
    ) as mock_test:
        await hass.services.async_call(DOMAIN, "test_announcement", {}, blocking=True)

    assert [call.args[0].player for call in mock_test.call_args_list] == [
        "media_player.kitchen"
    ]


async def test_options_update_keeps_switch_state(hass: HomeAssistant) -> None:
    """Saving unrelated options must not re-enable a clock switched off."""
    entry = await _setup_entry(hass, "media_player.kitchen", **{CONF_ENABLED: True})
    switch = _entity_id(hass, "switch", f"{entry.entry_id}_enabled")

    await hass.services.async_call(
        "switch", "turn_off", {"entity_id": switch}, blocking=True
    )
    assert hass.states.get(switch).state == "off"

    hass.config_entries.async_update_entry(
        entry, options={**entry.data, "start_hour": 9}
    )
    await hass.async_block_till_done()

    assert hass.data[DOMAIN][entry.entry_id].enabled is False
    assert hass.states.get(switch).state == "off"


async def test_options_enabled_change_updates_switch(hass: HomeAssistant) -> None:
    """Changing 'enabled' in the options is applied and shown by the switch."""
    entry = await _setup_entry(hass, "media_player.kitchen", **{CONF_ENABLED: True})
    switch = _entity_id(hass, "switch", f"{entry.entry_id}_enabled")
    assert hass.states.get(switch).state == "on"

    hass.config_entries.async_update_entry(
        entry, options={**entry.data, CONF_ENABLED: False}
    )
    await hass.async_block_till_done()

    assert hass.data[DOMAIN][entry.entry_id].enabled is False
    assert hass.states.get(switch).state == "off"


async def test_alexa_chime_failure_falls_back_to_default(hass: HomeAssistant) -> None:
    """If the chime call fails, the Alexa player plays the default chime."""
    calls: list[dict] = []

    async def fake_alexa_media(call: ServiceCall) -> None:
        calls.append(dict(call.data))
        if "<audio" in call.data["message"]:
            raise HomeAssistantError("audio not supported")

    hass.services.async_register("notify", "alexa_media", fake_alexa_media)
    entry = await _setup_entry(hass, "media_player.kitchen")
    pendulum = hass.data[DOMAIN][entry.entry_id]

    await pendulum._player.play_chime("https://example.com/chime.mp3")
    await hass.async_block_till_done()

    assert [c["data"]["type"] for c in calls] == ["tts", "announce"]
