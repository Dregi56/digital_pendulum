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

<br>👉Este es el README en Español. Usa el selector de idioma arriba


## ❤️ ¿Te gusta Digital Pendulum?

Si te resulta útil, considera dejar una ⭐ en GitHub:  
👉 **https://github.com/Dregi56/digital_pendulum**
<br>Gracias.

## 📌 Descripción

Digital Pendulum es una integración personalizada para Home Assistant que anuncia vocalmente la hora, igual que un péndulo digital 🕰️.


Utilizando un dispositivo Alexa como altavoz, el sistema:

- 📢 anuncia la hora cada hora y/o cada media hora (configurable)
- 🌍 habla automáticamente en el idioma configurado en Home Assistant  
- ⏰ funciona solo en una franja horaria configurable 
- 🔔 puede reproducir un sonido personalizado antes del anuncio
- 🔕 puede deshabilitar el anuncio de voz (solo campana)
- 🏰 puede reproducir la melodía Westminster a las 12 horas

El resultado es un efecto elegante y discreto, ideal para el hogar o la oficina.

## ✨ Funcionalidades principales

### 🕑 Anuncio automático de la hora
- cada hora (xx:00)
- cada media hora (xx:30) - opcional

### 🌐 Soporte multilingüe automático
- Italiano 🇮🇹
- Inglés 🇬🇧
- Francés 🇫🇷
- Alemán 🇩🇪 (con gestión correcta de "halb")
- Español 🇪🇸

fallback automático al italiano

### ⏱️ Franja horaria configurable
- ej. solo de 8:00 a 22:00

###  🔔 Campana opcional
- 🎵 12 sonidos predefinidos para elegir
- 🎶 posibilidad de usar un archivo de audio personalizado
- 🔕 sonido de notificación "announce" de Alexa (por defecto)

### 🧪 Función de prueba
- para probar el anuncio inmediatamente

### 🎯 Comportamiento

**Campana (Chime):**
- **Presets disponibles**: 12 sonidos entre los que se incluyen church-bell, simple-bell, clock-chime, etc.
- **Sonido personalizado**: Selecciona "custom" e introduce la ruta de tu archivo de audio
- **Por defecto**: Sonido "announce" de Alexa (si no seleccionas nada)
- **Desactivado**: Deshabilita "use_chime" para ningún sonido antes del anuncio

**Melodía Westminster (Tower Clock):**
- Opción separada "tower_clock"
- Suena **solo a las 12:00** (mediodía)
- Sustituye el chime normal a esa hora

**Anuncio de voz:**
- **Habilitado** (por defecto): Alexa pronuncia la hora después de la campana
- **Deshabilitado**: Solo sonido de campana, ningún anuncio de voz

**Anuncios de media hora:**
- **Habilitado** (por defecto): Anuncios a las :00 y :30
- **Deshabilitado**: Solo anuncios a las :00

## ⚙️ Cómo funciona

Digital Pendulum se sincroniza con el reloj del sistema y comprueba automáticamente cada minuto si es el momento de hacer un anuncio.

**Cuando se activa el anuncio:**
1. 🔔 Reproduce la campana elegida (si está habilitada)
2. ⏱️ Espera 1,2 segundos
3. 🗣️ Alexa pronuncia la hora en el idioma de Home Assistant (si está habilitado)

¡Todo ocurre automáticamente sin necesidad de configurar automatizaciones!

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

## 🔔 Chime (campana inicial)

Si la opción use_chime está activa:
- se reproduce el sonido de notificación de Alexa o el sonido elegido
- el sistema espera 1,2 segundos
- comienza el anuncio de voz (si está habilitado)

Esto crea un efecto similar a un péndulo real 🎶.

## 🧩 Opciones de configuración

| Opción | Descripción |
|------|------------|
| player | Dispositivo Alexa objetivo |
| start_hour | Hora de inicio de funcionamiento |
| end_hour | Hora de fin de funcionamiento |
| enabled | Habilita/deshabilita el péndulo |
| announce_half_hours | Habilita anuncios cada media hora (de lo contrario solo cada hora) |
| voice_announcement | Habilita/deshabilita el anuncio de voz de la hora |
| tower_clock | Habilita melodía Westminster a las 12:00 |
| use_chime | Activa/desactiva la campana antes del anuncio |
| preset_chime | Elección del sonido de campana (12 presets disponibles) |
| custom_chime_path | Ruta para sonido de campana personalizado |

Valores por defecto:

- ⏰ start_hour → 8
- ⏰ end_hour → 22
- 🔔 use_chime → True
- 🗣️ voice_announcement → True
- ⏰ announce_half_hours → True
- 🏰 tower_clock → False
- ✅ enabled → True

## 🧪 Prueba inmediata

Hay disponible un método de prueba manual:

Que:
- lee la hora actual
- genera una frase completa (ej. "Son las 15 y 42")
- la reproduce inmediatamente en el dispositivo Alexa  

Útil para verificar: idioma, volumen, chime, correcto funcionamiento del TTS

## 🔍 Sensor de estado

Digital Pendulum incluye un sensor de diagnóstico:

`binary_sensor.digital_pendulum_status_warning`

**Estados:**
- ✅ **OFF** - Todo funciona correctamente
- ⚠️ **ON** - Problemas detectados (integración desactivada, Alexa fuera de línea, etc.)

**Usos:**
- Monitoreo del panel de control
- Automatizaciones para notificaciones
- Diagnóstico rápido

## 📦 Requisitos

> ✨ **Disponible en HACS** - ¡instalación y actualizaciones simplificadas!

- 🏠 Home Assistant 2024.1.0 o superior
- 🔊 Alexa Media Player instalado y funcionando
- 📡 Dispositivo Alexa configurado como player

## 💾 Instalación

### Via HACS (recomendado)

1. Abre **HACS** en el menú lateral
2. Ve a **Integraciones**
3. Busca **"Digital Pendulum"**
4. Haz clic en **Descargar**
5. **Reinicia Home Assistant**
6. Ve a **Ajustes** → **Dispositivos y Servicios** → **Añadir Integración**
7. Busca **"Digital Pendulum"**
8. Sigue la configuración guiada

### Instalación manual

1. Descarga la última versión desde [GitHub](https://github.com/Dregi56/digital_pendulum/releases)
2. Extrae los archivos
3. Copia la carpeta `digital_pendulum` en `config/custom_components/`
4. Reinicia Home Assistant
5. Ve a **Ajustes** → **Dispositivos y Servicios** → **Añadir Integración**
6. Busca **"Digital Pendulum"**
7. Sigue la configuración guiada


## 🎯 Uso ideal

- ✔️ Hogares inteligentes
- ✔️ Oficinas
- ✔️ Espacios comunes
- ✔️ Efecto "péndulo moderno"
- ✔️ Recordatorio temporal no invasivo

## 🔧 Resolución de problemas

### Error "Cannot find EU skill" o problemas con Alexa

Problema de **Alexa Media Player**, no de Digital Pendulum.

**Solución rápida:**
1. Ajustes → Dispositivos y servicios → Alexa Media Player
2. Tres puntos → Recargar
3. Si no funciona: desinstala y reinstala Alexa Media Player

---

### Idioma incorrecto

Digital Pendulum utiliza automáticamente el idioma de Home Assistant.

1. Verifica: Ajustes → Sistema → General → Idioma
2. Idiomas soportados: 🇮🇹 🇬🇧 🇫🇷 🇩🇪 🇪🇸
3. Después de cambiar el idioma, reinicia Home Assistant

---

### Ningún anuncio

**Comprueba:**
- ¿Integración habilitada? (Interruptor ON)
- ¿Estás dentro de la franja horaria configurada? (por defecto 8:00-22:00)
- ¿Dispositivo Alexa en línea?
- Prueba el botón "Test"

---

### Solo campana o solo voz

- **Solo campana:** Activa "Voice announcement"
- **Solo voz:** Activa "Use chime"

---

### Westminster no suena a las 12

- Verifica que "Tower Clock" esté activo
- Funciona **solo a las 12:00** (mediodía, no medianoche)

---

## 🚀 Posibles evoluciones futuras

- ⏳ Anuncios cada 15 minutos
- 🔇 Volumen automático nocturno
- 🗓️ Anuncio del día
- 📣 Soporte para otros TTS

---

## 

## ☕ Apoya el proyecto

¿Te gusta este proyecto? Si te resulta útil, ¡invítame a un café virtual para apoyar los desarrollos futuros! Cada pequeña contribución es muy apreciada. 🙏

**Digital Pendulum es y seguirá siendo siempre gratuito y de código abierto.** ¡Las donaciones son completamente voluntarias! ❤️


[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/dregi56)

💡 **¿Prefieres otros métodos?** Puedes usar:

[![revolut](https://img.shields.io/badge/Revolut-0075EB?style=for-the-badge&logo=revolut&logoColor=white)](https://revolut.me/egidio5t9d)