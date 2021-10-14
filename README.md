## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `export DJANGO_SK="isihdihfihio"` La valeur de clé secrète doit être changée en production.
- `export DEBUG_DJANGO="True"`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`S

### Lancement de l'image depuis Docker

### Prérequis

- Installation de Docker

### Lancement de l'image depuis Docker

- Lancer Docker
- Exécuter la commande `docker run -p 8000:8000 -e DJANGO_SK="isihdihfihio" -e DEBUG_DJANGO="True" fortranvba/dap13:latest`. La valeur de clé secrète (DJANGO_SK) doit être changée en production.
- Le site est accessible à (l'adresse IP de la machine Docker):8000 ; Par exemple : http://192.168.99.100:8000/

## Déploiement du site

### Résumé

Le déploiement du site se fait par l'intermédiaire d'un pipeline CircleCI, défini dans le fichier config.yml du dossier .circleci.
- Lors d'un push de nouveau code sur le compte GitHub, CircleCI va créer une image Docker (construite à partir du fichier Dockerfile) et exécuter une série de test (linter et tests de l'application Django).
- Dans le cas où il s'agit de la branche principale du GitHub (branche main), l'image Docker est envoyée sur DockerHub.
- Toujours dans le cas où il s'agit de la branche principale du GitHub (branche main), l'image de DockerHub est envoyée vers Heroku pour y être exécuté, déployant ainsi le site.

### Prérequis

- Compte CircleCI
- Compte DockerHub

### Etapes pour lancer le déploiement

- Se connecter à son compte CircleCI en s'identifiant avec son compte GitHub.
- Dans l'onglet projet, ajouter le projet actuel (bouton Set Up Project), choisir l'option "If you already have .circleci/config.yml in your repo..." en mentionnant la branche `main`.
- Dans project settings, ajouter les variables d'environnement suivantes (à noter que celles-ci seront utilisées pour les tests et non pour le déploiement vers Heroku)
  - Name: DJANGO_SK Value: "kjgtdtetg564"
  - Name: DEBUG_DJANGO Value: "True"
Ainsi que les différents identifiants / mots de passe :
  - DOCKERHUB_USERNAME: Nom utilisateur DockerHub
  - DOCKERHUB_PASSWORD: Mot de passe utilisateur DockerHub
  - HEROKU_API_KEY: Clé API utilisateur Heroku (à récupérer dans Account Settings de Heroku)
  - HEROKU_APP_NAME: Nom utilisateur DockerHub
- Se connecter à son compte Heroku.
- Créer une application (son nom doit être le même que la variable précédente HEROKU_APP_NAME)
- Dans Settings de l'application, ajouter dans Config Vars les variables suivantes :
  - Name: DJANGO_SK Value: (Mettre la clé secrète Django à utiliser en production)
  - Name: DEBUG_DJANGO Value: "False"
- Le pipeline est maintenant en place.
