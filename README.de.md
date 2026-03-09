# 🕰️ Digital Pendulum

Eine sprechende digitale Pendeluhr für Home Assistant
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
[Polski](README.pl.md) |
[Čeština](README.cs.md) |
[Slovenčina](README.sk.md) |
[Português](README.pt.md)

<br>👉 Dies ist die deutsche README. Verwenden Sie die Sprachauswahl oben.

## ❤️ Gefällt Ihnen Digital Pendulum?

Wenn Sie es nützlich finden, hinterlassen Sie bitte ein ⭐ auf GitHub:  
👉 **https://github.com/Dregi56/digital_pendulum**
<br>Vielen Dank.

## 📌 Beschreibung

Digital Pendulum ist eine benutzerdefinierte Integration für Home Assistant, die die Uhrzeit ansagt, genau wie eine digitale Pendeluhr 🕰️.

Mit einem kompatiblen Smart Speaker als Wiedergabegerät:

- 📢 gibt das System die Uhrzeit jede Stunde und/oder jede halbe Stunde bekannt (konfigurierbar)
- 🌍 spricht es automatisch in der in Home Assistant eingestellten Sprache
- ⏰ arbeitet es nur innerhalb eines konfigurierbaren Zeitfensters
- 🔔 kann es einen benutzerdefinierten Klang vor der Ansage abspielen
- 🔕 kann die Sprachansage deaktiviert werden (nur Glocke)
- 🏰 kann es den Westminster-Chime um 12 Uhr abspielen

Das Ergebnis ist ein eleganter und dezenter Effekt, ideal für Zuhause oder Büro.

## 🔊 Unterstützte Geräte

Digital Pendulum unterstützt drei Wiedergabetypen:

| Typ | Beschreibung | Voraussetzung |
|------|-------------|-------------|
| **Alexa** | Amazon Echo Geräte | [alexa_media_player](https://github.com/custom-components/alexa_media_player) über HACS |
| **Google Home / Nest** | Google Home, Nest Mini, Nest Hub, Chromecast | Google Cast (native HA-Integration) |
| **Generisch** | Jedes andere HA media_player Gerät | TTS-Engine in HA konfiguriert (Funktionalität kann variieren) |

Bei der Einrichtung werden Sie zuerst gebeten, den Wiedergabetyp auszuwählen, dann das spezifische Gerät.

## ✨ Hauptfunktionen

### 🕑 Automatische Zeitansage
- jede Stunde (xx:00)
- jede halbe Stunde (xx:30) - optional (nur Glocke oder Glocke + Stimme, konfigurierbar)

### ⏱️ Konfigurierbare Verzögerung nach dem Glockenton
- einstellbare Wartezeit zwischen Glockenton und Sprachansage (Standard: 1,2 Sekunden)
- besonders nützlich für Google Home / Nest Geräte, die möglicherweise eine längere Verzögerung benötigen, um die Sprachansage korrekt abzuspielen

### 🌐 Automatische Mehrsprachunterstützung
- Italiano 🇮🇹
- English 🇬🇧
- Français 🇫🇷
- Deutsch 🇩🇪
- Español 🇪🇸
- Polski 🇵🇱
- Čeština 🇨🇿
- Slovenčina 🇸🇰
- Português 🇵🇹

automatischer Rückfall auf Italienisch

🌐 **Anpassbare Sprache:** Es ist möglich, eine andere Sprache als die in Home Assistant eingestellte zu wählen (nützlich zum Beispiel für diejenigen, die HA auf Englisch haben).

### 🕐 Konfigurierbares Zeitfenster
- z.B. nur von 8:00 bis 22:00

### 🔔 Optionale Glocke
- 🎵 12 voreingestellte Klänge zur Auswahl
- 🎶 Möglichkeit, eine benutzerdefinierte Audiodatei zu verwenden
- 🔕 Standard-Benachrichtigungston (wenn nichts ausgewählt ist)

### 🧪 Testfunktion
- zum sofortigen Ausprobieren der Ansage

### 🎯 Verhalten

**Glocke (Chime):**
- **Verfügbare Voreinstellungen**: 12 Klänge einschließlich church-bell, simple-bell, clock-chime usw.
- **Benutzerdefinierter Klang**: Wählen Sie "custom" und geben Sie den Pfad Ihrer Audiodatei ein
- **Standard**: Benachrichtigungston (wenn Sie nichts auswählen)
- **Deaktiviert**: Deaktivieren Sie "use_chime" für keinen Klang vor der Ansage

**Westminster-Melodie (Turmuhr):**
- Separate Option "tower_clock"
- Wird **nur um 12:00** (Mittag) abgespielt
- Ersetzt den normalen Glockenton zu dieser Zeit

**Sprachansage:**
- **Aktiviert** (Standard): Das Gerät spricht die Uhrzeit nach der Glocke aus
- **Deaktiviert**: Nur Glockenton, keine Sprachansage

**Sprachansage zur halben Stunde:**
- **Aktiviert** (Standard): Sprachansage wird sowohl um :00 als auch um :30 abgespielt
- **Deaktiviert**: Glocke spielt weiterhin um :30, aber keine Sprachansage

## ⚙️ Funktionsweise

Digital Pendulum synchronisiert sich mit der Systemuhr und überprüft automatisch jede Minute, ob es Zeit für eine Ansage ist.

**Wenn die Ansage ausgelöst wird:**
1. 🔔 Spielt den gewählten Glockenton ab (wenn aktiviert)
2. ⏱️ Wartet eine konfigurierbare Anzahl von Sekunden (Standard: 1,2 s) — erhöhen Sie diesen Wert für Google Home / Nest Geräte, wenn die Sprachansage nicht korrekt abgespielt wird
3. 🗣️ Das Gerät spricht die Uhrzeit in der Home Assistant Sprache aus (wenn aktiviert)

Alles geschieht automatisch ohne die Notwendigkeit, Automatisierungen zu konfigurieren!

## 🗣️ Sprachverarbeitung

Die Sprache wird automatisch von Home Assistant erkannt.

🌐 **Sprache der Ansagen:** Möglichkeit, die Sprache der Sprachansagen unabhängig von der in Home Assistant eingestellten Sprache zu wählen (verfügbar: Italiano, English, Deutsch, Español, Français, Português, Polski, Čeština, Slovenčina, oder Automatisch um der Sprache von Home Assistant zu folgen).

Ansagebeispiele:

| Sprache | Zeit | Ansage |
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

## 🔔 Glockenton (Einleitungsklang)

Wenn die Option use_chime aktiv ist:
- wird der Benachrichtigungston oder der gewählte Klang abgespielt
- wartet das System eine konfigurierbare Anzahl von Sekunden (Standard: 1,2)
- beginnt die Sprachansage (wenn aktiviert)

Dies erzeugt einen Effekt ähnlich einer echten Pendeluhr 🎶.

## 🧩 Konfigurationsoptionen

| Option | Beschreibung |
|------|------------|
| player_type | Typ des Wiedergabegeräts (Alexa, Google Home, Generisch) |
| player | Zielgerät |
| start_hour | Betriebsbeginn |
| end_hour | Betriebsende |
| enabled | Aktiviert/deaktiviert das Pendel |
| announce_half_hours | Aktiviert Ansagen jede halbe Stunde (sonst nur jede Stunde) |
| after_chime_delay | Wartezeit in Sekunden zwischen Glockenton und Sprachansage (Standard: 1,2) |
| announce_half_hours_voice | Aktiviert/deaktiviert Sprachansage zur halben Stunde (Glocke spielt weiterhin) |
| voice_announcement | Aktiviert/deaktiviert die Zeitsprachansage |
| tower_clock | Aktiviert Westminster-Melodie um 12:00 |
| use_chime | Aktiviert/deaktiviert den Glockenton vor der Ansage |
| preset_chime | Auswahl des Glockentons (12 verfügbare Voreinstellungen) |
| custom_chime_path | Pfad für benutzerdefinierten Glockenton |

Standardwerte:

- ⏰ start_hour → 8
- ⏰ end_hour → 22
- 🔔 use_chime → True
- 🗣️ voice_announcement → True
- ⏰ announce_half_hours → True
- 🏰 tower_clock → False
- ✅ enabled → True
- ⏱️ after_chime_delay → 1,2
- 🔇 announce_half_hours_voice → True

## 🧪 Sofortiger Test

Eine manuelle Testmethode ist verfügbar:

Diese:
- liest die aktuelle Uhrzeit
- generiert einen vollständigen Satz (z.B. "Es ist 15 Uhr 42")
- spielt ihn sofort auf dem ausgewählten Gerät ab

Nützlich zur Überprüfung: Sprache, Lautstärke, Glockenton, korrekte TTS-Funktion

## 🔍 Statussensor

Digital Pendulum enthält einen Diagnosesensor:

`binary_sensor.digital_pendulum_status_warning`

**Zustände:**
- ✅ **OFF** - Alles funktioniert korrekt
- ⚠️ **ON** - Probleme erkannt (Integration deaktiviert, Alexa offline usw.)

**Verwendung:**
- Dashboard-Überwachung
- Benachrichtigungsautomatisierungen
- Schnelldiagnose

## 📦 Anforderungen

> ✨ **Verfügbar auf HACS** - vereinfachte Installation und Updates!

- 🏠 Home Assistant 2024.1.0 oder höher
- 🔊 Ein kompatibles media_player Gerät (siehe [Unterstützte Geräte](#-unterstützte-geräte))
- 📡 Für Alexa: [alexa_media_player](https://github.com/custom-components/alexa_media_player) über HACS installiert
- 📡 Für Google Home / Nest: Google Cast Integration (nativ in HA)

## 💾 Installation

### Über HACS (empfohlen)

1. Öffnen Sie **HACS** im Seitenmenü
2. Gehen Sie zu **Integrationen**
3. Suchen Sie nach **"Digital Pendulum"**
4. Klicken Sie auf **Herunterladen**
5. **Home Assistant neu starten**
6. Gehen Sie zu **Einstellungen** → **Geräte & Dienste** → **Integration hinzufügen**
7. Suchen Sie nach **"Digital Pendulum"**
8. Folgen Sie der geführten Konfiguration

### Manuelle Installation

1. Laden Sie die neueste Version von [GitHub](https://github.com/Dregi56/digital_pendulum/releases) herunter
2. Entpacken Sie die Dateien
3. Kopieren Sie den Ordner `digital_pendulum` nach `config/custom_components/`
4. Home Assistant neu starten
5. Gehen Sie zu **Einstellungen** → **Geräte & Dienste** → **Integration hinzufügen**
6. Suchen Sie nach **"Digital Pendulum"**
7. Folgen Sie der geführten Konfiguration

## 🎯 Ideale Verwendung

- ✔️ Smart Homes
- ✔️ Büros
- ✔️ Gemeinschaftsbereiche
- ✔️ Effekt einer "modernen Pendeluhr"
- ✔️ Unaufdringliche Zeiterinnerung

## 🔧 Fehlerbehebung

### Alexa-Probleme oder Fehler "Cannot find EU skill"

Problem mit **alexa_media_player**, nicht mit Digital Pendulum.

**Schnelle Lösung:**
1. Einstellungen → Geräte und Dienste → Alexa Media Player
2. Drei Punkte → Neu laden
3. Wenn es nicht funktioniert: Alexa Media Player deinstallieren und neu installieren

---

### Google Home / Nest: keine Sprachansage

Digital Pendulum verwendet die in HA konfigurierte TTS-Engine für Google Geräte.

Dies ist ein bekanntes Timing-Problem bei Google Geräten. Die Sprachansage kann unterbrochen oder übersprungen werden, wenn die Verzögerung nach dem Glockenton zu kurz ist.

1. Überprüfen Sie, ob eine TTS-Engine in HA konfiguriert ist (Einstellungen → Sprachassistenten)
2. Überprüfen Sie das HA-Protokoll auf TTS-Fehler
3. Erhöhen Sie den Wert **"Verzögerung nach dem Glockenton"** (versuchen Sie 2,0 oder 3,0 Sekunden)
4. Verwenden Sie die Schaltfläche "Test" zur Überprüfung

---

### Falsche Sprache

Digital Pendulum verwendet automatisch die Home Assistant Sprache.

1. Überprüfen Sie: Einstellungen → System → Allgemein → Sprache
2. Unterstützte Sprachen: 🇮🇹 🇬🇧 🇫🇷 🇩🇪 🇪🇸 🇵🇱 🇨🇿 🇸🇰 🇵🇹
3. Nach einer Sprachänderung Home Assistant neu starten

---

### Keine Ansagen

**Überprüfen Sie:**
- Integration aktiviert? (Schalter ON)
- Befinden Sie sich im konfigurierten Zeitfenster? (Standard 8:00-22:00)
- Gerät online?
- Richtiger Wiedergabetyp ausgewählt? (Alexa, Google, Generisch)
- Versuchen Sie die Schaltfläche "Test"

---

### Nur Glocke oder nur Stimme

- **Nur Glocke:** Aktivieren Sie "Sprachansage"
- **Nur Stimme:** Aktivieren Sie "Glockenton verwenden"

---

### Westminster spielt nicht um 12

- Überprüfen Sie, ob "Turmuhr" aktiv ist
- Funktioniert **nur um 12:00** (Mittag, nicht Mitternacht)

---

## 🚀 Mögliche zukünftige Entwicklungen

- ⏳ Ansagen alle 15 Minuten
- 🔇 Automatische Nachtlautstärke

---

## ☕ Unterstützen Sie das Projekt

Gefällt Ihnen dieses Projekt? Wenn Sie es nützlich finden, kaufen Sie mir einen virtuellen Kaffee zur Unterstützung zukünftiger Entwicklungen! Jeder kleine Beitrag wird sehr geschätzt. 🙏

**Digital Pendulum ist und bleibt immer kostenlos und Open Source.** Spenden sind völlig freiwillig! ❤️

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/dregi56)

💡 **Bevorzugen Sie andere Methoden?** Sie können verwenden:

[![revolut](https://img.shields.io/badge/Revolut-0075EB?style=for-the-badge&logo=revolut&logoColor=white)](https://revolut.me/egidio5t9d)
