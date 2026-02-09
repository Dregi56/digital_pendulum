# 🕰️ Digital Pendulum

Un péndulo digital parlante para Home Assistant  
<br>**Autor:** Egidio Ziggiotto (Dregi56)  e-mail: [dregi@cyberservices.com](mailto:dregi@cyberservices.com)

[![HACS](https://img.shields.io/badge/HACS-Default-41BDF5.svg)](https://hacs.xyz/)
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

- 📢 anuncia la hora cada hora y/o cada media hora (configurable)
- 🌍 habla automáticamente en el idioma configurado en Home Assistant  
- ⏰ funciona solo dentro de un horario configurable 
- 🔔 puede reproducir un sonido personalizado antes del anuncio
- 🔕 puede desactivar el anuncio por voz (solo campana)
- 🏰 puede reproducir la melodía Westminster a las 12

El resultado es un efecto elegante y discreto, ideal para el hogar o la oficina.

## ✨ Funcionalidades principales

### 🕑 Anuncio automático de la hora
- cada hora (xx:00)
- cada media hora (xx:30) – opcional

### 🌐 Soporte multilingüe automático
- Italiano 🇮🇹
- Inglés 🇬🇧
- Francés 🇫🇷
- Alemán 🇩🇪 (con gestión correcta de «halb»)
- Español 🇪🇸

cambio automático al italiano en caso de fallo

### ⏱️ Horario configurable
- ej. solo de 8:00 a 22:00

###  🔔 Campana opcional
- 🎵 12 sonidos predefinidos para elegir
- 🎶 posibilidad de usar un archivo de audio personalizado
- 🔕 sonido de notificación «announce» de Alexa (por defecto)

### 🧪 Función de prueba
- para probar inmediatamente el anuncio

### 🎯 Comportamiento

**Campana (Chime):**
- **Preajustes disponibles**: 12 sonidos como church-bell, simple-bell, clock-chime, etc.
- **Sonido personalizado**: Selecciona «custom» e introduce la ruta del archivo de audio
- **Por defecto**: Sonido «announce» de Alexa (si no se selecciona nada)
- **Desactivado**: Desactiva «use_chime» para no reproducir ningún sonido antes del anuncio

**Melodía Westminster (Tower Clock):**
- Opción separada «tower_clock»
- Suena **solo a las 12:00** (mediodía)
- Reemplaza la campana normal a esa hora

**Anuncio por voz:**
- **Activado** (por defecto): Alexa anuncia la hora después de la campana
- **Desactivado**: Solo campana, sin anuncio por voz

**Anuncios de media hora:**
- **Activados** (por defecto): Anuncios a :00 y :30
- **Desactivados**: Solo anuncios a :00

## ⚙️ Funcionamiento

El núcleo del sistema es la clase:

class DigitalPendulum

que:
- se registra en un temporizador interno sincronizado (cada minuto en el segundo :00)
- comprueba:
  - si la integración está activada
  - si la hora está dentro del rango permitido
  - si el minuto es :00 (o :30 si está activado)
- construye el texto hablado según el idioma
- reproduce la campana (si está activada)
- envía el anuncio por voz al dispositivo Alexa (si está activado)

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
| 🇪🇸 ES | 11:00 | Son las 11 |

## 🔔 Campana (señal inicial)

Si la opción use_chime está activada:
- se reproduce el sonido de notificación de Alexa o el sonido seleccionado
- el sistema espera 1,2 segundos
- comienza el anuncio por voz (si está activado)

Esto crea un efecto similar al de un péndulo real 🎶.

## 🧩 Opciones de configuración

| Opción | Descripción |
|------|------------|
| player | Dispositivo Alexa objetivo |
| start_hour | Hora de inicio |
| end_hour | Hora de finalización |
| enabled | Activar/desactivar el péndulo |
| announce_half_hours | Activar anuncios cada media hora (si no, solo cada hora) |
| voice_announcement | Activar/desactivar el anuncio por voz |
| tower_clock | Activar melodía Westminster a las 12:00 |
| use_chime | Activar/desactivar la campana antes del anuncio |
| preset_chime | Selección del sonido de campana (12 preajustes disponibles) |
| custom_chime_path | Ruta del sonido personalizado |

Valores predeterminados:

- ⏰ start_hour → 8
- ⏰ end_hour → 22
- 🔔 use_chime → True
- 🗣️ voice_announcement → True
- ⏰ announce_half_hours → True
- 🏰 tower_clock → False
- ✅ enabled → True

## 🧪 Prueba inmediata

Hay disponible un método de prueba manual:

async_test_announcement()

Que:
- lee la hora actual
- genera una frase completa (ej. «Ore 15 e 42»)
- la reproduce inmediatamente en el dispositivo Alexa  

Útil para verificar: idioma, volumen, campana, correcto funcionamiento del TTS

## 📦 Requisitos

> ✨ **Disponible en HACS** – instalación y actualizaciones simplificadas

- 🏠 Home Assistant 2024.1.0 o superior
- 🔊 Alexa Media Player instalado y funcionando
- 📡 Dispositivo Alexa configurado como reproductor


## 🎯 Uso ideal

- ✔️ Hogares inteligentes
- ✔️ Oficinas
- ✔️ Áreas comunes
- ✔️ Efecto «péndulo moderno»
- ✔️ Recordatorio de tiempo no invasivo

## 🚀 Posibles evoluciones futuras

- ⏳ Anuncios cada 15 minutos
- 🔇 Volumen nocturno automático
- 🗓️ Anuncio del día
- 📣 Soporte para otros TTS

---

## 

## ☕ Apoya el proyecto

¿Te gusta este proyecto? Si te resulta útil, ¡invítame a un café virtual para apoyar futuras evoluciones! Cualquier pequeña contribución es muy apreciada. 🙏

**Digital Pendulum es y seguirá siendo siempre gratuito y de código abierto.** ¡Las donaciones son completamente voluntarias! ❤️


[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/dregi56)

💡 **¿Prefieres otros métodos?** Puedes usar:

[![revolut](https://img.shields.io/badge/Revolut-0075EB?style=for-the-badge&logo=revolut&logoColor=white)](https://revolut.me/egidio5t9d)
