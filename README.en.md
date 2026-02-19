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

Digital Pendulum is a custom integration for Home Assistant that vocally announces the time, just like a digital pendulum 🕰️.


Using an Alexa device as a speaker, the system:

- 📢 announces the time every hour and/or every half hour (configurable)
- 🌍 automatically speaks in the language set in Home Assistant  
- ⏰ only works within a configurable time slot 
- 🔔 can play a custom sound before the announcement
- 🔕 can disable the voice announcement (bell only)
- 🏰 can play the Westminster chime at 12 o'clock

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

### ⏱️ Configurable time slot
- e.g. only from 8:00 to 22:00

###  🔔 Optional bell
- 🎵 12 preset sounds to choose from
- 🎶 option to use a custom audio file
- 🔕 Alexa "announce" notification sound (default)

### 🧪 Test function
- to immediately try the announcement

### 🎯 Behaviour

**Bell (Chime):**
- **Available presets**: 12 sounds including church-bell, simple-bell, clock-chime, etc.
- **Custom sound**: Select "custom" and enter the path of your audio file
- **Default**: Alexa "announce" sound (if you select nothing)
- **Disabled**: Disable "use_chime" for no sound before the announcement

**Westminster Melody (Tower Clock):**
- Separate "tower_clock" option
- Plays **only at 12:00** (noon)
- Replaces the normal chime at that time

**Voice announcement:**
- **Enabled** (default): Alexa pronounces the time after the bell
- **Disabled**: Bell sound only, no voice announcement

**Half-hour announcements:**
- **Enabled** (default): Announcements at :00 and :30
- **Disabled**: Announcements at :00 only

## ⚙️ How it works

Digital Pendulum synchronises with the system clock and automatically checks every minute whether it is time to make an announcement.

**When the announcement triggers:**
1. 🔔 Plays the chosen bell (if enabled)
2. ⏱️ Waits 1.2 seconds
3. 🗣️ Alexa pronounces the time in the Home Assistant language (if enabled)

Everything happens automatically without the need to configure automations!

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

If the use_chime option is active:
- the Alexa notification sound or the chosen sound is played
- the system waits 1.2 seconds
- the voice announcement starts (if enabled)

This creates an effect similar to a real pendulum 🎶.

## 🧩 Configuration options

| Option | Description |
|------|------------|
| player | Target Alexa device |
| start_hour | Operating start time |
| end_hour | Operating end time |
| enabled | Enables/disables the pendulum |
| announce_half_hours | Enables announcements every half hour (otherwise every hour only) |
| voice_announcement | Enables/disables the voice time announcement |
| tower_clock | Enables Westminster melody at 12:00 |
| use_chime | Enables/disables the bell before the announcement |
| preset_chime | Choice of bell sound (12 available presets) |
| custom_chime_path | Path for custom bell sound |

Default values:

- ⏰ start_hour → 8
- ⏰ end_hour → 22
- 🔔 use_chime → True
- 🗣️ voice_announcement → True
- ⏰ announce_half_hours → True
- 🏰 tower_clock → False
- ✅ enabled → True

## 🧪 Immediate test

A manual test method is available:

Which:
- reads the current time
- generates a complete sentence (e.g. "It's 15 hours and 42 minutes")
- plays it immediately on the Alexa device  

Useful to verify: language, volume, chime, correct TTS operation

## 📦 Requirements

> ✨ **Available on HACS** - simplified installation and updates!

- 🏠 Home Assistant 2024.1.0 or higher
- 🔊 Alexa Media Player installed and working
- 📡 Alexa device configured as player

## 💾 Installation

### Via HACS (recommended)

1. Open **HACS** in the side menu
2. Go to **Integrations**
3. Search for **"Digital Pendulum"**
4. Click **Download**
5. **Restart Home Assistant**
6. Go to **Settings** → **Devices & Services** → **Add Integration**
7. Search for **"Digital Pendulum"**
8. Follow the guided configuration

### Manual installation

1. Download the latest release from [GitHub](https://github.com/Dregi56/digital_pendulum/releases)
2. Extract the files
3. Copy the `digital_pendulum` folder to `config/custom_components/`
4. Restart Home Assistant
5. Go to **Settings** → **Devices & Services** → **Add Integration**
6. Search for **"Digital Pendulum"**
7. Follow the guided configuration


## 🎯 Ideal use

- ✔️ Smart homes
- ✔️ Offices
- ✔️ Common areas
- ✔️ "Modern pendulum" effect
- ✔️ Non-invasive time reminder

## 🔧 Troubleshooting

### "Cannot find EU skill" error or Alexa issues

**Alexa Media Player** problem, not Digital Pendulum.

**Quick fix:**
1. Settings → Devices and services → Alexa Media Player
2. Three dots → Reload
3. If it doesn't work: uninstall and reinstall Alexa Media Player

---

### Wrong language

Digital Pendulum automatically uses the Home Assistant language.

1. Check: Settings → System → General → Language
2. Supported languages: 🇮🇹 🇬🇧 🇫🇷 🇩🇪 🇪🇸
3. After changing the language, restart Home Assistant

---

### No announcements

**Check:**
- Integration enabled? (Switch ON)
- Are you within the configured time slot? (default 8:00-22:00)
- Alexa device online?
- Try the "Test" button

---

### Bell only or voice only

- **Bell only:** Enable "Voice announcement"
- **Voice only:** Enable "Use chime"

---

### Westminster doesn't play at 12

- Check that "Tower Clock" is active
- Works **only at 12:00** (noon, not midnight)

---

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
