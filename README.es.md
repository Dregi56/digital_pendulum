# 🕰️ Digital Pendulum

Un péndulo digital parlante para Home Assistant  
<br>**Autor:** Egidio Ziggiotto (Dregi56)  e-mail: [dregi@cyberservices.com](mailto:dregi@cyberservices.com)


[![HACS](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://hacs.xyz/)
[![Version](https://img.shields.io/github/v/release/Dregi56/digital_pendulum)](https://github.com/Dregi56/digital_pendulum/releases)
![License](https://img.shields.io/github/license/Dregi56/digital_pendulum)
[![GitHub stars](https://img.shields.io/github/stars/Dregi56/digital_pendulum?style=social)](https://github.com/Dregi56/digital_pendulum)

🌍 Idiomas disponibles:
[Italiano](README.it.md) |
[English](README.en.md) |
[Deutsch](README.de.md) |
[Français](README.fr.md) |
[Español](README.es.md)

## ❤️ ¿Te gusta Digital Pendulum?

Si te resulta útil, considera dejar una ⭐ en GitHub:  
👉 **https://github.com/Dregi56/digital_pendulum**
<br>Gracias.

## 📌 Descripción

Digital Pendulum es una integración personalizada para Home Assistant que anuncia la hora por voz, al igual que un péndulo digital 🕰️.


Utilizando un dispositivo Alexa como altavoz, el sistema:

- 📢 anuncia la hora cada 30 minutos  
- 🌍 habla automáticamente el idioma configurado en Home Assistant  
- ⏰ funciona solo dentro de un rango horario configurable  
- 🔔 puede reproducir un sonido personalizado (por defecto el sonido “announce” (chime) antes del anuncio  

El resultado es un efecto elegante y discreto, ideal para el hogar o la oficina.

## ✨ Funcionalidades principales

### 🕑 Anuncio automático de la hora
- cada hora (xx:00)
- cada media hora (xx:30)

### 🌐 Soporte multilingüe automático
- Italiano 🇮🇹
- Inglés 🇬🇧
- Francés 🇫🇷
- Alemán 🇩🇪 (con gestión correcta de “halb”)
- Español 🇪🇸

retorno automático al italiano

### ⏱️ Rango horario configurable
- ej. solo de 8:00 a 22:00

###  🔔 Chime opcional
- 🔕 breve anuncio silencioso antes del TTS
- 🎵 sonidos personalizados. Si se define una ruta, sonido local

### 🧪 Función de prueba
- para probar inmediatamente el anuncio

## ⚙️ Cómo funciona

El corazón del sistema es la clase:

class DigitalPendulum

que:
- se registra en un temporizador interno (cada 1 minuto)
- comprueba:
  - si la integración está habilitada
  - si la hora está dentro del rango permitido
  - si el minuto es 00 o 30
- construye el texto hablado según el idioma
- envía el anuncio al dispositivo Alexa configurado

## 🗣️ Gestión de idiomas

El idioma se detecta automáticamente a partir de:

self.hass.config.language

Ejemplos de anuncios:

| Idioma | Hora | Anuncio |
|------|------|--------|
| 🇮🇹 IT | 10:30 | Ore 10 e trenta |
| 🇬🇧 EN | 14:00 | It's 14 o'clock |
| 🇫🇷 FR | 9:30 | Il est 9 heures trente |
| 🇩🇪 DE | 16:30 | Es ist halb 17 |
| 🇪🇸 ES | 11:00 | Son las 11 en punto |

## 🔔 Chime (campana inicial)

Si la opción use_chime está activa:
- se envía un anuncio vacío
- el sistema espera 1,3 segundos
- comienza el TTS con la hora  

Esto crea un efecto similar a un péndulo real 🎶.

## 🧩 Opciones de configuración

| Opción | Descripción |
|------|------------|
| enabled | Habilita o deshabilita el péndulo |
| start_hour | Hora de inicio de funcionamiento |
| end_hour | Hora de fin de funcionamiento |
| player | Dispositivo Alexa objetivo |
| use_chime | Habilita/deshabilita la campana |

Valores predeterminados:

- ⏰ start_hour → DEFAULT_START_HOUR  
- ⏰ end_hour → DEFAULT_END_HOUR  
- 🔔 use_chime → DEFAULT_USE_CHIME  
- ✅ enabled → DEFAULT_ENABLED  

## 🧪 Prueba inmediata

Está disponible un método de prueba manual:

async_test_announcement()

Que:
- lee la hora actual
- genera una frase completa (ej. “Ore 15 e 42”)
- la reproduce inmediatamente en el dispositivo Alexa  

Útil para verificar: idioma, volumen, chime, correcto funcionamiento del TTS

## 📦 Requisitos

- 🏠 Home Assistant
- 🔊 Alexa Media Player instalado y funcionando
- 📡 Dispositivo Alexa configurado como reproductor

## 🎯 Uso ideal

- ✔️ Hogares inteligentes
- ✔️ Oficinas
- ✔️ Áreas comunes
- ✔️ Efecto “péndulo moderno”
- ✔️ Recordatorio temporal no intrusivo

## 🚀 Posibles evoluciones futuras

- ⏳ Anuncios cada 15 minutos
- 🔇 Volumen nocturno automático
- 🗓️ Anuncio del día
- 📣 Soporte para otros motores TTS

---

## 

## ☕ Apoya el proyecto

¿Te gusta este proyecto? Si te resulta útil, ¡invítame a un café virtual para apoyar futuras evoluciones! Cada pequeña contribución es muy apreciada. 🙏

**Digital Pendulum es y siempre será gratuito y de código abierto.** ¡Las donaciones son completamente voluntarias! ❤️

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/dregi56)

💡 **¿Prefieres otros métodos?** Puedes usar:

[![revolut](https://img.shields.io/badge/Revolut-0075EB?style=for-the-badge&logo=revolut&logoColor=white)](https://revolut.me/egidio5t9d)
