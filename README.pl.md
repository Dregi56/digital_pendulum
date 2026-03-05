# 🕰️ Digital Pendulum

Mówiące cyfrowe wahadło dla Home Assistant
<br>**Autor:** Egidio Ziggiotto (Dregi56)  e-mail: [dregi@cyberservices.com](mailto:dregi@cyberservices.com)

[![HACS](https://img.shields.io/badge/HACS-Default-41BDF5.svg)](https://hacs.xyz/)
[![Version](https://img.shields.io/github/v/release/Dregi56/digital_pendulum)](https://github.com/Dregi56/digital_pendulum/releases)
![License](https://img.shields.io/github/license/Dregi56/digital_pendulum)
[![GitHub stars](https://img.shields.io/github/stars/Dregi56/digital_pendulum?style=social)](https://github.com/Dregi56/digital_pendulum)

🌍 Dostępne języki:
[Italiano](README.it.md) |
[English](README.en.md) |
[Español](README.es.md) |
[Deutsch](README.de.md) |
[Français](README.fr.md) |
[Polski](README.pl.md) |
[Čeština](README.cs.md) |
[Slovenčina](README.sk.md) |
[Português](README.pt.md)

<br>👉 To jest README w języku polskim. Użyj selektora języka powyżej.

## ❤️ Podoba Ci się Digital Pendulum?

Jeśli uważasz go za przydatny, rozważ pozostawienie ⭐ na GitHubie:  
👉 **https://github.com/Dregi56/digital_pendulum**
<br>Dziękujemy.

## 📌 Opis

Digital Pendulum to niestandardowa integracja dla Home Assistant, która głosowo ogłasza godzinę, podobnie jak cyfrowy zegar wahadłowy 🕰️.

Używając kompatybilnego głośnika inteligentnego jako odtwarzacza, system:

- 📢 ogłasza godzinę co godzinę i/lub co pół godziny (konfigurowalne)
- 🌍 automatycznie mówi w języku ustawionym w Home Assistant
- ⏰ działa tylko w konfigurowalnym przedziale czasowym
- 🔔 może odtwarzać niestandardowy dźwięk przed ogłoszeniem
- 🔕 może wyłączyć ogłoszenie głosowe (tylko dzwonek)
- 🏰 może odtwarzać melodię Westminster o godzinie 12

Efektem jest elegancki i dyskretny efekt, idealny do domu lub biura.

## 🔊 Obsługiwane urządzenia

Digital Pendulum obsługuje trzy typy odtwarzaczy:

| Typ | Opis | Wymaganie |
|------|-------------|-------------|
| **Alexa** | Urządzenia Amazon Echo | [alexa_media_player](https://github.com/custom-components/alexa_media_player) przez HACS |
| **Google Home / Nest** | Google Home, Nest Mini, Nest Hub, Chromecast | Google Cast (natywna integracja HA) |
| **Ogólny** | Dowolne inne urządzenie HA media_player | Silnik TTS skonfigurowany w HA (funkcjonalność może się różnić) |

Podczas konfiguracji zostaniesz najpierw poproszony o wybranie typu odtwarzacza, a następnie konkretnego urządzenia.

## ✨ Główne funkcje

### 🕑 Automatyczne ogłaszanie godziny
- co godzinę (xx:00)
- co pół godziny (xx:30) - opcjonalne (tylko dzwonek lub dzwonek + głos, konfigurowalne)

### ⏱️ Konfigurowalne opóźnienie po dzwonku
- regulowany czas oczekiwania między dzwonkiem a ogłoszeniem głosowym (domyślnie: 1,2 sekundy)
- szczególnie przydatne dla urządzeń Google Home / Nest, które mogą potrzebować dłuższego opóźnienia, aby poprawnie odtworzyć ogłoszenie głosowe

### 🌐 Automatyczna obsługa wielu języków
- Italiano 🇮🇹
- English 🇬🇧
- Français 🇫🇷
- Deutsch 🇩🇪
- Español 🇪🇸
- Polski 🇵🇱
- Čeština 🇨🇿
- Slovenčina 🇸🇰
- Português 🇵🇹

automatyczny powrót do języka włoskiego

### 🕐 Konfigurowalny przedział czasowy
- np. tylko od 8:00 do 22:00

### 🔔 Opcjonalny dzwonek
- 🎵 12 predefiniowanych dźwięków do wyboru
- 🎶 opcja użycia własnego pliku audio
- 🔕 domyślny dźwięk powiadomienia (jeśli nic nie zostanie wybrane)

### 🧪 Funkcja testowa
- aby natychmiast wypróbować ogłoszenie

### 🎯 Zachowanie

**Dzwonek (Chime):**
- **Dostępne ustawienia wstępne**: 12 dźwięków, w tym church-bell, simple-bell, clock-chime itp.
- **Niestandardowy dźwięk**: Wybierz "custom" i wprowadź ścieżkę do swojego pliku audio
- **Domyślny**: dźwięk powiadomienia (jeśli nic nie wybierzesz)
- **Wyłączony**: Wyłącz "use_chime", aby nie było dźwięku przed ogłoszeniem

**Melodia Westminster (Zegar wieżowy):**
- Osobna opcja "tower_clock"
- Odtwarza się **tylko o 12:00** (południe)
- Zastępuje normalny dzwonek o tej porze

**Ogłoszenie głosowe:**
- **Włączone** (domyślnie): urządzenie wymawia godzinę po dzwonku
- **Wyłączone**: tylko dźwięk dzwonka, bez ogłoszenia głosowego

**Ogłoszenie głosowe o półgodzinach:**
- **Włączone** (domyślnie): ogłoszenie głosowe jest odtwarzane zarówno o :00, jak i o :30
- **Wyłączone**: dzwonek nadal gra o :30, ale bez ogłoszenia głosowego

## ⚙️ Jak to działa

Digital Pendulum synchronizuje się z zegarem systemowym i automatycznie sprawdza co minutę, czy nadszedł czas na ogłoszenie.

**Gdy ogłoszenie się uruchamia:**
1. 🔔 Odtwarza wybrany dzwonek (jeśli jest włączony)
2. ⏱️ Czeka konfigurowalną liczbę sekund (domyślnie: 1,2 s) — zwiększ tę wartość dla urządzeń Google Home / Nest, jeśli ogłoszenie głosowe nie odtwarza się poprawnie
3. 🗣️ Urządzenie wymawia godzinę w języku Home Assistant (jeśli jest włączone)

Wszystko dzieje się automatycznie bez konieczności konfigurowania automatyzacji!

## 🗣️ Obsługa języka

Język jest automatycznie wykrywany z:

self.hass.config.language

Przykłady ogłoszeń:

| Język | Godzina | Ogłoszenie |
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

## 🔔 Dzwonek (dźwięk początkowy)

Jeśli opcja use_chime jest aktywna:
- odtwarzany jest dźwięk powiadomienia lub wybrany dźwięk
- system czeka konfigurowalną liczbę sekund (domyślnie: 1,2)
- rozpoczyna się ogłoszenie głosowe (jeśli jest włączone)

Tworzy to efekt podobny do prawdziwego wahadła 🎶.

## 🧩 Opcje konfiguracji

| Opcja | Opis |
|------|------------|
| player_type | Typ urządzenia odtwarzającego (Alexa, Google Home, Ogólny) |
| player | Urządzenie docelowe |
| start_hour | Godzina rozpoczęcia działania |
| end_hour | Godzina zakończenia działania |
| enabled | Włącza/wyłącza wahadło |
| announce_half_hours | Włącza ogłoszenia co pół godziny (w przeciwnym razie tylko co godzinę) |
| after_chime_delay | Czas oczekiwania w sekundach między dzwonkiem a ogłoszeniem głosowym (domyślnie: 1,2) |
| announce_half_hours_voice | Włącza/wyłącza ogłoszenie głosowe o półgodzinach (dzwonek nadal gra) |
| voice_announcement | Włącza/wyłącza głosowe ogłoszenie godziny |
| tower_clock | Włącza melodię Westminster o 12:00 |
| use_chime | Włącza/wyłącza dzwonek przed ogłoszeniem |
| preset_chime | Wybór dźwięku dzwonka (12 dostępnych ustawień wstępnych) |
| custom_chime_path | Ścieżka do niestandardowego dźwięku dzwonka |

Wartości domyślne:

- ⏰ start_hour → 8
- ⏰ end_hour → 22
- 🔔 use_chime → True
- 🗣️ voice_announcement → True
- ⏰ announce_half_hours → True
- 🏰 tower_clock → False
- ✅ enabled → True
- ⏱️ after_chime_delay → 1,2
- 🔇 announce_half_hours_voice → True

## 🧪 Natychmiastowy test

Dostępna jest metoda ręcznego testu:

Która:
- odczytuje aktualny czas
- generuje pełne zdanie (np. "Jest 15 godzin i 42 minuty")
- odtwarza je natychmiast na wybranym urządzeniu

Przydatne do weryfikacji: języka, głośności, dzwonka, prawidłowego działania TTS

## 🔍 Czujnik stanu

Digital Pendulum zawiera czujnik diagnostyczny:

`binary_sensor.digital_pendulum_status_warning`

**Stany:**
- ✅ **OFF** - Wszystko działa poprawnie
- ⚠️ **ON** - Wykryto problemy (integracja wyłączona, Alexa offline itp.)

**Zastosowania:**
- Monitorowanie pulpitu nawigacyjnego
- Automatyzacje powiadomień
- Szybka diagnostyka

## 📦 Wymagania

> ✨ **Dostępne na HACS** - uproszczona instalacja i aktualizacje!

- 🏠 Home Assistant 2024.1.0 lub wyższy
- 🔊 Kompatybilne urządzenie media_player (zobacz [Obsługiwane urządzenia](#-obsługiwane-urządzenia))
- 📡 Dla Alexa: [alexa_media_player](https://github.com/custom-components/alexa_media_player) zainstalowany przez HACS
- 📡 Dla Google Home / Nest: integracja Google Cast (natywna w HA)

## 💾 Instalacja

### Przez HACS (zalecane)

1. Otwórz **HACS** w menu bocznym
2. Przejdź do **Integracje**
3. Wyszukaj **"Digital Pendulum"**
4. Kliknij **Pobierz**
5. **Uruchom ponownie Home Assistant**
6. Przejdź do **Ustawienia** → **Urządzenia i usługi** → **Dodaj integrację**
7. Wyszukaj **"Digital Pendulum"**
8. Postępuj zgodnie z konfiguracją prowadzoną

### Instalacja ręczna

1. Pobierz najnowszą wersję z [GitHub](https://github.com/Dregi56/digital_pendulum/releases)
2. Rozpakuj pliki
3. Skopiuj folder `digital_pendulum` do `config/custom_components/`
4. Uruchom ponownie Home Assistant
5. Przejdź do **Ustawienia** → **Urządzenia i usługi** → **Dodaj integrację**
6. Wyszukaj **"Digital Pendulum"**
7. Postępuj zgodnie z konfiguracją prowadzoną

## 🎯 Idealne zastosowanie

- ✔️ Inteligentne domy
- ✔️ Biura
- ✔️ Obszary wspólne
- ✔️ Efekt "nowoczesnego wahadła"
- ✔️ Nienachalne przypomnienie o godzinie

## 🔧 Rozwiązywanie problemów

### Problemy z Alexą lub błąd "Cannot find EU skill"

Problem z **alexa_media_player**, nie z Digital Pendulum.

**Szybkie rozwiązanie:**
1. Ustawienia → Urządzenia i usługi → Alexa Media Player
2. Trzy kropki → Przeładuj
3. Jeśli nie działa: odinstaluj i zainstaluj ponownie Alexa Media Player

---

### Google Home / Nest: brak ogłoszenia głosowego

Digital Pendulum używa silnika TTS skonfigurowanego w HA dla urządzeń Google.

Jest to znany problem z synchronizacją czasową w urządzeniach Google. Ogłoszenie głosowe może być przerwane lub pominięte, jeśli opóźnienie po dzwonku jest zbyt krótkie.

1. Sprawdź, czy w HA jest skonfigurowany silnik TTS (Ustawienia → Asystenci głosowi)
2. Sprawdź dziennik HA pod kątem błędów TTS
3. Zwiększ wartość **"Opóźnienie po dzwonku"** (spróbuj 2,0 lub 3,0 sekundy)
4. Użyj przycisku "Test", aby sprawdzić

---

### Niewłaściwy język

Digital Pendulum automatycznie używa języka Home Assistant.

1. Sprawdź: Ustawienia → System → Ogólne → Język
2. Obsługiwane języki: 🇮🇹 🇬🇧 🇫🇷 🇩🇪 🇪🇸 🇵🇱 🇨🇿 🇸🇰 🇵🇹
3. Po zmianie języka uruchom ponownie Home Assistant

---

### Brak ogłoszeń

**Sprawdź:**
- Integracja włączona? (Przełącznik ON)
- Czy jesteś w skonfigurowanym przedziale czasowym? (domyślnie 8:00-22:00)
- Urządzenie online?
- Wybrany właściwy typ odtwarzacza? (Alexa, Google, Ogólny)
- Spróbuj przycisku "Test"

---

### Tylko dzwonek lub tylko głos

- **Tylko dzwonek:** Włącz "Ogłoszenie głosowe"
- **Tylko głos:** Włącz "Użyj dzwonka"

---

### Westminster nie gra o 12

- Sprawdź, czy "Zegar wieżowy" jest aktywny
- Działa **tylko o 12:00** (południe, nie północ)

---

## 🚀 Możliwy przyszły rozwój

- ⏳ Ogłoszenia co 15 minut
- 🔇 Automatyczna głośność nocna

---

## ☕ Wesprzyj projekt

Podoba Ci się ten projekt? Jeśli uważasz go za przydatny, kup mi wirtualną kawę, aby wesprzeć przyszły rozwój! Każdy mały wkład jest bardzo doceniany. 🙏

**Digital Pendulum jest i zawsze pozostanie darmowy i open source.** Darowizny są całkowicie dobrowolne! ❤️

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/dregi56)

💡 **Wolisz inne metody?** Możesz użyć:

[![revolut](https://img.shields.io/badge/Revolut-0075EB?style=for-the-badge&logo=revolut&logoColor=white)](https://revolut.me/egidio5t9d)
