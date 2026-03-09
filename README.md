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
[Français](README.fr.md) |
[Polski](README.pl.md) |
[Čeština](README.cs.md) |
[Slovenčina](README.sk.md) |
[Português](README.pt.md)

<br>👉This is the English README. Use the language selector above


## ❤️ Do you like Digital Pendulum?

If you find it useful, consider leaving a ⭐ on GitHub:  
👉 **https://github.com/Dregi56/digital_pendulum**
<br>Thank you.

## 📌 Description

Digital Pendulum is a custom integration for Home Assistant that vocally announces the time, just like a digital pendulum 🕰️.

Using a compatible smart speaker as a player, the system:

- 📢 announces the time every hour and/or every half hour (configurable)
- 🌍 automatically speaks in the language set in Home Assistant  
- ⏰ only works within a configurable time slot 
- 🔔 can play a custom sound before the announcement
- 🔕 can disable the voice announcement (bell only)
- 🏰 can play the Westminster chime at 12 o'clock

The result is an elegant and discreet effect, ideal for home or office.

## 🔊 Supported Devices

Digital Pendulum supports three player types:

| Type | Description | Requirement |
|------|-------------|-------------|
| **Alexa** | Amazon Echo devices | [alexa_media_player](https://github.com/custom-components/alexa_media_player) via HACS |
| **Google Home / Nest** | Google Home, Nest Mini, Nest Hub, Chromecast | Google Cast (native HA integration) |
| **Generic** | Any other HA media_player device | TTS engine configured in HA (functionality may vary) |

During setup you will be asked to select the player type first, then the specific device.

## ✨ Main features

### 🕑 Automatic time announcement
- every hour (xx:00)
- every half hour (xx:30) - optional (chime only or chime + voice, configurable)

### ⏱️ Configurable delay after chime
- adjustable waiting time between chime and voice announcement (default: 1.2 seconds)
- useful especially for Google Home / Nest devices, which may need a longer delay to play the voice announcement correctly

### 🌐 Automatic multilingual support
- Italian 🇮🇹
- English 🇬🇧
- French 🇫🇷
- German 🇩🇪
- Spanish 🇪🇸
- Polish 🇵🇱
- Czech 🇨🇿
- Slovak 🇸🇰
- Portuguese 🇵🇹
  
automatic fallback to Italian

🌐 **Customizable language:** You can choose a different language from the one set in Home Assistant (useful for example for those who have HA in English but want announcements in their native language).

### 🕐 Configurable time slot
- e.g. only from 8:00 to 22:00

###  🔔 Optional bell
- 🎵 12 preset sounds to choose from
- 🎶 option to use a custom audio file
- 🔕 default notification sound (if nothing is selected)
- ⏳ Option for a dedicated half-hour sound

### 🧪 Test function
- to immediately try the announcement

### 🎯 Behaviour

**Bell (Chime):**
- **Available presets**: 12 sounds including church-bell, simple-bell, clock-chime, etc.
- **Custom sound**: Select "custom" and enter the path of your audio file
- **Default**: notification sound (if you select nothing)
- **Disabled**: Disable "use_chime" for no sound before the announcement

**Westminster Melody (Tower Clock):**
- Separate "tower_clock" option
- Plays **only at 12:00** (noon)
- Replaces the normal chime at that time

**Voice announcement:**
- **Enabled** (default): the device pronounces the time after the bell
- **Disabled**: Bell sound only, no voice announcement

**Half-hour voice announcement:**
- **Enabled** (default): voice announcement plays at both :00 and :30
- **Disabled**: chime still plays at :30, but no voice announcement

## ⚙️ How it works

Digital Pendulum synchronises with the system clock and automatically checks every minute whether it is time to make an announcement.

**When the announcement triggers:**
1. 🔔 Plays the chosen bell (if enabled)
2. ⏱️ Waits a configurable number of seconds (default: 1.2s) — increase this value for Google Home / Nest devices if the voice announcement does not play correctly
3. 🗣️ The device pronounces the time in the Home Assistant language (if enabled)

Everything happens automatically without the need to configure automations!

## 🗣️ Language handling

The language is automatically detected from:

self.hass.config.language

Announcement examples:

| Language | Time | Announcement |
|------|------|--------|
| 🇮🇹 IT | 10:30 | Ore 10 e trenta |
| 🇬🇧 EN | 14:00 | It's 2 o'clock in the afternoon |
| 🇫🇷 FR | 9:30 | Il est 9 heures trente |
| 🇩🇪 DE | 16:30 | Es ist halb 17 |
| 🇪🇸 ES | 11:00 | Son las 11 |
| 🇵🇱 PL | 15:30 | Wpół do czwartej |
| 🇨🇿 CS | 8:30 | Půl deváté |
| 🇸🇰 SK | 8:30 | Pol deviatej |
| 🇵🇹 PT | 10:30 | São 10 e meia |

## 🔔 Chime (initial bell)

If the use_chime option is active:
- the notification sound or the chosen sound is played
- the system waits a configurable number of seconds (default: 1.2)
- the voice announcement starts (if enabled)

This creates an effect similar to a real pendulum 🎶.

## 🧩 Configuration options

| Option | Description |
|------|------------|
| player_type | Type of player device (Alexa, Google Home, Generic) |
| player | Target device |
| start_hour | Operating start time |
| end_hour | Operating end time |
| enabled | Enables/disables the pendulum |
| announce_half_hours | Enables announcements every half hour (otherwise every hour only) |
| after_chime_delay | Waiting time in seconds between chime and voice announcement (default: 1.2) |
| announce_half_hours_voice | Enables/disables voice announcement at half hours (chime still plays) |
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
- ⏱️ after_chime_delay → 1.2
- 🔇 announce_half_hours_voice → True

## 🧪 Immediate test

A manual test method is available:

Which:
- reads the current time
- generates a complete sentence (e.g. "It's 15 hours and 42 minutes")
- plays it immediately on the selected device

Useful to verify: language, volume, chime, correct TTS operation

## 🔍 Status Sensor

Digital Pendulum includes a diagnostic sensor:

`binary_sensor.digital_pendulum_status_warning`

**States:**
- ✅ **OFF** - Everything working correctly
- ⚠️ **ON** - Issues detected (integration disabled, Alexa offline, etc.)

**Uses:**
- Dashboard monitoring
- Notification automations
- Quick diagnostics

## 📦 Requirements

> ✨ **Available on HACS** - simplified installation and updates!

- 🏠 Home Assistant 2024.1.0 or higher
- 🔊 A compatible media_player device (see [Supported Devices](#-supported-devices))
- 📡 For Alexa: [alexa_media_player](https://github.com/custom-components/alexa_media_player) installed via HACS
- 📡 For Google Home / Nest: Google Cast integration (native in HA)

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

### Alexa issues or "Cannot find EU skill" error

**alexa_media_player** problem, not Digital Pendulum.

**Quick fix:**
1. Settings → Devices and services → Alexa Media Player
2. Three dots → Reload
3. If it doesn't work: uninstall and reinstall Alexa Media Player

---

### Google Home / Nest: no voice announcement

Digital Pendulum uses the TTS engine configured in HA for Google devices.

This is a known timing issue with Google devices. The voice announcement may be cut or skipped if the delay after the chime is too short.

1. Check that a TTS engine is configured in HA (Settings → Voice assistants)
2. Check the HA log for TTS errors
3. Increase the **"Delay after chime"** value (try 2.0 or 3.0 seconds)
4. Try the "Test" button to verify
---

### Wrong language

Digital Pendulum automatically uses the Home Assistant language.

1. Check: Settings → System → General → Language
2. Supported languages: 🇮🇹 🇬🇧 🇫🇷 🇩🇪 🇪🇸 🇵🇱 🇨🇿 🇸🇰 🇵🇹
3. After changing the language, restart Home Assistant

---

### No announcements

**Check:**
- Integration enabled? (Switch ON)
- Are you within the configured time slot? (default 8:00-22:00)
- Device online?
- Correct player type selected? (Alexa, Google, Generic)
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


---

## ☕ Support the project

Do you like this project? If you find it useful, buy me a virtual coffee to support future developments! Every small contribution is greatly appreciated. 🙏

**Digital Pendulum is and will always remain free and open source.** Donations are completely voluntary! ❤️


[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/dregi56)

💡 **Prefer other methods?** You can use:

[![revolut](https://img.shields.io/badge/Revolut-0075EB?style=for-the-badge&logo=revolut&logoColor=white)](https://revolut.me/egidio5t9d)
