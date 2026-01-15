# 🕰️ Digital Pendulum

Un pendolo digitale parlante per Home Assistant
<br>**Autore:** Egidio Ziggiotto (Dregi56)  e-mail: [dregi@cyberservices.com](mailto:dregi@cyberservices.com)


[![HACS](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://hacs.xyz/)
[![Version](https://img.shields.io/github/v/release/Dregi56/digital_pendulum)](https://github.com/Dregi56/digital_pendulum/releases)
![License](https://img.shields.io/github/license/Dregi56/digital_pendulum)
[![GitHub stars](https://img.shields.io/github/stars/Dregi56/digital_pendulum?style=social)](https://github.com/Dregi56/digital_pendulum)


## ❤️ Ti piace Digital Pendulum?

Se ti è utile, considera di lasciare una ⭐ su GitHub:  
👉 **https://github.com/Dregi56/digital_pendulum**
<br>Grazie.

## 📌 Descrizione

Digital Pendulum è un’integrazione personalizzata per Home Assistant che annuncia vocalmente l’orario, proprio come un pendolo digitale 🕰️.


Utilizzando un dispositivo Alexa come speaker, il sistema:

- 📢 annuncia l’ora ogni 30 minuti  
- 🌍 parla automaticamente nella lingua impostata in Home Assistant  
- ⏰ funziona solo in una fascia oraria configurabile  
- 🔔 può riprodurre un suono di campanella (chime) prima dell’annuncio  

Il risultato è un effetto elegante e discreto, ideale per casa o ufficio.

## ✨ Funzionalità principali

### 🕑 Annuncio automatico dell’orario
- ogni ora (xx:00)
- ogni mezz’ora (xx:30)

### 🌐 Supporto multilingua automatico
- Italiano 🇮🇹
- Inglese 🇬🇧
- Francese 🇫🇷
- Tedesco 🇩🇪 (con gestione corretta di “halb”)
- Spagnolo 🇪🇸

fallback automatico in italiano

### ⏱️ Fascia oraria configurabile
- es. solo dalle 8:00 alle 22:00

### 🔔 Chime opzionale
- breve annuncio silenzioso prima del TTS

### 🧪 Funzione di test
- per provare immediatamente l’annuncio

## ⚙️ Come funziona

Il cuore del sistema è la classe:

class DigitalPendulum

che:
- si registra a un timer interno (ogni 1 minuto)
- controlla:
  - se l’integrazione è abilitata
  - se l’orario rientra nella fascia consentita
  - se il minuto è 00 o 30
- costruisce il testo parlato in base alla lingua
- invia l’annuncio al dispositivo Alexa configurato

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
| 🇪🇸 ES | 11:00 | Son las 11 en punto |

## 🔔 Chime (campanella iniziale)

Se l’opzione use_chime è attiva:
- viene inviato un announce vuoto
- il sistema attende 1,5 secondi
- parte il TTS con l’orario  

Questo crea un effetto simile a un vero pendolo 🎶.

## 🧩 Opzioni di configurazione

| Opzione | Descrizione |
|------|------------|
| enabled | Abilita o disabilita il pendolo |
| start_hour | Ora di inizio funzionamento |
| end_hour | Ora di fine funzionamento |
| player | Dispositivo Alexa target |
| use_chime | Attiva/disattiva la campanella |

Valori di default:

- ⏰ start_hour → DEFAULT_START_HOUR  
- ⏰ end_hour → DEFAULT_END_HOUR  
- 🔔 use_chime → DEFAULT_USE_CHIME  
- ✅ enabled → DEFAULT_ENABLED  

## 🧪 Test immediato

È disponibile un metodo di test manuale:

async_test_announcement()

Che:
- legge l’orario attuale
- genera una frase completa (es. “Ore 15 e 42”)
- la riproduce subito sul dispositivo Alexa  

Utile per verificare: lingua, volume, chime, corretto funzionamento del TTS

## 📦 Requisiti

- 🏠 Home Assistant
- 🔊 Alexa Media Player installato e funzionante
- 📡 Dispositivo Alexa configurato come player

## 🎯 Uso ideale

- ✔️ Case intelligenti
- ✔️ Uffici
- ✔️ Ambienti comuni
- ✔️ Effetto “pendolo moderno”
- ✔️ Promemoria temporale non invasivo

## 🚀 Possibili evoluzioni future

- ⏳ Annunci ogni 15 minuti
- 🔇 Volume automatico notturno
- 🗓️ Annuncio del giorno
- 🎵 Suoni personalizzati
- 📣 Supporto ad altri TTS

---

## 

## ☕ Supporta il progetto

Ti piace questo progetto? Se lo trovi utile, offrimi un caffè virtuale per sostenere le evoluzioni future! Ogni piccolo contributo è super apprezzato. 🙏

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/dregi56)

💡 **Preferisci altri metodi?** Puoi usare:

[![revolut](https://img.shields.io/badge/Revolut-0075EB?style=for-the-badge&logo=revolut&logoColor=white)](https://revolut.me/egidio5t9d)