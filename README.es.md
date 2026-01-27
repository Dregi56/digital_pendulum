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
[Español](README.es.md) |
[Deutsch](README.de.md) |
[Français](README.fr.md) 
<br>👉Este es el README en español. Usa el selector de idioma de arriba

## ❤️ ¿Te gusta Digital Pendulum?

Si te resulta útil, considera dejar una ⭐ en GitHub:  
👉 **https://github.com/Dregi56/digital_pendulum**
<br>Gracias.

## 📌 Descripción

Digital Pendulum es una integración personalizada para Home Assistant que anuncia la hora por voz, como un péndulo digital 🕰️.


Usando un dispositivo Alexa como altavoz, el sistema:

- 📢 anuncia la hora cada 30 minutos  
- 🌍 habla automáticamente en el idioma configurado en Home Assistant  
- ⏰ funciona solo dentro de un intervalo horario configurable 
- 🔔 puede reproducir un sonido personalizado (por defecto el sonido 'announce' (chime)) antes del anuncio
- 🏰 puede reproducir la melodía de Westminster a las 12 en punto  

El resultado es un efecto elegante y discreto, ideal para el hogar o la oficina.

## ✨ Funciones principales

### 🕑 Anuncio automático de la hora
- cada hora en punto (xx:00)
- cada media hora (xx:30)

### 🌐 Soporte multilingüe automático
- Italiano 🇮🇹
- Inglés 🇬🇧
- Francés 🇫🇷
- Alemán 🇩🇪 (con gestión correcta de “halb”)
- Español 🇪🇸

retorno automático al italiano

### ⏱️ Intervalo horario configurable
- p. ej., solo de 8:00 a 22:00

### 🔔 Campana opcional
- 🔕 breve anuncio silencioso antes del TTS
- 🎵 sonidos personalizados. Si se define una ruta, sonido local

### 🧪 Función de prueba
- para probar inmediatamente el anuncio

### 🎯 Comportamiento
- Preset: "church-bell": sonido predeterminado
- Preset: "simple-bell": campana elegida de la biblioteca
- Preset: "custom" + ruta vacía: sonido 'announce' de Alexa
- Preset: "custom" + ruta válida: reproduce un archivo seleccionado
- Preset: "tower-clock": melodía de Westminster a las 12 en punto
- Use Chime: OFF: sin sonido, solo TTS (anuncio de la hora)

## ⚙️ Cómo funciona

El corazón del sistema es la clase:

class DigitalPendulum

que:
- se registra en un temporizador interno (cada 1 minuto)
- comprueba:
  - si la integración está habilitada
  - si la hora está dentro del intervalo permitido
  - si el minuto es 00 o 30
- construye el texto hablado según el idioma
- envía el anuncio al dispositivo Alexa configurado

## 🗣️ Gestión de idiomas

El idioma se detecta automáticamente desde:

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

Si la opción use_chime está activada:
- se envía un anuncio vacío
- el sistema espera 1,3 segundos
- comienza el TTS con la hora  

Esto crea un efecto similar al de un péndulo real 🎶.

## 🧩 Opciones de configuración

| Opción | Descripción |
|------|------------|
| player | Dispositivo Alexa de destino |
| start_hour | Hora de inicio |
| end_hour | Hora de fin |
| enabled | Habilitar/deshabilitar el péndulo |
| tower-clock | Habilitar/deshabilitar la melodía de las 12 |
| use_chime | Activar/desactivar la campana |

Valores predeterminados:

- ⏰ start_hour → DEFAULT_START_HOUR  
- ⏰ end_hour → DEFAULT_END_HOUR  
- 🔔 use_chime → DEFAULT_USE_CHIME  
- ✅ enabled → DEFAULT_ENABLED  

## 🧪 Prueba inmediata

Hay disponible un método de prueba manual:

async_test_announcement()

Que:
- lee la hora actual
- genera una frase completa (p. ej., “Son las 15:42”)
- la reproduce inmediatamente en el dispositivo Alexa  

Útil para verificar: idioma, volumen, campana, correcto funcionamiento del TTS

## 📦 Requisitos

- 🏠 Home Assistant
- 🔊 Alexa Media Player instalado y funcionando
- 📡 Dispositivo Alexa configurado como reproductor

## 🎯 Uso ideal

- ✔️ Hogares inteligentes
- ✔️ Oficinas
- ✔️ Espacios comunes
- ✔️ Efecto “péndulo moderno”
- ✔️ Recordatorio del tiempo no invasivo

## 🚀 Posibles evoluciones futuras

- ⏳ Anuncios cada 15 minutos
- 🔇 Volumen nocturno automático
- 🗓️ Anuncio del día
- 📣 Soporte para otros sistemas TTS

---

## 

## ☕ Apoya el proyecto

¿Te gusta este proyecto? Si te resulta útil, ¡invítame a un café virtual para apoyar futuras evoluciones! Cualquier pequeña contribución es muy apreciada. 🙏

**Digital Pendulum es y seguirá siendo siempre gratuito y de código abierto.** ¡Las donaciones son completamente voluntarias! ❤️


[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/dregi56)

💡 **¿Prefieres otros métodos?** Puedes usar:

[![revolut](https://img.shields.io/badge/Revolut-0075EB?style=for-the-badge&logo=revolut&logoColor=white)](https://revolut.me/egidio5t9d)
