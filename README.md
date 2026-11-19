# Pipeline de données sur les incendies de forêt

## Branche `feature/ingestion-csv`

Cette branche étend le stack Docker initial avec une première chaîne d’ingestion CSV opérationnelle pour les données BDIFF sur les incendies de forêt.

Le pipeline permet désormais de :

- charger la configuration d’une source CSV depuis `config/sources.yml` ;
- lire un fichier CSV volumineux ligne par ligne ;
- gérer plusieurs encodages et un séparateur configurable ;
- ignorer les lignes de métadonnées précédant l’en-tête ;
- appliquer des contrôles de qualité propres aux données BDIFF ;
- insérer les lignes valides dans PostgreSQL ;
- conserver les lignes rejetées avec leur motif ;
- journaliser chaque chargement ;
- éviter la réinsertion des mêmes lignes ;
- orchestrer et superviser l’exécution dans Dagster ;
- archiver une copie du fichier traité.

## Résultat du premier test

Le fichier `Incendies.csv` a été matérialisé avec succès dans Dagster :

| Indicateur | Résultat |
|---|---:|
| Fichiers traités | 1 |
| Lignes lues | 2 541 |
| Lignes insérées | 2 540 |
| Lignes rejetées | 1 |
| Taux de validation | 99,96 % |

La ligne rejetée correspond à une commune absente à la position 5. Elle est conservée dans `audit.rejected_records` avec son numéro de ligne, son contenu brut et le motif du rejet.

---

## Architecture

```text
Incendies.csv
      |
      v
config/sources.yml
      |
      v
Dagster - ingest_csv_sources
      |
      +--------------------------+
      |                          |
      v                          v
Validation BDIFF          Journal d'audit
      |                    audit.load_log
      |
      +---------------+
      |               |
      v               v
Lignes valides     Lignes invalides
raw.csv_records    audit.rejected_records
      |
      v
Future couche dbt
staging -> marts
      |
      v
Power BI
```

## Composants du stack

| Composant | Version ou rôle |
|---|---|
| PostgreSQL | 17 Alpine, données brutes et audit |
| Dagster Webserver | Supervision et matérialisation des assets |
| Dagster Daemon | Exécutions et automatisations en arrière-plan |
| Python | 3.13 |
| dbt Core | Future transformation `raw -> staging -> marts` |
| Docker Compose | Construction et connexion des services |

---

## Arborescence principale

```text
.
├── .env.example
├── .gitignore
├── Dockerfile
├── README.md
├── docker-compose.yml
├── requirements.txt
├── workspace.yaml
├── config/
│   └── sources.yml
├── dagster_home/
│   └── dagster.yaml
├── data/
│   ├── incoming/
│   │   └── .gitkeep
│   ├── archive/
│   │   └── .gitkeep
│   └── rejected/
│       └── .gitkeep
├── dbt/
│   ├── dbt_project.yml
│   ├── profiles.yml
│   └── macros/
│       └── generate_schema_name.sql
├── sql/
│   └── init/
│       ├── 010_raw_csv_records.sql
│       ├── 020_audit_load_log.sql
│       └── 030_audit_rejected_records.sql
└── src/
    └── pipeline/
        ├── definitions.py
        ├── assets/
        │   └── csv_assets.py
        ├── config/
        │   └── source_loader.py
        ├── connectors/
        │   └── csv_connector.py
        ├── repositories/
        │   └── csv_repository.py
        └── validators/
            └── bdiff_validator.py
```

---

## 1. Prérequis

Installer et démarrer :

- Git ;
- Docker Desktop avec le moteur Linux/WSL2 ;
- PowerShell ;
- Python 3.13 pour les tests locaux facultatifs.

Vérifier Docker :

```powershell
docker --version
docker compose version
docker info
```

Vérifier Python :

```powershell
py -3.13 --version
```

---

## 2. Récupérer le projet et la branche

```powershell
git clone URL_DU_DEPOT
Set-Location feux-de-foret-ile-de-france
git switch feature/ingestion-csv
```

Si la branche distante existe uniquement sur GitHub :

```powershell
git fetch origin
git switch --track origin/feature/ingestion-csv
```

---

## 3. Configuration locale

Créer `.env` à partir de l’exemple :

```powershell
Copy-Item .\.env.example .\.env
notepad .\.env
```

Le vrai `.env` ne doit pas être versionné :

```powershell
git check-ignore -v .env
```

Variables CSV attendues :

```env
CSV_SOURCES_CONFIG=/app/config/sources.yml
CSV_INCOMING_DIR=/app/data/incoming
CSV_ARCHIVE_DIR=/app/data/archive
CSV_REJECTED_DIR=/app/data/rejected
CSV_DEFAULT_BATCH_SIZE=1000
```

`/app` est le répertoire interne des conteneurs Docker. Les correspondances sont définies dans `docker-compose.yml` :

| Dossier Windows du projet | Chemin dans Dagster |
|---|---|
| `./config` | `/app/config` |
| `./data/incoming` | `/app/data/incoming` |
| `./data/archive` | `/app/data/archive` |
| `./data/rejected` | `/app/data/rejected` |
| `./src` | `/app/src` |

---

## 4. Configurer la source BDIFF

Le fichier `config/sources.yml` contient :

```yaml
csv_sources:
  - name: bdiff_incendies_2025
    enabled: true
    file_name: Incendies.csv
    delimiter: ";"
    encoding: "utf-8-sig"
    fallback_encodings:
      - "utf-8"
      - "cp1252"
      - "latin-1"
    header_row: 3
    skip_blank_rows: true
    batch_size: 1000
    archive_after_success: true
    domain: bdiff
    expected_column_count: 24
    required_positions:
      - 1
      - 2
      - 3
      - 4
      - 5
      - 6
      - 7
```

La ligne 3 contient les en-têtes. Les lignes 1 et 2 sont des métadonnées de l’export BDIFF.

Le fichier CSV doit être placé ici :

```text
data/incoming/Incendies.csv
```

Le fichier source réel ne doit pas être poussé sur Git s’il est volumineux ou s’il doit rester local.

---

## 5. Contrôles de qualité BDIFF

Le validateur contrôle notamment :

- la présence des sept champs structurants ;
- une année comprise entre 1900 et 2100 ;
- le format du département ;
- le format du code INSEE ;
- la date de première alerte ;
- les surfaces numériques et positives ou nulles ;
- la nature de l’incendie ;
- les compteurs de décès et de bâtiments détruits ;
- la présence de 24 colonnes.

Les formats de date acceptés incluent notamment :

```text
2025-01-01 01:08:00
2025-01-01 01:08
01/01/2025 01:08:00
01/01/2025 01:08
```

Une ligne invalide n’interrompt pas le traitement complet. Elle est enregistrée dans `audit.rejected_records`.

---

## 6. Valider Docker Compose

```powershell
docker compose config --quiet
docker compose config --services
```

Services attendus :

```text
postgres
dagster-webserver
dagster-daemon
```

Le service dbt est activé séparément avec son profil Compose :

```powershell
docker compose --profile forest_fire_warehouse config --services
```

---

## 7. Construire et démarrer le stack

```powershell
docker compose build --no-cache
docker compose up -d postgres dagster-webserver dagster-daemon
docker compose ps
```

États attendus :

- PostgreSQL : `healthy` ;
- Dagster Webserver : `healthy` ;
- Dagster Daemon : `Up`.

Dagster est accessible sur :

```text
http://localhost:3000
```

PostgreSQL est accessible depuis Windows sur :

```text
localhost:5433
```

Entre conteneurs, PostgreSQL reste accessible sur :

```text
postgres:5432
```

---

## 8. Initialiser PostgreSQL

Les scripts de `sql/init` sont automatiquement exécutés uniquement lors de la création d’un volume PostgreSQL vide.

Sur un volume existant, les exécuter manuellement :

```powershell
Get-Content .\sql\init\010_raw_csv_records.sql |
    docker compose exec -T postgres `
    psql -U pipeline -d warehouse

Get-Content .\sql\init\020_audit_load_log.sql |
    docker compose exec -T postgres `
    psql -U pipeline -d warehouse

Get-Content .\sql\init\030_audit_rejected_records.sql |
    docker compose exec -T postgres `
    psql -U pipeline -d warehouse
```

Tables attendues :

```text
raw.csv_records
audit.load_log
audit.rejected_records
```

Vérification :

```powershell
docker compose exec postgres `
    psql -U pipeline -d warehouse `
    -c "SELECT table_schema, table_name FROM information_schema.tables WHERE table_schema IN ('raw','audit') ORDER BY table_schema, table_name;"
```

---

## 9. Tester les fichiers dans Dagster

Vérifier la configuration :

```powershell
docker compose exec dagster-webserver `
    sh -c "ls -la /app/config && cat /app/config/sources.yml"
```

Vérifier la source :

```powershell
docker compose exec dagster-webserver `
    python -c "from pipeline.config.source_loader import load_csv_sources; print(load_csv_sources())"
```

Vérifier le CSV :

```powershell
docker compose exec dagster-webserver `
    sh -c "ls -la /app/data/incoming"
```

Prétester la première ligne :

```powershell
docker compose exec dagster-webserver `
    python -c "from pathlib import Path; from pipeline.connectors.csv_connector import iter_csv_rows; from pipeline.validators.bdiff_validator import validate_bdiff; row=next(iter_csv_rows(Path('/app/data/incoming/Incendies.csv'),delimiter=';',encoding='utf-8-sig',fallback_encodings=['utf-8','cp1252','latin-1'],header_row=3)); print(validate_bdiff(row[1],24,[1,2,3,4,5,6,7]))"
```

Résultat attendu :

```text
[]
```

---

## 10. Lancer l’ingestion

Dans Dagster :

1. ouvrir `http://localhost:3000` ;
2. ouvrir l’asset `ingest_csv_sources` ;
3. cliquer sur **Materialize** ;
4. suivre l’exécution dans **Events**.

Métadonnées attendues pour le fichier de test :

```text
files: ["Incendies.csv"]
rows_read: 2541
rows_inserted: 2540
rows_rejected: 1
```

---

## 11. Vérifier le résultat

### Journal d’audit

```powershell
docker compose exec postgres `
    psql -U pipeline -d warehouse `
    -c "SELECT pipeline_name, source_name, source_file, status, rows_read, rows_inserted, rows_rejected, started_at, completed_at, error_message FROM audit.load_log ORDER BY started_at DESC LIMIT 3;"
```

### Lignes valides

```powershell
docker compose exec postgres `
    psql -U pipeline -d warehouse `
    -c "SELECT source_name, COUNT(*) FROM raw.csv_records GROUP BY source_name;"
```

### Lignes rejetées

```powershell
docker compose exec postgres `
    psql -U pipeline -d warehouse `
    -c "SELECT source_file, source_row_number, reason FROM audit.rejected_records ORDER BY rejected_at DESC LIMIT 10;"
```

### Archivage

```powershell
Get-ChildItem .\data\archive
```

Le pipeline copie le fichier traité dans `data/archive` après une exécution réussie.

---

## 12. Idempotence

Chaque ligne reçoit un hash SHA-256 calculé à partir de son contenu normalisé.

La contrainte suivante évite les doublons du même fichier :

```text
source_name + source_file + row_hash
```

Une seconde matérialisation du même fichier doit lire les lignes, mais ne doit pas les insérer une seconde fois.

---

## 13. Sécurité et versionnement

Ne pas pousser :

- `.env` ;
- `.venv/` ;
- les caches Python `__pycache__/` et `*.pyc` ;
- les logs Dagster ;
- les fichiers CSV réels dans `data/incoming` ;
- les copies de fichiers dans `data/archive` et `data/rejected` ;
- les cibles dbt `target/` et `dbt_packages/`.

Conserver uniquement les `.gitkeep` dans les dossiers `data`.

Vérifier avant tout commit :

```powershell
git status --short
git check-ignore -v .env
git check-ignore -v .\data\incoming\Incendies.csv
```

---

## 14. Arrêter le stack

Conserver les données PostgreSQL :

```powershell
docker compose down
```

Ne pas utiliser la commande suivante si les données doivent être conservées :

```powershell
docker compose down -v
```

---

## 15. Prochaines étapes

- créer le modèle dbt `staging.stg_bdiff_incendies` ;
- typer les 24 colonnes du CSV ;
- construire les dimensions et la table de faits dans `marts` ;
- ajouter les tests unitaires et d’intégration ;
- automatiser l’ingestion avec un sensor Dagster ;
- connecter Power BI aux tables du schéma `marts`.
