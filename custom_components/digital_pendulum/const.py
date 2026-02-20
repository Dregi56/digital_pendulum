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
CONF_ANNOUNCE_HALF_HOURS = "announce_half_hours"
CONF_VOICE_ANNOUNCEMENT = "voice_announcement"

# Defaults
DEFAULT_ANNOUNCE_HALF_HOURS = True
DEFAULT_VOICE_ANNOUNCEMENT = True
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
    "chimes-silver": {
        "name": "Chimes silver",
        "url": "https://raw.githubusercontent.com/Dregi56/digital_pendulum/main/sounds/chimes-silver.mp3"
    },
    "bell-grave": {
        "name": "Bell Grave",
        "url": "https://raw.githubusercontent.com/Dregi56/digital_pendulum/main/sounds/bell-grave.mp3"
    },
    "bells-bong": {
        "name": "Bells Bong",
        "url": "https://raw.githubusercontent.com/Dregi56/digital_pendulum/main/sounds/bells-bong.mp3"
    },
    "bells-med": {
        "name": "Bells Med",
        "url": "https://raw.githubusercontent.com/Dregi56/digital_pendulum/main/sounds/bells-med.mp3"
    },
    "church-bell-distant": {
        "name": "Church Bell Distant",
        "url": "https://raw.githubusercontent.com/Dregi56/digital_pendulum/main/sounds/church-bell-distant.mp3"
    },
    "church-bell_la": {
        "name": "Church Bell La",
        "url": "https://raw.githubusercontent.com/Dregi56/digital_pendulum/main/sounds/church-bell_la.mp3"
    },
    "church-clock-strikes": {
        "name": "Church Clock Strikes",
        "url": "https://raw.githubusercontent.com/Dregi56/digital_pendulum/main/sounds/church-clock-strikes.mp3"
    },
    "clock-bell-chimes": {
        "name": "Clock Bell Chimes",
        "url": "https://raw.githubusercontent.com/Dregi56/digital_pendulum/main/sounds/clock-bell-chimes.mp3"
    },
    "clock-strikes": {
        "name": "Clock Strikes",
        "url": "https://raw.githubusercontent.com/Dregi56/digital_pendulum/main/sounds/clock-strikes.mp3"
    },
    "oldclock-bell": {
        "name": "Oldclock Bell",
        "url": "https://raw.githubusercontent.com/Dregi56/digital_pendulum/main/sounds/oldclock-bell.mp3"
    },
    "grandfathers-ding-dong": {
        "name": "Grandfathers ding dong",
        "url": "https://raw.githubusercontent.com/Dregi56/digital_pendulum/main/sounds/grandfathers-ding-dong.mp3"
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




