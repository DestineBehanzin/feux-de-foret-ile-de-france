# Stack Docker du pipeline de données

Ce dépôt met en place l'infrastructure technique du pipeline.

La stack contient :

- PostgreSQL 17 pour le stockage des données et des métadonnées ;
- Dagster Webserver pour superviser le pipeline ;
- Dagster Daemon pour les planifications et traitements en arrière-plan ;
- dbt Core pour les futures transformations SQL ;
- Python 3.13 comme environnement d'exécution de Dagster et dbt ;
- Docker Compose pour construire, connecter et démarrer les services.

## Architecture

```text
                         Docker Compose
                               |
               +---------------+---------------+
               |               |               |
               v               v               v
          PostgreSQL      Dagster Web      Dagster Daemon
          port interne       port 3000       planifications
             5432
               ^
               |
               +---------------+
                               |
                              dbt
                      exécution ponctuelle
```


## 1. Prérequis

### Logiciels

Installer les composants suivants :

- Git ;
- Docker Desktop avec le moteur Linux/WSL2 ;
- Python 3.13 ;
- PowerShell 7 ou Windows PowerShell.

### Vérifier Docker

Ouvrir Docker Desktop et attendre que le moteur soit démarré.

```powershell
docker --version
docker compose version
docker info
```

La commande `docker info` doit afficher une section `Server`.

### Vérifier Python 3.13

```powershell
py -0p
py -3.13 --version
```

Résultat attendu :

```text
Python 3.13.x
```

Si Python 3.13 n'est pas installé :

```powershell
winget install --id Python.Python.3.13 -e
```

Fermer et rouvrir PowerShell après l'installation.

---

## 2. Récupérer le projet

```powershell
git clone URL_DU_DEPOT
Set-Location NOM_DU_DEPOT
```

Vérifier le contenu :

```powershell
Get-ChildItem
```

Fichiers attendus :

```text
pipeline_stack/
├── .dockerignore
├── .env.example
├── .gitignore
├── Dockerfile
├── README.md
├── docker-compose.yml
├── requirements.txt
├── workspace.yaml
├── dagster_home/
│   └── dagster.yaml
├── dbt/
│   ├── dbt_project.yml
│   └── profiles.yml
└── src/
    └── pipeline/
        ├── __init__.py
        └── definitions.py
```

---

## 3. Créer l'environnement virtuel Python 3.13

L'environnement virtuel est utile pour les tests locaux. Docker possède son propre environnement Python indépendant.

### Supprimer un ancien environnement

```powershell
if (Test-Path ".\.venv") {
    Remove-Item ".\.venv" -Recurse -Force
}
```

### Créer le nouvel environnement

```powershell
py -3.13 -m venv .venv
```

Vérifier sa version avant activation :

```powershell
.\.venv\Scripts\python.exe --version
```

### Activer l'environnement

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Le terminal doit commencer par `(.venv)`.

```powershell
python --version
Get-Command python
```

Le chemin doit pointer vers :

```text
pipeline_stack\.venv\Scripts\python.exe
```

---

## 4. Installer les dépendances Python locales

```powershell
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
python -m pip check
```

Résultat attendu pour la dernière commande :

```text
No broken requirements found.
```

Tester les outils principaux :

```powershell
python -c "import dagster, requests, sqlalchemy, psycopg; print('Imports Python OK')"
dagster --version
dbt --version
pytest --version
```

---

## 5. Configurer les variables d'environnement

Le fichier `docker-compose.yml` utilise des variables et ne contient pas les valeurs locales directement.

Créer `.env` à partir de l'exemple :

```powershell
Copy-Item ".\.env.example" ".\.env" -Force
notepad .\.env
```

Configuration minimale :

```env
# Docker Compose
COMPOSE_PROJECT_NAME=pipeline-stack
RESTART_POLICY=unless-stopped
PIPELINE_DOCKERFILE=Dockerfile

# PostgreSQL
POSTGRES_IMAGE=postgres:17-alpine
POSTGRES_CONTAINER_NAME=pipeline_postgres
POSTGRES_DB=warehouse
POSTGRES_USER=pipeline
POSTGRES_PASSWORD=change_me
POSTGRES_HOST=postgres
POSTGRES_HOST_PORT=5433
POSTGRES_CONTAINER_PORT=5432
POSTGRES_VOLUME_NAME=pipeline_postgres_data
POSTGRES_HEALTHCHECK_INTERVAL=5s
POSTGRES_HEALTHCHECK_TIMEOUT=5s
POSTGRES_HEALTHCHECK_RETRIES=12
DATABASE_URL=postgresql+psycopg://pipeline:change_me@postgres:5432/warehouse

# Dagster
DAGSTER_WEBSERVER_CONTAINER_NAME=pipeline_dagster_webserver
DAGSTER_DAEMON_CONTAINER_NAME=pipeline_dagster_daemon
DAGSTER_HOME=/opt/dagster/dagster_home
DAGSTER_HOST=0.0.0.0
DAGSTER_HOST_PORT=3000
DAGSTER_PORT=3000
DAGSTER_WORKSPACE_PATH=/app/workspace.yaml
DAGSTER_HEALTHCHECK_INTERVAL=20s
DAGSTER_HEALTHCHECK_TIMEOUT=10s
DAGSTER_HEALTHCHECK_RETRIES=10
DAGSTER_HEALTHCHECK_START_PERIOD=45s

# dbt
DBT_CONTAINER_NAME=pipeline_dbt
DBT_PROFILE=tools
DBT_WORKING_DIR=/app/dbt
DBT_PROFILES_DIR=/app/dbt

# Réseau Docker
DATA_NETWORK_NAME=pipeline_data_network
DATA_NETWORK_DRIVER=bridge
```

### Choix du port PostgreSQL

Le port interne de PostgreSQL reste `5432`.

- utiliser `POSTGRES_HOST_PORT=5432` si le port est libre sur Windows ;
- utiliser `POSTGRES_HOST_PORT=5433` si un autre PostgreSQL utilise déjà `5432`.

La valeur `DATABASE_URL` doit continuer à utiliser `postgres:5432`, car Dagster et dbt communiquent avec PostgreSQL sur le réseau Docker interne.

### Sécurité

Le fichier `.env` ne doit jamais être poussé sur GitHub.

```powershell
git check-ignore -v .env
```

Résultat attendu : `.env` est ignoré par `.gitignore`.

---

## 6. Vérifier la configuration Docker Compose

```powershell
docker compose config --quiet
```

Une sortie vide indique que la configuration est valide.

Lister les services :

```powershell
docker compose --profile tools config --services
```

Résultat attendu :

```text
postgres
dagster-webserver
dagster-daemon
dbt
```

Attention : afficher la configuration résolue peut révéler les valeurs de `.env`. Ne jamais versionner un fichier `compose-resolved.yml`.

---

## 7. Construire l'image Python 3.13

Le `Dockerfile` construit l'environnement Python utilisé dans les conteneurs Dagster et dbt.

Première construction :

```powershell
docker compose --progress plain build --no-cache dagster-webserver
```

Construire les autres services en réutilisant le cache :

```powershell
docker compose build dagster-daemon dbt
```

Vérifier Python dans le conteneur :

```powershell
docker compose run --rm dagster-webserver python --version
```

Résultat attendu :

```text
Python 3.13.x
```

Tester les dépendances dans l'image :

```powershell
docker compose run --rm dagster-webserver `
  python -c "import dagster, requests, sqlalchemy, psycopg; print('Image Dagster OK')"
```

---

## 8. Démarrer PostgreSQL

```powershell
docker compose up -d postgres
```

Vérifier le service :

```powershell
docker compose ps postgres
```

Le statut doit devenir `healthy`.

Tester PostgreSQL depuis son conteneur :

```powershell
docker compose exec postgres `
  pg_isready -U pipeline -d warehouse
```

Résultat attendu :

```text
accepting connections
```

### Connexion depuis Windows

Avec `POSTGRES_HOST_PORT=5433` :

```text
Hôte : localhost
Port : 5433
Base : warehouse
Utilisateur : pipeline
```

Depuis les autres conteneurs :

```text
Hôte : postgres
Port : 5432
```

---

## 9. Démarrer Dagster

```powershell
docker compose up -d dagster-webserver dagster-daemon
```

Vérifier l'état :

```powershell
docker compose ps
```

Consulter les logs :

```powershell
docker compose logs --tail 150 dagster-webserver dagster-daemon
```

Ouvrir l'interface :

```text
http://localhost:3000
```

La définition Dagster de cette branche est volontairement vide :

```python
from dagster import Definitions


defs = Definitions(assets=[])
```

Le stack peut ainsi démarrer sans inclure d'ingestion CSV, API ou WFS.

---

## 10. Tester dbt

dbt appartient au profil Compose `tools` et ne reste pas actif en permanence.

Afficher sa version :

```powershell
docker compose --profile tools run --rm dbt --version
```

Tester la configuration PostgreSQL :

```powershell
docker compose --profile tools run --rm `
  dbt debug --profiles-dir /app/dbt
```

Les transformations seront exécutées plus tard avec :

```powershell
docker compose --profile tools run --rm `
  dbt build --profiles-dir /app/dbt
```

Cette commande n'est utile que lorsque des modèles dbt existent.

---

## 11. Démarrer le stack complet

Une fois les tests unitaires réussis :

```powershell
docker compose up -d postgres dagster-webserver dagster-daemon
```

Ou simplement :

```powershell
docker compose up -d
```

Le service dbt n'est pas démarré par défaut à cause du profil `tools`.

Vérifier :

```powershell
docker compose ps
```

---

## 12. Arrêter le stack

Arrêter et supprimer les conteneurs tout en conservant les données PostgreSQL :

```powershell
docker compose down
```

Arrêter les services sans supprimer les conteneurs :

```powershell
docker compose stop
```

Redémarrer :

```powershell
docker compose start
```

### Attention aux volumes

La commande suivante supprime aussi le volume PostgreSQL :

```powershell
docker compose down -v
```

Ne pas l'utiliser si la base contient des données à conserver.

---

## 13. Modifier `.env`

Après une modification de port, de nom de conteneur ou d'identifiant PostgreSQL :

```powershell
docker compose up -d --force-recreate `
  postgres dagster-webserver dagster-daemon
```

Un simple `restart` ne réinjecte pas toujours les nouvelles variables dans les conteneurs existants.

Si `requirements.txt` ou le `Dockerfile` change, reconstruire :

```powershell
docker compose up -d --build
```


```powershell
# Créer et activer Python 3.13
py -3.13 -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1

# Installer les dépendances locales
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt

# Créer la configuration locale
Copy-Item .\.env.example .\.env -Force

# Valider et construire
Docker compose config --quiet
docker compose build dagster-webserver dagster-daemon dbt

# Démarrer
Docker compose up -d postgres dagster-webserver dagster-daemon

# Vérifier
Docker compose ps
docker compose exec postgres pg_isready -U pipeline -d warehouse

# Tester dbt
docker compose --profile tools run --rm dbt --version
```

> Sous PowerShell, les commandes Docker ne sont pas sensibles à la casse, mais la forme recommandée reste `docker compose` en minuscules.


