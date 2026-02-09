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
[Français](README.fr.md) 
<br>👉This is the Italian README. Use the language selector above


## ❤️ Ti piace Digital Pendulum?

Se ti è utile, considera di lasciare una ⭐ su GitHub:  
👉 **https://github.com/Dregi56/digital_pendulum**
<br>Grazie.

## 📌 Descrizione

Digital Pendulum è un'integrazione personalizzata per Home Assistant che annuncia vocalmente l'orario, proprio come un pendolo digitale 🕰️.


Utilizzando un dispositivo Alexa come speaker, il sistema:

- 📢 annuncia l'orario ogni ora e/o ogni mezz'ora (configurabile)
- 🌍 parla automaticamente nella lingua impostata in Home Assistant  
- ⏰ funziona solo in una fascia oraria configurabile 
- 🔔 può riprodurre un suono personalizzato prima dell'annuncio
- 🔕 può disabilitare l'annuncio vocale (solo campana)
- 🏰 può riprodurre la melodia Westminster alle ore 12

Il risultato è un effetto elegante e discreto, ideale per casa o ufficio.

## ✨ Funzionalità principali

### 🕑 Annuncio automatico dell'orario
- ogni ora (xx:00)
- ogni mezz'ora (xx:30) - opzionale

### 🌐 Supporto multilingua automatico
- Italiano 🇮🇹
- Inglese 🇬🇧
- Francese 🇫🇷
- Tedesco 🇩🇪 (con gestione corretta di "halb")
- Spagnolo 🇪🇸

fallback automatico in italiano

### ⏱️ Fascia oraria configurabile
- es. solo dalle 8:00 alle 22:00

###  🔔 Campana opzionale
- 🎵 12 suoni predefiniti tra cui scegliere
- 🎶 possibilità di usare un file audio personalizzato
- 🔕 suono di notifica "announce" di Alexa (default)

### 🧪 Funzione di test
- per provare immediatamente l'annuncio

### 🎯 Comportamento

**Campana (Chime):**
- **Preset disponibili**: 12 suoni tra cui church-bell, simple-bell, clock-chime, ecc.
- **Suono personalizzato**: Seleziona "custom" e inserisci il path del tuo file audio
- **Default**: Suono "announce" di Alexa (se non selezioni nulla)
- **Disattivato**: Disabilita "use_chime" per nessun suono prima dell'annuncio

**Melodia Westminster (Tower Clock):**
- Opzione separata "tower_clock"
- Suona **solo alle ore 12:00** (mezzogiorno)
- Sostituisce il chime normale a quell'ora

**Annuncio vocale:**
- **Abilitato** (default): Alexa pronuncia l'ora dopo la campana
- **Disabilitato**: Solo suono campana, nessun annuncio vocale

**Annunci mezz'ora:**
- **Abilitato** (default): Annunci alle :00 e :30
- **Disabilitato**: Solo annunci alle :00

## ⚙️ Come funziona

Il cuore del sistema è la classe:

class DigitalPendulum

che:
- si registra a un timer interno sincronizzato (ogni minuto allo :00 dei secondi)
- controlla:
  - se l'integrazione è abilitata
  - se l'orario rientra nella fascia consentita
  - se il minuto è :00 (o :30 se abilitato)
- costruisce il testo parlato in base alla lingua
- riproduce la campana (se abilitata)
- invia l'annuncio vocale al dispositivo Alexa (se abilitato)

## 🗣️ Gestione delle lingue

La lingua viene rilevata automaticamente da:

self.hass.config.language

Esempi di annunci:

| Lingua | Orario | Annuncio |
|------|------|--------|
| 🇮🇹 IT | 10:30 | Ore 10 e trenta |
| 🇬🇧 EN | 14:00 | It's 14 o'clock |
| 🇫🇷 FR | 9:30 | Il est 9 heures trente |
| 🇩🇪 DE | 16:30 | Es ist halb 17 |
| 🇪🇸 ES | 11:00 | Son las 11 |

## 🔔 Chime (campana iniziale)

Se l'opzione use_chime è attiva:
- viene riprodotto il suono di notifica di Alexa o il suono scelto
- il sistema attende 1,2 secondi
- parte l'annuncio vocale (se abilitato)

Questo crea un effetto simile a un vero pendolo 🎶.

## 🧩 Opzioni di configurazione

| Opzione | Descrizione |
|------|------------|
| player | Dispositivo Alexa target |
| start_hour | Ora di inizio funzionamento |
| end_hour | Ora di fine funzionamento |
| enabled | Abilita/disabilita il pendolo |
| announce_half_hours | Abilita annunci ogni mezz'ora (altrimenti solo ogni ora) |
| voice_announcement | Abilita/disabilita l'annuncio vocale dell'ora |
| tower_clock | Abilita melodia Westminster alle ore 12:00 |
| use_chime | Attiva/disattiva la campana prima dell'annuncio |
| preset_chime | Scelta del suono campana (12 preset disponibili) |
| custom_chime_path | Path per suono campana personalizzato |

Valori di default:

- ⏰ start_hour → 8
- ⏰ end_hour → 22
- 🔔 use_chime → True
- 🗣️ voice_announcement → True
- ⏰ announce_half_hours → True
- 🏰 tower_clock → False
- ✅ enabled → True

## 🧪 Test immediato

È disponibile un metodo di test manuale:

async_test_announcement()

Che:
- legge l'orario attuale
- genera una frase completa (es. "Ore 15 e 42")
- la riproduce subito sul dispositivo Alexa  

Utile per verificare: lingua, volume, chime, corretto funzionamento del TTS

## 📦 Requisiti

> ✨ **Disponibile su HACS** - installazione e aggiornamenti semplificati!

- 🏠 Home Assistant 2024.1.0 o superiore
- 🔊 Alexa Media Player installato e funzionante
- 📡 Dispositivo Alexa configurato come player


## 🎯 Uso ideale

- ✔️ Case intelligenti
- ✔️ Uffici
- ✔️ Ambienti comuni
- ✔️ Effetto "pendolo moderno"
- ✔️ Promemoria temporale non invasivo

## 🚀 Possibili evoluzioni future

- ⏳ Annunci ogni 15 minuti
- 🔇 Volume automatico notturno
- 🗓️ Annuncio del giorno
- 📣 Supporto ad altri TTS

---

## 

## ☕ Supporta il progetto

Ti piace questo progetto? Se lo trovi utile, offrimi un caffè virtuale per sostenere le evoluzioni future! Ogni piccolo contributo è super apprezzato. 🙏

**Digital Pendulum è e rimarrà sempre gratuito e open source.** Le donazioni sono completamente volontarie! ❤️


[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/dregi56)

💡 **Preferisci altri metodi?** Puoi usare:

[![revolut](https://img.shields.io/badge/Revolut-0075EB?style=for-the-badge&logo=revolut&logoColor=white)](https://revolut.me/egidio5t9d)
