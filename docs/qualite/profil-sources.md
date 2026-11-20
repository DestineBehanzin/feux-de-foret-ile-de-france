# Profil des sources

> Projet : feux de forêt en Île-de-France (commande du SDIS 77, saison 2027)
> Produit le 20/11/2026 par `scripts/qualite/profil_sources.py`, sur les fichiers bruts téléchargés le 20/11/2026.
> Commande : `python scripts/qualite/profil_sources.py data/incoming > docs/qualite/profil-sources.md`
> Sources non profilées : **IFM Copernicus** (pas encore téléchargé) et **arrêtés préfectoraux** (table pas encore constituée).

## BDIFF (`bdiff_2025.csv`)

- Lignes : 2 541 (France) · 55 (Seine-et-Marne) · 24 colonnes
- Bornes de `Date de première alerte` : 01/01/2025 01:08 → 31/12/2025 16:22 ; dates illisibles : 0
- Doublons sur (`Département`, `Numéro`) : 0
- Départements présents : 90
- Communes du 77 présentes : 25 sur 507 du référentiel ; codes INSEE du 77 absents du référentiel : 0 

**France entière**

| Champ requis | Lignes remplies | Taux de remplissage |
|---|---|---|
| `Numéro` | 2 541 / 2 541 | 100,0 % |
| `Département` | 2 541 / 2 541 | 100,0 % |
| `Code INSEE` | 2 541 / 2 541 | 100,0 % |
| `Date de première alerte` | 2 541 / 2 541 | 100,0 % |
| `Surface parcourue (m2)` | 2 541 / 2 541 | 100,0 % |
| `Surface forêt (m2)` | 2 541 / 2 541 | 100,0 % |
| `Nature` | 1 405 / 2 541 | 55,3 % |

**Seine-et-Marne**

| Champ requis | Lignes remplies | Taux de remplissage |
|---|---|---|
| `Code INSEE` | 55 / 55 | 100,0 % |
| `Date de première alerte` | 55 / 55 | 100,0 % |
| `Surface parcourue (m2)` | 55 / 55 | 100,0 % |
| `Surface forêt (m2)` | 55 / 55 | 100,0 % |
| `Nature` | 25 / 55 | 45,5 % |

Valeurs de `Précision des surfaces` (77) : Estimées = 55

Valeurs de `Précision de la donnée` (France) : (vide) = 2471, Données partielles ou non valides = 70

## Archives de la Météo des forêts (`mdf_2024.csv.gz`, `mdf_2025.csv.gz`, `mdf_2026.csv.gz`)

| Saison | Séparateur | Lignes | Départements | Première publication | Dernière publication | Jours du 77 | Jours du 77 manquants | Doublons (date, dép.) | Valeurs de `niveau_j1` hors 1-4 | Champs vides |
|---|---|---|---|---|---|---|---|---|---|---|
| 2024 | `,` | 11 520 | 96 | 2024-06-03 | 2024-09-30 | 120 | 0 | 0 | 0 | 0 |
| 2025 | `,` | 11 520 | 96 | 2025-06-03 | 2025-09-30 | 120 | 0 | 0 | 0 | 0 |
| 2026 | `;` | 12 576 | 96 | 2026-05-28 | 2026-10-05 | 131 | 0 | 0 | 0 | 0 |

## Comptes des SDIS (`ofgl-base-sdis.csv`)

- Lignes : 84 420 · colonnes : 21 · exercices : 2012 → 2025
- Départements avec un budget principal, par exercice : de 97 à 97 (attendu : 97, soit 101 départements moins 75, 92, 93, 94)
- Doublons sur (`Exercice`, `Code Département`, `Agrégat`) pour le budget principal : 0

| Champ requis | Lignes remplies | Taux de remplissage |
|---|---|---|
| `Exercice` | 84 420 / 84 420 | 100,0 % |
| `Code Département` | 84 420 / 84 420 | 100,0 % |
| `CBUDG` | 84 420 / 84 420 | 100,0 % |
| `Agrégat` | 84 420 / 84 420 | 100,0 % |
| `Montant` | 84 420 / 84 420 | 100,0 % |
| `Population totale SDIS` | 84 420 / 84 420 | 100,0 % |

## Jours fériés (`jours_feries_metropole.csv`)

- Lignes : 286 · bornes : 2006-01-01 → 2031-12-25 · dates en double : 1 (2008-05-01)

| Champ requis | Lignes remplies | Taux de remplissage |
|---|---|---|
| `date` | 286 / 286 | 100,0 % |
| `nom_jour_ferie` | 286 / 286 | 100,0 % |

## Vacances scolaires (`vacances_scolaires.csv`)

- Lignes : 14 245 · bornes : 1990-01-01 → 2028-12-31 · jours manquants : 0 · dates en double : 0
- `nom_vacances` vide hors vacances (attendu) : 8 514 lignes ; `nom_vacances` vide un jour de vacances zone C : 0

| Champ requis | Lignes remplies | Taux de remplissage |
|---|---|---|
| `date` | 14 245 / 14 245 | 100,0 % |
| `vacances_zone_c` | 14 245 / 14 245 | 100,0 % |

## Admin Express, communes d'Île-de-France (`communes_idf.csv`)

- Lignes : 1 266 · codes INSEE en double : 0
- Communes par département : 75 = 1, 77 = 507, 78 = 259, 91 = 194, 92 = 36, 93 = 39, 94 = 47, 95 = 183

| Champ requis | Lignes remplies | Taux de remplissage |
|---|---|---|
| `code_insee` | 1 266 / 1 266 | 100,0 % |
| `nom_officiel` | 1 266 / 1 266 | 100,0 % |
| `code_insee_du_departement` | 1 266 / 1 266 | 100,0 % |
| `population` | 1 266 / 1 266 | 100,0 % |

## BD Forêt V2, surface forestière par commune du 77 (`surface_foret_par_commune_77.csv`)

- Communes : 507 (référentiel : 507) · communes sans forêt : 5 · surface forestière totale : 151 101 ha
- Communes du référentiel absentes : 0

