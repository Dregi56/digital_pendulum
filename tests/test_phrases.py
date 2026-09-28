"""Tests for the announcement phrases."""

import pytest
from homeassistant.core import HomeAssistant
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.digital_pendulum.const import (
    CONF_LANGUAGE,
    CONF_PLAYER_DEVICE,
    CONF_PLAYER_TYPE,
    DOMAIN,
)
from custom_components.digital_pendulum.pendulum import DigitalPendulum


@pytest.fixture
def pendulum(hass: HomeAssistant) -> DigitalPendulum:
    entry = MockConfigEntry(
        domain=DOMAIN,
        data={CONF_PLAYER_TYPE: "alexa", CONF_PLAYER_DEVICE: "media_player.x"},
    )
    return DigitalPendulum(hass, entry)


@pytest.mark.parametrize(
    ("language", "hour", "minute", "expected"),
    [
        # Italian: midnight, noon and one o'clock
        ("it", 0, 0, "È mezzanotte"),
        ("it", 0, 30, "Mezzanotte e trenta"),
        ("it", 12, 0, "È mezzogiorno"),
        ("it", 12, 30, "Mezzogiorno e trenta"),
        ("it", 1, 0, "È l'una"),
        ("it", 1, 30, "L'una e trenta"),
        ("it", 13, 0, "Ore 13"),
        ("it", 15, 30, "Ore 15 e trenta"),
        # Spanish: half past twelve
        ("es", 12, 30, "Son las doce y media"),
        ("es", 0, 30, "Son las doce y media"),
        ("es", 12, 0, "Es mediodía"),
        ("es", 13, 30, "Es la una y media"),
        ("es", 15, 0, "Son las 3"),
        # Portuguese: singular/plural agreement
        ("pt", 12, 30, "É meio-dia e meia"),
        ("pt", 1, 30, "É uma e meia"),
        ("pt", 10, 30, "São 10 e meia"),
        ("pt", 15, 30, "São 15 e meia"),
        ("pt", 1, 0, "É uma hora"),
        ("pt", 15, 0, "São 15 horas"),
        # English: noon and midnight
        ("en", 12, 0, "It's noon"),
        ("en", 0, 0, "It's midnight"),
        ("en", 12, 30, "It's 12 thirty in the afternoon"),
        ("en", 14, 0, "It's 2 o'clock in the afternoon"),
        # French: one o'clock is singular
        ("fr", 1, 0, "Il est une heure"),
        ("fr", 1, 30, "Il est une heure et demie"),
        ("fr", 13, 0, "Il est 13 heures"),
        ("fr", 12, 30, "Il est midi et demi"),
        # Unchanged languages keep their phrases
        ("de", 16, 30, "Es ist halb fünf"),
        ("de", 16, 0, "Es ist 16 Uhr"),
    ],
)
def test_build_text(pendulum, language, hour, minute, expected) -> None:
    pendulum.language = language
    assert pendulum._build_text(hour, minute) == expected


@pytest.mark.parametrize(
    ("language", "hour", "minute", "expected"),
    [
        ("it", 15, 7, "Ore 15 e 7"),
        ("it", 0, 5, "Mezzanotte e 5"),
        ("it", 1, 20, "L'una e 20"),
        ("es", 12, 5, "Son las doce y 5"),
        ("es", 13, 5, "Es la una y 5"),
        ("pt", 12, 5, "É meio-dia e 5"),
        ("pt", 10, 5, "São 10 e 5"),
        ("fr", 1, 5, "Il est une heure 5"),
        ("fr", 15, 5, "Il est 15 heures 5"),
        ("de", 15, 5, "Es ist 15 Uhr 5"),
        ("en", 15, 5, "It's 3:05 in the afternoon"),
    ],
)
def test_build_text_with_minutes(pendulum, language, hour, minute, expected) -> None:
    pendulum.language = language
    assert pendulum._build_text_with_minutes(hour, minute) == expected
