"""Tests for the Script player type."""

from homeassistant import config_entries, data_entry_flow
from homeassistant.core import HomeAssistant, ServiceCall
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.digital_pendulum.const import (
    CONF_AFTER_CHIME_DELAY,
    CONF_PLAYER_DEVICE,
    CONF_PLAYER_TYPE,
    DOMAIN,
    PRESET_CHIMES,
)
from custom_components.digital_pendulum.player_script import ScriptPlayer


def _capture_script_calls(hass: HomeAssistant) -> list[dict]:
    calls: list[dict] = []

    async def fake_turn_on(call: ServiceCall) -> None:
        calls.append(dict(call.data))

    hass.services.async_register("script", "turn_on", fake_turn_on)
    return calls


async def _setup_script_entry(hass: HomeAssistant) -> MockConfigEntry:
    entry = MockConfigEntry(
        domain=DOMAIN,
        data={
            CONF_PLAYER_TYPE: "script",
            CONF_PLAYER_DEVICE: "script.clock",
            CONF_AFTER_CHIME_DELAY: 0,
        },
    )
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()
    return entry


async def test_script_player_selected(hass: HomeAssistant) -> None:
    entry = await _setup_script_entry(hass)
    assert isinstance(hass.data[DOMAIN][entry.entry_id]._player, ScriptPlayer)


async def test_chime_then_announcement_run_the_script(hass: HomeAssistant) -> None:
    """The script receives the chime URL first, then the localized text."""
    calls = _capture_script_calls(hass)
    entry = await _setup_script_entry(hass)
    pendulum = hass.data[DOMAIN][entry.entry_id]
    pendulum.language = "it"

    await pendulum._speak(pendulum._build_text(15, 0), 15, 0)

    assert calls == [
        {
            "entity_id": "script.clock",
            "variables": {"chime_url": PRESET_CHIMES["church-bell"]["url"]},
        },
        {
            "entity_id": "script.clock",
            "variables": {"message": "Ore 15", "language": "it"},
        },
    ]


async def test_default_chime_sends_empty_url(hass: HomeAssistant) -> None:
    calls = _capture_script_calls(hass)
    entry = await _setup_script_entry(hass)

    await hass.data[DOMAIN][entry.entry_id]._player.play_default_chime()

    assert calls[0]["variables"] == {"chime_url": ""}


async def test_missing_script_is_logged_not_raised(hass: HomeAssistant, caplog) -> None:
    """Without the script service the error is logged and nothing raises."""
    entry = await _setup_script_entry(hass)

    await hass.data[DOMAIN][entry.entry_id]._player.speak("Ore 15", "it")

    assert "error running script 'script.clock'" in caplog.text


async def _start_user_flow(hass: HomeAssistant, player_type: str, device: str):
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    return await hass.config_entries.flow.async_configure(
        result["flow_id"],
        {CONF_PLAYER_TYPE: player_type, CONF_PLAYER_DEVICE: device},
    )


async def test_config_flow_script_type_requires_script(hass: HomeAssistant) -> None:
    result = await _start_user_flow(hass, "script", "media_player.kitchen")
    assert result["type"] is data_entry_flow.FlowResultType.FORM
    assert result["errors"] == {CONF_PLAYER_DEVICE: "script_required"}


async def test_config_flow_media_type_rejects_script(hass: HomeAssistant) -> None:
    result = await _start_user_flow(hass, "alexa", "script.clock")
    assert result["type"] is data_entry_flow.FlowResultType.FORM
    assert result["errors"] == {CONF_PLAYER_DEVICE: "media_player_required"}


async def test_config_flow_script_type_creates_entry(hass: HomeAssistant) -> None:
    result = await _start_user_flow(hass, "script", "script.clock")
    assert result["type"] is data_entry_flow.FlowResultType.CREATE_ENTRY
    assert result["data"][CONF_PLAYER_TYPE] == "script"
    assert result["data"][CONF_PLAYER_DEVICE] == "script.clock"


async def test_options_flow_validates_player(hass: HomeAssistant) -> None:
    entry = await _setup_script_entry(hass)
    result = await hass.config_entries.options.async_init(entry.entry_id)
    result = await hass.config_entries.options.async_configure(
        result["flow_id"],
        {CONF_PLAYER_TYPE: "script", CONF_PLAYER_DEVICE: "media_player.kitchen"},
    )
    assert result["type"] is data_entry_flow.FlowResultType.FORM
    assert result["errors"] == {CONF_PLAYER_DEVICE: "script_required"}
