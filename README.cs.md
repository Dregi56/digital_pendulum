# 🕰️ Digital Pendulum
Mluvící digitální kyvadlo pro Home Assistant
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
[Slovenčina](README.sk.md)
<br>👉 Toto je README v češtině. Použijte výběr jazyka výše.

## ❤️ Líbí se vám Digital Pendulum?
Pokud vám přijde užitečný, zvažte zanechání ⭐ na GitHubu:  
👉 **https://github.com/Dregi56/digital_pendulum**
<br>Děkuji.

## 📌 Popis
Digital Pendulum je vlastní integrace pro Home Assistant, která hlasově oznamuje čas, přesně jako digitální kyvadlo 🕰️.
Pomocí zařízení Alexa jako reproduktoru systém:
- 📢 oznamuje čas každou hodinu a/nebo každou půlhodinu (konfigurovatelné)
- 🌍 automaticky mluví jazykem nastaveným v Home Assistant  
- ⏰ funguje pouze v konfigurovatelném časovém rozsahu
- 🔔 může přehrát vlastní zvuk před oznámením
- 🔕 může zakázat hlasové oznámení (pouze zvon)
- 🏰 může přehrát melodii Westminster ve 12 hodin

Výsledkem je elegantní a diskrétní efekt, ideální pro domov nebo kancelář.

## ✨ Hlavní funkce

### 🕑 Automatické oznamování času
- každou hodinu (xx:00)
- každou půlhodinu (xx:30) - volitelné

### 🌐 Automatická podpora více jazyků
- Italština 🇮🇹
- Angličtina 🇬🇧
- Francouzština 🇫🇷
- Němčina 🇩🇪 (se správným zpracováním výrazu "halb")
- Španělština 🇪🇸
- Polština 🇵🇱
- Čeština 🇨🇿 (se správným zpracováním výrazu "půl")
- Slovenština 🇸🇰 (se správným zpracováním výrazu "pol")

automatický záložní jazyk: italština

### ⏱️ Konfigurovatelný časový rozsah
- např. pouze od 8:00 do 22:00

### 🔔 Volitelný zvon
- 🎵 12 přednastavených zvuků na výběr
- 🎶 možnost použít vlastní zvukový soubor
- 🔕 oznamovací zvuk "announce" Alexa (výchozí)

### 🧪 Testovací funkce
- pro okamžité vyzkoušení oznámení

### 🎯 Chování

**Zvon (Chime):**
- **Dostupné předvolby**: 12 zvuků včetně church-bell, simple-bell, clock-chime atd.
- **Vlastní zvuk**: Vyberte "custom" a zadejte cestu k vašemu zvukovému souboru
- **Výchozí**: Zvuk "announce" Alexa (pokud nic nevyberete)
- **Vypnuto**: Zakažte "use_chime" pro žádný zvuk před oznámením

**Melodie Westminster (Tower Clock):**
- Samostatná možnost "tower_clock"
- Hraje **pouze ve 12:00** (poledne)
- Nahrazuje normální chime v tu hodinu

**Hlasové oznámení:**
- **Zapnuto** (výchozí): Alexa vysloví čas po zvonu
- **Vypnuto**: Pouze zvuk zvonu, žádné hlasové oznámení

**Oznámení půlhodiny:**
- **Zapnuto** (výchozí): Oznámení v :00 a :30
- **Vypnuto**: Pouze oznámení v :00

## ⚙️ Jak to funguje
Digital Pendulum se synchronizuje se systémovými hodinami a automaticky každou minutu kontroluje, zda je čas na oznámení.

**Když se spustí oznámení:**
1. 🔔 Přehraje zvolený zvon (je-li zapnut)
2. ⏱️ Počká 1,2 sekundy
3. 🗣️ Alexa vysloví čas v jazyce Home Assistant (je-li zapnuto)

Vše probíhá automaticky bez nutnosti konfigurovat automatizace!

## 🗣️ Správa jazyků
Jazyk je automaticky detekován z:
self.hass.config.language

Příklady oznámení:
| Jazyk | Čas | Oznámení |
|------|------|--------|
| 🇮🇹 IT | 10:30 | Ore 10 e trenta |
| 🇬🇧 EN | 14:00 | It's 14 o'clock |
| 🇫🇷 FR | 9:30 | Il est 9 heures trente |
| 🇩🇪 DE | 16:30 | Es ist halb 17 |
| 🇪🇸 ES | 11:00 | Son las 11 |
| 🇵🇱 PL | 15:30 | Wpół do czwartej |
| 🇨🇿 CS | 8:30 | Půl deváté |
| 🇸🇰 SK | 8:30 | Pol deviatej |

## 🔔 Chime (úvodní zvon)
Je-li možnost use_chime aktivní:
- přehraje se oznamovací zvuk Alexa nebo zvolený zvuk
- systém počká 1,2 sekundy
- spustí se hlasové oznámení (je-li zapnuto)

Tím vznikne efekt podobný skutečnému kyvadlu 🎶.

## 🧩 Možnosti konfigurace
| Možnost | Popis |
|------|------------|
| player | Cílové zařízení Alexa |
| start_hour | Čas zahájení činnosti |
| end_hour | Čas ukončení činnosti |
| enabled | Zapnutí/vypnutí kyvadla |
| announce_half_hours | Zapnutí oznámení každou půlhodinu (jinak pouze každou hodinu) |
| voice_announcement | Zapnutí/vypnutí hlasového oznámení času |
| tower_clock | Zapnutí melodie Westminster ve 12:00 |
| use_chime | Zapnutí/vypnutí zvonu před oznámením |
| preset_chime | Výběr zvuku zvonu (12 dostupných předvoleb) |
| custom_chime_path | Cesta k vlastnímu zvukovému souboru zvonu |

Výchozí hodnoty:
- ⏰ start_hour → 8
- ⏰ end_hour → 22
- 🔔 use_chime → True
- 🗣️ voice_announcement → True
- ⏰ announce_half_hours → True
- 🏰 tower_clock → False
- ✅ enabled → True

## 🧪 Okamžitý test
Je dostupná metoda ručního testování, která:
- přečte aktuální čas
- vygeneruje úplnou větu (např. "Je přesně osm hodin")
- okamžitě ji přehraje na zařízení Alexa

Užitečné pro ověření: jazyka, hlasitosti, chime, správného fungování TTS

## 🔍 Stavový senzor
Digital Pendulum obsahuje diagnostický senzor:
`binary_sensor.digital_pendulum_status_warning`

**Stavy:**
- ✅ **OFF** - Vše funguje správně
- ⚠️ **ON** - Zjištěny problémy (integrace zakázána, Alexa offline atd.)

**Využití:**
- Sledování na dashboardu
- Automatizace pro notifikace
- Rychlá diagnostika

## 📦 Požadavky
> ✨ **Dostupné v HACS** - zjednodušená instalace a aktualizace!
- 🏠 Home Assistant 2024.1.0 nebo vyšší
- 🔊 Alexa Media Player nainstalovaný a funkční
- 📡 Zařízení Alexa nakonfigurované jako přehrávač

## 💾 Instalace

### Přes HACS (doporučeno)
1. Otevřete **HACS** v postranní nabídce
2. Přejděte na **Integrace**
3. Vyhledejte **"Digital Pendulum"**
4. Klikněte na **Stáhnout**
5. **Restartujte Home Assistant**
6. Přejděte do **Nastavení** → **Zařízení a služby** → **Přidat integraci**
7. Vyhledejte **"Digital Pendulum"**
8. Postupujte podle průvodce konfigurací

### Ruční instalace
1. Stáhněte nejnovější verzi z [GitHubu](https://github.com/Dregi56/digital_pendulum/releases)
2. Rozbalte soubory
3. Zkopírujte složku `digital_pendulum` do `config/custom_components/`
4. Restartujte Home Assistant
5. Přejděte do **Nastavení** → **Zařízení a služby** → **Přidat integraci**
6. Vyhledejte **"Digital Pendulum"**
7. Postupujte podle průvodce konfigurací

## 🎯 Ideální použití
- ✔️ Chytré domácnosti
- ✔️ Kanceláře
- ✔️ Společné prostory
- ✔️ Efekt "moderního kyvadla"
- ✔️ Nenápadná časová připomínka

## 🔧 Řešení problémů

### Chyba "Cannot find EU skill" nebo problémy s Alexou
Problém s **Alexa Media Player**, nikoli s Digital Pendulum.

**Rychlé řešení:**
1. Nastavení → Zařízení a služby → Alexa Media Player
2. Tři tečky → Znovu načíst
3. Pokud nefunguje: odinstalujte a znovu nainstalujte Alexa Media Player

---

### Špatný jazyk
Digital Pendulum automaticky používá jazyk Home Assistant.
1. Zkontrolujte: Nastavení → Systém → Obecné → Jazyk
2. Podporované jazyky: 🇮🇹 🇬🇧 🇫🇷 🇩🇪 🇪🇸 🇵🇱 🇨🇿 🇸🇰
3. Po změně jazyka restartujte Home Assistant

---

### Žádné oznámení
**Zkontrolujte:**
- Je integrazione zapnuta? (Přepínač ON)
- Jste v nakonfigurovaném časovém rozsahu? (výchozí 8:00–22:00)
- Je zařízení Alexa online?
- Zkuste tlačítko "Test"

---

### Pouze zvon nebo pouze hlas
- **Pouze zvon:** Zapněte "Voice announcement"
- **Pouze hlas:** Zapněte "Use chime"

---

### Westminster nezní ve 12
- Ověřte, že je aktivní "Tower Clock"
- Funguje **pouze ve 12:00** (poledne, nikoli půlnoc)

---

## 🚀 Možný budoucí vývoj
- ⏳ Oznámení každých 15 minut
- 🔇 Automatická noční hlasitost
- 🗓️ Oznámení dne
- 📣 Podpora dalších TTS

---

## ☕ Podpořte projekt
Líbí se vám tento projekt? Pokud vám přijde užitečný, dejte mi virtuální kávu na podporu budoucího vývoje! Každý malý příspěvek je velmi ceněn. 🙏

**Digital Pendulum je a vždy bude zdarma a open source.** Dary jsou zcela dobrovolné! ❤️

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/dregi56)

💡 **Preferujete jiné metody?** Můžete použít:
[![revolut](https://img.shields.io/badge/Revolut-0075EB?style=for-the-badge&logo=revolut&logoColor=white)](https://revolut.me/egidio5t9d)
