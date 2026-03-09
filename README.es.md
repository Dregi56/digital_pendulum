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
[Français](README.fr.md) |
[Polski](README.pl.md) |
[Čeština](README.cs.md) |
[Slovenčina](README.sk.md) |
[Português](README.pt.md)

<br>👉 Este es el README en español. Use el selector de idioma de arriba.

## ❤️ ¿Le gusta Digital Pendulum?

Si le resulta útil, considere dejar una ⭐ en GitHub:  
👉 **https://github.com/Dregi56/digital_pendulum**
<br>Gracias.

## 📌 Descripción

Digital Pendulum es una integración personalizada para Home Assistant que anuncia vocalmente la hora, como un péndulo digital 🕰️.

Usando un altavoz inteligente compatible como reproductor, el sistema:

- 📢 anuncia la hora cada hora y/o cada media hora (configurable)
- 🌍 habla automáticamente en el idioma configurado en Home Assistant
- ⏰ solo funciona dentro de un intervalo de tiempo configurable
- 🔔 puede reproducir un sonido personalizado antes del anuncio
- 🔕 puede desactivar el anuncio de voz (solo campana)
- 🏰 puede reproducir el carillón de Westminster a las 12 en punto

El resultado es un efecto elegante y discreto, ideal para el hogar o la oficina.

## 🔊 Dispositivos compatibles

Digital Pendulum admite tres tipos de reproductores:

| Tipo | Descripción | Requisito |
|------|-------------|-------------|
| **Alexa** | Dispositivos Amazon Echo | [alexa_media_player](https://github.com/custom-components/alexa_media_player) vía HACS |
| **Google Home / Nest** | Google Home, Nest Mini, Nest Hub, Chromecast | Google Cast (integración nativa de HA) |
| **Genérico** | Cualquier otro dispositivo HA media_player | Motor TTS configurado en HA (la funcionalidad puede variar) |

Durante la configuración se le pedirá primero que seleccione el tipo de reproductor y luego el dispositivo específico.

## ✨ Características principales

### 🕑 Anuncio automático de la hora
- cada hora (xx:00)
- cada media hora (xx:30) - opcional (solo campana o campana + voz, configurable)

### ⏱️ Retraso configurable después de la campana
- tiempo de espera ajustable entre la campana y el anuncio de voz (predeterminado: 1,2 segundos)
- especialmente útil para dispositivos Google Home / Nest, que pueden necesitar un retraso mayor para reproducir correctamente el anuncio de voz

### 🌐 Soporte multilingüe automático
- Italiano 🇮🇹
- English 🇬🇧
- Français 🇫🇷
- Deutsch 🇩🇪
- Español 🇪🇸
- Polski 🇵🇱
- Čeština 🇨🇿
- Slovenčina 🇸🇰
- Português 🇵🇹

retorno automático al italiano

🌐 **Idioma personalizable:** Es posible elegir un idioma diferente al configurado en Home Assistant (útil por ejemplo para quienes tienen HA en inglés).

### 🕐 Intervalo de tiempo configurable
- p.ej. solo de 8:00 a 22:00

### 🔔 Campana opcional
- 🎵 12 sonidos predefinidos para elegir
- 🎶 opción de usar un archivo de audio personalizado
- 🔕 sonido de notificación predeterminado (si no se selecciona nada)
- ⏳ opción de sonido dedicado para la media hora
  
### 🧪 Función de prueba
- para probar el anuncio inmediatamente

### 🎯 Comportamiento

**Campana (Chime):**
- **Preajustes disponibles**: 12 sonidos incluyendo church-bell, simple-bell, clock-chime, etc.
- **Sonido personalizado**: Seleccione "custom" e introduzca la ruta de su archivo de audio
- **Predeterminado**: sonido de notificación (si no selecciona nada)
- **Desactivado**: Desactive "use_chime" para no tener sonido antes del anuncio

**Melodía de Westminster (Reloj de torre):**
- Opción separada "tower_clock"
- Se reproduce **solo a las 12:00** (mediodía)
- Reemplaza la campana normal en ese momento

**Anuncio de voz:**
- **Activado** (predeterminado): el dispositivo pronuncia la hora después de la campana
- **Desactivado**: solo sonido de campana, sin anuncio de voz

**Anuncio de voz en la media hora:**
- **Activado** (predeterminado): el anuncio de voz se reproduce tanto en :00 como en :30
- **Desactivado**: la campana sigue sonando en :30, pero sin anuncio de voz

## ⚙️ Cómo funciona

Digital Pendulum se sincroniza con el reloj del sistema y comprueba automáticamente cada minuto si es hora de hacer un anuncio.

**Cuando se activa el anuncio:**
1. 🔔 Reproduce la campana elegida (si está activada)
2. ⏱️ Espera un número configurable de segundos (predeterminado: 1,2 s) — aumente este valor para dispositivos Google Home / Nest si el anuncio de voz no se reproduce correctamente
3. 🗣️ El dispositivo pronuncia la hora en el idioma de Home Assistant (si está activado)

¡Todo ocurre automáticamente sin necesidad de configurar automatizaciones!

## 🗣️ Gestión del idioma

El idioma se detecta automáticamente desde Home Assistant.

🌐 **Idioma de los anuncios:** Posibilidad de elegir el idioma de los anuncios de voz independientemente del idioma configurado en Home Assistant (disponibles: Italiano, English, Deutsch, Español, Français, Português, Polski, Čeština, Slovenčina, o Automático para seguir el idioma de Home Assistant).

Ejemplos de anuncios:

| Idioma | Hora | Anuncio |
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

## 🔔 Campana (sonido inicial)

Si la opción use_chime está activa:
- se reproduce el sonido de notificación o el sonido elegido
- el sistema espera un número configurable de segundos (predeterminado: 1,2)
- comienza el anuncio de voz (si está activado)

Esto crea un efecto similar a un péndulo real 🎶.

## 🧩 Opciones de configuración

| Opción | Descripción |
|------|------------|
| player_type | Tipo de dispositivo reproductor (Alexa, Google Home, Genérico) |
| player | Dispositivo de destino |
| start_hour | Hora de inicio de operación |
| end_hour | Hora de fin de operación |
| enabled | Activa/desactiva el péndulo |
| announce_half_hours | Activa los anuncios cada media hora (de lo contrario solo cada hora) |
| after_chime_delay | Tiempo de espera en segundos entre la campana y el anuncio de voz (predeterminado: 1,2) |
| announce_half_hours_voice | Activa/desactiva el anuncio de voz en las medias horas (la campana sigue sonando) |
| voice_announcement | Activa/desactiva el anuncio de voz de la hora |
| tower_clock | Activa la melodía de Westminster a las 12:00 |
| use_chime | Activa/desactiva la campana antes del anuncio |
| preset_chime | Elección del sonido de campana (12 preajustes disponibles) |
| custom_chime_path | Ruta para el sonido de campana personalizado |

Valores predeterminados:

- ⏰ start_hour → 8
- ⏰ end_hour → 22
- 🔔 use_chime → True
- 🗣️ voice_announcement → True
- ⏰ announce_half_hours → True
- 🏰 tower_clock → False
- ✅ enabled → True
- ⏱️ after_chime_delay → 1,2
- 🔇 announce_half_hours_voice → True

## 🧪 Prueba inmediata

Hay disponible un método de prueba manual:

Que:
- lee la hora actual
- genera una frase completa (p.ej. "Son las 15 horas y 42 minutos")
- la reproduce inmediatamente en el dispositivo seleccionado

Útil para verificar: idioma, volumen, campana, correcto funcionamiento del TTS

## 🔍 Sensor de estado

Digital Pendulum incluye un sensor de diagnóstico:

`binary_sensor.digital_pendulum_status_warning`

**Estados:**
- ✅ **OFF** - Todo funciona correctamente
- ⚠️ **ON** - Problemas detectados (integración desactivada, Alexa sin conexión, etc.)

**Usos:**
- Monitoreo del panel de control
- Automatizaciones de notificaciones
- Diagnóstico rápido

## 📦 Requisitos

> ✨ **Disponible en HACS** - ¡instalación y actualizaciones simplificadas!

- 🏠 Home Assistant 2024.1.0 o superior
- 🔊 Un dispositivo media_player compatible (ver [Dispositivos compatibles](#-dispositivos-compatibles))
- 📡 Para Alexa: [alexa_media_player](https://github.com/custom-components/alexa_media_player) instalado vía HACS
- 📡 Para Google Home / Nest: integración Google Cast (nativa en HA)

## 💾 Instalación

### Vía HACS (recomendado)

1. Abra **HACS** en el menú lateral
2. Vaya a **Integraciones**
3. Busque **"Digital Pendulum"**
4. Haga clic en **Descargar**
5. **Reinicie Home Assistant**
6. Vaya a **Configuración** → **Dispositivos y servicios** → **Añadir integración**
7. Busque **"Digital Pendulum"**
8. Siga la configuración guiada

### Instalación manual

1. Descargue la última versión de [GitHub](https://github.com/Dregi56/digital_pendulum/releases)
2. Extraiga los archivos
3. Copie la carpeta `digital_pendulum` a `config/custom_components/`
4. Reinicie Home Assistant
5. Vaya a **Configuración** → **Dispositivos y servicios** → **Añadir integración**
6. Busque **"Digital Pendulum"**
7. Siga la configuración guiada

## 🎯 Uso ideal

- ✔️ Hogares inteligentes
- ✔️ Oficinas
- ✔️ Áreas comunes
- ✔️ Efecto de "péndulo moderno"
- ✔️ Recordatorio de hora no invasivo

## 🔧 Solución de problemas

### Problemas con Alexa o error "Cannot find EU skill"

Problema con **alexa_media_player**, no con Digital Pendulum.

**Solución rápida:**
1. Configuración → Dispositivos y servicios → Alexa Media Player
2. Tres puntos → Recargar
3. Si no funciona: desinstale y reinstale Alexa Media Player

---

### Google Home / Nest: sin anuncio de voz

Digital Pendulum usa el motor TTS configurado en HA para dispositivos Google.

Este es un problema de temporización conocido con los dispositivos Google. El anuncio de voz puede cortarse u omitirse si el retraso después de la campana es demasiado corto.

1. Compruebe que hay un motor TTS configurado en HA (Configuración → Asistentes de voz)
2. Compruebe el registro de HA para errores de TTS
3. Aumente el valor de **"Retraso después de la campana"** (pruebe 2,0 o 3,0 segundos)
4. Use el botón "Test" para verificar

---

### Idioma incorrecto

Digital Pendulum usa automáticamente el idioma de Home Assistant.

1. Compruebe: Configuración → Sistema → General → Idioma
2. Idiomas compatibles: 🇮🇹 🇬🇧 🇫🇷 🇩🇪 🇪🇸 🇵🇱 🇨🇿 🇸🇰 🇵🇹
3. Después de cambiar el idioma, reinicie Home Assistant

---

### Sin anuncios

**Compruebe:**
- ¿Integración activada? (Interruptor ON)
- ¿Está dentro del intervalo de tiempo configurado? (predeterminado 8:00-22:00)
- ¿Dispositivo en línea?
- ¿Tipo de reproductor correcto seleccionado? (Alexa, Google, Genérico)
- Pruebe el botón "Test"

---

### Solo campana o solo voz

- **Solo campana:** Active "Anuncio de voz"
- **Solo voz:** Active "Usar campana"

---

### Westminster no suena a las 12

- Compruebe que "Reloj de torre" está activo
- Funciona **solo a las 12:00** (mediodía, no medianoche)

---

## 🚀 Posibles desarrollos futuros

- ⏳ Anuncios cada 15 minutos
- 🔇 Volumen nocturno automático

---

## ☕ Apoye el proyecto

¿Le gusta este proyecto? Si le resulta útil, ¡cómpreme un café virtual para apoyar los desarrollos futuros! Cada pequeña contribución es muy apreciada. 🙏

**Digital Pendulum es y seguirá siendo siempre gratuito y de código abierto.** ¡Las donaciones son completamente voluntarias! ❤️

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/dregi56)

💡 **¿Prefiere otros métodos?** Puede usar:

[![revolut](https://img.shields.io/badge/Revolut-0075EB?style=for-the-badge&logo=revolut&logoColor=white)](https://revolut.me/egidio5t9d)
