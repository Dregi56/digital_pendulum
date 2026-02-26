# 🕰️ Digital Pendulum

Ein sprechendes digitales Pendel für Home Assistant
<br>**Autor:** Egidio Ziggiotto (Dregi56)  e-mail: [dregi@cyberservices.com](mailto:dregi@cyberservices.com)

[![HACS](https://img.shields.io/badge/HACS-Default-41BDF5.svg)](https://hacs.xyz/)
[![Version](https://img.shields.io/github/v/release/Dregi56/digital_pendulum)](https://github.com/Dregi56/digital_pendulum/releases)
![License](https://img.shields.io/github/license/Dregi56/digital_pendulum)
[![GitHub stars](https://img.shields.io/github/stars/Dregi56/digital_pendulum?style=social)](https://github.com/Dregi56/digital_pendulum)

🌍 Verfügbare Sprachen:
[Italiano](README.it.md) |
[English](README.en.md) |
[Español](README.es.md) |
[Deutsch](README.de.md) |
[Français](README.fr.md) |
[Polski](README.pl.md) 

<br>👉Dies ist die Deutsche README. Verwenden Sie den Sprachauswähler oben


## ❤️ Gefällt Ihnen Digital Pendulum?

Wenn Sie es nützlich finden, hinterlassen Sie bitte ein ⭐ auf GitHub:  
👉 **https://github.com/Dregi56/digital_pendulum**
<br>Danke.

## 📌 Beschreibung

Digital Pendulum ist eine benutzerdefinierte Integration für Home Assistant, die die Uhrzeit akustisch ansagt, genau wie ein digitales Pendel 🕰️.


Mit einem Alexa-Gerät als Lautsprecher kann das System:

- 📢 die Uhrzeit jede Stunde und/oder jede halbe Stunde ansagen (konfigurierbar)
- 🌍 automatisch in der in Home Assistant eingestellten Sprache sprechen  
- ⏰ nur innerhalb eines konfigurierbaren Zeitfensters funktionieren 
- 🔔 vor der Ansage einen benutzerdefinierten Ton abspielen
- 🔕 die Sprachansage deaktivieren (nur Glocke)
- 🏰 um 12 Uhr die Westminster-Melodie abspielen

Das Ergebnis ist ein eleganter und dezenter Effekt, ideal für Zuhause oder Büro.

## ✨ Hauptfunktionen

### 🕑 Automatische Zeitansage
- jede Stunde (xx:00)
- jede halbe Stunde (xx:30) - optional

### 🌐 Automatische Mehrsprachunterstützung
- Italienisch 🇮🇹
- Englisch 🇬🇧
- Französisch 🇫🇷
- Deutsch 🇩🇪 (mit korrekter Behandlung von "halb")
- Spanisch 🇪🇸
- Polish 🇵🇱
- 
automatischer Fallback auf Italienisch

### ⏱️ Konfigurierbares Zeitfenster
- z.B. nur von 8:00 bis 22:00 Uhr

###  🔔 Optionale Glocke
- 🎵 12 voreingestellte Töne zur Auswahl
- 🎶 Möglichkeit, eine benutzerdefinierte Audiodatei zu verwenden
- 🔕 Alexa "announce" Benachrichtigungston (Standard)

### 🧪 Testfunktion
- um die Ansage sofort auszuprobieren

### 🎯 Verhalten

**Glocke (Chime):**
- **Verfügbare Presets**: 12 Töne darunter church-bell, simple-bell, clock-chime, usw.
- **Benutzerdefinierter Ton**: Wählen Sie "custom" und geben Sie den Pfad Ihrer Audiodatei ein
- **Standard**: Alexa "announce" Ton (wenn Sie nichts auswählen)
- **Deaktiviert**: Deaktivieren Sie "use_chime" für keinen Ton vor der Ansage

**Westminster-Melodie (Tower Clock):**
- Separate Option "tower_clock"
- Spielt **nur um 12:00 Uhr** (Mittag)
- Ersetzt den normalen Chime zu dieser Zeit

**Sprachansage:**
- **Aktiviert** (Standard): Alexa spricht die Uhrzeit nach der Glocke aus
- **Deaktiviert**: Nur Glockenton, keine Sprachansage

**Halbstunden-Ansagen:**
- **Aktiviert** (Standard): Ansagen um :00 und :30
- **Deaktiviert**: Nur Ansagen um :00

## ⚙️ Wie es funktioniert

Digital Pendulum synchronisiert sich mit der Systemuhr und prüft automatisch jede Minute, ob es Zeit für eine Ansage ist.

**Wenn die Ansage ausgelöst wird:**
1. 🔔 Spielt die gewählte Glocke ab (wenn aktiviert)
2. ⏱️ Wartet 1,2 Sekunden
3. 🗣️ Alexa spricht die Uhrzeit in der Home Assistant Sprache (wenn aktiviert)

Alles geschieht automatisch, ohne Automationen konfigurieren zu müssen!

## 🗣️ Sprachverwaltung

Die Sprache wird automatisch erkannt von:

self.hass.config.language

Ansage-Beispiele:

| Sprache | Uhrzeit | Ansage |
|------|------|--------|
| 🇮🇹 IT | 10:30 | Ore 10 e trenta |
| 🇬🇧 EN | 14:00 | It's 14 o'clock |
| 🇫🇷 FR | 9:30 | Il est 9 heures trente |
| 🇩🇪 DE | 16:30 | Es ist halb 17 |
| 🇪🇸 ES | 11:00 | Son las 11 |
| 🇵🇱 PL | 15:30 |Jest godzina 15:30 |

## 🔔 Chime (Eröffnungsglocke)

Wenn die Option use_chime aktiv ist:
- wird der Alexa-Benachrichtigungston oder der gewählte Ton abgespielt
- wartet das System 1,2 Sekunden
- beginnt die Sprachansage (wenn aktiviert)

Dies erzeugt einen Effekt ähnlich einem echten Pendel 🎶.

## 🧩 Konfigurationsoptionen

| Option | Beschreibung |
|------|------------|
| player | Ziel-Alexa-Gerät |
| start_hour | Betriebsstartzeit |
| end_hour | Betriebsendzeit |
| enabled | Aktiviert/deaktiviert das Pendel |
| announce_half_hours | Aktiviert Ansagen jede halbe Stunde (sonst nur jede Stunde) |
| voice_announcement | Aktiviert/deaktiviert die Sprachzeitansage |
| tower_clock | Aktiviert Westminster-Melodie um 12:00 Uhr |
| use_chime | Aktiviert/deaktiviert die Glocke vor der Ansage |
| preset_chime | Wahl des Glockenklangs (12 verfügbare Presets) |
| custom_chime_path | Pfad für benutzerdefinierten Glockenklang |

Standardwerte:

- ⏰ start_hour → 8
- ⏰ end_hour → 22
- 🔔 use_chime → True
- 🗣️ voice_announcement → True
- ⏰ announce_half_hours → True
- 🏰 tower_clock → False
- ✅ enabled → True

## 🧪 Soforttest

Eine manuelle Testmethode ist verfügbar:

Diese Funktion:
- die aktuelle Uhrzeit liest
- einen vollständigen Satz generiert (z.B. "Es ist 15 Uhr 42")
- ihn sofort auf dem Alexa-Gerät wiedergibt  

Nützlich zur Überprüfung von: Sprache, Lautstärke, Chime, korrektem TTS-Betrieb

## 🔍 Statussensor

Digital Pendulum enthält einen Diagnosesensor:

`binary_sensor.digital_pendulum_status_warning`

**Zustände:**
- ✅ **OFF** - Alles funktioniert einwandfrei
- ⚠️ **ON** - Probleme erkannt (Integration deaktiviert, Alexa offline, usw.)

**Verwendung:**
- Dashboard-Überwachung
- Automatisierungen für Benachrichtigungen
- Schnelldiagnose

## 📦 Voraussetzungen

> ✨ **Verfügbar auf HACS** - vereinfachte Installation und Updates!

- 🏠 Home Assistant 2024.1.0 oder höher
- 🔊 Alexa Media Player installiert und funktionsfähig
- 📡 Alexa-Gerät als Player konfiguriert

## 💾 Installation

### Über HACS (empfohlen)

1. Öffnen Sie **HACS** im Seitenmenü
2. Gehen Sie zu **Integrationen**
3. Suchen Sie nach **"Digital Pendulum"**
4. Klicken Sie auf **Herunterladen**
5. **Home Assistant neu starten**
6. Gehen Sie zu **Einstellungen** → **Geräte und Dienste** → **Integration hinzufügen**
7. Suchen Sie nach **"Digital Pendulum"**
8. Folgen Sie der geführten Konfiguration

### Manuelle Installation

1. Laden Sie die neueste Version von [GitHub](https://github.com/Dregi56/digital_pendulum/releases) herunter
2. Extrahieren Sie die Dateien
3. Kopieren Sie den Ordner `digital_pendulum` nach `config/custom_components/`
4. Home Assistant neu starten
5. Gehen Sie zu **Einstellungen** → **Geräte und Dienste** → **Integration hinzufügen**
6. Suchen Sie nach **"Digital Pendulum"**
7. Folgen Sie der geführten Konfiguration


## 🎯 Ideale Verwendung

- ✔️ Smart Homes
- ✔️ Büros
- ✔️ Gemeinschaftsbereiche
- ✔️ Effekt "modernes Pendel"
- ✔️ Nicht-invasive Zeiterinnerung

## 🔧 Fehlerbehebung

### Fehler "Cannot find EU skill" oder Alexa-Probleme

Problem mit **Alexa Media Player**, nicht mit Digital Pendulum.

**Schnelle Lösung:**
1. Einstellungen → Geräte und Dienste → Alexa Media Player
2. Drei Punkte → Neu laden
3. Falls es nicht funktioniert: Alexa Media Player deinstallieren und neu installieren

---

### Falsche Sprache

Digital Pendulum verwendet automatisch die Home Assistant Sprache.

1. Überprüfen Sie: Einstellungen → System → Allgemein → Sprache
2. Unterstützte Sprachen: 🇮🇹 🇬🇧 🇫🇷 🇩🇪 🇪🇸
3. Nach dem Ändern der Sprache Home Assistant neu starten

---

### Keine Ansagen

**Überprüfen Sie:**
- Integration aktiviert? (Schalter EIN)
- Befinden Sie sich im konfigurierten Zeitfenster? (Standard 8:00-22:00 Uhr)
- Alexa-Gerät online?
- Versuchen Sie die Schaltfläche "Test"

---

### Nur Glocke oder nur Stimme

- **Nur Glocke:** Aktivieren Sie "Voice announcement"
- **Nur Stimme:** Aktivieren Sie "Use chime"

---

### Westminster läutet nicht um 12 Uhr

- Überprüfen Sie, ob "Tower Clock" aktiv ist
- Funktioniert **nur um 12:00 Uhr** (Mittag, nicht Mitternacht)

---

## 🚀 Mögliche zukünftige Entwicklungen

- ⏳ Ansagen alle 15 Minuten
- 🔇 Automatische Nachtlautstärke
- 🗓️ Tagesansage
- 📣 Unterstützung anderer TTS

---

## 

## ☕ Unterstützen Sie das Projekt

Gefällt Ihnen dieses Projekt? Wenn Sie es nützlich finden, spendieren Sie mir einen virtuellen Kaffee, um zukünftige Entwicklungen zu unterstützen! Jeder kleine Beitrag wird sehr geschätzt. 🙏

**Digital Pendulum ist und bleibt immer kostenlos und Open Source.** Spenden sind vollkommen freiwillig! ❤️


[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/dregi56)

💡 **Bevorzugen Sie andere Methoden?** Sie können verwenden:

[![revolut](https://img.shields.io/badge/Revolut-0075EB?style=for-the-badge&logo=revolut&logoColor=white)](https://revolut.me/egidio5t9d)
