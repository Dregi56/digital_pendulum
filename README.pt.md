# 🕰️ Digital Pendulum

Um pêndulo digital falante para Home Assistant
<br>**Autor:** Egidio Ziggiotto (Dregi56)  e-mail: [dregi@cyberservices.com](mailto:dregi@cyberservices.com)

[![HACS](https://img.shields.io/badge/HACS-Default-41BDF5.svg)](https://hacs.xyz/)
[![Version](https://img.shields.io/github/v/release/Dregi56/digital_pendulum)](https://github.com/Dregi56/digital_pendulum/releases)
![License](https://img.shields.io/github/license/Dregi56/digital_pendulum)
[![GitHub stars](https://img.shields.io/github/stars/Dregi56/digital_pendulum?style=social)](https://github.com/Dregi56/digital_pendulum)

🌍 Idiomas disponíveis:
[Italiano](README.it.md) |
[English](README.en.md) |
[Español](README.es.md) |
[Deutsch](README.de.md) |
[Français](README.fr.md) |
[Polski](README.pl.md) |
[Čeština](README.cs.md) |
[Slovenčina](README.sk.md) |
[Português](README.pt.md)

<br>👉 Este é o README em português. Use o seletor de idioma acima.

## ❤️ Gosta do Digital Pendulum?

Se o achar útil, considere deixar uma ⭐ no GitHub:  
👉 **https://github.com/Dregi56/digital_pendulum**
<br>Obrigado.

## 📌 Descrição

Digital Pendulum é uma integração personalizada para Home Assistant que anuncia vocalmente a hora, como um pêndulo digital 🕰️.

Usando um altifalante inteligente compatível como reprodutor, o sistema:

- 📢 anuncia a hora a cada hora e/ou a cada meia hora (configurável)
- 🌍 fala automaticamente no idioma configurado no Home Assistant
- ⏰ funciona apenas dentro de um intervalo de tempo configurável
- 🔔 pode reproduzir um som personalizado antes do anúncio
- 🔕 pode desativar o anúncio de voz (apenas sino)
- 🏰 pode reproduzir o carrilhão de Westminster ao meio-dia

O resultado é um efeito elegante e discreto, ideal para casa ou escritório.

## 🔊 Dispositivos compatíveis

Digital Pendulum suporta três tipos de reprodutores:

| Tipo | Descrição | Requisito |
|------|-------------|-------------|
| **Alexa** | Dispositivos Amazon Echo | [alexa_media_player](https://github.com/custom-components/alexa_media_player) via HACS |
| **Google Home / Nest** | Google Home, Nest Mini, Nest Hub, Chromecast | Google Cast (integração nativa HA) |
| **Genérico** | Qualquer outro dispositivo HA media_player | Motor TTS configurado no HA (a funcionalidade pode variar) |

Durante a configuração, será solicitado que selecione primeiro o tipo de reprodutor e depois o dispositivo específico.

## ✨ Funcionalidades principais

### 🕑 Anúncio automático da hora
- a cada hora (xx:00)
- a cada meia hora (xx:30) - opcional (apenas sino ou sino + voz, configurável)

### ⏱️ Pausa configurável após o sino
- tempo de espera ajustável entre o sino e o anúncio de voz (padrão: 1,2 segundos)
- especialmente útil para dispositivos Google Home / Nest, que podem precisar de uma pausa mais longa para reproduzir corretamente o anúncio de voz

### 🌐 Suporte multilingue automático
- Italiano 🇮🇹
- English 🇬🇧
- Français 🇫🇷
- Deutsch 🇩🇪
- Español 🇪🇸
- Polski 🇵🇱
- Čeština 🇨🇿
- Slovenčina 🇸🇰
- Português 🇵🇹

retorno automático ao italiano

🌐 **Idioma personalizável:** É possível escolher um idioma diferente do configurado no Home Assistant (útil por exemplo para quem tem o HA em inglês).

### 🕐 Intervalo de tempo configurável
- ex. apenas das 8:00 às 22:00

### 🔔 Sino opcional
- 🎵 12 sons predefinidos para escolher
- 🎶 opção de usar um ficheiro de áudio personalizado
- 🔕 som de notificação padrão (se nada for selecionado)
- ⏳ Opção de som dedicado para a meia hora
  
### 🧪 Função de teste
- para experimentar imediatamente o anúncio

### 🎯 Comportamento

**Sino (Chime):**
- **Predefinições disponíveis**: 12 sons incluindo church-bell, simple-bell, clock-chime, etc.
- **Som personalizado**: Selecione "custom" e introduza o caminho do seu ficheiro de áudio
- **Padrão**: som de notificação (se não selecionar nada)
- **Desativado**: Desative "use_chime" para não ter som antes do anúncio

**Melodia de Westminster (Relógio de Torre):**
- Opção separada "tower_clock"
- Reproduz **apenas às 12:00** (meio-dia)
- Substitui o sino normal nesse momento

**Anúncio de voz:**
- **Ativado** (padrão): o dispositivo pronuncia a hora após o sino
- **Desativado**: apenas som do sino, sem anúncio de voz

**Anúncio de voz na meia hora:**
- **Ativado** (padrão): o anúncio de voz é reproduzido tanto às :00 como às :30
- **Desativado**: o sino continua a tocar às :30, mas sem anúncio de voz

## ⚙️ Como funciona

Digital Pendulum sincroniza-se com o relógio do sistema e verifica automaticamente a cada minuto se é hora de fazer um anúncio.

**Quando o anúncio é ativado:**
1. 🔔 Reproduz o sino escolhido (se ativado)
2. ⏱️ Aguarda um número configurável de segundos (padrão: 1,2 s) — aumente este valor para dispositivos Google Home / Nest se o anúncio de voz não for reproduzido corretamente
3. 🗣️ O dispositivo pronuncia a hora no idioma do Home Assistant (se ativado)

Tudo acontece automaticamente sem necessidade de configurar automatizações!

## 🗣️ Gestão do idioma

O idioma é detetado automaticamente pelo Home Assistant.
🌐 **Idioma dos anúncios:** Possibilidade de escolher o idioma dos anúncios vocais independentemente do idioma configurado no Home Assistant (disponíveis: Italiano, English, Deutsch, Español, Français, Português, Polski, Čeština, Slovenčina, ou Automático para seguir o idioma do Home Assistant).

Exemplos de anúncios:

| Idioma | Hora | Anúncio |
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

## 🔔 Sino (som inicial)

Se a opção use_chime estiver ativa:
- o som de notificação ou o som escolhido é reproduzido
- o sistema aguarda um número configurável de segundos (padrão: 1,2)
- o anúncio de voz começa (se ativado)

Isto cria um efeito semelhante a um pêndulo real 🎶.

## 🧩 Opções de configuração

| Opção | Descrição |
|------|------------|
| player_type | Tipo de dispositivo reprodutor (Alexa, Google Home, Genérico) |
| player | Dispositivo de destino |
| start_hour | Hora de início de funcionamento |
| end_hour | Hora de fim de funcionamento |
| enabled | Ativa/desativa o pêndulo |
| announce_half_hours | Ativa os anúncios a cada meia hora (caso contrário apenas a cada hora) |
| after_chime_delay | Tempo de espera em segundos entre o sino e o anúncio de voz (padrão: 1,2) |
| announce_half_hours_voice | Ativa/desativa o anúncio de voz nas meias horas (o sino continua a tocar) |
| voice_announcement | Ativa/desativa o anúncio de voz da hora |
| tower_clock | Ativa a melodia de Westminster às 12:00 |
| use_chime | Ativa/desativa o sino antes do anúncio |
| preset_chime | Escolha do som do sino (12 predefinições disponíveis) |
| custom_chime_path | Caminho para o som do sino personalizado |

Valores padrão:

- ⏰ start_hour → 8
- ⏰ end_hour → 22
- 🔔 use_chime → True
- 🗣️ voice_announcement → True
- ⏰ announce_half_hours → True
- 🏰 tower_clock → False
- ✅ enabled → True
- ⏱️ after_chime_delay → 1,2
- 🔇 announce_half_hours_voice → True

## 🧪 Teste imediato

Está disponível um método de teste manual:

Que:
- lê a hora atual
- gera uma frase completa (ex. "São 15 horas e 42 minutos")
- reproduz-a imediatamente no dispositivo selecionado

Útil para verificar: idioma, volume, sino, correto funcionamento do TTS

## 🔍 Sensor de estado

Digital Pendulum inclui um sensor de diagnóstico:

`binary_sensor.digital_pendulum_status_warning`

**Estados:**
- ✅ **OFF** - Tudo a funcionar corretamente
- ⚠️ **ON** - Problemas detetados (integração desativada, Alexa offline, etc.)

**Utilizações:**
- Monitorização do painel de controlo
- Automatizações de notificações
- Diagnóstico rápido

## 📦 Requisitos

> ✨ **Disponível no HACS** - instalação e atualizações simplificadas!

- 🏠 Home Assistant 2024.1.0 ou superior
- 🔊 Um dispositivo media_player compatível (ver [Dispositivos compatíveis](#-dispositivos-compatíveis))
- 📡 Para Alexa: [alexa_media_player](https://github.com/custom-components/alexa_media_player) instalado via HACS
- 📡 Para Google Home / Nest: integração Google Cast (nativa no HA)

## 💾 Instalação

### Via HACS (recomendado)

1. Abra o **HACS** no menu lateral
2. Vá a **Integrações**
3. Pesquise **"Digital Pendulum"**
4. Clique em **Transferir**
5. **Reinicie o Home Assistant**
6. Vá a **Definições** → **Dispositivos e serviços** → **Adicionar integração**
7. Pesquise **"Digital Pendulum"**
8. Siga a configuração guiada

### Instalação manual

1. Transfira a versão mais recente do [GitHub](https://github.com/Dregi56/digital_pendulum/releases)
2. Extraia os ficheiros
3. Copie a pasta `digital_pendulum` para `config/custom_components/`
4. Reinicie o Home Assistant
5. Vá a **Definições** → **Dispositivos e serviços** → **Adicionar integração**
6. Pesquise **"Digital Pendulum"**
7. Siga a configuração guiada

## 🎯 Utilização ideal

- ✔️ Casas inteligentes
- ✔️ Escritórios
- ✔️ Áreas comuns
- ✔️ Efeito de "pêndulo moderno"
- ✔️ Lembrete de hora não invasivo

## 🔧 Resolução de problemas

### Problemas com a Alexa ou erro "Cannot find EU skill"

Problema com o **alexa_media_player**, não com o Digital Pendulum.

**Solução rápida:**
1. Definições → Dispositivos e serviços → Alexa Media Player
2. Três pontos → Recarregar
3. Se não funcionar: desinstale e reinstale o Alexa Media Player

---

### Google Home / Nest: sem anúncio de voz

O Digital Pendulum usa o motor TTS configurado no HA para dispositivos Google.

Este é um problema de temporização conhecido com os dispositivos Google. O anúncio de voz pode ser cortado ou ignorado se a pausa após o sino for demasiado curta.

1. Verifique se está configurado um motor TTS no HA (Definições → Assistentes de voz)
2. Verifique o registo do HA para erros de TTS
3. Aumente o valor de **"Pausa após o sino"** (experimente 2,0 ou 3,0 segundos)
4. Use o botão "Teste" para verificar

---

### Idioma errado

O Digital Pendulum usa automaticamente o idioma do Home Assistant.

1. Verifique: Definições → Sistema → Geral → Idioma
2. Idiomas suportados: 🇮🇹 🇬🇧 🇫🇷 🇩🇪 🇪🇸 🇵🇱 🇨🇿 🇸🇰 🇵🇹
3. Após alterar o idioma, reinicie o Home Assistant

---

### Sem anúncios

**Verifique:**
- Integração ativada? (Interruptor ON)
- Está dentro do intervalo de tempo configurado? (padrão 8:00-22:00)
- Dispositivo online?
- Tipo de reprodutor correto selecionado? (Alexa, Google, Genérico)
- Experimente o botão "Teste"

---

### Apenas sino ou apenas voz

- **Apenas sino:** Ative "Anúncio de voz"
- **Apenas voz:** Ative "Usar sino"

---

### Westminster não toca às 12

- Verifique se "Relógio de Torre" está ativo
- Funciona **apenas às 12:00** (meio-dia, não meia-noite)

---

## 🚀 Possíveis desenvolvimentos futuros

- ⏳ Anúncios a cada 15 minutos
- 🔇 Volume noturno automático

---

## ☕ Apoie o projeto

Gosta deste projeto? Se o achar útil, ofereça-me um café virtual para apoiar desenvolvimentos futuros! Cada pequena contribuição é muito apreciada. 🙏

**Digital Pendulum é e continuará sempre a ser gratuito e open source.** As doações são completamente voluntárias! ❤️

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/dregi56)

💡 **Prefere outros métodos?** Pode usar:

[![revolut](https://img.shields.io/badge/Revolut-0075EB?style=for-the-badge&logo=revolut&logoColor=white)](https://revolut.me/egidio5t9d)
