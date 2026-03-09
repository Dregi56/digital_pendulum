# 🕰️ Digital Pendulum

Une horloge à pendule numérique parlante pour Home Assistant
<br>**Auteur:** Egidio Ziggiotto (Dregi56)  e-mail: [dregi@cyberservices.com](mailto:dregi@cyberservices.com)

[![HACS](https://img.shields.io/badge/HACS-Default-41BDF5.svg)](https://hacs.xyz/)
[![Version](https://img.shields.io/github/v/release/Dregi56/digital_pendulum)](https://github.com/Dregi56/digital_pendulum/releases)
![License](https://img.shields.io/github/license/Dregi56/digital_pendulum)
[![GitHub stars](https://img.shields.io/github/stars/Dregi56/digital_pendulum?style=social)](https://github.com/Dregi56/digital_pendulum)

🌍 Langues disponibles:
[Italiano](README.it.md) |
[English](README.en.md) |
[Español](README.es.md) |
[Deutsch](README.de.md) |
[Français](README.fr.md) |
[Polski](README.pl.md) |
[Čeština](README.cs.md) |
[Slovenčina](README.sk.md) |
[Português](README.pt.md)

<br>👉 Ceci est le README en français. Utilisez le sélecteur de langue ci-dessus.

## ❤️ Vous aimez Digital Pendulum ?

Si vous le trouvez utile, pensez à laisser une ⭐ sur GitHub :  
👉 **https://github.com/Dregi56/digital_pendulum**
<br>Merci.

## 📌 Description

Digital Pendulum est une intégration personnalisée pour Home Assistant qui annonce vocalement l'heure, comme une horloge à pendule numérique 🕰️.

En utilisant un haut-parleur intelligent compatible comme lecteur, le système :

- 📢 annonce l'heure toutes les heures et/ou toutes les demi-heures (configurable)
- 🌍 parle automatiquement dans la langue configurée dans Home Assistant
- ⏰ fonctionne uniquement dans un créneau horaire configurable
- 🔔 peut jouer un son personnalisé avant l'annonce
- 🔕 peut désactiver l'annonce vocale (sonnerie uniquement)
- 🏰 peut jouer le carillon de Westminster à 12 heures

Le résultat est un effet élégant et discret, idéal pour la maison ou le bureau.

## 🔊 Appareils compatibles

Digital Pendulum prend en charge trois types de lecteurs :

| Type | Description | Prérequis |
|------|-------------|-------------|
| **Alexa** | Appareils Amazon Echo | [alexa_media_player](https://github.com/custom-components/alexa_media_player) via HACS |
| **Google Home / Nest** | Google Home, Nest Mini, Nest Hub, Chromecast | Google Cast (intégration native HA) |
| **Générique** | Tout autre appareil HA media_player | Moteur TTS configuré dans HA (les fonctionnalités peuvent varier) |

Lors de la configuration, il vous sera d'abord demandé de sélectionner le type de lecteur, puis l'appareil spécifique.

## ✨ Fonctionnalités principales

### 🕑 Annonce automatique de l'heure
- toutes les heures (xx:00)
- toutes les demi-heures (xx:30) - optionnel (sonnerie uniquement ou sonnerie + voix, configurable)

### ⏱️ Délai configurable après la sonnerie
- temps d'attente réglable entre la sonnerie et l'annonce vocale (défaut : 1,2 secondes)
- particulièrement utile pour les appareils Google Home / Nest, qui peuvent nécessiter un délai plus long pour reproduire correctement l'annonce vocale

### 🌐 Support multilingue automatique
- Italiano 🇮🇹
- English 🇬🇧
- Français 🇫🇷
- Deutsch 🇩🇪
- Español 🇪🇸
- Polski 🇵🇱
- Čeština 🇨🇿
- Slovenčina 🇸🇰
- Português 🇵🇹

retour automatique à l'italien

🌐 **Langue personnalisable:** Il est possible de choisir une langue différente de celle configurée dans Home Assistant (utile par exemple pour ceux qui ont HA en anglais).

### 🕐 Créneau horaire configurable
- ex. uniquement de 8h00 à 22h00

### 🔔 Sonnerie optionnelle
- 🎵 12 sons prédéfinis au choix
- 🎶 option d'utiliser un fichier audio personnalisé
- 🔕 son de notification par défaut (si rien n'est sélectionné)
- ⏳ Option pour un son dédié à la demi-heure

### 🧪 Fonction de test
- pour essayer immédiatement l'annonce

### 🎯 Comportement

**Sonnerie (Chime) :**
- **Préréglages disponibles** : 12 sons dont church-bell, simple-bell, clock-chime, etc.
- **Son personnalisé** : Sélectionnez "custom" et entrez le chemin de votre fichier audio
- **Par défaut** : son de notification (si vous ne sélectionnez rien)
- **Désactivé** : Désactivez "use_chime" pour aucun son avant l'annonce

**Mélodie de Westminster (Horloge de tour) :**
- Option séparée "tower_clock"
- Joue **uniquement à 12:00** (midi)
- Remplace la sonnerie normale à ce moment

**Annonce vocale :**
- **Activée** (par défaut) : l'appareil prononce l'heure après la sonnerie
- **Désactivée** : son de sonnerie uniquement, pas d'annonce vocale

**Annonce vocale à la demi-heure :**
- **Activée** (par défaut) : l'annonce vocale est diffusée à la fois à :00 et à :30
- **Désactivée** : la sonnerie joue toujours à :30, mais sans annonce vocale

## ⚙️ Fonctionnement

Digital Pendulum se synchronise avec l'horloge système et vérifie automatiquement chaque minute s'il est temps de faire une annonce.

**Lorsque l'annonce se déclenche :**
1. 🔔 Joue la sonnerie choisie (si activée)
2. ⏱️ Attend un nombre configurable de secondes (défaut : 1,2 s) — augmentez cette valeur pour les appareils Google Home / Nest si l'annonce vocale ne se joue pas correctement
3. 🗣️ L'appareil prononce l'heure dans la langue de Home Assistant (si activée)

Tout se passe automatiquement sans avoir besoin de configurer des automatisations !

## 🗣️ Gestion de la langue

La langue est automatiquement détectée depuis :

self.hass.config.language

Exemples d'annonces :

| Langue | Heure | Annonce |
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

## 🔔 Sonnerie (son initial)

Si l'option use_chime est active :
- le son de notification ou le son choisi est joué
- le système attend un nombre configurable de secondes (défaut : 1,2)
- l'annonce vocale commence (si activée)

Cela crée un effet similaire à un vrai pendule 🎶.

## 🧩 Options de configuration

| Option | Description |
|------|------------|
| player_type | Type d'appareil lecteur (Alexa, Google Home, Générique) |
| player | Appareil cible |
| start_hour | Heure de début de fonctionnement |
| end_hour | Heure de fin de fonctionnement |
| enabled | Active/désactive le pendule |
| announce_half_hours | Active les annonces toutes les demi-heures (sinon toutes les heures uniquement) |
| after_chime_delay | Temps d'attente en secondes entre la sonnerie et l'annonce vocale (défaut : 1,2) |
| announce_half_hours_voice | Active/désactive l'annonce vocale à la demi-heure (la sonnerie joue toujours) |
| voice_announcement | Active/désactive l'annonce vocale de l'heure |
| tower_clock | Active la mélodie de Westminster à 12:00 |
| use_chime | Active/désactive la sonnerie avant l'annonce |
| preset_chime | Choix du son de sonnerie (12 préréglages disponibles) |
| custom_chime_path | Chemin pour le son de sonnerie personnalisé |

Valeurs par défaut :

- ⏰ start_hour → 8
- ⏰ end_hour → 22
- 🔔 use_chime → True
- 🗣️ voice_announcement → True
- ⏰ announce_half_hours → True
- 🏰 tower_clock → False
- ✅ enabled → True
- ⏱️ after_chime_delay → 1,2
- 🔇 announce_half_hours_voice → True

## 🧪 Test immédiat

Une méthode de test manuel est disponible :

Qui :
- lit l'heure actuelle
- génère une phrase complète (ex. "Il est 15 heures et 42 minutes")
- la joue immédiatement sur l'appareil sélectionné

Utile pour vérifier : la langue, le volume, la sonnerie, le bon fonctionnement du TTS

## 🔍 Capteur d'état

Digital Pendulum inclut un capteur de diagnostic :

`binary_sensor.digital_pendulum_status_warning`

**États :**
- ✅ **OFF** - Tout fonctionne correctement
- ⚠️ **ON** - Problèmes détectés (intégration désactivée, Alexa hors ligne, etc.)

**Utilisations :**
- Surveillance du tableau de bord
- Automatisations de notifications
- Diagnostic rapide

## 📦 Prérequis

> ✨ **Disponible sur HACS** - installation et mises à jour simplifiées !

- 🏠 Home Assistant 2024.1.0 ou supérieur
- 🔊 Un appareil media_player compatible (voir [Appareils compatibles](#-appareils-compatibles))
- 📡 Pour Alexa : [alexa_media_player](https://github.com/custom-components/alexa_media_player) installé via HACS
- 📡 Pour Google Home / Nest : intégration Google Cast (native dans HA)

## 💾 Installation

### Via HACS (recommandé)

1. Ouvrez **HACS** dans le menu latéral
2. Allez dans **Intégrations**
3. Recherchez **"Digital Pendulum"**
4. Cliquez sur **Télécharger**
5. **Redémarrez Home Assistant**
6. Allez dans **Paramètres** → **Appareils et services** → **Ajouter une intégration**
7. Recherchez **"Digital Pendulum"**
8. Suivez la configuration guidée

### Installation manuelle

1. Téléchargez la dernière version depuis [GitHub](https://github.com/Dregi56/digital_pendulum/releases)
2. Extrayez les fichiers
3. Copiez le dossier `digital_pendulum` dans `config/custom_components/`
4. Redémarrez Home Assistant
5. Allez dans **Paramètres** → **Appareils et services** → **Ajouter une intégration**
6. Recherchez **"Digital Pendulum"**
7. Suivez la configuration guidée

## 🎯 Utilisation idéale

- ✔️ Maisons intelligentes
- ✔️ Bureaux
- ✔️ Espaces communs
- ✔️ Effet "pendule moderne"
- ✔️ Rappel d'heure non invasif

## 🔧 Dépannage

### Problèmes avec Alexa ou erreur "Cannot find EU skill"

Problème avec **alexa_media_player**, pas avec Digital Pendulum.

**Solution rapide :**
1. Paramètres → Appareils et services → Alexa Media Player
2. Trois points → Recharger
3. Si ça ne fonctionne pas : désinstallez et réinstallez Alexa Media Player

---

### Google Home / Nest : pas d'annonce vocale

Digital Pendulum utilise le moteur TTS configuré dans HA pour les appareils Google.

Il s'agit d'un problème de synchronisation connu avec les appareils Google. L'annonce vocale peut être coupée ou ignorée si le délai après la sonnerie est trop court.

1. Vérifiez qu'un moteur TTS est configuré dans HA (Paramètres → Assistants vocaux)
2. Vérifiez le journal HA pour les erreurs TTS
3. Augmentez la valeur **"Délai après la sonnerie"** (essayez 2,0 ou 3,0 secondes)
4. Utilisez le bouton "Test" pour vérifier

---

### Mauvaise langue

Digital Pendulum utilise automatiquement la langue de Home Assistant.

1. Vérifiez : Paramètres → Système → Général → Langue
2. Langues prises en charge : 🇮🇹 🇬🇧 🇫🇷 🇩🇪 🇪🇸 🇵🇱 🇨🇿 🇸🇰 🇵🇹
3. Après avoir changé la langue, redémarrez Home Assistant

---

### Pas d'annonces

**Vérifiez :**
- Intégration activée ? (Interrupteur ON)
- Êtes-vous dans le créneau horaire configuré ? (défaut 8h00-22h00)
- Appareil en ligne ?
- Type de lecteur correct sélectionné ? (Alexa, Google, Générique)
- Essayez le bouton "Test"

---

### Sonnerie uniquement ou voix uniquement

- **Sonnerie uniquement :** Activez "Annonce vocale"
- **Voix uniquement :** Activez "Utiliser la sonnerie"

---

### Westminster ne joue pas à 12h

- Vérifiez que "Horloge de tour" est active
- Fonctionne **uniquement à 12:00** (midi, pas minuit)

---

## 🚀 Développements futurs possibles

- ⏳ Annonces toutes les 15 minutes
- 🔇 Volume nocturne automatique

---

## ☕ Soutenez le projet

Vous aimez ce projet ? Si vous le trouvez utile, offrez-moi un café virtuel pour soutenir les développements futurs ! Chaque petite contribution est très appréciée. 🙏

**Digital Pendulum est et restera toujours gratuit et open source.** Les dons sont entièrement volontaires ! ❤️

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/dregi56)

💡 **Vous préférez d'autres méthodes ?** Vous pouvez utiliser :

[![revolut](https://img.shields.io/badge/Revolut-0075EB?style=for-the-badge&logo=revolut&logoColor=white)](https://revolut.me/egidio5t9d)
