# 🕰️ Digital Pendulum

A talking digital pendulum for Home Assistant  
<br>**Author:** Egidio Ziggiotto (Dregi56)  e-mail: [dregi@cyberservices.com](mailto:dregi@cyberservices.com)

[![HACS](https://img.shields.io/badge/HACS-Default-41BDF5.svg)](https://hacs.xyz/)
[![Version](https://img.shields.io/github/v/release/Dregi56/digital_pendulum)](https://github.com/Dregi56/digital_pendulum/releases)
![License](https://img.shields.io/github/license/Dregi56/digital_pendulum)
[![GitHub stars](https://img.shields.io/github/stars/Dregi56/digital_pendulum?style=social)](https://github.com/Dregi56/digital_pendulum)

🌍 Available languages:
[Italiano](README.it.md) |
[English](README.en.md) |
[Español](README.es.md) |
[Deutsch](README.de.md) |
[Français](README.fr.md) 
<br>👉This is the English README. Use the language selector above


## ❤️ Do you like Digital Pendulum?

If you find it useful, consider leaving a ⭐ on GitHub:  
👉 **https://github.com/Dregi56/digital_pendulum**
<br>Thank you.

## 📌 Description

Digital Pendulum is a custom integration for Home Assistant that announces the time vocally, just like a digital pendulum clock 🕰️.


Using an Alexa device as a speaker, the system:

- 📢 announces the time every hour and/or every half hour (configurable)
- 🌍 automatically speaks in the language set in Home Assistant  
- ⏰ works only within a configurable time range 
- 🔔 can play a custom sound before the announcement
- 🔕 can disable voice announcements (chime only)
- 🏰 can play the Westminster melody at 12 o'clock

The result is an elegant and discreet effect, ideal for home or office.

## ✨ Main features

### 🕑 Automatic time announcement
- every hour (xx:00)
- every half hour (xx:30) - optional

### 🌐 Automatic multilingual support
- Italian 🇮🇹
- English 🇬🇧
- French 🇫🇷
- German 🇩🇪 (with correct handling of "halb")
- Spanish 🇪🇸

automatic fallback to Italian

### ⏱️ Configurable time range
- e.g. only from 8:00 to 22:00

###  🔔 Optional chime
- 🎵 12 predefined sounds to choose from
- 🎶 ability to use a custom audio file
- 🔕 Alexa "announce" notification sound (default)

### 🧪 Test function
- to immediately test the announcement

### 🎯 Behavior

**Chime:**
- **Available presets**: 12 sounds including church-bell, simple-bell, clock-chime, etc.
- **Custom sound**: Select "custom" and enter the path to your audio file
- **Default**: Alexa "announce" sound (if nothing is selected)
- **Disabled**: Disable "use_chime" for no sound before the announcement

**Westminster Melody (Tower Clock):**
- Separate "tower_clock" option
- Plays **only at 12:00** (noon)
- Replaces the normal chime at that time

**Voice announcement:**
- **Enabled** (default): Alexa speaks the time after the chime
- **Disabled**: Chime only, no voice announcement

**Half-hour announcements:**
- **Enabled** (default): Announcements at :00 and :30
- **Disabled**: Announcements only at :00

## ⚙️ How it works

The core of the system is the class:

class DigitalPendulum

which:
- registers itself to a synchronized internal timer (every minute at second :00)
- checks:
  - whether the integration is enabled
  - whether the time is within the allowed range
  - whether the minute is :00 (or :30 if enabled)
- builds the spoken text based on the language
- plays the chime (if enabled)
- sends the voice announcement to the Alexa device (if enabled)

## 🗣️ Language management

The language is automatically detected from:

self.hass.config.language

Announcement examples:

| Language | Time | Announcement |
|------|------|--------|
| 🇮🇹 IT | 10:30 | Ore 10 e trenta |
| 🇬🇧 EN | 14:00 | It's 14 o'clock |
| 🇫🇷 FR | 9:30 | Il est 9 heures trente |
| 🇩🇪 DE | 16:30 | Es ist halb 17 |
| 🇪🇸 ES | 11:00 | Son las 11 |

## 🔔 Chime (initial bell)

If the use_chime option is enabled:
- the Alexa notification sound or selected sound is played
- the system waits 1.2 seconds
- the voice announcement starts (if enabled)

This creates an effect similar to a real pendulum clock 🎶.

## 🧩 Configuration options

| Option | Description |
|------|------------|
| player | Target Alexa device |
| start_hour | Start time |
| end_hour | End time |
| enabled | Enable/disable the pendulum |
| announce_half_hours | Enable half-hour announcements (otherwise hourly only) |
| voice_announcement | Enable/disable voice time announcement |
| tower_clock | Enable Westminster melody at 12:00 |
| use_chime | Enable/disable chime before announcement |
| preset_chime | Chime sound selection (12 presets available) |
| custom_chime_path | Path for custom chime sound |

Default values:

- ⏰ start_hour → 8
- ⏰ end_hour → 22
- 🔔 use_chime → True
- 🗣️ voice_announcement → True
- ⏰ announce_half_hours → True
- 🏰 tower_clock → False
- ✅ enabled → True

## 🧪 Instant test

A manual test method is available:

async_test_announcement()

Which:
- reads the current time
- generates a complete phrase (e.g. "Ore 15 e 42")
- plays it immediately on the Alexa device  

Useful to verify: language, volume, chime, correct TTS operation

## 📦 Requirements

> ✨ **Available on HACS** - simplified installation and updates!

- 🏠 Home Assistant 2024.1.0 or later
- 🔊 Alexa Media Player installed and working
- 📡 Alexa device configured as player


## 🎯 Ideal use

- ✔️ Smart homes
- ✔️ Offices
- ✔️ Common areas
- ✔️ "Modern pendulum" effect
- ✔️ Non-intrusive time reminder

## 🚀 Possible future developments

- ⏳ Announcements every 15 minutes
- 🔇 Automatic night volume
- 🗓️ Day announcement
- 📣 Support for other TTS

---

## 

## ☕ Support the project

Do you like this project? If you find it useful, buy me a virtual coffee to support future developments! Every small contribution is greatly appreciated. 🙏

**Digital Pendulum is and will always remain free and open source.** Donations are completely voluntary! ❤️


[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/dregi56)

💡 **Prefer other methods?** You can use:

[![revolut](https://img.shields.io/badge/Revolut-0075EB?style=for-the-badge&logo=revolut&logoColor=white)](https://revolut.me/egidio5t9d)
