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

## ❤️ Gostou do Digital Pendulum?
Se o achar útil, considere deixar uma ⭐ no GitHub:  
👉 **https://github.com/Dregi56/digital_pendulum**
<br>Obrigado.

## 📌 Descrição
Digital Pendulum é uma integração personalizada para Home Assistant que anuncia vocalmente a hora, tal como um pêndulo digital 🕰️.
Utilizando um smart speaker compatível como player, o sistema:
- 📢 anuncia a hora a cada hora e/ou a cada meia hora (configurável)
- 🌍 fala automaticamente no idioma definido no Home Assistant  
- ⏰ funciona apenas numa faixa horária configurável 
- 🔔 pode reproduzir um som personalizado antes do anúncio
- 🔕 pode desativar o anúncio vocal (apenas sino)
- 🏰 pode tocar o carrilhão Westminster às 12:00

O resultado é um efeito elegante e discreto, ideal para casa ou escritório.

## 🔊 Dispositivos Suportados
Digital Pendulum suporta três tipos de player:

| Tipo | Descrição | Requisito |
|------|-------------|-----------|
| **Alexa** | Dispositivos Amazon Echo | [alexa_media_player](https://github.com/custom-components/alexa_media_player) via HACS |
| **Google Home / Nest** | Google Home, Nest Mini, Nest Hub, Chromecast | Integração Google Cast (nativa no HA) |
| **Generic** | Qualquer outro dispositivo media_player do HA | Motor TTS configurado no HA (funcionalidade pode variar) |

Durante a configuração, será solicitado que selecione primeiro o tipo de player e depois o dispositivo específico.

## ✨ Funcionalidades principais

### 🕑 Anúncio automático da hora
- a cada hora (xx:00)
- a cada meia hora (xx:30) - opcional

### 🌐 Suporte multilíngue automático
- Italiano 🇮🇹
- Inglês 🇬🇧
- Francês 🇫🇷
- Alemão 🇩🇪 (com gestão correta de "halb")
- Espanhol 🇪🇸
- Polaco 🇵🇱
- Checo 🇨🇿
- Eslovaco 🇸🇰
- Português 🇵🇹

fallback automático em italiano

### ⏱️ Faixa horária configurável
- ex. apenas das 8:00 às 22:00

### 🔔 Sino opcional
- 🎵 12 sons predefinidos para escolher
- 🎶 opção para usar um ficheiro de áudio personalizado
- 🔕 som de notificação predefinido (se nada for selecionado)

### 🧪 Função de teste
- para experimentar imediatamente o anúncio

### 🎯 Comportamento
**Sino (Chime):**
- **Predefinições disponíveis**: 12 sons, incluindo church-bell, simple-bell, clock-chime, etc.
- **Som personalizado**: Selecione "custom" e insira o caminho do seu ficheiro de áudio
- **Predefinido**: som de notificação (se não selecionar nada)
- **Desativado**: Desative "use_chime" para nenhum som antes do anúncio

**Melodia Westminster (Torre do relógio):**
- Opção separada "tower_clock"
- Toca **apenas às 12:00** (meio-dia)
- Substitui o chime normal nesse momento

**Anúncio vocal:**
- **Ativado** (predefinido): o dispositivo pronuncia a hora após o sino
- **Desativado**: apenas som do sino, sem anúncio vocal

**Anúncios a cada meia hora:**
- **Ativados** (predefinido): anúncios às :00 e às :30
- **Desativados**: anúncios apenas às :00

## ⚙️ Como funciona
Digital Pendulum sincroniza-se com o relógio do sistema e verifica automaticamente a cada minuto se é altura de fazer um anúncio.

**Quando o anúncio é acionado:**
1. 🔔 Reproduz o sino escolhido (se ativado)
2. ⏱️ Aguarda 1,2 segundos
3. 🗣️ O dispositivo pronuncia a hora no idioma do Home Assistant (se ativado)

Tudo acontece automaticamente sem necessidade de configurar automações!

## 🗣️ Gestão do idioma
O idioma é detetado automaticamente a partir de:
```
self.hass.config.language
```

Exemplos de anúncio:

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

## 🔔 Chime (sino inicial)
Se a opção use_chime estiver ativa:
- é reproduzido o som de notificação ou o som escolhido
- o sistema aguarda 1,2 segundos
- inicia o anúncio vocal (se ativado)

Isto cria um efeito semelhante a um verdadeiro pêndulo 🎶.

## 🧩 Opções de configuração

| Opção | Descrição |
|------|------------|
| player_type | Tipo de dispositivo player (Alexa, Google Home, Generic) |
| player | Dispositivo de destino |
| start_hour | Hora de início de funcionamento |
| end_hour | Hora de fim de funcionamento |
| enabled | Ativa/desativa o pêndulo |
| announce_half_hours | Ativa anúncios a cada meia hora (caso contrário, apenas a cada hora) |
| voice_announcement | Ativa/desativa o anúncio vocal da hora |
| tower_clock | Ativa a melodia Westminster às 12:00 |
| use_chime | Ativa/desativa o sino antes do anúncio |
| preset_chime | Escolha do som do sino (12 predefinições disponíveis) |
| custom_chime_path | Caminho para som de sino personalizado |

Valores predefinidos:
- ⏰ start_hour → 8
- ⏰ end_hour → 22
- 🔔 use_chime → True
- 🗣️ voice_announcement → True
- ⏰ announce_half_hours → True
- 🏰 tower_clock → False
- ✅ enabled → True

## 🧪 Teste imediato
Está disponível um método de teste manual que:
- lê a hora atual
- gera uma frase completa (ex. "São 15 horas e 42 minutos")
- reproduz-na imediatamente no dispositivo selecionado

Útil para verificar: idioma, volume, chime, correto funcionamento do TTS

## 🔍 Sensor de estado
Digital Pendulum inclui um sensor de diagnóstico:

`binary_sensor.digital_pendulum_status_warning`

**Estados:**
- ✅ **OFF** - Tudo funciona corretamente
- ⚠️ **ON** - Problemas detetados (integração desativada, Alexa offline, etc.)

**Utilizações:**
- Monitorização do dashboard
- Automações para notificações
- Diagnóstico rápido

## 📦 Requisitos
> ✨ **Disponível no HACS** - instalação e atualizações simplificadas!

- 🏠 Home Assistant 2024.1.0 ou superior
- 🔊 Um dispositivo media_player compatível (ver [Dispositivos Suportados](#-dispositivos-suportados))
- 📡 Para Alexa: [alexa_media_player](https://github.com/custom-components/alexa_media_player) instalado via HACS
- 📡 Para Google Home / Nest: integração Google Cast (nativa no HA)

## 💾 Instalação

### Via HACS (recomendado)
1. Abra o **HACS** no menu lateral
2. Vá para **Integrações**
3. Pesquise **"Digital Pendulum"**
4. Clique em **Transferir**
5. **Reinicie o Home Assistant**
6. Vá para **Definições** → **Dispositivos e serviços** → **Adicionar integração**
7. Pesquise **"Digital Pendulum"**
8. Siga a configuração guiada

### Instalação manual
1. Transfira a última versão do [GitHub](https://github.com/Dregi56/digital_pendulum/releases)
2. Extraia os ficheiros
3. Copie a pasta `digital_pendulum` para `config/custom_components/`
4. Reinicie o Home Assistant
5. Vá para **Definições** → **Dispositivos e serviços** → **Adicionar integração**
6. Pesquise **"Digital Pendulum"**
7. Siga a configuração guiada

## 🎯 Uso ideal
- ✔️ Casas inteligentes
- ✔️ Escritórios
- ✔️ Áreas comuns
- ✔️ Efeito "pêndulo moderno"
- ✔️ Lembrete horário não invasivo

## 🔧 Resolução de problemas

### Erro "Cannot find EU skill" ou problemas com Alexa
Problema do **alexa_media_player**, não do Digital Pendulum.

**Solução rápida:**
1. Definições → Dispositivos e serviços → Alexa Media Player
2. Três pontos → Recarregar
3. Se não funcionar: desinstale e reinstale o Alexa Media Player

---

### Google Home / Nest: sem anúncio vocal
Digital Pendulum usa o motor TTS configurado no HA para os dispositivos Google.
1. Verifique que um motor TTS está configurado no HA (Definições → Assistentes de voz)
2. Experimente o botão "Teste" para verificar
3. Consulte o registo do HA para erros de TTS

---

### Idioma incorreto
Digital Pendulum usa automaticamente o idioma do Home Assistant.
1. Verifique: Definições → Sistema → Geral → Idioma
2. Idiomas suportados: 🇮🇹 🇬🇧 🇫🇷 🇩🇪 🇪🇸 🇵🇱 🇨🇿 🇸🇰 🇵🇹
3. Após alterar o idioma, reinicie o Home Assistant

---

### Sem anúncio
**Verifique:**
- Integração ativada? (Switch ON)
- Está na faixa horária configurada? (padrão 8:00-22:00)
- Dispositivo online?
- Tipo de player correto selecionado? (Alexa, Google, Generic)
- Experimente o botão "Teste"

---

### Apenas sino ou apenas voz
- **Apenas sino:** Ative "Anúncio vocal"
- **Apenas voz:** Ative "Usar chime"

---

### Westminster não toca às 12
- Verifique que "Torre do relógio" está ativo
- Funciona **apenas às 12:00** (meio-dia, não meia-noite)

---

## 🚀 Possíveis desenvolvimentos futuros
- ⏳ Anúncios a cada 15 minutos
- 🔇 Volume noturno automático
- 🗓️ Anúncio do dia
- 📣 Suporte para motores TTS e players adicionais

---

## ☕ Apoie o projeto
Gostou deste projeto? Se o achar útil, ofereça-me um café virtual para apoiar os desenvolvimentos futuros! Cada pequena contribuição é muito apreciada. 🙏

**Digital Pendulum é e permanecerá sempre gratuito e de código aberto.** As doações são completamente voluntárias! ❤️

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/dregi56)

💡 **Prefere outros métodos?** Pode usar:

[![revolut](https://img.shields.io/badge/Revolut-0075EB?style=for-the-badge&logo=revolut&logoColor=white)](https://revolut.me/egidio5t9d)
