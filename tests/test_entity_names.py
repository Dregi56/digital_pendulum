"""Entity names come from the translations."""

import pytest
from homeassistant.core import HomeAssistant
from homeassistant.helpers import entity_registry as er
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.digital_pendulum.const import (
    CONF_PLAYER_DEVICE,
    CONF_PLAYER_TYPE,
    DOMAIN,
)


@pytest.mark.parametrize(
    ("language", "names"),
    [
        (
            "en",
            {
                "switch": "Digital Pendulum Enabled",
                "button": "Digital Pendulum Test Announcement",
                "binary_sensor": "Digital Pendulum Status Warning",
            },
        ),
        (
            "it",
            {
                "switch": "Digital Pendulum Abilitato",
                "button": "Digital Pendulum Test Annuncio",
                "binary_sensor": "Digital Pendulum Avviso Stato",
            },
        ),
    ],
)
async def test_entity_names_are_translated(hass: HomeAssistant, language, names) -> None:
    hass.config.language = language
    entry = MockConfigEntry(
        domain=DOMAIN,
        data={CONF_PLAYER_TYPE: "alexa", CONF_PLAYER_DEVICE: "media_player.x"},
    )
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    registry = er.async_get(hass)
    unique_ids = {
        "switch": f"{entry.entry_id}_enabled",
        "button": f"{entry.entry_id}_test_button",
        "binary_sensor": f"{entry.entry_id}_status_warning",
    }
    for domain, unique_id in unique_ids.items():
        entity_id = registry.async_get_entity_id(domain, DOMAIN, unique_id)
        assert hass.states.get(entity_id).attributes["friendly_name"] == names[domain]
