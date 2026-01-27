# 🕰️ Digital Pendulum

Un pendule numérique parlant pour Home Assistant  
<br>**Auteur :** Egidio Ziggiotto (Dregi56)  e-mail : [dregi@cyberservices.com](mailto:dregi@cyberservices.com)


[![HACS](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://hacs.xyz/)
[![Version](https://img.shields.io/github/v/release/Dregi56/digital_pendulum)](https://github.com/Dregi56/digital_pendulum/releases)
![License](https://img.shields.io/github/license/Dregi56/digital_pendulum)
[![GitHub stars](https://img.shields.io/github/stars/Dregi56/digital_pendulum?style=social)](https://github.com/Dregi56/digital_pendulum)

🌍 Langues disponibles :
[Italiano](README.it.md) |
[English](README.en.md) |
[Español](README.es.md) |
[Deutsch](README.de.md) |
[Français](README.fr.md) 
<br>👉Ceci est le README en français. Utilisez le sélecteur de langue ci-dessus

> ⚠️ **Digital Pendulum est une intégration via HACS uniquement**
<br> Nécessite l'intégration **Alexa Media Player** installée et opérationnelle.

## ❤️ Vous aimez Digital Pendulum ?

S’il vous est utile, pensez à laisser une ⭐ sur GitHub :  
👉 **https://github.com/Dregi56/digital_pendulum**
<br>Merci.

## 📌 Description

Digital Pendulum est une intégration personnalisée pour Home Assistant qui annonce vocalement l’heure, comme un pendule numérique 🕰️.


En utilisant un appareil Alexa comme haut-parleur, le système :

- 📢 annonce l’heure toutes les 30 minutes  
- 🌍 parle automatiquement dans la langue définie dans Home Assistant  
- ⏰ fonctionne uniquement dans une plage horaire configurable 
- 🔔 peut lire un son personnalisé (par défaut le son Alexa « announce » (carillon)) avant l’annonce
- 🏰 peut jouer la mélodie de Westminster à 12 heures  

Le résultat est un effet élégant et discret, idéal pour la maison ou le bureau.

## ✨ Fonctionnalités principales

### 🕑 Annonce automatique de l’heure
- chaque heure pile (xx:00)
- chaque demi-heure (xx:30)

### 🌐 Support multilingue automatique
- Italien 🇮🇹
- Anglais 🇬🇧
- Français 🇫🇷
- Allemand 🇩🇪 (avec gestion correcte de « halb »)
- Espagnol 🇪🇸

repli automatique vers l’italien

### ⏱️ Plage horaire configurable
- ex. uniquement de 8:00 à 22:00

### 🔔 Carillon optionnel
- 🔕 brève annonce silencieuse avant le TTS
- 🎵 sons personnalisés. Si un chemin est défini, son local

### 🧪 Fonction de test
- pour tester immédiatement l’annonce

### 🎯 Comportement
- Preset : "church-bell" : son par défaut
- Preset : "simple-bell" : cloche choisie dans la bibliothèque
- Preset : "custom" + chemin vide : son Alexa « announce »
- Preset : "custom" + chemin valide : joue un fichier sélectionné
- Preset : "tower-clock" : mélodie de Westminster à 12 heures
- Use Chime : OFF : aucun son, uniquement le TTS (annonce de l’heure)

## ⚙️ Fonctionnement

Le cœur du système est la classe :

class DigitalPendulum

qui :
- s’enregistre sur un minuteur interne (toutes les 1 minute)
- vérifie :
  - si l’intégration est activée
  - si l’heure est dans la plage autorisée
  - si la minute est 00 ou 30
- construit le texte parlé selon la langue
- envoie l’annonce à l’appareil Alexa configuré

## 🗣️ Gestion des langues

La langue est détectée automatiquement à partir de :

self.hass.config.language

Exemples d’annonces :

| Langue | Heure | Annonce |
|------|------|--------|
| 🇮🇹 IT | 10:30 | Ore 10 e trenta |
| 🇬🇧 EN | 14:00 | It's 14 o'clock |
| 🇫🇷 FR | 9:30 | Il est 9 heures trente |
| 🇩🇪 DE | 16:30 | Es ist halb 17 |
| 🇪🇸 ES | 11:00 | Son las 11 |

## 🔔 Chime (carillon initial)

Si l’option use_chime est activée :
- une annonce vide est envoyée
- le système attend 1,3 seconde
- le TTS avec l’heure démarre  

Cela crée un effet similaire à un vrai pendule 🎶.

## 🧩 Options de configuration

| Option | Description |
|------|------------|
| player | Appareil Alexa cible |
| start_hour | Heure de début |
| end_hour | Heure de fin |
| enabled | Activer/désactiver le pendule |
| tower-clock | Activer/désactiver la mélodie de 12 heures |
| use_chime | Activer/désactiver le carillon |

Valeurs par défaut :

- ⏰ start_hour → DEFAULT_START_HOUR  
- ⏰ end_hour → DEFAULT_END_HOUR  
- 🔔 use_chime → DEFAULT_USE_CHIME  
- ✅ enabled → DEFAULT_ENABLED  

## 🧪 Test immédiat

Une méthode de test manuel est disponible :

async_test_announcement()

Qui :
- lit l’heure actuelle
- génère une phrase complète (ex. « Il est 15:42 »)
- la joue immédiatement sur l’appareil Alexa  

Utile pour vérifier : langue, volume, carillon, bon fonctionnement du TTS

## 📦 Prérequis

- 🏠 Home Assistant
- 🔊 Alexa Media Player installé et fonctionnel
- 📡 Appareil Alexa configuré comme lecteur

## 🎯 Utilisation idéale

- ✔️ Maisons intelligentes
- ✔️ Bureaux
- ✔️ Espaces communs
- ✔️ Effet « pendule moderne »
- ✔️ Rappel du temps non intrusif

## 🚀 Évolutions futures possibles

- ⏳ Annonces toutes les 15 minutes
- 🔇 Volume nocturne automatique
- 🗓️ Annonce du jour
- 📣 Support d’autres systèmes TTS

---

## 

## ☕ Soutenir le projet

Vous aimez ce projet ? S’il vous est utile, offrez-moi un café virtuel pour soutenir les évolutions futures ! Chaque petite contribution est grandement appréciée. 🙏

**Digital Pendulum est et restera toujours gratuit et open source.** Les dons sont entièrement volontaires ! ❤️


[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/dregi56)

💡 **Vous préférez d’autres méthodes ?** Vous pouvez utiliser :

[![revolut](https://img.shields.io/badge/Revolut-0075EB?style=for-the-badge&logo=revolut&logoColor=white)](https://revolut.me/egidio5t9d)
