# 🕰️ Digital Pendulum  

Cyfrowy zegar wahadłowy z zapowiedzią głosową dla Home Assistant  
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

<br>👉To jest polska wersja README. Użyj selektora języka powyżej.

---

## ❤️ Podoba Ci się Digital Pendulum?

Jeśli projekt jest dla Ciebie przydatny, rozważ zostawienie ⭐ na GitHub:  
👉 **https://github.com/Dregi56/digital_pendulum**  
<br>Dziękuję.

---

## 📌 Opis

Digital Pendulum to niestandardowa integracja dla Home Assistant, która ogłasza godzinę głosowo – jak cyfrowy zegar wahadłowy 🕰️.

Wykorzystując urządzenie Alexa jako głośnik, system:

- 📢 ogłasza godzinę co pełną godzinę i/lub co pół godziny (konfigurowalne)  
- 🌍 automatycznie mówi w języku ustawionym w Home Assistant  
- ⏰ działa tylko w konfigurowalnym przedziale czasowym  
- 🔔 może odtworzyć spersonalizowany dźwięk przed zapowiedzią  
- 🔕 może wyłączyć zapowiedź głosową (tylko dzwonek)  
- 🏰 może odtworzyć melodię Westminster o godzinie 12  

Efekt jest elegancki i dyskretny – idealny do domu lub biura.

---

## ✨ Główne funkcje

### 🕑 Automatyczne ogłaszanie godziny
- co godzinę (xx:00)  
- co pół godziny (xx:30) – opcjonalnie  

### 🌐 Automatyczna obsługa wielu języków
- Włoski 🇮🇹
- Angielski 🇬🇧
- Francuski 🇫🇷
- Niemiecki 🇩🇪
- Hiszpański 🇪🇸
- Polski 🇵🇱
- Czeski 🇨🇿
- Słowacki 🇸🇰
- Portugalski 🇵🇹

automatyczny fallback na włoski

---

### ⏱️ Konfigurowalny przedział godzin
- np. tylko od 8:00 do 22:00  

### 🔔 Opcjonalny dzwonek
- 🎵 12 predefiniowanych dźwięków do wyboru  
- 🎶 możliwość użycia własnego pliku audio  
- 🔕 domyślny dźwięk powiadomienia Alexa „announce”  

### 🧪 Funkcja testowa
- umożliwia natychmiastowe przetestowanie zapowiedzi  

---

## 🎯 Działanie

**Dzwonek (Chime):**
- **Dostępne presety**: 12 dźwięków, m.in. church-bell, simple-bell, clock-chime itp.  
- **Dźwięk własny**: wybierz „custom” i podaj ścieżkę do pliku audio  
- **Domyślny**: dźwięk „announce” Alexa (jeśli nic nie wybrano)  
- **Wyłączony**: wyłącz „use_chime”, aby nie było dźwięku przed zapowiedzią  

**Melodia Westminster (Tower Clock):**
- Osobna opcja „tower_clock”  
- Odtwarzana **tylko o 12:00** (w południe)  
- Zastępuje zwykły dzwonek o tej godzinie  

**Zapowiedź głosowa:**
- **Włączona** (domyślnie): Alexa ogłasza godzinę po dzwonku  
- **Wyłączona**: tylko dzwonek, bez zapowiedzi  

**Zapowiedzi co pół godziny:**
- **Włączone** (domyślnie): zapowiedzi o :00 i :30  
- **Wyłączone**: tylko o :00  

---

## ⚙️ Jak to działa

Digital Pendulum synchronizuje się z zegarem systemowym i co minutę sprawdza, czy nadszedł czas ogłoszenia godziny.

**Gdy nadchodzi moment ogłoszenia:**
1. 🔔 Odtwarza wybrany dźwięk (jeśli włączony)  
2. ⏱️ Czeka 1,2 sekundy  
3. 🗣️ Alexa ogłasza godzinę w języku Home Assistant (jeśli włączona)  

Wszystko działa automatycznie – bez potrzeby tworzenia automatyzacji!

---

## 🗣️ Obsługa języków

Język jest automatycznie wykrywany z:

self.hass.config.language  

Przykłady zapowiedzi:

| Język | Godzina | Zapowiedź |
|------|---------|-----------|
| 🇮🇹 IT | 10:30 | Ore 10 e trenta |
| 🇬🇧 EN | 14:00 | It's 2 o'clock in the afternoon |
| 🇫🇷 FR | 9:30 | Il est 9 heures trente |
| 🇩🇪 DE | 16:30 | Es ist halb 17 |
| 🇪🇸 ES | 11:00 | Son las 11 |
| 🇵🇱 PL | 15:30 | Wpół do czwartej |
| 🇨🇿 CS | 8:30 | Půl deváté |
| 🇸🇰 SK | 8:30 | Pol deviatej |
| 🇵🇹 PT | 10:30 | São 10 e meia |
---

## 🔔 Chime (dzwonek początkowy)

Jeśli opcja use_chime jest aktywna:
- odtwarzany jest dźwięk powiadomienia Alexa lub wybrany dźwięk  
- system czeka 1,2 sekundy  
- rozpoczyna się zapowiedź głosowa (jeśli włączona)  

Tworzy to efekt podobny do prawdziwego zegara wahadłowego 🎶.

---

## 🧩 Opcje konfiguracji

| Opcja | Opis |
|-------|------|
| player | Docelowe urządzenie Alexa |
| start_hour | Godzina rozpoczęcia działania |
| end_hour | Godzina zakończenia działania |
| enabled | Włącza/wyłącza wahadło |
| announce_half_hours | Włącza zapowiedzi co pół godziny |
| voice_announcement | Włącza/wyłącza zapowiedź głosową |
| tower_clock | Włącza melodię Westminster o 12:00 |
| use_chime | Włącza/wyłącza dzwonek przed zapowiedzią |
| preset_chime | Wybór dźwięku (12 presetów) |
| custom_chime_path | Ścieżka do własnego pliku dźwiękowego |

Wartości domyślne:

- ⏰ start_hour → 8  
- ⏰ end_hour → 22  
- 🔔 use_chime → True  
- 🗣️ voice_announcement → True  
- ⏰ announce_half_hours → True  
- 🏰 tower_clock → False  
- ✅ enabled → True  

---

## 🧪 Natychmiastowy test

Dostępna jest funkcja testowa, która:

- odczytuje aktualną godzinę  
- generuje pełne zdanie (np. „Jest godzina 15:42”)  
- natychmiast odtwarza je na urządzeniu Alexa  

Przydatne do sprawdzenia: języka, głośności, dzwonka, poprawności działania TTS.

---

## 🔍 Sensor stanu

Digital Pendulum zawiera sensor diagnostyczny:

`binary_sensor.digital_pendulum_status_warning`

**Stany:**
- ✅ **OFF** – wszystko działa poprawnie  
- ⚠️ **ON** – wykryto problem (integracja wyłączona, Alexa offline itp.)  

**Zastosowanie:**
- monitorowanie na dashboardzie  
- automatyzacje powiadomień  
- szybka diagnostyka  

---

## 📦 Wymagania

> ✨ **Dostępne w HACS** – łatwa instalacja i aktualizacje!

- 🏠 Home Assistant 2024.1.0 lub nowszy  
- 🔊 Alexa Media Player zainstalowany i działający  
- 📡 Urządzenie Alexa skonfigurowane jako odtwarzacz  

---

## 💾 Instalacja

### Przez HACS (zalecane)

1. Otwórz **HACS** w menu bocznym  
2. Przejdź do **Integracje**  
3. Wyszukaj **„Digital Pendulum”**  
4. Kliknij **Pobierz**  
5. **Uruchom ponownie Home Assistant**  
6. Przejdź do **Ustawienia** → **Urządzenia i usługi** → **Dodaj integrację**  
7. Wyszukaj **„Digital Pendulum”**  
8. Postępuj zgodnie z kreatorem konfiguracji  

---

### Instalacja ręczna

1. Pobierz najnowszą wersję z GitHub  
2. Rozpakuj pliki  
3. Skopiuj folder `digital_pendulum` do `config/custom_components/`  
4. Uruchom ponownie Home Assistant  
5. Przejdź do **Ustawienia** → **Urządzenia i usługi** → **Dodaj integrację**  
6. Wyszukaj **„Digital Pendulum”**  
7. Postępuj zgodnie z kreatorem konfiguracji  

---

## 🎯 Idealne zastosowanie

- ✔️ Inteligentne domy  
- ✔️ Biura  
- ✔️ Przestrzenie wspólne  
- ✔️ Efekt „nowoczesnego wahadła”  
- ✔️ Nienachalny sygnał czasu  

---

## 🔧 Rozwiązywanie problemów

### Błąd „Cannot find EU skill” lub problemy z Alexa

To problem **Alexa Media Player**, nie Digital Pendulum.

**Szybkie rozwiązanie:**
1. Ustawienia → Urządzenia i usługi → Alexa Media Player  
2. Trzy kropki → Przeładuj  
3. Jeśli nie działa: odinstaluj i zainstaluj ponownie  

---

### Zły język

Digital Pendulum używa języka ustawionego w Home Assistant.

1. Sprawdź: Ustawienia → System → Ogólne → Język  
2. Obsługiwane języki: 🇮🇹 🇬🇧 🇫🇷 🇩🇪 🇪🇸 🇵🇱 🇨🇿 🇸🇰 🇵🇹 
3. Po zmianie języka uruchom ponownie Home Assistant  

---

### Brak zapowiedzi

Sprawdź:
- Czy integracja jest włączona?  
- Czy jesteś w ustawionym przedziale godzin? (domyślnie 8:00–22:00)  
- Czy urządzenie Alexa jest online?  
- Użyj przycisku „Test”  

---

### Tylko dzwonek lub tylko głos

- **Tylko dzwonek:** włącz „Voice announcement”  
- **Tylko głos:** włącz „Use chime”  

---

### Westminster nie gra o 12

- Sprawdź, czy „Tower Clock” jest włączone  
- Działa **tylko o 12:00** (w południe, nie o północy)  

---

## 🚀 Możliwe przyszłe funkcje

- ⏳ Zapowiedzi co 15 minut  
- 🔇 Automatyczne wyciszenie nocne  
- 🗓️ Ogłoszenie dnia tygodnia  
- 📣 Obsługa innych silników TTS  

---

## ☕ Wspieraj projekt

Podoba Ci się ten projekt? Jeśli jest dla Ciebie przydatny, możesz postawić mi wirtualną kawę, aby wesprzeć jego dalszy rozwój! Każde wsparcie jest bardzo mile widziane. 🙏  

**Digital Pendulum jest i zawsze będzie darmowy oraz open source.** Darowizny są całkowicie dobrowolne! ❤️  

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/dregi56)

💡 **Wolisz inne metody?** Możesz użyć:

[![revolut](https://img.shields.io/badge/Revolut-0075EB?style=for-the-badge&logo=revolut&logoColor=white)](https://revolut.me/egidio5t9d)

💡 **Wolisz inne metody?** Możesz użyć:

[![revolut](https://img.shields.io/badge/Revolut-0075EB?style=for-the-badge&logo=revolut&logoColor=white)](https://revolut.me/egidio5t9d)
