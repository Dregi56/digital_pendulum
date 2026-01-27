# 🕰️ Digital Pendulum

A talking digital pendulum for Home Assistant  
<br>**Author:** Egidio Ziggiotto (Dregi56)  e-mail: [dregi@cyberservices.com](mailto:dregi@cyberservices.com)


[![HACS](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://hacs.xyz/)
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

> ⚠️ **Digital Pendulum is a HACS-only integration**
> It requires the **Alexa Media Player** integration installed and working.

## ❤️ Do you like Digital Pendulum?

If you find it useful, consider leaving a ⭐ on GitHub:  
👉 **https://github.com/Dregi56/digital_pendulum**
<br>Thank you.

## 📌 Description

Digital Pendulum is a custom integration for Home Assistant that announces the time vocally, just like a digital pendulum 🕰️.


Using an Alexa device as a speaker, the system:

- 📢 announces the time every 30 minutes  
- 🌍 automatically speaks in the language set in Home Assistant  
- ⏰ works only within a configurable time range 
- 🔔 can play a custom sound (by default the 'announce' (chime) sound) before the announcement
- 🏰 can play the Westminster melody at 12 o'clock  

The result is an elegant and discreet effect, ideal for home or office.

## ✨ Main features

### 🕑 Automatic time announcement
- every hour (xx:00)
- every half hour (xx:30)

### 🌐 Automatic multilingual support
- Italian 🇮🇹
- English 🇬🇧
- French 🇫🇷
- German 🇩🇪 (with correct handling of “halb”)
- Spanish 🇪🇸

automatic fallback to Italian

### ⏱️ Configurable time range
- e.g. only from 8:00 to 22:00

### 🔔 Optional chime
- 🔕 short silent announcement before TTS
- 🎵 custom sounds. If a path is defined, local sound

### 🧪 Test function
- to immediately test the announcement

### 🎯 Behavior
- Preset: "church-bell": default sound
- Preset: "simple-bell": bell chosen from library
- Preset: "custom" + empty path: Alexa 'announce' sound
- Preset: "custom" + valid path: plays a selected file
- Preset: "tower-clock": Westminster melody at 12 o'clock
- Use Chime: OFF: no sound, TTS only (time announcement)

## ⚙️ How it works

The heart of the system is the class:

class DigitalPendulum

which:
- registers to an internal timer (every 1 minute)
- checks:
  - whether the integration is enabled
  - whether the time is within the allowed range
  - whether the minute is 00 or 30
- builds the spoken text based on the language
- sends the announcement to the configured Alexa device

## 🗣️ Language handling

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
- an empty announce is sent
- the system waits 1.3 seconds
- the TTS with the time starts  

This creates an effect similar to a real pendulum 🎶.

## 🧩 Configuration options

| Option | Description |
|------|------------|
| player | Target Alexa device |
| start_hour | Start time |
| end_hour | End time |
| enabled | Enable/disable the pendulum |
| tower-clock | Enable/disable 12 o'clock melody |
| use_chime | Enable/disable the chime |

Default values:

- ⏰ start_hour → DEFAULT_START_HOUR  
- ⏰ end_hour → DEFAULT_END_HOUR  
- 🔔 use_chime → DEFAULT_USE_CHIME  
- ✅ enabled → DEFAULT_ENABLED  

## 🧪 Immediate test

A manual test method is available:

async_test_announcement()

Which:
- reads the current time
- generates a full sentence (e.g. “It's 15:42”)
- immediately plays it on the Alexa device  

Useful to verify: language, volume, chime, correct TTS operation

## 📦 Requirements

- 🏠 Home Assistant
- 🔊 Alexa Media Player installed and working
- 📡 Alexa device configured as player

## 🎯 Ideal use

- ✔️ Smart homes
- ✔️ Offices
- ✔️ Shared spaces
- ✔️ “Modern pendulum” effect
- ✔️ Non-intrusive time reminder

## 🚀 Possible future developments

- ⏳ Announcements every 15 minutes
- 🔇 Automatic night volume
- 🗓️ Day announcement
- 📣 Support for other TTS engines

---

## 

## ☕ Support the project

Do you like this project? If you find it useful, buy me a virtual coffee to support future developments! Every small contribution is greatly appreciated. 🙏

**Digital Pendulum is and will always remain free and open source.** Donations are completely voluntary! ❤️


[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/dregi56)

💡 **Prefer other methods?** You can use:

[![revolut](https://img.shields.io/badge/Revolut-0075EB?style=for-the-badge&logo=revolut&logoColor=white)](https://revolut.me/egidio5t9d)
