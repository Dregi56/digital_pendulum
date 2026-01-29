# 🕰️ Digital Pendulum

Ein sprechendes digitales Pendel für Home Assistant  
<br>**Autor:** Egidio Ziggiotto (Dregi56)  E-Mail: [dregi@cyberservices.com](mailto:dregi@cyberservices.com)


[![HACS](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://hacs.xyz/)
[![Version](https://img.shields.io/github/v/release/Dregi56/digital_pendulum)](https://github.com/Dregi56/digital_pendulum/releases)
![License](https://img.shields.io/github/license/Dregi56/digital_pendulum)
[![GitHub stars](https://img.shields.io/github/stars/Dregi56/digital_pendulum?style=social)](https://github.com/Dregi56/digital_pendulum)

🌍 Verfügbare Sprachen:
[Italiano](README.it.md) |
[English](README.en.md) |
[Español](README.es.md) |
[Deutsch](README.de.md) |
[Français](README.fr.md) 
<br>👉Dies ist die deutsche README. Verwenden Sie oben die Sprachauswahl

## ❤️ Gefällt dir Digital Pendulum?

Wenn es dir nützlich ist, hinterlasse bitte einen ⭐ auf GitHub:  
👉 **https://github.com/Dregi56/digital_pendulum**
<br>Danke.

## 📌 Beschreibung

Digital Pendulum ist eine benutzerdefinierte Integration für Home Assistant, die die Uhrzeit sprachlich ansagt – genau wie ein digitales Pendel 🕰️.


Mit einem Alexa-Gerät als Lautsprecher kann das System:

- 📢 die Uhrzeit alle 30 Minuten ansagen  
- 🌍 automatisch in der in Home Assistant eingestellten Sprache sprechen  
- ⏰ nur innerhalb eines konfigurierbaren Zeitfensters arbeiten 
- 🔔 vor der Ansage einen benutzerdefinierten Ton abspielen (standardmäßig der Alexa-„announce“-Ton (Chime))
- 🏰 um 12 Uhr die Westminster-Melodie abspielen  

Das Ergebnis ist ein eleganter und diskreter Effekt, ideal für Zuhause oder das Büro.

## ✨ Hauptfunktionen

### 🕑 Automatische Zeitansage
- jede volle Stunde (xx:00)
- jede halbe Stunde (xx:30)

### 🌐 Automatische Mehrsprachenunterstützung
- Italienisch 🇮🇹
- Englisch 🇬🇧
- Französisch 🇫🇷
- Deutsch 🇩🇪 (mit korrekter Behandlung von „halb“)
- Spanisch 🇪🇸

automatischer Fallback auf Italienisch

### ⏱️ Konfigurierbares Zeitfenster
- z. B. nur von 8:00 bis 22:00 Uhr

### 🔔 Optionale Glocke
- 🔕 kurze stille Ankündigung vor dem TTS
- 🎵 benutzerdefinierte Sounds. Wenn ein Pfad definiert ist, lokaler Sound

### 🧪 Testfunktion
- um die Ansage sofort zu testen

### 🎯 Verhalten
- Preset: "church-bell": Standardsound
- Preset: "simple-bell": Glocke aus der Bibliothek
- Preset: "custom" + leerer Pfad: Alexa-„announce“-Sound
- Preset: "custom" + gültiger Pfad: spielt eine ausgewählte Datei ab
- Preset: "tower-clock": Westminster-Melodie um 12 Uhr
- Use Chime: OFF: kein Sound, nur TTS (Zeitansage)

## ⚙️ Funktionsweise

Das Herz des Systems ist die Klasse:

class DigitalPendulum

die:
- sich an einen internen Timer registriert (jede 1 Minute)
- prüft:
  - ob die Integration aktiviert ist
  - ob die Uhrzeit innerhalb des erlaubten Zeitfensters liegt
  - ob die Minute 00 oder 30 ist
- den gesprochenen Text basierend auf der Sprache erstellt
- die Ansage an das konfigurierte Alexa-Gerät sendet

## 🗣️ Sprachverwaltung

Die Sprache wird automatisch erkannt über:

self.hass.config.language

Beispiele für Ansagen:

| Sprache | Uhrzeit | Ansage |
|------|------|--------|
| 🇮🇹 IT | 10:30 | Ore 10 e trenta |
| 🇬🇧 EN | 14:00 | It's 14 o'clock |
| 🇫🇷 FR | 9:30 | Il est 9 heures trente |
| 🇩🇪 DE | 16:30 | Es ist halb 17 |
| 🇪🇸 ES | 11:00 | Son las 11 |

## 🔔 Chime (Anfangsglocke)

Wenn die Option use_chime aktiviert ist:
- wird eine leere Ankündigung gesendet
- das System wartet 1,3 Sekunden
- anschließend startet das TTS mit der Uhrzeit  

Dies erzeugt einen Effekt ähnlich einem echten Pendel 🎶.

## 🧩 Konfigurationsoptionen

| Option | Beschreibung |
|------|------------|
| player | Ziel-Alexa-Gerät |
| start_hour | Startzeit |
| end_hour | Endzeit |
| enabled | Pendel aktivieren/deaktivieren |
| tower-clock | 12-Uhr-Melodie aktivieren/deaktivieren |
| use_chime | Glocke aktivieren/deaktivieren |

Standardwerte:

- ⏰ start_hour → DEFAULT_START_HOUR  
- ⏰ end_hour → DEFAULT_END_HOUR  
- 🔔 use_chime → DEFAULT_USE_CHIME  
- ✅ enabled → DEFAULT_ENABLED  

## 🧪 Sofortiger Test

Eine manuelle Testmethode ist verfügbar:

async_test_announcement()

Diese:
- liest die aktuelle Uhrzeit
- erzeugt einen vollständigen Satz (z. B. „Es ist 15:42“)
- spielt ihn sofort auf dem Alexa-Gerät ab  

Nützlich zur Überprüfung von: Sprache, Lautstärke, Chime, korrekter TTS-Funktion

## 📦 Voraussetzungen
> ⚠️ **Digital Pendulum ist eine reine HACS-Integration**
> 
- 🏠 Home Assistant
- 🔊 Alexa Media Player installiert und funktionsfähig
- 📡 Alexa-Gerät als Player konfiguriert

## 🎯 Idealer Einsatz

- ✔️ Smarte Wohnungen
- ✔️ Büros
- ✔️ Gemeinschaftsbereiche
- ✔️ „Modernes Pendel“-Effekt
- ✔️ Unaufdringliche Zeit-Erinnerung

## 🚀 Mögliche zukünftige Erweiterungen

- ⏳ Ansagen alle 15 Minuten
- 🔇 Automatische Nachtlautstärke
- 🗓️ Tagesansage
- 📣 Unterstützung weiterer TTS-Systeme

---

## 

## ☕ Unterstütze das Projekt

Gefällt dir dieses Projekt? Wenn du es nützlich findest, spendiere mir einen virtuellen Kaffee, um zukünftige Entwicklungen zu unterstützen! Jeder noch so kleine Beitrag wird sehr geschätzt. 🙏

**Digital Pendulum ist und bleibt immer kostenlos und Open Source.** Spenden sind vollkommen freiwillig! ❤️


[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/dregi56)

💡 **Bevorzugst du andere Methoden?** Du kannst verwenden:

[![revolut](https://img.shields.io/badge/Revolut-0075EB?style=for-the-badge&logo=revolut&logoColor=white)](https://revolut.me/egidio5t9d)
