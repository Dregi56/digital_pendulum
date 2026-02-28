# 🕰️ Digital Pendulum

Un pendolo digitale parlante per Home Assistant
<br>**Autore:** Egidio Ziggiotto (Dregi56)  e-mail: [dregi@cyberservices.com](mailto:dregi@cyberservices.com)

[![HACS](https://img.shields.io/badge/HACS-Default-41BDF5.svg)](https://hacs.xyz/)
[![Version](https://img.shields.io/github/v/release/Dregi56/digital_pendulum)](https://github.com/Dregi56/digital_pendulum/releases)
![License](https://img.shields.io/github/license/Dregi56/digital_pendulum)
[![GitHub stars](https://img.shields.io/github/stars/Dregi56/digital_pendulum?style=social)](https://github.com/Dregi56/digital_pendulum)

🌍 Lingue disponibili:
[Italiano](README.it.md) |
[English](README.en.md) |
[Español](README.es.md) |
[Deutsch](README.de.md) |
[Français](README.fr.md) |
[Polski](README.pl.md) |
[Čeština](README.cs.md) |
[Slovenčina](README.sk.md) |
[Português](README.pt.md)

<br>👉Questo è README in italiano. Usa il selettore di linguaggio qui sopra.


## ❤️ Ti piace Digital Pendulum?

Se lo trovi utile, considera di lasciare una ⭐ su GitHub:  
👉 **https://github.com/Dregi56/digital_pendulum**
<br>Grazie.

## 📌 Descrizione

Digital Pendulum è un'integrazione custom per Home Assistant che annuncia vocalmente l'ora, proprio come un pendolo digitale 🕰️.

Utilizzando uno smart speaker compatibile come player, il sistema:

- 📢 annuncia l'ora ogni ora e/o ogni mezz'ora (configurabile)
- 🌍 parla automaticamente nella lingua impostata in Home Assistant  
- ⏰ funziona solo in una fascia oraria configurabile 
- 🔔 può riprodurre un suono personalizzato prima dell'annuncio
- 🔕 può disabilitare l'annuncio vocale (solo campana)
- 🏰 può suonare il carillon Westminster alle 12:00

Il risultato è un effetto elegante e discreto, ideale per casa o ufficio.

## 🔊 Dispositivi Supportati

Digital Pendulum supporta tre tipi di player:

| Tipo | Descrizione | Requisito |
|------|-------------|-----------|
| **Alexa** | Dispositivi Amazon Echo | [alexa_media_player](https://github.com/custom-components/alexa_media_player) via HACS |
| **Google Home / Nest** | Google Home, Nest Mini, Nest Hub, Chromecast | Integrazione Google Cast (nativa in HA) |
| **Generic** | Qualsiasi altro dispositivo media_player di HA | Motore TTS configurato in HA (funzionalità può variare) |

Durante la configurazione ti verrà chiesto di selezionare prima il tipo di player, poi il dispositivo specifico.

## ✨ Funzionalità principali

### 🕑 Annuncio automatico dell'ora
- ogni ora (xx:00)
- ogni mezz'ora (xx:30) - opzionale

### 🌐 Supporto multilingua automatico
- Italiano 🇮🇹
- Inglese 🇬🇧
- Francese 🇫🇷
- Tedesco 🇩🇪 (con gestione corretta di "halb")
- Spagnolo 🇪🇸
- Polacco 🇵🇱
- Ceco 🇨🇿
- Slovacco 🇸🇰
- Portoghese 🇵🇹
  
fallback automatico in italiano

### ⏱️ Fascia oraria configurabile
- es. solo dalle 8:00 alle 22:00

###  🔔 Campana opzionale
- 🎵 12 suoni preimpostati tra cui scegliere
- 🎶 opzione per usare un file audio personalizzato
- 🔕 suono di notifica predefinito (se non si seleziona nulla)

### 🧪 Funzione di test
- per provare immediatamente l'annuncio

### 🎯 Comportamento

**Campana (Chime):**
- **Preset disponibili**: 12 suoni tra cui church-bell, simple-bell, clock-chime, ecc.
- **Suono personalizzato**: Seleziona "custom" e inserisci il percorso del tuo file audio
- **Predefinito**: suono di notifica (se non selezioni nulla)
- **Disabilitato**: Disabilita "use_chime" per nessun suono prima dell'annuncio

**Melodia Westminster (Torre dell'orologio):**
- Opzione separata "tower_clock"
- Suona **solo alle 12:00** (mezzogiorno)
- Sostituisce il normale chime in quel momento

**Annuncio vocale:**
- **Abilitato** (predefinito): il dispositivo pronuncia l'ora dopo la campana
- **Disabilitato**: solo suono della campana, nessun annuncio vocale

**Annunci ogni mezz'ora:**
- **Abilitati** (predefinito): annunci alle :00 e alle :30
- **Disabilitati**: annunci solo alle :00

## ⚙️ Come funziona

Digital Pendulum si sincronizza con l'orologio di sistema e controlla automaticamente ogni minuto se è il momento di fare un annuncio.

**Quando scatta l'annuncio:**
1. 🔔 Riproduce la campana scelta (se abilitata)
2. ⏱️ Attende 1,2 secondi
3. 🗣️ Il dispositivo pronuncia l'ora nella lingua di Home Assistant (se abilitato)

Tutto avviene automaticamente senza bisogno di configurare automazioni!

## 🗣️ Gestione della lingua

La lingua viene rilevata automaticamente da:

self.hass.config.language

Esempi di annuncio:

| Lingua | Ora | Annuncio |
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

## 🔔 Chime (campana iniziale)

Se l'opzione use_chime è attiva:
- viene riprodotto il suono di notifica o il suono scelto
- il sistema attende 1,2 secondi
- inizia l'annuncio vocale (se abilitato)

Questo crea un effetto simile a un vero pendolo 🎶.

## 🧩 Opzioni di configurazione

| Opzione | Descrizione |
|------|------------|
| player_type | Tipo di dispositivo player (Alexa, Google Home, Generic) |
| player | Dispositivo di destinazione |
| start_hour | Ora di inizio operatività |
| end_hour | Ora di fine operatività |
| enabled | Abilita/disabilita il pendolo |
| announce_half_hours | Abilita annunci ogni mezz'ora (altrimenti solo ogni ora) |
| voice_announcement | Abilita/disabilita l'annuncio vocale dell'ora |
| tower_clock | Abilita la melodia Westminster alle 12:00 |
| use_chime | Abilita/disabilita la campana prima dell'annuncio |
| preset_chime | Scelta del suono della campana (12 preset disponibili) |
| custom_chime_path | Percorso per suono campana personalizzato |

Valori predefiniti:

- ⏰ start_hour → 8
- ⏰ end_hour → 22
- 🔔 use_chime → True
- 🗣️ voice_announcement → True
- ⏰ announce_half_hours → True
- 🏰 tower_clock → False
- ✅ enabled → True

## 🧪 Test immediato

È disponibile un metodo di test manuale che:
- legge l'ora corrente
- genera una frase completa (es. "Sono le 15 e 42 minuti")
- la riproduce immediatamente sul dispositivo selezionato

Utile per verificare: lingua, volume, chime, corretto funzionamento del TTS

## 🔍 Sensore di stato

Digital Pendulum include un sensore diagnostico:

`binary_sensor.digital_pendulum_status_warning`

**Stati:**
- ✅ **OFF** - Tutto funziona correttamente
- ⚠️ **ON** - Problemi rilevati (integrazione disabilitata, Alexa offline, ecc.)

**Utilizzi:**
- Monitoraggio dashboard
- Automazioni per notifiche
- Diagnostica rapida

## 📦 Requisiti

> ✨ **Disponibile su HACS** - installazione e aggiornamenti semplificati!

- 🏠 Home Assistant 2024.1.0 o superiore
- 🔊 Un dispositivo media_player compatibile (vedi [Dispositivi Supportati](#-dispositivi-supportati))
- 📡 Per Alexa: [alexa_media_player](https://github.com/custom-components/alexa_media_player) installato via HACS
- 📡 Per Google Home / Nest: integrazione Google Cast (nativa in HA)

## 💾 Installazione

### Tramite HACS (consigliato)

1. Apri **HACS** nel menu laterale
2. Vai su **Integrazioni**
3. Cerca **"Digital Pendulum"**
4. Clicca su **Scarica**
5. **Riavvia Home Assistant**
6. Vai su **Impostazioni** → **Dispositivi e servizi** → **Aggiungi integrazione**
7. Cerca **"Digital Pendulum"**
8. Segui la configurazione guidata

### Installazione manuale

1. Scarica l'ultima versione da [GitHub](https://github.com/Dregi56/digital_pendulum/releases)
2. Estrai i file
3. Copia la cartella `digital_pendulum` in `config/custom_components/`
4. Riavvia Home Assistant
5. Vai su **Impostazioni** → **Dispositivi e servizi** → **Aggiungi integrazione**
6. Cerca **"Digital Pendulum"**
7. Segui la configurazione guidata


## 🎯 Uso ideale

- ✔️ Case intelligenti
- ✔️ Uffici
- ✔️ Aree comuni
- ✔️ Effetto "pendolo moderno"
- ✔️ Promemoria orario non invasivo

## 🔧 Risoluzione dei problemi

### Errore "Cannot find EU skill" o problemi con Alexa

Problema di **alexa_media_player**, non di Digital Pendulum.

**Soluzione rapida:**
1. Impostazioni → Dispositivi e servizi → Alexa Media Player
2. Tre puntini → Ricarica
3. Se non funziona: disinstalla e reinstalla Alexa Media Player

---

### Google Home / Nest: nessun annuncio vocale

Digital Pendulum usa il motore TTS configurato in HA per i dispositivi Google.

1. Verifica che un motore TTS sia configurato in HA (Impostazioni → Assistenti vocali)
2. Prova il pulsante "Test" per verificare
3. Controlla il log di HA per errori TTS

---

### Lingua errata

Digital Pendulum usa automaticamente la lingua di Home Assistant.

1. Controlla: Impostazioni → Sistema → Generale → Lingua
2. Lingue supportate: 🇮🇹 🇬🇧 🇫🇷 🇩🇪 🇪🇸 🇵🇱 🇨🇿 🇸🇰 🇵🇹
3. Dopo aver cambiato la lingua, riavvia Home Assistant

---

### Nessun annuncio

**Verifica:**
- Integrazione abilitata? (Switch ON)
- Sei nella fascia oraria configurata? (default 8:00-22:00)
- Dispositivo online?
- Tipo di player corretto selezionato? (Alexa, Google, Generic)
- Prova il pulsante "Test"

---

### Solo campana o solo voce

- **Solo campana:** Abilita "Annuncio vocale"
- **Solo voce:** Abilita "Usa chime"

---

### Westminster non suona alle 12

- Verifica che "Torre dell'orologio" sia attivo
- Funziona **solo alle 12:00** (mezzogiorno, non mezzanotte)

---

## 🚀 Possibili sviluppi futuri

- ⏳ Annunci ogni 15 minuti
- 🔇 Volume notturno automatico
- 🗓️ Annuncio del giorno
- 📣 Supporto per motori TTS e player aggiuntivi

---

## ☕ Supporta il progetto

Ti piace questo progetto? Se lo trovi utile, offrimi un caffè virtuale per supportare i futuri sviluppi! Ogni piccolo contributo è molto apprezzato. 🙏

**Digital Pendulum è e rimarrà sempre gratuito e open source.** Le donazioni sono completamente volontarie! ❤️


[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/dregi56)

💡 **Preferisci altri metodi?** Puoi usare:

[![revolut](https://img.shields.io/badge/Revolut-0075EB?style=for-the-badge&logo=revolut&logoColor=white)](https://revolut.me/egidio5t9d)

💡 **Preferisci altri metodi?** Puoi usare:

[![revolut](https://img.shields.io/badge/Revolut-0075EB?style=for-the-badge&logo=revolut&logoColor=white)](https://revolut.me/egidio5t9d)
