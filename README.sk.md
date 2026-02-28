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
Ak vám príde užitočný, zvážte zanechanie ⭐ na GitHube:  
👉 **https://github.com/Dregi56/digital_pendulum**
<br>Ďakujem.

## 📌 Popis
Digital Pendulum je vlastná integrácia pre Home Assistant, ktorá hlasovo oznamuje čas, presne ako digitálne kyvadlo 🕰️.
Pomocou zariadenia Alexa ako reproduktora systém:
- 📢 oznamuje čas každú hodinu a/alebo každú polhodinu (konfigurovateľné)
- 🌍 automaticky hovorí jazykom nastaveným v Home Assistant  
- ⏰ funguje iba v konfigurovateľnom časovom rozsahu
- 🔔 môže prehrať vlastný zvuk pred oznámením
- 🔕 môže zakázať hlasové oznámenie (iba zvon)
- 🏰 môže prehrať melódiu Westminster o 12 hodín

Výsledkom je elegantný a diskrétny efekt, ideálny pre domov alebo kanceláriu.

## ✨ Hlavné funkcie

### 🕑 Automatické oznamovanie času
- každú hodinu (xx:00)
- každú polhodinu (xx:30) - voliteľné

### 🌐 Automatická podpora viacerých jazykov
- Taliančina 🇮🇹
- Angličtina 🇬🇧
- Francúzština 🇫🇷
- Nemčina 🇩🇪 (so správnym spracovaním výrazu "halb")
- Španielčina 🇪🇸
- Poľština 🇵🇱
- Čeština 🇨🇿 (so správnym spracovaním výrazu "půl")
- Slovenčina 🇸🇰 (so správnym spracovaním výrazu "pol")
- Portugalčina 🇵🇹

automatický záložný jazyk: taliančina

### ⏱️ Konfigurovateľný časový rozsah
- napr. iba od 8:00 do 22:00

### 🔔 Voliteľný zvon
- 🎵 12 prednastavených zvukov na výber
- 🎶 možnosť použiť vlastný zvukový súbor
- 🔕 oznamovací zvuk "announce" Alexa (predvolený)

### 🧪 Testovacia funkcia
- na okamžité vyskúšanie oznámenia

### 🎯 Správanie

**Zvon (Chime):**
- **Dostupné predvoľby**: 12 zvukov vrátane church-bell, simple-bell, clock-chime atď.
- **Vlastný zvuk**: Vyberte "custom" a zadajte cestu k vášmu zvukovému súboru
- **Predvolený**: Zvuk "announce" Alexa (ak nič nevyberiete)
- **Vypnuté**: Zakážte "use_chime" pre žiadny zvuk pred oznámením

**Melódia Westminster (Tower Clock):**
- Samostatná možnosť "tower_clock"
- Hrá **iba o 12:00** (poludnie)
- Nahrádza normálny chime v tú hodinu

**Hlasové oznámenie:**
- **Zapnuté** (predvolené): Alexa vysloví čas po zvone
- **Vypnuté**: Iba zvuk zvona, žiadne hlasové oznámenie

**Oznámenia polhodiny:**
- **Zapnuté** (predvolené): Oznámenia v :00 a :30
- **Vypnuté**: Iba oznámenia v :00

## ⚙️ Ako to funguje
Digital Pendulum sa synchronizuje so systémovými hodinami a automaticky každú minútu kontroluje, či je čas na oznámenie.

**Keď sa spustí oznámenie:**
1. 🔔 Prehrá zvolený zvon (ak je zapnutý)
2. ⏱️ Počká 1,2 sekundy
3. 🗣️ Alexa vysloví čas v jazyku Home Assistant (ak je zapnuté)

Všetko prebieha automaticky bez potreby konfigurovať automatizácie!

## 🗣️ Správa jazykov
Jazyk je automaticky detekovaný z:
self.hass.config.language

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

## 🔔 Chime (úvodný zvon)
Ak je možnosť use_chime aktívna:
- prehrá sa oznamovací zvuk Alexa alebo zvolený zvuk
- systém počká 1,2 sekundy
- spustí sa hlasové oznámenie (ak je zapnuté)

Tým vznikne efekt podobný skutočnému kyvadlu 🎶.

## 🧩 Možnosti konfigurácie
| Možnosť | Popis |
|------|------------|
| player | Cieľové zariadenie Alexa |
| start_hour | Čas začiatku činnosti |
| end_hour | Čas ukončenia činnosti |
| enabled | Zapnutie/vypnutie kyvadla |
| announce_half_hours | Zapnutie oznámení každú polhodinu (inak iba každú hodinu) |
| voice_announcement | Zapnutie/vypnutie hlasového oznámenia času |
| tower_clock | Zapnutie melódie Westminster o 12:00 |
| use_chime | Zapnutie/vypnutie zvona pred oznámením |
| preset_chime | Výber zvuku zvona (12 dostupných predvolieb) |
| custom_chime_path | Cesta k vlastnému zvukovému súboru zvona |

Predvolené hodnoty:
- ⏰ start_hour → 8
- ⏰ end_hour → 22
- 🔔 use_chime → True
- 🗣️ voice_announcement → True
- ⏰ announce_half_hours → True
- 🏰 tower_clock → False
- ✅ enabled → True

## 🧪 Okamžitý test
Je dostupná metóda ručného testovania, ktorá:
- prečíta aktuálny čas
- vygeneruje úplnú vetu (napr. "Je presne osem hodín")
- okamžite ju prehrá na zariadení Alexa

Užitočné na overenie: jazyka, hlasitosti, chime, správneho fungovania TTS

## 🔍 Stavový senzor
Digital Pendulum obsahuje diagnostický senzor:
`binary_sensor.digital_pendulum_status_warning`

**Stavy:**
- ✅ **OFF** - Všetko funguje správne
- ⚠️ **ON** - Zistené problémy (integrácia zakázaná, Alexa offline atď.)

**Využitie:**
- Sledovanie na dashboarde
- Automatizácie pre notifikácie
- Rýchla diagnostika

## 📦 Požiadavky
> ✨ **Dostupné v HACS** - zjednodušená inštalácia a aktualizácie!
- 🏠 Home Assistant 2024.1.0 alebo vyšší
- 🔊 Alexa Media Player nainštalovaný a funkčný
- 📡 Zariadenie Alexa nakonfigurované ako prehrávač

## 💾 Inštalácia

### Cez HACS (odporúčané)
1. Otvorte **HACS** v bočnej ponuke
2. Prejdite na **Integrácie**
3. Vyhľadajte **"Digital Pendulum"**
4. Kliknite na **Stiahnuť**
5. **Reštartujte Home Assistant**
6. Prejdite do **Nastavenia** → **Zariadenia a služby** → **Pridať integráciu**
7. Vyhľadajte **"Digital Pendulum"**
8. Postupujte podľa sprievodcu konfiguráciou

### Ručná inštalácia
1. Stiahnite najnovšiu verziu z [GitHubu](https://github.com/Dregi56/digital_pendulum/releases)
2. Rozbaľte súbory
3. Skopírujte priečinok `digital_pendulum` do `config/custom_components/`
4. Reštartujte Home Assistant
5. Prejdite do **Nastavenia** → **Zariadenia a služby** → **Pridať integráciu**
6. Vyhľadajte **"Digital Pendulum"**
7. Postupujte podľa sprievodcu konfiguráciou

## 🎯 Ideálne použitie
- ✔️ Inteligentné domácnosti
- ✔️ Kancelárie
- ✔️ Spoločné priestory
- ✔️ Efekt "moderného kyvadla"
- ✔️ Nenápadná časová pripomienka

## 🔧 Riešenie problémov

### Chyba "Cannot find EU skill" alebo problémy s Alexou
Problém s **Alexa Media Player**, nie s Digital Pendulum.

**Rýchle riešenie:**
1. Nastavenia → Zariadenia a služby → Alexa Media Player
2. Tri bodky → Znovu načítať
3. Ak nefunguje: odinštalujte a znovu nainštalujte Alexa Media Player

---

### Nesprávny jazyk
Digital Pendulum automaticky používa jazyk Home Assistant.
1. Skontrolujte: Nastavenia → Systém → Všeobecné → Jazyk
2. Podporované jazyky: 🇮🇹 🇬🇧 🇫🇷 🇩🇪 🇪🇸 🇵🇱 🇨🇿 🇸🇰 🇵🇹
3. Po zmene jazyka reštartujte Home Assistant

---

### Žiadne oznámenie
**Skontrolujte:**
- Je integrácia zapnutá? (Prepínač ON)
- Ste v nakonfigurovanom časovom rozsahu? (predvolené 8:00–22:00)
- Je zariadenie Alexa online?
- Skúste tlačidlo "Test"

---

### Iba zvon alebo iba hlas
- **Iba zvon:** Zapnite "Voice announcement"
- **Iba hlas:** Zapnite "Use chime"

---

### Westminster nezní o 12
- Overte, že je aktívny "Tower Clock"
- Funguje **iba o 12:00** (poludnie, nie polnoc)

---

## 🚀 Možný budúci vývoj
- ⏳ Oznámenia každých 15 minút
- 🔇 Automatická nočná hlasitosť
- 🗓️ Oznámenie dňa
- 📣 Podpora ďalších TTS

---

## ☕ Podporte projekt
Páči sa vám tento projekt? Ak vám príde užitočný, dajte mi virtuálnu kávu na podporu budúceho vývoja! Každý malý príspevok je veľmi cenený. 🙏

**Digital Pendulum je a vždy bude zadarmo a open source.** Dary sú úplne dobrovoľné! ❤️

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/dregi56)

💡 **Preferujete iné metódy?** Môžete použiť:
[![revolut](https://img.shields.io/badge/Revolut-0075EB?style=for-the-badge&logo=revolut&logoColor=white)](https://revolut.me/egidio5t9d)
