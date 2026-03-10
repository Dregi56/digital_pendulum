# 🕰️ Digital Pendulum

Hovoriace digitálne kyvadlo pre Home Assistant
<br>**Autor:** Egidio Ziggiotto (Dregi56)  e-mail: [dregi@cyberservices.com](mailto:dregi@cyberservices.com)

[![HACS](https://img.shields.io/badge/HACS-Default-41BDF5.svg)](https://hacs.xyz/)
[![Version](https://img.shields.io/github/v/release/Dregi56/digital_pendulum)](https://github.com/Dregi56/digital_pendulum/releases)
![License](https://img.shields.io/github/license/Dregi56/digital_pendulum)
[![GitHub stars](https://img.shields.io/github/stars/Dregi56/digital_pendulum?style=social)](https://github.com/Dregi56/digital_pendulum)

🌍 Dostupné jazyky:
[Italiano](README.it.md) |
[English](README.en.md) |
[Español](README.es.md) |
[Deutsch](README.de.md) |
[Français](README.fr.md) |
[Polski](README.pl.md) |
[Čeština](README.cs.md) |
[Slovenčina](README.sk.md) |
[Português](README.pt.md)

<br>👉 Toto je README v slovenčine. Použite výber jazyka vyššie.

## ❤️ Páči sa vám Digital Pendulum?

Ak ho považujete za užitočný, zvážte zanechanie ⭐ na GitHube:  
👉 **https://github.com/Dregi56/digital_pendulum**
<br>Ďakujeme.

## 📌 Popis

Digital Pendulum je vlastná integrácia pre Home Assistant, ktorá hlasovo oznamuje čas, podobne ako digitálne kyvadlové hodiny 🕰️.

Pomocou kompatibilného inteligentného reproduktora ako prehrávača systém:

- 📢 oznamuje čas každú hodinu a/alebo každú pol hodinu (konfigurovateľné)
- 🌍 automaticky hovorí v jazyku nastavenom v Home Assistant
- ⏰ funguje len v konfigurovateľnom časovom rozsahu
- 🔔 môže prehrať vlastný zvuk pred oznámením
- 🔕 môže vypnúť hlasové oznámenie (iba zvonček)
- 🏰 môže prehrať westminsterský chorál o 12 hodín

Výsledkom je elegantný a nenápadný efekt, ideálny pre domov alebo kanceláriu.

## 🔊 Podporované zariadenia

Digital Pendulum podporuje tri typy prehrávačov:

| Typ | Popis | Požiadavka |
|------|-------------|-------------|
| **Alexa** | Zariadenia Amazon Echo | [alexa_media_player](https://github.com/custom-components/alexa_media_player) cez HACS |
| **Google Home / Nest** | Google Home, Nest Mini, Nest Hub, Chromecast | Google Cast (natívna integrácia HA) |
| **Všeobecný** | Akékoľvek iné zariadenie HA media_player | TTS engine nakonfigurovaný v HA (funkčnosť sa môže líšiť) |

Počas nastavenia budete najskôr požiadaní o výber typu prehrávača, potom konkrétneho zariadenia.

## ✨ Hlavné funkcie

### 🕑 Automatické oznamovanie času
- každú hodinu (xx:00)
- každú pol hodinu (xx:30) - voliteľné (iba zvonček alebo zvonček + hlas, konfigurovateľné)

### ⏱️ Konfigurovateľná pauza po zvončeku
- nastaviteľný čas čakania medzi zvončekom a hlasovým oznámením (predvolené: 1,2 sekundy)
- obzvlášť užitočné pre zariadenia Google Home / Nest, ktoré môžu potrebovať dlhšiu pauzu na správne prehranie hlasového oznámenia

### 🌐 Automatická viacjazyčná podpora
- Italiano 🇮🇹
- English 🇬🇧
- Français 🇫🇷
- Deutsch 🇩🇪
- Español 🇪🇸
- Polski 🇵🇱
- Čeština 🇨🇿
- Slovenčina 🇸🇰
- Português 🇵🇹

🌐 **Jazyk prispôsobiteľný:** Je možné zvoliť iný jazyk ako ten nastavený v Home Assistant (užitočné napríklad pre tých, ktorí majú HA v angličtine).

### 🕐 Konfigurovateľný časový rozsah
- napr. iba od 8:00 do 22:00

### 🔔 Voliteľný zvonček
- 🎵 12 prednastavených zvukov na výber
- 🎶 možnosť použitia vlastného zvukového súboru
- 🔕 predvolený zvuk oznámenia (ak nie je nič vybrané)
- ⏳ Možnosť vyhradeného zvuku pre polhodinu

### 🧪 Testovacia funkcia
- na okamžité vyskúšanie oznámenia

### 🎯 Správanie

**Zvonček (Chime):**
- **Dostupné predvoľby**: 12 zvukov vrátane church-bell, simple-bell, clock-chime atď.
- **Vlastný zvuk**: Vyberte "custom" a zadajte cestu k vášmu zvukovému súboru
- **Predvolený**: zvuk oznámenia (ak nič nevyberiete)
- **Vypnutý**: Vypnite "use_chime" pre žiadny zvuk pred oznámením

**Westminsterská melódia (Vežové hodiny):**
- Samostatná možnosť "tower_clock"
- Prehráva sa **iba o 12:00** (poludnie)
- Nahrádza normálny zvonček v tom čase

**Hlasové oznámenie:**
- **Zapnuté** (predvolené): zariadenie vyslovuje čas po zvončeku
- **Vypnuté**: iba zvuk zvončeka, žiadne hlasové oznámenie

**Hlasové oznámenie v polhodinách:**
- **Zapnuté** (predvolené): hlasové oznámenie sa prehráva o :00 aj o :30
- **Vypnuté**: zvonček stále hrá o :30, ale bez hlasového oznámenia

## ⚙️ Ako to funguje

Digital Pendulum sa synchronizuje so systémovými hodinami a automaticky každú minútu kontroluje, či je čas na oznámenie.

**Keď sa spustí oznámenie:**
1. 🔔 Prehrá vybraný zvonček (ak je zapnutý)
2. ⏱️ Čaká konfigurovateľný počet sekúnd (predvolené: 1,2 s) — zvýšte túto hodnotu pre zariadenia Google Home / Nest, ak sa hlasové oznámenie neprehráva správne
3. 🗣️ Zariadenie vysloví čas v jazyku Home Assistant (ak je zapnuté)

Všetko prebieha automaticky bez potreby konfigurovať automatizácie!

## 🗣️ Spracovanie jazyka

Jazyk sa automaticky rozpoznáva z Home Assistant.

🌐 **Jazyk oznámení:** Možnosť zvoliť jazyk hlasových oznámení nezávisle od jazyka nastaveného v Home Assistant (dostupné: Italiano, English, Deutsch, Español, Français, Português, Polski, Čeština, Slovenčina, alebo Automaticky pre sledovanie jazyka Home Assistant).

Príklady oznámení:

| Jazyk | Čas | Oznámenie |
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

## 🔔 Zvonček (úvodný zvuk)

Ak je možnosť use_chime aktívna:
- prehrá sa zvuk oznámenia alebo vybraný zvuk
- systém čaká konfigurovateľný počet sekúnd (predvolené: 1,2)
- spustí sa hlasové oznámenie (ak je zapnuté)

Vzniká tak efekt podobný skutočnému kyvadlu 🎶.

## 🧩 Možnosti konfigurácie

| Možnosť | Popis |
|------|------------|
| player_type | Typ prehrávača (Alexa, Google Home, Všeobecný) |
| player | Cieľové zariadenie |
| start_hour | Čas začiatku prevádzky |
| end_hour | Čas konca prevádzky |
| enabled | Zapína/vypína kyvadlo |
| announce_half_hours | Zapína oznámenia každú pol hodinu (inak iba každú hodinu) |
| after_chime_delay | Čas čakania v sekundách medzi zvončekom a hlasovým oznámením (predvolené: 1,2) |
| announce_half_hours_voice | Zapína/vypína hlasové oznámenie v polhodinách (zvonček stále hrá) |
| voice_announcement | Zapína/vypína hlasové oznámenie času |
| tower_clock | Zapína westminstersku melódiu o 12:00 |
| use_chime | Zapína/vypína zvonček pred oznámením |
| preset_chime | Výber zvuku zvončeka (12 dostupných predvolieb) |
| custom_chime_path | Cesta k vlastnému zvuku zvončeka |

Predvolené hodnoty:

- ⏰ start_hour → 8
- ⏰ end_hour → 22
- 🔔 use_chime → True
- 🗣️ voice_announcement → True
- ⏰ announce_half_hours → True
- 🏰 tower_clock → False
- ✅ enabled → True
- ⏱️ after_chime_delay → 1,2
- 🔇 announce_half_hours_voice → True

## 🧪 Okamžitý test

K dispozícii je metóda ručného testu:

Ktorá:
- prečíta aktuálny čas
- vygeneruje celú vetu (napr. "Je 15 hodín a 42 minút")
- okamžite ju prehrá na vybranom zariadení

Užitočné na overenie: jazyka, hlasitosti, zvončeka, správnej funkcie TTS

## 🔍 Stavový senzor

Digital Pendulum obsahuje diagnostický senzor:

`binary_sensor.digital_pendulum_status_warning`

**Stavy:**
- ✅ **OFF** - Všetko funguje správne
- ⚠️ **ON** - Zistené problémy (integrácia vypnutá, Alexa offline atď.)

**Použitie:**
- Monitorovanie dashboardu
- Automatizácie oznámení
- Rýchla diagnostika

## 📦 Požiadavky

> ✨ **Dostupné na HACS** - zjednodušená inštalácia a aktualizácie!

- 🏠 Home Assistant 2024.1.0 alebo vyšší
- 🔊 Kompatibilné zariadenie media_player (pozri [Podporované zariadenia](#-podporované-zariadenia))
- 📡 Pre Alexa: [alexa_media_player](https://github.com/custom-components/alexa_media_player) nainštalovaný cez HACS
- 📡 Pre Google Home / Nest: integrácia Google Cast (natívna v HA)

## 💾 Inštalácia

### Cez HACS (odporúčané)

1. Otvorte **HACS** v bočnom menu
2. Prejdite na **Integrácie**
3. Vyhľadajte **"Digital Pendulum"**
4. Kliknite na **Stiahnuť**
5. **Reštartujte Home Assistant**
6. Prejdite na **Nastavenia** → **Zariadenia a služby** → **Pridať integráciu**
7. Vyhľadajte **"Digital Pendulum"**
8. Postupujte podľa sprievodcu konfiguráciou

### Ručná inštalácia

1. Stiahnite najnovšiu verziu z [GitHubu](https://github.com/Dregi56/digital_pendulum/releases)
2. Rozbaľte súbory
3. Skopírujte priečinok `digital_pendulum` do `config/custom_components/`
4. Reštartujte Home Assistant
5. Prejdite na **Nastavenia** → **Zariadenia a služby** → **Pridať integráciu**
6. Vyhľadajte **"Digital Pendulum"**
7. Postupujte podľa sprievodcu konfiguráciou

## 🎯 Ideálne použitie

- ✔️ Inteligentné domácnosti
- ✔️ Kancelárie
- ✔️ Spoločné priestory
- ✔️ Efekt "moderného kyvadla"
- ✔️ Nenápadná pripomienka času

## 🔧 Riešenie problémov

### Problémy s Alexou alebo chyba "Cannot find EU skill"

Problém s **alexa_media_player**, nie s Digital Pendulum.

**Rýchle riešenie:**
1. Nastavenia → Zariadenia a služby → Alexa Media Player
2. Tri bodky → Znovu načítať
3. Ak nefunguje: odinštalujte a znovu nainštalujte Alexa Media Player

---

### Google Home / Nest: žiadne hlasové oznámenie

Digital Pendulum používa TTS engine nakonfigurovaný v HA pre zariadenia Google.

Ide o známy problém s časovaním u zariadení Google. Hlasové oznámenie môže byť prerušené alebo preskočené, ak je pauza po zvončeku príliš krátka.

1. Skontrolujte, že je v HA nakonfigurovaný TTS engine (Nastavenia → Hlasové asistenty)
2. Skontrolujte log HA pre chyby TTS
3. Zvýšte hodnotu **"Pauza po zvončeku"** (skúste 2,0 alebo 3,0 sekundy)
4. Na overenie použite tlačidlo "Test"

---

### Nesprávny jazyk

Digital Pendulum automaticky používa jazyk Home Assistant.

1. Skontrolujte: Nastavenia → Systém → Všeobecné → Jazyk
2. Podporované jazyky: 🇮🇹 🇬🇧 🇫🇷 🇩🇪 🇪🇸 🇵🇱 🇨🇿 🇸🇰 🇵🇹
3. Po zmene jazyka reštartujte Home Assistant

---

### Žiadne oznámenia

**Skontrolujte:**
- Je integrácia zapnutá? (Prepínač ON)
- Ste v nakonfigurovanom časovom rozsahu? (predvolené 8:00-22:00)
- Je zariadenie online?
- Je vybraný správny typ prehrávača? (Alexa, Google, Všeobecný)
- Skúste tlačidlo "Test"

---

### Iba zvonček alebo iba hlas

- **Iba zvonček:** Zapnite "Hlasové oznámenie"
- **Iba hlas:** Zapnite "Použiť zvonček"

---

### Westminster nehrá o 12

- Skontrolujte, že je aktívna možnosť "Vežové hodiny"
- Funguje **iba o 12:00** (poludnie, nie polnoc)

---

## 🚀 Možný budúci vývoj

- ⏳ Oznámenia každých 15 minút
- 🔇 Automatická nočná hlasitosť

---

## ☕ Podporte projekt

Páči sa vám tento projekt? Ak ho považujete za užitočný, kúpte mi virtuálnu kávu na podporu budúceho vývoja! Každý malý príspevok je veľmi cenený. 🙏

**Digital Pendulum je a vždy zostane zadarmo a open source.** Dary sú úplne dobrovoľné! ❤️

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/dregi56)

💡 **Preferujete iné metódy?** Môžete použiť:

[![revolut](https://img.shields.io/badge/Revolut-0075EB?style=for-the-badge&logo=revolut&logoColor=white)](https://revolut.me/egidio5t9d)
