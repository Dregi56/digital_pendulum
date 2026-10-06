"""Diagnostics support for Digital Pendulum."""

from __future__ import annotations

from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for a config entry.

    The configuration only holds entity ids, hours and sound choices, so
    there is nothing to redact.
    """
    pendulum = hass.data.get(DOMAIN, {}).get(entry.entry_id)
    diagnostics: dict[str, Any] = {
        "entry": {
            "title": entry.title,
            "version": entry.version,
            "data": dict(entry.data),
            "options": dict(entry.options),
        },
        "ha_language": hass.config.language,
        "time_zone": hass.config.time_zone,
    }
    if pendulum is None:
        diagnostics["runtime"] = "not loaded"
        return diagnostics

    player_state = hass.states.get(pendulum.player) if pendulum.player else None
    diagnostics["runtime"] = {
        "enabled": pendulum.enabled,
        "player_class": type(pendulum._player).__name__,
        "player_entity": pendulum.player,
        "player_state": player_state.state if player_state else None,
        "player_attributes": {
            key: player_state.attributes.get(key)
            for key in ("friendly_name", "supported_features", "volume_level", "device_class")
            if player_state and key in player_state.attributes
        },
        "announcement_language": pendulum._normalize_language(),
        "announcement_style": pendulum.announcement_style,
        "start_hour": pendulum.start_hour,
        "end_hour": pendulum.end_hour,
    }
    return diagnostics
