DOMAIN = "digital_pendulum"

CONF_ENABLED = "enabled"
DEFAULT_ENABLED = True

CONF_START_HOUR = "start_hour"
CONF_END_HOUR = "end_hour"
CONF_PLAYER_DEVICE = "player_device"
CONF_USE_CHIME = "use_chime"
CONF_CUSTOM_CHIME_PATH = "custom_chime_path"
CONF_PRESET_CHIME = "preset_chime"
CONF_TOWER_CLOCK = "tower_clock"

DEFAULT_START_HOUR = 8
DEFAULT_END_HOUR = 22
DEFAULT_USE_CHIME = True
DEFAULT_CUSTOM_CHIME_PATH = ""
DEFAULT_PRESET_CHIME = "church-bell"
DEFAULT_TOWER_CLOCK = False

SWITCH_ENTITY_ID = "digital_pendulum_enabled"

# Lista suoni predefiniti
PRESET_CHIMES = {
    "church-bell": {
        "name": "Church Bell",
        "url": "https://raw.githubusercontent.com/Dregi56/digital_pendulum/main/sounds/church-bell.mp3"
    },
    "clock-chime": {
        "name": "Clock Chime",
        "url": "https://raw.githubusercontent.com/Dregi56/digital_pendulum/main/sounds/clock-chime.mp3"
    },
    "simple-bell": {
        "name": "Simple Bell",
        "url": "https://raw.githubusercontent.com/Dregi56/digital_pendulum/main/sounds/simple-bell.mp3"
    },
    "gong": {
        "name": "Gong",
        "url": "https://raw.githubusercontent.com/Dregi56/digital_pendulum/main/sounds/gong.mp3"
    },
    "doorbell": {
        "name": "Doorbell",
        "url": "https://raw.githubusercontent.com/Dregi56/digital_pendulum/main/sounds/doorbell.mp3"
    },
    "wind-chimes": {
        "name": "Wind Chimes",
        "url": "https://raw.githubusercontent.com/Dregi56/digital_pendulum/main/sounds/wind-chimes.mp3"
    },
    "westminster": {
        "name": "Westminster",
        "url": "https://raw.githubusercontent.com/Dregi56/digital_pendulum/main/sounds/westminster.mp3"
    },
    "custom": {
        "name": "Custom (use custom path)",
        "url": ""
    }
}
