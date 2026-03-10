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

<br>👉 Questo è il README in italiano. Usa il selettore di lingua qui sopra.

## ❤️ Ti piace Digital Pendulum?

Se lo trovi utile, considera di lasciare una ⭐ su GitHub:  
👉 **https://github.com/Dregi56/digital_pendulum**
<br>Grazie.

## 📌 Descrizione

Digital Pendulum è un'integrazione personalizzata per Home Assistant che annuncia vocalmente l'ora, proprio come un pendolo digitale 🕰️.

Utilizzando un altoparlante intelligente compatibile come player, il sistema:

- 📢 annuncia l'ora ogni ora e/o ogni mezz'ora (configurabile)
- 🌍 parla automaticamente nella lingua impostata in Home Assistant
- ⏰ funziona solo all'interno di una fascia oraria configurabile
- 🔔 può riprodurre un suono personalizzato prima dell'annuncio
- 🔕 può disabilitare l'annuncio vocale (solo campana)
- 🏰 può riprodurre il carillon di Westminster alle 12

Il risultato è un effetto elegante e discreto, ideale per la casa o l'ufficio.

## 🔊 Dispositivi supportati

Digital Pendulum supporta tre tipi di player:

| Tipo | Descrizione | Requisito |
|------|-------------|-------------|
| **Alexa** | Dispositivi Amazon Echo | [alexa_media_player](https://github.com/custom-components/alexa_media_player) tramite HACS |
| **Google Home / Nest** | Google Home, Nest Mini, Nest Hub, Chromecast | Google Cast (integrazione nativa HA) |
| **Generico** | Qualsiasi altro dispositivo HA media_player | Motore TTS configurato in HA (le funzionalità possono variare) |

Durante la configurazione ti verrà chiesto di selezionare prima il tipo di player, poi il dispositivo specifico.

## ✨ Funzionalità principali

### 🕑 Annuncio automatico dell'ora
- ogni ora (xx:00)
- ogni mezz'ora (xx:30) - opzionale (solo campana o campana + voce, configurabile)

### ⏱️ Pausa configurabile dopo la campana
- tempo di attesa regolabile tra la campana e l'annuncio vocale (default: 1,2 secondi)
- utile soprattutto per i dispositivi Google Home / Nest, che potrebbero aver bisogno di una pausa più lunga per riprodurre correttamente l'annuncio vocale

### 🌐 Supporto multilingua automatico
- Italiano 🇮🇹
- English 🇬🇧
- Français 🇫🇷
- Deutsch 🇩🇪
- Español 🇪🇸
- Polski 🇵🇱
- Čeština 🇨🇿
- Slovenčina 🇸🇰
- Português 🇵🇹

fallback automatico all'italiano

### 🕐 Fascia oraria configurabile
- es. solo dalle 8:00 alle 22:00

### 🔔 Campana opzionale
- 🎵 12 suoni preimpostati tra cui scegliere
- 🎶 opzione per usare un file audio personalizzato
- 🔕 suono di notifica predefinito (se non viene selezionato nulla)

### 🧪 Funzione di test
- per provare immediatamente l'annuncio

### 🎯 Comportamento

**Campana (Chime):**
- **Preset disponibili**: 12 suoni tra cui church-bell, simple-bell, clock-chime, ecc.
- **Suono personalizzato**: Seleziona "custom" e inserisci il percorso del tuo file audio
- **Predefinito**: suono di notifica (se non selezioni nulla)
- **Disabilitato**: Disabilita "use_chime" per nessun suono prima dell'annuncio

**Melodia di Westminster (Orologio a Torre):**
- Opzione separata "tower_clock"
- Suona **solo alle 12:00** (mezzogiorno)
- Sostituisce la campana normale in quel momento

**Annuncio vocale:**
- **Abilitato** (default): il dispositivo pronuncia l'ora dopo la campana
- **Disabilitato**: solo suono della campana, nessun annuncio vocale

**Annuncio vocale alla mezz'ora:**
- **Abilitato** (default): l'annuncio vocale viene riprodotto sia alle :00 che alle :30
- **Disabilitato**: la campana suona comunque alle :30, ma senza annuncio vocale

## ⚙️ Come funziona

Digital Pendulum si sincronizza con l'orologio di sistema e controlla automaticamente ogni minuto se è il momento di fare un annuncio.

**Quando scatta l'annuncio:**
1. 🔔 Riproduce la campana scelta (se abilitata)
2. ⏱️ Attende un numero configurabile di secondi (default: 1,2 s) — aumenta questo valore per i dispositivi Google Home / Nest se l'annuncio vocale non viene riprodotto correttamente
3. 🗣️ Il dispositivo pronuncia l'ora nella lingua di Home Assistant (se abilitato)

Tutto avviene automaticamente senza bisogno di configurare automazioni!

## 🗣️ Gestione della lingua

La lingua viene rilevata automaticamente da:

self.hass.config.language

Esempi di annunci:

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

## 🔔 Campana (suono iniziale)

Se l'opzione use_chime è attiva:
- viene riprodotto il suono di notifica o il suono scelto
- il sistema attende un numero configurabile di secondi (default: 1,2)
- inizia l'annuncio vocale (se abilitato)

Si crea così un effetto simile a un vero pendolo 🎶.

## 🧩 Opzioni di configurazione

| Opzione | Descrizione |
|------|------------|
| player_type | Tipo di dispositivo player (Alexa, Google Home, Generico) |
| player | Dispositivo di destinazione |
| start_hour | Ora di inizio operatività |
| end_hour | Ora di fine operatività |
| enabled | Abilita/disabilita il pendolo |
| announce_half_hours | Abilita gli annunci ogni mezz'ora (altrimenti solo ogni ora) |
| after_chime_delay | Tempo di attesa in secondi tra la campana e l'annuncio vocale (default: 1,2) |
| announce_half_hours_voice | Abilita/disabilita l'annuncio vocale alle mezz'ore (la campana suona comunque) |
| voice_announcement | Abilita/disabilita l'annuncio vocale dell'ora |
| tower_clock | Abilita la melodia di Westminster alle 12:00 |
| use_chime | Abilita/disabilita la campana prima dell'annuncio |
| preset_chime | Scelta del suono della campana (12 preset disponibili) |
| custom_chime_path | Percorso per il suono campana personalizzato |

Valori predefiniti:

- ⏰ start_hour → 8
- ⏰ end_hour → 22
- 🔔 use_chime → True
- 🗣️ voice_announcement → True
- ⏰ announce_half_hours → True
- 🏰 tower_clock → False
- ✅ enabled → True
- ⏱️ after_chime_delay → 1,2
- 🔇 announce_half_hours_voice → True

## 🧪 Test immediato

È disponibile un metodo di test manuale:

Che:
- legge l'ora corrente
- genera una frase completa (es. "Sono le 15 e 42 minuti")
- la riproduce immediatamente sul dispositivo selezionato

Utile per verificare: lingua, volume, campana, corretto funzionamento del TTS

## 🔍 Sensore di stato

Digital Pendulum include un sensore diagnostico:

`binary_sensor.digital_pendulum_status_warning`

**Stati:**
- ✅ **OFF** - Tutto funziona correttamente
- ⚠️ **ON** - Problemi rilevati (integrazione disabilitata, Alexa offline, ecc.)

**Utilizzi:**
- Monitoraggio dashboard
- Automazioni di notifica
- Diagnostica rapida

## 📦 Requisiti

> ✨ **Disponibile su HACS** - installazione e aggiornamenti semplificati!

- 🏠 Home Assistant 2024.1.0 o superiore
- 🔊 Un dispositivo media_player compatibile (vedi [Dispositivi supportati](#-dispositivi-supportati))
- 📡 Per Alexa: [alexa_media_player](https://github.com/custom-components/alexa_media_player) installato tramite HACS
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

## 🎯 Utilizzo ideale

- ✔️ Case intelligenti
- ✔️ Uffici
- ✔️ Aree comuni
- ✔️ Effetto "pendolo moderno"
- ✔️ Promemoria dell'ora non invasivo

## 🔧 Risoluzione dei problemi

### Problemi con Alexa o errore "Cannot find EU skill"

Problema con **alexa_media_player**, non con Digital Pendulum.

**Soluzione rapida:**
1. Impostazioni → Dispositivi e servizi → Alexa Media Player
2. Tre punti → Ricarica
3. Se non funziona: disinstalla e reinstalla Alexa Media Player

---

### Google Home / Nest: nessun annuncio vocale

Digital Pendulum utilizza il motore TTS configurato in HA per i dispositivi Google.

Si tratta di un noto problema di temporizzazione con i dispositivi Google. L'annuncio vocale può essere interrotto o saltato se la pausa dopo la campana è troppo breve.

1. Verifica che sia configurato un motore TTS in HA (Impostazioni → Assistenti vocali)
2. Controlla il log di HA per errori TTS
3. Aumenta il valore **"Pausa dopo la campana"** (prova 2,0 o 3,0 secondi)
4. Usa il pulsante "Test" per verificare

---

### Lingua errata

Digital Pendulum usa automaticamente la lingua di Home Assistant.

1. Verifica: Impostazioni → Sistema → Generale → Lingua
2. Lingue supportate: 🇮🇹 🇬🇧 🇫🇷 🇩🇪 🇪🇸 🇵🇱 🇨🇿 🇸🇰 🇵🇹
3. Dopo aver cambiato la lingua, riavvia Home Assistant

---

### Nessun annuncio

**Verifica:**
- Integrazione abilitata? (Interruttore ON)
- Sei nella fascia oraria configurata? (default 8:00-22:00)
- Dispositivo online?
- Tipo di player corretto selezionato? (Alexa, Google, Generico)
- Prova il pulsante "Test"

---

### Solo campana o solo voce

- **Solo campana:** Abilita "Annuncio vocale"
- **Solo voce:** Abilita "Usa campana"

---

### Westminster non suona alle 12

- Verifica che "Orologio a Torre" sia attivo
- Funziona **solo alle 12:00** (mezzogiorno, non mezzanotte)

---

## 🚀 Possibili sviluppi futuri

- ⏳ Annunci ogni 15 minuti
- 🔇 Volume notturno automatico

---

## ☕ Supporta il progetto

Ti piace questo progetto? Se lo trovi utile, offrimi un caffè virtuale per supportare i futuri sviluppi! Ogni piccolo contributo è molto apprezzato. 🙏

**Digital Pendulum è e rimarrà sempre gratuito e open source.** Le donazioni sono completamente volontarie! ❤️

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/dregi56)

💡 **Preferisci altri metodi?** Puoi usare:

[![revolut](https://img.shields.io/badge/Revolut-0075EB?style=for-the-badge&logo=revolut&logoColor=white)](https://revolut.me/egidio5t9d)
