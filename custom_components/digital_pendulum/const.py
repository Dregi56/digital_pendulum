DOMAIN = "digital_pendulum"

CONF_ENABLED = "enabled"
DEFAULT_ENABLED = True

CONF_START_HOUR = "start_hour"
CONF_END_HOUR = "end_hour"
CONF_PLAYER_DEVICE = "player_device"
CONF_USE_CHIME = "use_chime"
CONF_CUSTOM_CHIME_PATH = "custom_chime_path"
CONF_PRESET_CHIME = "preset_chime"

DEFAULT_START_HOUR = 8
DEFAULT_END_HOUR = 22
DEFAULT_USE_CHIME = True
DEFAULT_CUSTOM_CHIME_PATH = ""
DEFAULT_PRESET_CHIME = "church-bell"

SWITCH_ENTITY_ID = "digital_pendulum_enabled"

#----- Lista suoni predefiniti  ------
PRESET_CHIMES = {
    "church-bell": {
        "name": "Church Bell",
        "url": "https://raw.githubusercontent.com/Dregi56/digital_pendulum/main/sounds/church-bell.mp3"
    },
    "church-bell_la": {
        "name": "Church Bell_la",
        "url": "https://raw.githubusercontent.com/Dregi56/digital_pendulum/main/sounds/church-bell_la.mp3"
    },
    "church-bell-distant": {
        "name": "Church Bell Distant",
        "url": "https://raw.githubusercontent.com/Dregi56/digital_pendulum/main/sounds/church-bell-distant.mp3"
    },
    "church-clock-strikes": {
        "name": "Church-Clock-Strikes",
        "url": "https://raw.githubusercontent.com/Dregi56/digital_pendulum/main/sounds/church-clock-strikes.mp3"
    },
    "clock-bell-chimes": {
        "name": "Clock-Bell-Chimes",
        "url": "https://raw.githubusercontent.com/Dregi56/digital_pendulum/main/sounds/clock-bell-chimes.mp3"
    },
    "clock-strikes": {
        "name": "Clock Strikes",
        "url": "https://raw.githubusercontent.com/Dregi56/digital_pendulum/main/sounds/clock-strikes.mp3"
    },
    "grandfather-clock-strikes": {
        "name": "Grandfather Clock",
        "url": "https://raw.githubusercontent.com/Dregi56/digital_pendulum/main/sounds/grandfather-clock-strikes.mp3"
    },
    "grandfathers-clock-ding-dong": {
        "name": "Clock Ding Dong",
        "url": "https://raw.githubusercontent.com/Dregi56/digital_pendulum/main/sounds/grandfathers-clock-ding-dong.mp3"
    },
    "oldclock": {
        "name": "Oldclock",
        "url": "https://raw.githubusercontent.com/Dregi56/digital_pendulum/main/sounds/oldclock.mp3"
    },
    "oldclock-2": {
        "name": "Wind Chimes",
        "url": "https://raw.githubusercontent.com/Dregi56/digital_pendulum/main/sounds/oldclock-2.mp3"
    },
    "oldclock-bell": {
        "name": "Oldclock Bell",
        "url": "https://raw.githubusercontent.com/Dregi56/digital_pendulum/main/sounds/oldclock-bell.mp3"
    },
    "pendulum-clock-ding-dong": {
        "name": "Pendulum Ding Dong",
        "url": "https://raw.githubusercontent.com/Dregi56/digital_pendulum/main/sounds/pendulum-clock-ding-dong.mp3"
    },
    "pendulum-clock-ding-dong-2": {
        "name": "Ding Dong P",
        "url": "https://raw.githubusercontent.com/Dregi56/digital_pendulum/main/sounds/pendulum-clock-ding-dong-2.mp3"
    },
    "custom": {
        "name": "Custom (use custom path)",
        "url": ""
    }
}