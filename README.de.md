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
[Deutsch](README.de.md) |
[Français](README.fr.md) |
[Español](README.es.md)

## ❤️ Gefällt dir Digital Pendulum?

Wenn es dir nützlich ist, hinterlasse bitte einen ⭐ auf GitHub:  
👉 **https://github.com/Dregi56/digital_pendulum**
<br>Danke.

## 📌 Beschreibung

Digital Pendulum ist eine benutzerdefinierte Integration für Home Assistant, die die Uhrzeit per Sprachausgabe ankündigt – genau wie ein digitales Pendel 🕰️.


Mit einem Alexa-Gerät als Lautsprecher verwendet das System:

- 📢 kündigt die Uhrzeit alle 30 Minuten an  
- 🌍 spricht automatisch die in Home Assistant eingestellte Sprache  
- ⏰ funktioniert nur innerhalb eines konfigurierbaren Zeitfensters  
- 🔔 kann einen benutzerdefinierten Ton abspielen (standardmäßig der „announce“-Ton (Chime) vor der Ansage  

Das Ergebnis ist ein eleganter und unaufdringlicher Effekt, ideal für Zuhause oder Büro.

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
- z. B. nur von 8:00 bis 22:00

###  🔔 Optionaler Chime
- 🔕 kurze stille Ankündigung vor dem TTS
- 🎵 benutzerdefinierte Sounds. Wenn ein Pfad definiert ist, lokaler Sound

### 🧪 Testfunktion
- um die Ansage sofort zu testen

## ⚙️ Funktionsweise

Das Herzstück des Systems ist die Klasse:

class DigitalPendulum

die:
- sich bei einem internen Timer registriert (jede 1 Minute)
- prüft:
  - ob die Integration aktiviert ist
  - ob die Uhrzeit innerhalb des erlaubten Zeitfensters liegt
  - ob die Minute 00 oder 30 ist
- den gesprochenen Text basierend auf der Sprache erstellt
- die Ansage an das konfigurierte Alexa-Gerät sendet

## 🗣️ Sprachverwaltung

Die Sprache wird automatisch ermittelt aus:

self.hass.config.language

Beispiele für Ansagen:

| Sprache | Uhrzeit | Ansage |
|------|------|--------|
| 🇮🇹 IT | 10:30 | Ore 10 e trenta |
| 🇬🇧 EN | 14:00 | It's 14 o'clock |
| 🇫🇷 FR | 9:30 | Il est 9 heures trente |
| 🇩🇪 DE | 16:30 | Es ist halb 17 |
| 🇪🇸 ES | 11:00 | Son las 11 en punto |

## 🔔 Chime (Startglocke)

Wenn die Option use_chime aktiviert ist:
- wird eine leere Ankündigung gesendet
- das System wartet 1,5 Sekunden
- die TTS-Zeitansage startet  

Dies erzeugt einen Effekt ähnlich einem echten Pendel 🎶.

## 🧩 Konfigurationsoptionen

| Option | Beschreibung |
|------|------------|
| enabled | Aktiviert oder deaktiviert das Pendel |
| start_hour | Startzeit des Betriebs |
| end_hour | Endzeit des Betriebs |
| player | Ziel-Alexa-Gerät |
| use_chime | Aktiviert/deaktiviert den Chime |

Standardwerte:

- ⏰ start_hour → DEFAULT_START_HOUR  
- ⏰ end_hour → DEFAULT_END_HOUR  
- 🔔 use_chime → DEFAULT_USE_CHIME  
- ✅ enabled → DEFAULT_ENABLED  

## 🧪 Sofortiger Test

Eine manuelle Testmethode ist verfügbar:

async_test_announcement()

Die:
- die aktuelle Uhrzeit liest
- einen vollständigen Satz erzeugt (z. B. „Ore 15 e 42“)
- ihn sofort auf dem Alexa-Gerät wiedergibt  

Nützlich zur Überprüfung von: Sprache, Lautstärke, Chime, korrekter TTS-Funktion

## 📦 Voraussetzungen

- 🏠 Home Assistant
- 🔊 Alexa Media Player installiert und funktionsfähig
- 📡 Alexa-Gerät als Player konfiguriert

## 🎯 Ideale Verwendung

- ✔️ Smart Homes
- ✔️ Büros
- ✔️ Gemeinschaftsbereiche
- ✔️ „Modernes Pendel“-Effekt
- ✔️ Unaufdringliche Zeit-Erinnerung

## 🚀 Mögliche zukünftige Erweiterungen

- ⏳ Ansagen alle 15 Minuten
- 🔇 Automatische Nachtlautstärke
- 🗓️ Tagesansage
- 📣 Unterstützung weiterer TTS-Engines

---

## 

## ☕ Projekt unterstützen

Gefällt dir dieses Projekt? Wenn du es nützlich findest, spendiere mir einen virtuellen Kaffee, um zukünftige Weiterentwicklungen zu unterstützen! Jeder kleine Beitrag wird sehr geschätzt. 🙏

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/dregi56)

💡 **Bevorzugst du andere Methoden?** Du kannst verwenden:

[![revolut](https://img.shields.io/badge/Revolut-0075EB?style=for-the-badge&logo=revolut&logoColor=white)](https://revolut.me/egidio5t9d)
