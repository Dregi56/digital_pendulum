# 🕰️ Digital Pendulum

Un pendule numérique parlant pour Home Assistant
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
 
<br>👉Ceci est le README en Français. Utilisez le sélecteur de langue ci-dessus

## ❤️ Vous aimez Digital Pendulum?

Si vous le trouvez utile, pensez à laisser une ⭐ sur GitHub:  
👉 **https://github.com/Dregi56/digital_pendulum**
<br>Merci.

## 📌 Description

Digital Pendulum est une intégration personnalisée pour Home Assistant qui annonce vocalement l'heure, tout comme une pendule numérique 🕰️.


En utilisant un appareil Alexa comme haut-parleur, le système:

- 📢 annonce l'heure toutes les heures et/ou toutes les demi-heures (configurable)
- 🌍 parle automatiquement dans la langue configurée dans Home Assistant  
- ⏰ fonctionne uniquement dans une plage horaire configurable 
- 🔔 peut reproduire un son personnalisé avant l'annonce
- 🔕 peut désactiver l'annonce vocale (sonnerie uniquement)
- 🏰 peut reproduire la mélodie Westminster à 12 heures

Le résultat est un effet élégant et discret, idéal pour la maison ou le bureau.

## ✨ Fonctionnalités principales

### 🕑 Annonce automatique de l'heure
- toutes les heures (xx:00)
- toutes les demi-heures (xx:30) - optionnel

### 🌐 Support multilingue automatique
- Italien 🇮🇹
- Anglais 🇬🇧
- Français 🇫🇷
- Allemand 🇩🇪 (avec gestion correcte de "halb")
- Espagnol 🇪🇸
- Polski 🇵🇱

fallback automatique en italien

### ⏱️ Plage horaire configurable
- ex. uniquement de 8h00 à 22h00

###  🔔 Sonnerie optionnelle
- 🎵 12 sons prédéfinis au choix
- 🎶 possibilité d'utiliser un fichier audio personnalisé
- 🔕 son de notification "announce" d'Alexa (par défaut)

### 🧪 Fonction de test
- pour essayer l'annonce immédiatement

### 🎯 Comportement

**Sonnerie (Chime):**
- **Presets disponibles**: 12 sons dont church-bell, simple-bell, clock-chime, etc.
- **Son personnalisé**: Sélectionnez "custom" et entrez le chemin de votre fichier audio
- **Par défaut**: Son "announce" d'Alexa (si vous ne sélectionnez rien)
- **Désactivé**: Désactivez "use_chime" pour aucun son avant l'annonce

**Mélodie Westminster (Tower Clock):**
- Option séparée "tower_clock"
- Sonne **uniquement à 12h00** (midi)
- Remplace le chime normal à cette heure

**Annonce vocale:**
- **Activée** (par défaut): Alexa prononce l'heure après la sonnerie
- **Désactivée**: Son de sonnerie uniquement, aucune annonce vocale

**Annonces demi-heure:**
- **Activées** (par défaut): Annonces à :00 et :30
- **Désactivées**: Annonces à :00 uniquement

## ⚙️ Comment ça fonctionne

Digital Pendulum se synchronise avec l'horloge système et vérifie automatiquement chaque minute s'il est temps de faire une annonce.

**Quand l'annonce se déclenche:**
1. 🔔 Reproduit la sonnerie choisie (si activée)
2. ⏱️ Attend 1,2 secondes
3. 🗣️ Alexa prononce l'heure dans la langue de Home Assistant (si activée)

Tout se passe automatiquement sans avoir besoin de configurer des automatisations!

## 🗣️ Gestion des langues

La langue est détectée automatiquement depuis:

self.hass.config.language

Exemples d'annonces:

| Langue | Heure | Annonce |
|------|------|--------|
| 🇮🇹 IT | 10:30 | Ore 10 e trenta |
| 🇬🇧 EN | 14:00 | It's 14 o'clock |
| 🇫🇷 FR | 9:30 | Il est 9 heures trente |
| 🇩🇪 DE | 16:30 | Es ist halb 17 |
| 🇪🇸 ES | 11:00 | Son las 11 |
| 🇵🇱 PL | 15:30 | Wpół do czwartej |
| 🇨🇿 CS | 8:30 | Půl deváté |
| 🇸🇰 SK | 8:30 | Pol deviatej |

## 🔔 Chime (sonnerie initiale)

Si l'option use_chime est active:
- le son de notification d'Alexa ou le son choisi est reproduit
- le système attend 1,2 secondes
- l'annonce vocale démarre (si activée)

Cela crée un effet similaire à une vraie pendule 🎶.

## 🧩 Options de configuration

| Option | Description |
|------|------------|
| player | Appareil Alexa cible |
| start_hour | Heure de début de fonctionnement |
| end_hour | Heure de fin de fonctionnement |
| enabled | Active/désactive la pendule |
| announce_half_hours | Active les annonces toutes les demi-heures (sinon toutes les heures uniquement) |
| voice_announcement | Active/désactive l'annonce vocale de l'heure |
| tower_clock | Active la mélodie Westminster à 12h00 |
| use_chime | Active/désactive la sonnerie avant l'annonce |
| preset_chime | Choix du son de sonnerie (12 presets disponibles) |
| custom_chime_path | Chemin pour son de sonnerie personnalisé |

Valeurs par défaut:

- ⏰ start_hour → 8
- ⏰ end_hour → 22
- 🔔 use_chime → True
- 🗣️ voice_announcement → True
- ⏰ announce_half_hours → True
- 🏰 tower_clock → False
- ✅ enabled → True

## 🧪 Test immédiat

Une méthode de test manuelle est disponible:

Qui:
- lit l'heure actuelle
- génère une phrase complète (ex. "Il est 15 heures 42")
- la reproduit immédiatement sur l'appareil Alexa  

Utile pour vérifier: langue, volume, chime, bon fonctionnement du TTS

## 🔍 Capteur d'état

Digital Pendulum inclut un capteur de diagnostic :

`binary_sensor.digital_pendulum_status_warning`

**États :**
- ✅ **OFF** - Tout fonctionne correctement
- ⚠️ **ON** - Problèmes détectés (intégration désactivée, Alexa hors ligne, etc.)

**Utilisations :**
- Surveillance du tableau de bord
- Automatisations pour notifications
- Diagnostic rapide

## 📦 Prérequis

> ✨ **Disponible sur HACS** - installation et mises à jour simplifiées!

- 🏠 Home Assistant 2024.1.0 ou supérieur
- 🔊 Alexa Media Player installé et fonctionnel
- 📡 Appareil Alexa configuré comme player

## 💾 Installation

### Via HACS (recommandé)

1. Ouvrez **HACS** dans le menu latéral
2. Allez dans **Intégrations**
3. Recherchez **"Digital Pendulum"**
4. Cliquez sur **Télécharger**
5. **Redémarrez Home Assistant**
6. Allez dans **Paramètres** → **Appareils et Services** → **Ajouter une Intégration**
7. Recherchez **"Digital Pendulum"**
8. Suivez la configuration guidée

### Installation manuelle

1. Téléchargez la dernière version depuis [GitHub](https://github.com/Dregi56/digital_pendulum/releases)
2. Extrayez les fichiers
3. Copiez le dossier `digital_pendulum` dans `config/custom_components/`
4. Redémarrez Home Assistant
5. Allez dans **Paramètres** → **Appareils et Services** → **Ajouter une Intégration**
6. Recherchez **"Digital Pendulum"**
7. Suivez la configuration guidée


## 🎯 Utilisation idéale

- ✔️ Maisons intelligentes
- ✔️ Bureaux
- ✔️ Espaces communs
- ✔️ Effet "pendule moderne"
- ✔️ Rappel temporel non invasif

## 🔧 Résolution des problèmes

### Erreur "Cannot find EU skill" ou problèmes Alexa

Problème d'**Alexa Media Player**, pas de Digital Pendulum.

**Solution rapide:**
1. Paramètres → Appareils et services → Alexa Media Player
2. Trois points → Recharger
3. Si ça ne fonctionne pas: désinstallez et réinstallez Alexa Media Player

---

### Mauvaise langue

Digital Pendulum utilise automatiquement la langue de Home Assistant.

1. Vérifiez: Paramètres → Système → Général → Langue
2. Langues supportées: 🇮🇹 🇬🇧 🇫🇷 🇩🇪 🇪🇸
3. Après avoir changé la langue, redémarrez Home Assistant

---

### Aucune annonce

**Vérifiez:**
- Intégration activée? (Interrupteur ON)
- Êtes-vous dans la plage horaire configurée? (par défaut 8h00-22h00)
- Appareil Alexa en ligne?
- Essayez le bouton "Test"

---

### Sonnerie uniquement ou voix uniquement

- **Sonnerie uniquement:** Activez "Voice announcement"
- **Voix uniquement:** Activez "Use chime"

---

### Westminster ne sonne pas à 12h

- Vérifiez que "Tower Clock" est actif
- Fonctionne **uniquement à 12h00** (midi, pas minuit)

---

## 🚀 Évolutions futures possibles

- ⏳ Annonces toutes les 15 minutes
- 🔇 Volume automatique nocturne
- 🗓️ Annonce du jour
- 📣 Support d'autres TTS

---

## 

## ☕ Soutenez le projet

Vous aimez ce projet? Si vous le trouvez utile, offrez-moi un café virtuel pour soutenir les développements futurs! Chaque petite contribution est très appréciée. 🙏

**Digital Pendulum est et restera toujours gratuit et open source.** Les dons sont entièrement volontaires! ❤️


[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/dregi56)

💡 **Vous préférez d'autres méthodes?** Vous pouvez utiliser:

[![revolut](https://img.shields.io/badge/Revolut-0075EB?style=for-the-badge&logo=revolut&logoColor=white)](https://revolut.me/egidio5t9d)
