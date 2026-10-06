"""Tests for the announcement phrases."""

import pytest
from homeassistant.core import HomeAssistant
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.digital_pendulum.const import (
    ANNOUNCEMENT_STYLE_CLASSIC,
    ANNOUNCEMENT_STYLE_COLLOQUIAL,
    CONF_ANNOUNCEMENT_STYLE,
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
        # Italian, classic style (default): unchanged
        ("it", 0, 0, "Ore 0"),
        ("it", 12, 0, "Ore 12"),
        ("it", 1, 0, "Ore una"),
        ("it", 1, 30, "Ore una e trenta"),
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
        ("it", 1, 20, "Ore una e 20"),
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


@pytest.mark.parametrize(
    ("hour", "minute", "expected"),
    [
        (0, 0, "È mezzanotte"),
        (0, 30, "È mezzanotte e mezza"),
        (12, 0, "È mezzogiorno"),
        (12, 30, "È mezzogiorno e mezza"),
        (1, 0, "È l'una"),
        (13, 30, "È l'una e mezza"),
        (3, 0, "Sono le 3"),
        (15, 30, "Sono le 3 e mezza"),
        (23, 0, "Sono le 11"),
    ],
)
def test_build_text_italian_colloquial(pendulum, hour, minute, expected) -> None:
    pendulum.language = "it"
    pendulum.announcement_style = ANNOUNCEMENT_STYLE_COLLOQUIAL
    assert pendulum._build_text(hour, minute) == expected


@pytest.mark.parametrize(
    ("hour", "minute", "expected"),
    [
        (15, 7, "Sono le 3 e 7"),
        (0, 5, "È mezzanotte e 5"),
        (13, 20, "È l'una e 20"),
        (12, 45, "È mezzogiorno e 45"),
    ],
)
def test_build_text_with_minutes_italian_colloquial(pendulum, hour, minute, expected) -> None:
    pendulum.language = "it"
    pendulum.announcement_style = ANNOUNCEMENT_STYLE_COLLOQUIAL
    assert pendulum._build_text_with_minutes(hour, minute) == expected


def test_colloquial_style_does_not_change_other_languages(pendulum) -> None:
    pendulum.language = "en"
    pendulum.announcement_style = ANNOUNCEMENT_STYLE_COLLOQUIAL
    assert pendulum._build_text(15, 30) == "It's 3 thirty in the afternoon"


@pytest.mark.parametrize(
    ("config", "expected"),
    [
        ({}, ANNOUNCEMENT_STYLE_CLASSIC),
        ({CONF_ANNOUNCEMENT_STYLE: ANNOUNCEMENT_STYLE_COLLOQUIAL}, ANNOUNCEMENT_STYLE_COLLOQUIAL),
    ],
)
def test_announcement_style_from_config(hass: HomeAssistant, config, expected) -> None:
    entry = MockConfigEntry(
        domain=DOMAIN,
        data={
            CONF_PLAYER_TYPE: "alexa",
            CONF_PLAYER_DEVICE: "media_player.x",
            CONF_LANGUAGE: "it",
            **config,
        },
    )
    pendulum = DigitalPendulum(hass, entry)
    assert pendulum.announcement_style == expected
    assert pendulum._build_text(1, 0) == ("È l'una" if config else "Ore una")
