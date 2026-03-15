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
[Slovenčina](README.sk.md) |
[Português](README.pt.md)

<br>👉 Toto je český README. Použijte výběr jazyka výše.

## ❤️ Líbí se vám Digital Pendulum?

Pokud vám přijde užitečný, zvažte zanechání ⭐ na GitHubu:  
👉 **https://github.com/Dregi56/digital_pendulum**
<br>Děkujeme.

## 📌 Popis

Digital Pendulum je vlastní integrace pro Home Assistant, která hlasově oznamuje čas, podobně jako digitální kyvadlové hodiny 🕰️.

Pomocí kompatibilního chytrého reproduktoru systém:

- 📢 oznamuje čas každou hodinu a/nebo každou půl hodinu (konfigurovatelné)
- 🌍 automaticky mluví v jazyce nastaveném v Home Assistant
- ⏰ funguje pouze v konfigurovatelném časovém rozsahu
- 🔔 může přehrát vlastní zvuk před oznámením
- 🔕 může zakázat hlasové oznámení (pouze zvon)
- 🏰 může přehrát westminsterský chorál ve 12 hodin

Výsledkem je elegantní a nenápadný efekt, ideální pro domov nebo kancelář.

## 🔊 Podporovaná zařízení

Digital Pendulum podporuje tři typy přehrávačů:

| Typ | Popis | Požadavek |
|------|-------------|-------------|
| **Alexa** | Zařízení Amazon Echo | [alexa_media_player](https://github.com/custom-components/alexa_media_player) přes HACS |
| **Google Home / Nest** | Google Home, Nest Mini, Nest Hub, Chromecast | Google Cast (nativní integrace HA) |
| **Generický** | Jakékoliv jiné zařízení HA media_player | TTS engine nakonfigurovaný v HA (funkčnost se může lišit) |

Během nastavení budete nejprve požádáni o výběr typu přehrávače, poté konkrétního zařízení.

## ✨ Hlavní funkce

### 🕑 Automatické oznamování času
- každou hodinu (xx:00)
- každou půl hodinu (xx:30) - volitelné (pouze zvon nebo zvon + hlas, konfigurovatelné)

### ⏱️ Konfigurovatelná prodleva po zvonu
- nastavitelná čekací doba mezi zvonkem a hlasovým oznámením (výchozí: 1,2 sekundy)
- užitečné zejména pro zařízení Google Home / Nest, která mohou potřebovat delší prodlevu pro správné přehrání hlasového oznámení

### 🌐 Automatická vícejazyčná podpora
- Italiano 🇮🇹
- English 🇬🇧
- Français 🇫🇷
- Deutsch 🇩🇪
- Español 🇪🇸
- Polski 🇵🇱
- Čeština 🇨🇿
- Slovenčina 🇸🇰
- Português 🇵🇹

🌐 **Přizpůsobitelný jazyk:** Je možné zvolit jiný jazyk než ten nastavený v Home Assistant (užitečné například pro ty, kteří mají HA v angličtině).

### 🕐 Konfigurovatelný časový rozsah
- např. pouze od 8:00 do 22:00

### 🔔 Volitelný zvon
- 🎵 12 přednastavených zvuků na výběr
- 🎶 možnost použití vlastního zvukového souboru
- 🔕 výchozí zvuk oznámení (pokud není nic vybráno)
- ⏳ Opcja dedykowanego dźwięku dla półgodziny

### 🧪 Testovací funkce
- pro okamžité vyzkoušení oznámení

### 🎯 Chování

**Zvon (Chime):**
- **Dostupné předvolby**: 12 zvuků včetně church-bell, simple-bell, clock-chime atd.
- **Vlastní zvuk**: Vyberte "custom" a zadejte cestu k vašemu zvukovému souboru
- **Výchozí**: zvuk oznámení (pokud nic nevyberete)
- **Zakázáno**: Vypněte "use_chime" pro žádný zvuk před oznámením

**Westminsterská melodie (věžní hodiny):**
- Samostatná možnost "tower_clock"
- Přehrává se **pouze ve 12:00** (poledne)
- Nahrazuje normální zvon v tu dobu

**Hlasové oznámení:**
- **Zapnuto** (výchozí): zařízení vyslovuje čas po zvonu
- **Vypnuto**: pouze zvuk zvonu, žádné hlasové oznámení

**Hlasové oznámení v půl hodině:**
- **Zapnuto** (výchozí): hlasové oznámení se přehrává v :00 i :30
- **Vypnuto**: zvon stále hraje v :30, ale žádné hlasové oznámení

## ⚙️ Jak to funguje

Digital Pendulum se synchronizuje se systémovými hodinami a automaticky každou minutu kontroluje, zda je čas na oznámení.

**Když se spustí oznámení:**
1. 🔔 Přehraje vybraný zvon (pokud je zapnut)
2. ⏱️ Čeká konfigurovatelný počet sekund (výchozí: 1,2 s) — zvyšte tuto hodnotu pro zařízení Google Home / Nest, pokud se hlasové oznámení nepřehraje správně
3. 🗣️ Zařízení vysloví čas v jazyce Home Assistant (pokud je zapnuto)

Vše probíhá automaticky bez nutnosti konfigurovat automatizace!

## 🗣️ Zpracování jazyka

Jazyk je automaticky rozpoznán z Home Assistant.

🌐 **Jazyk oznámení:** Možnost zvolit jazyk hlasových oznámení nezávisle na jazyce nastaveném v Home Assistant (dostupné: Italiano, English, Deutsch, Español, Français, Português, Polski, Čeština, Slovenčina, nebo Automaticky pro sledování jazyka Home Assistant).

Příklady oznámení:

| Jazyk | Čas | Oznámení |
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

## 🔔 Zvon (úvodní zvonění)

Pokud je možnost use_chime aktivní:
- přehraje se zvuk oznámení nebo vybraný zvuk
- systém čeká konfigurovatelný počet sekund (výchozí: 1,2)
- spustí se hlasové oznámení (pokud je zapnuto)

Vzniká tak efekt podobný skutečnému kyvadlu 🎶.

## 🧩 Možnosti konfigurace

| Možnost | Popis |
|------|------------|
| player_type | Typ přehrávače (Alexa, Google Home, Generický) |
| player | Cílové zařízení |
| start_hour | Čas začátku provozu |
| end_hour | Čas konce provozu |
| enabled | Zapíná/vypíná kyvadlo |
| announce_half_hours | Zapíná oznámení každou půl hodinu (jinak pouze každou hodinu) |
| after_chime_delay | Čekací doba v sekundách mezi zvonkem a hlasovým oznámením (výchozí: 1,2) |
| announce_half_hours_voice | Zapíná/vypíná hlasové oznámení v půl hodinách (zvon stále hraje) |
| voice_announcement | Zapíná/vypíná hlasové oznámení času |
| tower_clock | Zapíná westminsterskou melodii ve 12:00 |
| use_chime | Zapíná/vypíná zvon před oznámením |
| preset_chime | Výběr zvuku zvonu (12 dostupných předvoleb) |
| custom_chime_path | Cesta k vlastnímu zvuku zvonu |

Výchozí hodnoty:

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

K dispozici je metoda ručního testu:

Která:
- přečte aktuální čas
- vygeneruje celou větu (např. "Je 15 hodin a 42 minut")
- okamžitě ji přehraje na vybraném zařízení

Užitečné pro ověření: jazyka, hlasitosti, zvonu, správné funkce TTS

## 🔍 Stavový senzor

Digital Pendulum obsahuje diagnostický senzor:

`binary_sensor.digital_pendulum_status_warning`

**Stavy:**
- ✅ **OFF** - Vše funguje správně
- ⚠️ **ON** - Zjištěny problémy (integrace zakázána, Alexa offline atd.)

**Použití:**
- Monitorování dashboardu
- Automatizace oznámení
- Rychlá diagnostika

## 📦 Požadavky

> ✨ **Dostupné na HACS** - zjednodušená instalace a aktualizace!

- 🏠 Home Assistant 2024.1.0 nebo vyšší
- 🔊 Kompatibilní zařízení media_player (viz [Podporovaná zařízení](#-podporovaná-zařízení))
- 📡 Pro Alexa: [alexa_media_player](https://github.com/custom-components/alexa_media_player) nainstalovaný přes HACS
- 📡 Pro Google Home / Nest: integrace Google Cast (nativní v HA)

## 💾 Instalace

### Přes HACS (doporučeno)

1. Otevřete **HACS** v postranním menu
2. Přejděte na **Integrace**
3. Vyhledejte **"Digital Pendulum"**
4. Klikněte na **Stáhnout**
5. **Restartujte Home Assistant**
6. Přejděte na **Nastavení** → **Zařízení a služby** → **Přidat integraci**
7. Vyhledejte **"Digital Pendulum"**
8. Postupujte podle průvodce konfigurací

### Ruční instalace

1. Stáhněte nejnovější verzi z [GitHubu](https://github.com/Dregi56/digital_pendulum/releases)
2. Rozbalte soubory
3. Zkopírujte složku `digital_pendulum` do `config/custom_components/`
4. Restartujte Home Assistant
5. Přejděte na **Nastavení** → **Zařízení a služby** → **Přidat integraci**
6. Vyhledejte **"Digital Pendulum"**
7. Postupujte podle průvodce konfigurací

## 🎯 Ideální použití

- ✔️ Chytré domácnosti
- ✔️ Kanceláře
- ✔️ Společné prostory
- ✔️ Efekt "moderního kyvadla"
- ✔️ Nenápadná připomínka času

## 🔧 Řešení problémů

### Problémy s Alexou nebo chyba "Cannot find EU skill"

Problém s **alexa_media_player**, nikoli s Digital Pendulum.

**Rychlé řešení:**
1. Nastavení → Zařízení a služby → Alexa Media Player
2. Tři tečky → Znovu načíst
3. Pokud nefunguje: odinstalujte a znovu nainstalujte Alexa Media Player

---

### Google Home / Nest: žádné hlasové oznámení

Digital Pendulum používá TTS engine nakonfigurovaný v HA pro zařízení Google.

Jedná se o známý problém s časováním u zařízení Google. Hlasové oznámení může být přerušeno nebo přeskočeno, pokud je prodleva po zvonu příliš krátká.

1. Zkontrolujte, že je v HA nakonfigurován TTS engine (Nastavení → Hlasové asistenty)
2. Zkontrolujte log HA pro chyby TTS
3. Zvyšte hodnotu **"Prodleva po zvonu"** (zkuste 2,0 nebo 3,0 sekundy)
4. Pro ověření zkuste tlačítko "Test"

---

### Špatný jazyk

Digital Pendulum automaticky používá jazyk Home Assistant.

1. Zkontrolujte: Nastavení → Systém → Obecné → Jazyk
2. Podporované jazyky: 🇮🇹 🇬🇧 🇫🇷 🇩🇪 🇪🇸 🇵🇱 🇨🇿 🇸🇰 🇵🇹
3. Po změně jazyka restartujte Home Assistant

---

### Žádná oznámení

**Zkontrolujte:**
- Je integrace zapnuta? (Přepínač ON)
- Jste v nakonfigurovaném časovém rozsahu? (výchozí 8:00-22:00)
- Je zařízení online?
- Je vybrán správný typ přehrávače? (Alexa, Google, Generický)
- Zkuste tlačítko "Test"

---

### Pouze zvon nebo pouze hlas

- **Pouze zvon:** Zapněte "Hlasové oznámení"
- **Pouze hlas:** Zapněte "Použít zvon"

---

### Westminster nehraje ve 12

- Zkontrolujte, že je aktivní "Věžní hodiny"
- Funguje **pouze ve 12:00** (poledne, ne půlnoc)

---

## 🚀 Možný budoucí vývoj

- ⏳ Oznámení každých 15 minut
- 🔇 Automatická noční hlasitost

---

## ☕ Podpořte projekt

Líbí se vám tento projekt? Pokud vám přijde užitečný, kupte mi virtuální kávu na podporu budoucího vývoje! Každý malý příspěvek je velmi ceněn. 🙏

**Digital Pendulum je a vždy zůstane zdarma a open source.** Dary jsou zcela dobrovolné! ❤️

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/dregi56)

💡 **Preferujete jiné metody?** Můžete použít:

[![revolut](https://img.shields.io/badge/Revolut-0075EB?style=for-the-badge&logo=revolut&logoColor=white)](https://revolut.me/egidio5t9d)
