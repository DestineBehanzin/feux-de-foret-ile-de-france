# Spécification — Île-de-France (Seine-et-Marne)

Groupe : Destiné BEHANZIN (chef de projet, responsable sources) · Sandrine YAO (responsable qualité et conformité) · Audrey MOBOU (responsable pipeline et modèle) · Version du 2026-11-20 (brouillon proposé par Sandrine YAO, à répartir par section)

> Ce fichier rassemble les décisions et renvoie aux pièces : analyses (`docs/analyse/`), fiches et inventaire (`docs/sources/`), matrice (`docs/sources/matrice.md`), journal (`docs/journal-des-decisions.md`), glossaire (`docs/glossaire.md`), profil des sources (`docs/qualite/profil-sources.md`).

## 1. La décision

Le commanditaire est la direction du SDIS 77 (Seine-et-Marne), qui prépare la saison des feux 2027 avec un budget qui ne permet pas de renforcer le dispositif partout et tout l'été. Elle doit décider où concentrer ses moyens humains et financiers, et à partir de quel niveau de la Météo des forêts déclencher le dispositif renforcé (patrouilles, guet), sachant que le seuil actuel est contesté par les chefs de centre. L'échéance est la soutenance du 11 décembre 2026, pour une application à la saison 2027.

## 2. Les questions retenues

| N° | Question | Décision qu'elle éclaire | Proposée par |
|---|---|---|---|
| Q1 | Où faut-il concentrer nos moyens, humains comme financiers, pour lutter au mieux contre les départs de feu ? | Zones (communes) et périodes (mois, heures, types de jour) où renforcer prévention, surveillance et intervention | Commande, reprise par le groupe |
| Q2 | À partir de quel niveau de la Météo des forêts devons-nous déclencher le dispositif renforcé ? | Seuil de déclenchement des patrouilles et du guet pour 2027 | Commande, reprise par le groupe |
| Q3 | Le seuil actuel convient-il (fausses alertes, feux partis par indice bas) ? | Garder, modifier ou compléter la règle de déclenchement (autre indicateur au printemps, maille plus fine) | Commande (reproches des chefs de centre) |
| Q4 | Comment se comporte l'indice dans le 77 et la région, et comment le 77 se situe-t-il par rapport au reste du territoire ? | Argumenter une demande de renforts ou de cofinancement | Commande |

Questions écartées, avec la raison et le renvoi au journal :

- « Quels sont les niveaux d'indice disponibles ? » et « Où peut-on avoir les données sur les indices ? » (analyse de Sandrine) : questions de découverte des sources, qui ne mènent à aucune décision (journal D14).
- « Quels sont les indicateurs de feux de forêt ? » et « Quels sont les moyens mis en place ? » (analyse de Sandrine) : reformulées et intégrées à Q1 et Q4 (journal D14).

## 3. Les sources retenues

| Source | Fiche | Localisation (URL, API, fichier) | Mode de récupération | Champs utiles | Questions servies |
|---|---|---|---|---|---|
| BDIFF | `docs/sources/fiche-bdiff.md` | https://bdiff.agriculture.gouv.fr/ | Export manuel CSV (`Incendies.csv`), France entière, une année ou plus par export | `Numéro`, `Année`, `Département`, `Code INSEE`, `Nom de la commune`, `Date de première alerte`, `Surface parcourue (m2)`, `Surface forêt (m2)`, `Nature`, `Précision des surfaces`, `Précision de la donnée` | Q1, Q2, Q3, Q4 |
| IFM Copernicus | `docs/sources/fiche-ifm-copernicus.md` | https://ewds.climate.copernicus.eu/datasets/cems-fire-historical-v1 | Téléchargement NetCDF sur l'emprise de l'Île-de-France, 2006-2026 | temps, latitude, longitude, Fire weather index (option : Fine fuel moisture code) | Q2, Q3, Q4 |
| Météo des forêts | `docs/sources/fiche-meteo-des-forets.md` | https://www.data.gouv.fr/datasets/archives-de-la-meteo-des-forets (`mdf_2024.csv.gz`, `mdf_2025.csv.gz`, `mdf_2026.csv.gz`) | Téléchargement direct des CSV compressés ; API Météo-France pour la saison 2027 | `date`, `num_dep`, `niveau_j1`, `niveau_j2` | Q2, Q3, Q4 |
| BD Forêt V2 | `docs/sources/fiche-bd-foret-v2.md` | Service WFS IGN, couche `LANDCOVER.FORESTINVENTORY.V2:formation_vegetale` | Script `extraire_bdforet_77.py` (pagination WFS) | `code_tfv`, `tfv_g11`, `geom` | Q1, Q3, Q4 |
| Admin Express | `docs/sources/fiche-admin-express.md` | Service WFS IGN, couches `ADMINEXPRESS-COG.LATEST:commune` et `:departement` | Script `extraire_admin_express.py` | `code_insee`, `nom_officiel`, `code_insee_du_departement`, `population`, `date_du_recensement`, `geometrie` | Q1, Q3, Q4 |
| Comptes des SDIS (OFGL) | `docs/sources/fiche-comptes-sdis-ofgl.md` | https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/ofgl-base-sdis/exports/csv?use_labels=true | Téléchargement direct CSV | `Exercice`, `Code Département`, `Code Région`, `CBUDG`, `Agrégat`, `Montant`, `Montant en € par habitant`, `Population totale SDIS`, `Catégorie population du SDIS`, `Département rural` | Q1, Q4 |
| Jours fériés | `docs/sources/fiche-jours-feries.md` | https://etalab.github.io/jours-feries-france-data/csv/jours_feries_metropole.csv | Téléchargement direct CSV | `date`, `nom_jour_ferie` | Q1, Q2, Q3 |
| Vacances scolaires | `docs/sources/fiche-vacances-scolaires.md` | https://raw.githubusercontent.com/AntoineAugusti/vacances-scolaires/master/data.csv | Téléchargement direct CSV | `date`, `vacances_zone_c`, `nom_vacances` | Q1, Q2, Q3 |
| Arrêtés préfectoraux du 77 | `docs/sources/fiche-arretes-prefectoraux-77.md` | https://www.seine-et-marne.gouv.fr/Actualites/Incendies-points-de-situation-et-arretes-prefectoraux (PDF) | Relevé manuel dans un CSV (`id_arrete`, `date_debut`, `date_fin`, `perimetre`, `type_mesure`, `plage_horaire`, `url_source`) | tous | Q2, Q3 |

Sources écartées, avec la raison :

- **EFFIS** : téléchargement indisponible (certificat expiré), historique sur demande (journal D06).
- **Interventions SDIS** : « feux de végétations » mélange forêts, champs et broussailles, grain annuel (D11).
- **Statistiques nationales des SDIS** : effectifs seulement, une année, en PDF (D08).
- **Pyronear** : images, pas de jointure possible (D12).
- **Forêts publiques, PPFCI / PDPFCI, Stratégie nationale** : contenu à vérifier, écartées si rien d'exploitable (D10).
- **Trafic routier, OpenStreetMap, festivals** : hypothèse de fréquentation gardée comme piste qualitative (D18).
- **Données internes du SDIS 77** : non publiques (D02).

## 4. Les sources de référence

| Donnée | Sources concernées | Source de référence | Pourquoi |
|---|---|---|---|
| Départs de feu de forêt | BDIFF, Interventions SDIS (« Feux de végétations ») | **BDIFF** | Grain du feu, définition stricte de la forêt ; les interventions mélangent forêt, champs et broussailles |
| Danger de feu par jour | Météo des forêts, IFM Copernicus | **Météo des forêts** pour les niveaux (c'est l'indice de la commande) ; **IFM** pour les jours hors saison et l'historique | La commande porte sur les niveaux de la Météo des forêts ; seul l'IFM couvre le printemps et 2006-2023 |
| Population d'un département | OFGL (`Population totale SDIS` : 1 468 459 en 2025 pour le 77), Admin Express (somme des communes : 1 468 108) | **OFGL** pour les ratios départementaux | Une valeur par exercice, cohérente avec les montants par habitant |
| Population d'une commune | Admin Express | **Admin Express** | Seule source au grain communal |
| Liste, codes et noms des communes | BDIFF (`Code INSEE`, `Nom de la commune`), Admin Express | **Admin Express** | Référentiel officiel à jour (COG) |
| Codes et noms des départements | BDIFF, Météo des forêts, OFGL, Admin Express | **Admin Express** | Référentiel commun ; codes harmonisés sur 2 caractères |
| Surface de forêt | BD Forêt V2, BDIFF (`Surface forêt (m2)` = forêt brûlée) | **BD Forêt V2** pour la forêt existante ; **BDIFF** pour la forêt brûlée | Ce ne sont pas les mêmes grandeurs |

## 5. Les manques

Matrice complète : `docs/sources/matrice.md`

| Question | Ce qui manque | Décision | Ce que la décision coûte | Journal |
|---|---|---|---|---|
| Q1 | Localisation et nombre des moyens (casernes, engins, effectifs) | Approximer : moyens financiers par l'OFGL | Moyens exprimés en euros, pas en engins ni en pompiers | D02, D08 |
| Q1 | Localisation des feux à l'intérieur d'une commune | Renoncer : grain communal | Fontainebleau couvre presque tout le massif : pas de zonage interne | D07 |
| Q2 | Assez de jours orange croisables avec des feux (1 seul en 2024-2025 dans le 77) | Approximer : seuil d'IFM 2006-2025, traduit en niveau | Recommandation indirecte, efficacité non observable | D04 |
| Q2 | Dates d'activation et coût du dispositif actuel | Renoncer (non public) | Coût exprimé en nombre de jours d'activation | D02 |
| Q2, Q3 | Feux de l'été 2026 (BDIFF arrêtée en 2025) | Approximer : étude de cas (Météo des forêts, arrêtés) | Pas de nombre de départs de feu pour 2026 | D05, D06 |
| Q3 | Seuil actuellement appliqué par le SDIS 77 | Renoncer : tester tous les seuils | Pas de jugement direct sur le seuil réel | D15 |
| Q2, Q3 | Mesures réellement prises pendant les jours de danger | Collecter : relevé manuel des arrêtés | Exhaustivité non garantie | D09 |

## 6. Les incohérences repérées et les transformations nécessaires

| Sources | Nature (format de date, unité, recouvrement, clé) | Exemple tiré du fichier | Transformation nécessaire |
|---|---|---|---|
| Météo des forêts 2024-2025 / 2026 | Format : séparateur et nom de colonne | `2025-06-03T14:50:06Z,1,1,1,Ain` en 2025 ; `2026-05-28T14:50:07Z;01;1;1;Ain` en 2026 (`dep_nom` puis `nom_dep`) | Lire avec le bon séparateur selon l'année ; renommer en `nom_departement` |
| Météo des forêts × BDIFF, OFGL | Clé : code département | `num_dep` = `1` en 2025, `01` en 2026 ; `Code Département` = `01` dans l'OFGL | Compléter à 2 caractères (`zfill(2)`) ; garder `2A`, `2B` en texte |
| Météo des forêts × BDIFF | Format de date : date de publication et date cible | `date` = `2026-07-11T14:50:05Z`, `niveau_j1` = `3` s'applique au 12/07/2026 | `date_cible = date(date) + 1 jour` pour `niveau_j1`, + 2 jours pour `niveau_j2` |
| BDIFF | Format de fichier | 2 lignes avant l'en-tête : `"Nombre d'incendies suivant les critères de sélection : 2541"` puis les critères | Ignorer les 2 premières lignes (`skiprows=2`) |
| BDIFF | Format de date | `Date de première alerte` = date et heure (alerte à la minute) | Extraire `date_alerte` (jour) et `heure_alerte` |
| BDIFF | Unité | `Surface parcourue (m2)` en m² | Diviser par 10 000 → hectares |
| BDIFF (avant / depuis 2023) | Recouvrement des colonnes de surface | Depuis 2023 : `Surfaces agricoles (m2)`, `Autres surfaces (m2)` ; avant : `Surfaces non boisées (m2)`… (définitions BDIFF) | Ne garder que `Surface parcourue (m2)` et `Surface forêt (m2)`, communs aux deux périodes |
| BDIFF × Admin Express | Clé : code commune | Codes BDIFF des années anciennes peut-être absents d'Admin Express (communes fusionnées) ; 0 code absent en 2025 (profil) | Table de passage ancien code → code actuel (COG) pour 2006-2024 |
| BDIFF × Météo des forêts | Recouvrement géographique | BDIFF : 90 départements en 2025, y compris outre-mer ; Météo des forêts : 96 départements métropolitains | Restreindre les comparaisons à la métropole |
| OFGL | Format long | Une ligne par `Agrégat` (84 420 lignes) | Filtrer `CBUDG` = `1`, pivoter un agrégat par colonne |
| OFGL × Admin Express | Recouvrement | 97 départements dans l'OFGL (sans 75, 92, 93, 94) ; 101 dans Admin Express | Comparaison francilienne limitée à 77, 78, 91, 95 |
| Jours fériés | Clé en double | `2008-05-01` présent 2 fois (« 1er mai » et « Ascension ») | Dédoublonner sur `date` |
| Vacances scolaires | Format booléen | `vacances_zone_c` = `True` / `False` (texte) | Convertir en booléen |
| IFM × communes | Grain spatial | Maille de 0,25° ; le 77 couvre quelques mailles | Rattacher chaque commune à la maille qui contient son centre ; valeur départementale = maximum (choix à documenter) |
| BD Forêt × communes | Grain spatial | 13 194 polygones de végétation dans le 77 | Intersection avec les communes, somme des surfaces → `surface_foret_ha` par `code_insee` |

## 7. Conformité

| Champ | Source | Question qui le justifie | Décision (garder, pseudonymiser, écarter) | Technique |
|---|---|---|---|---|
| `Code INSEE`, `Nom de la commune` | BDIFF | Q1, Q3, Q4 | Garder | Aucune : localisation à la commune, pas de personne |
| `Date de première alerte` | BDIFF | Q1, Q2, Q3 | Garder | Publication agrégée (jour, mois, heure) ; jamais la date-heure exacte d'un feu isolé dans une petite commune |
| `Nature` | BDIFF | Q1 | Garder pour l'analyse, publier en agrégé | Ne pas publier la cause d'un feu individuel dans une commune de moins de 5 feux sur la période |
| `Nombre de décès`, `Nombre de bâtiments totalement détruits`, `Nombre de bâtiments partiellement détruits` | BDIFF | Aucune | Écarter | Colonnes non chargées dans la couche nettoyée |
| `population` | Admin Express | Q1, Q4 | Garder | Total communal : pas de donnée personnelle |
| Noms de personnes ou d'entreprises éventuellement cités | Arrêtés préfectoraux | Aucune | Écarter | Seuls `date_debut`, `date_fin`, `perimetre`, `type_mesure`, `plage_horaire` sont relevés |
| Images | Pyronear | Aucune | Écarter | Source non chargée |

Risque de ré-identification par croisement : **faible**. Aucune source retenue ne contient de personne. Le seul risque est de croiser, pour une petite commune, la date et l'heure exactes d'un feu, sa cause (« malveillance ») et des articles de presse, ce qui pourrait désigner une affaire judiciaire. On publie donc les feux en agrégé (commune × mois, ou département × jour), et la cause seulement au niveau du département.

## 8. Historisation

| Source | Ce qui change dans le temps | Exemple | Ce que l'on garde |
|---|---|---|---|
| Météo des forêts | Format des fichiers selon la saison | 2026 : séparateur `;`, `num_dep` sur 2 caractères, `nom_dep` | Chaque fichier brut tel quel, avec sa date de téléchargement et son empreinte SHA-256 |
| BDIFF | Découpage des surfaces depuis 2023 ; corrections possibles d'anciennes fiches | Colonnes de surface différentes avant et depuis 2023 (définitions BDIFF) | Chaque export brut, daté ; on ne recharge pas par-dessus |
| Admin Express | Limites et codes des communes (fusions) ; population mise à jour | Version `LATEST`, population 2023 (2022 pour quelques communes) | L'édition utilisée (date d'extraction) et une table de passage des anciens codes |
| BD Forêt V2 | Millésime par département, mise à jour irrégulière | Élaborée entre 2007 et 2018 | La date d'extraction ; une seule version |
| Comptes des SDIS | Ajout d'un exercice par an ; métadonnées parfois en retard | data.gouv.fr affiche 2012-2023, le fichier contient 2012-2025 | Le fichier téléchargé, daté |
| Jours fériés | Fenêtre glissante (20 ans de passé) | Fichier actuel : 2006 → 2031 | Le fichier téléchargé, archivé (2006 sortira de la fenêtre) |
| Vacances scolaires | Ajout des années futures | Fichier actuel : 1990 → 2028 | Le fichier téléchargé, daté |
| IFM Copernicus | Versions du produit | Jeu `cems-fire-historical-v1` | Le nom de version dans les métadonnées de chargement |
| Arrêtés préfectoraux | Nouveaux arrêtés, abrogations | Arrêté du 21/08/2026 réouvrant 80 % du massif | Une ligne par arrêté, jamais modifiée ; une abrogation est une nouvelle ligne |

## 9. Entrées attendues et qualité

Pour chaque source retenue, ce que vous exigez d'elle :

| Source | Champs requis | Champs pouvant être vides (raison) | Clé et grain | Référentiel attendu | Période attendue |
|---|---|---|---|---|---|
| BDIFF | `Numéro`, `Département`, `Code INSEE`, `Date de première alerte`, `Surface parcourue (m2)` | `Nature` (origine inconnue : 54,5 % de vides dans le 77 en 2025) ; `Surface forêt (m2)` peut valoir 0 | (`Département`, `Numéro`) · un feu | Communes Admin Express | 2006 → 2025 |
| Météo des forêts | `date`, `num_dep`, `niveau_j1` | `niveau_j2` (sert seulement à la stabilité) | (`date_cible`, `num_dep`) · un département × un jour | 96 départements métropolitains | Saisons 2024, 2025, 2026 |
| IFM Copernicus | temps, latitude, longitude, Fire weather index | aucun | (jour, maille) · une maille × un jour | Grille 0,25° couvrant l'Île-de-France | 2006 → 2026 |
| BD Forêt V2 | `code_tfv`, `geom` | `essence` (non utilisée) | `id` · un polygone | Département 77 (Admin Express) | Dernière édition |
| Admin Express | `code_insee`, `code_insee_du_departement`, `population`, `geometrie` | aucun | `code_insee` · une commune | Code officiel géographique | Dernière édition |
| Comptes des SDIS | `Exercice`, `Code Département`, `CBUDG`, `Agrégat`, `Montant`, `Population totale SDIS` | aucun | (`Exercice`, `Code Département`, `Agrégat`) pour `CBUDG` = `1` · un département × un exercice × un agrégat | 97 départements (101 moins 75, 92, 93, 94) | 2012 → 2025 |
| Jours fériés | `date`, `nom_jour_ferie` | aucun | `date` · un jour férié | Calendrier | 2006 → 2026 |
| Vacances scolaires | `date`, `vacances_zone_c` | `nom_vacances` (vide hors vacances) | `date` · un jour | Calendrier continu | 2006 → 2026 |
| Arrêtés préfectoraux | `id_arrete`, `date_debut`, `type_mesure`, `perimetre`, `url_source` | `date_fin` (arrêté jusqu'à nouvel ordre), `plage_horaire` | `id_arrete` · un arrêté | Communes Admin Express | 2024 → 2026 |

Profil de chaque source : taux de remplissage des champs requis, entités présentes comparées au référentiel, bornes des dates. Chaque chiffre vient du fichier de votre région. Fichier ou requête qui l'a produit : `scripts/qualite/profil_sources.py`, résultat dans `docs/qualite/profil-sources.md`. Points saillants :

- BDIFF 2025 : 2 541 feux, champs requis remplis à 100 % ; `Nature` remplie à 55,3 % (France) et 45,5 % (77) ; 0 doublon ; 25 communes du 77 sur 507, toutes reconnues par le référentiel ; dates du 01/01/2025 au 31/12/2025.
- Météo des forêts : 96 départements chaque saison ; 77 présent 120, 120 et 131 jours, sans jour manquant ; 0 doublon ; `niveau_j1` toujours entre 1 et 4.
- Comptes des SDIS : 84 420 lignes, 0 vide ; 97 départements chaque exercice ; 0 doublon sur la clé.
- Jours fériés : 286 lignes, 1 date en double (`2008-05-01`). Vacances : 14 245 jours, 0 manquant, 0 doublon.
- Admin Express : 1 266 communes en Île-de-France, dont 507 dans le 77, 0 doublon. BD Forêt : 507 communes sur 507 couvertes, 151 101 ha de forêt.

Règles de qualité (trois au minimum, sur deux niveaux de complétude et une autre dimension) :

| N° | Source | Niveau ou dimension | Sélecteur | Prédicat | Seuil (et sa justification) | Décision (bloquer, alerter, tolérer) |
|---|---|---|---|---|---|---|
| R1 | BDIFF | Complétude, niveau du champ | Toutes les lignes | `Code INSEE`, `Date de première alerte`, `Département` non vides | 100 % (profil : 100 % en 2025 ; sans ces champs, un feu ne se rattache ni à une commune ni à un jour) | **Bloquer** la ligne (rejet journalisé dans `audit`) |
| R2 | BDIFF | Complétude, niveau du champ | Lignes du 77 | Part de `Nature` non vide | ≥ 40 % (profil : 45,5 % dans le 77 en 2025 ; en dessous, la répartition des causes n'est plus interprétable) | **Alerter** ; tolérer au-dessus |
| R3 | Météo des forêts | Complétude, niveau de l'entité | (`num_dep` = `77`) pour chaque saison | Un niveau pour chaque jour entre la première et la dernière publication | 0 jour manquant (profil : 0 en 2024, 2025, 2026 ; un trou fausserait le compte des jours d'activation) | **Bloquer** le chargement de la saison |
| R4 | Comptes des SDIS | Complétude, niveau de l'entité | `CBUDG` = `1`, chaque `Exercice` | Nombre de départements distincts | = 97 (profil : 97 chaque exercice) | **Alerter** si inférieur |
| R5 | Météo des forêts | Validité | Toutes les lignes | `niveau_j1` ∈ {1, 2, 3, 4} | 100 % (profil : 0 valeur hors domaine) | **Bloquer** la ligne |
| R6 | Jours fériés | Unicité | Toutes les lignes | Une seule ligne par `date` | 0 doublon après transformation (profil : 1 doublon brut, `2008-05-01`, attendu) | **Tolérer** le brut, **bloquer** si un doublon subsiste en couche nettoyée |
| R7 | BDIFF × Admin Express | Cohérence (intégrité référentielle) | Lignes du 77 | `Code INSEE` présent dans Admin Express | 100 % (profil : 0 code absent en 2025) | **Alerter** et rattacher via la table de passage (communes fusionnées) |
| R8 | BDIFF | Validité | Toutes les lignes | `Surface parcourue (m2)` ≥ `Surface forêt (m2)` ≥ 0 | 100 % (la forêt brûlée est une partie de la surface parcourue) | **Alerter** |

Ce que ces indicateurs de qualité ne permettent pas d'affirmer :

- Que **tous les feux ont été saisis** dans la BDIFF : un feu absent n'est pas détectable (exemple : 2 feux dans le 78 en 2025 contre 55 dans le 77, différence réelle ou saisie inégale ?).
- Que les **surfaces sont exactes** : toutes celles du 77 sont estimées, aucune mesurée.
- Que la **cause** renseignée est juste : elle est déclarative.
- Que la Météo des forêts « se trompe » : un jour orange sans feu n'est pas une erreur de l'indice, qui mesure un danger.

## 10. Architecture

Schéma : `docs/architecture.md` (diagramme Mermaid)

| Couche | Rôle | Contenu envisagé | Outil | Questions servies |
|---|---|---|---|---|
| Sources | Ce que vous recevez, tel quel | Fichiers CSV (BDIFF, Météo des forêts, OFGL, jours fériés, vacances), NetCDF (IFM), réponses WFS (BD Forêt, Admin Express), CSV saisi à la main (arrêtés) déposés dans `data/incoming/` | Python (scripts de téléchargement), dépôt manuel | Q1 à Q4 |
| Données brutes | Conservées sans modification | `raw.csv_records` : une ligne par enregistrement source, contenu en JSONB, nom du fichier, date de chargement, empreinte SHA-256 ; `audit` : lots, rejets, erreurs ; fichiers originaux archivés dans `data/archive/` | PostgreSQL, Dagster (assets d'ingestion) | Q1 à Q4 |
| Données nettoyées | Types, formats, doublons, valeurs manquantes traitées | Un modèle `staging` par source : codes département sur 2 caractères, dates typées, `date_cible` de la Météo des forêts, surfaces en hectares, OFGL pivoté sur `CBUDG` = `1`, jours fériés dédoublonnés | dbt (`staging`), tests dbt (R1 à R8) | Q1 à Q4 |
| Données consolidées | Sources croisées au même grain | `intermediate` : table jour × département (niveau, IFM, nombre de feux, type de jour, arrêté en vigueur) ; table commune (feux, forêt, population) ; table département × année (feux, population, dépenses) | dbt (`intermediate`) | Q1, Q2, Q3, Q4 |
| Données prêtes pour l'analyse | Ce que lisent les indicateurs | `marts` : faits et dimensions (`fait_feux`, `fait_danger_jour`, `dim_commune`, `dim_departement`, `dim_calendrier`), contrat stable pour l'exploitation | dbt (`marts`) | Q1, Q2, Q3, Q4 |
| Restitution | Ce que lit le commanditaire | Carte des communes prioritaires, calendrier d'activation, tableau « seuil × feux couverts × jours d'activation », classement des départements | Streamlit ou Power BI (à trancher) | Q1, Q2, Q3, Q4 |

Hypothèses : ce que vous pensez construire sans l'avoir encore vu en cours, et pourquoi :

- Un **asset Dagster par source**, planifié une fois par an (BDIFF, OFGL) ou une fois par jour en saison (API Météo des forêts en 2027) : chaque source a son rythme.
- L'**IFM** est chargé en table jour × maille dans `raw`, puis ramené au département dans `intermediate` : la grille ne se joint pas directement aux autres sources.
- Les **géométries** (BD Forêt, communes) sont traitées en Python pour produire une table attributaire (`surface_foret_par_commune`) : PostGIS n'est pas nécessaire pour nos questions.

## 11. Contraintes

| Contrainte | Comment l'architecture la respecte |
|---|---|
| Outils gratuits uniquement | Python, PostgreSQL, Dagster, dbt Core, Docker sont libres et gratuits ; toutes les sources sont publiques et gratuites (journal D02) ; pour la restitution, Streamlit est gratuit (Power BI Desktop aussi, mais le partage en ligne est payant) |
| Conserver les données brutes | Fichiers originaux archivés dans `data/archive/` ; `raw.csv_records` garde chaque ligne telle quelle (JSONB) avec son empreinte SHA-256 ; aucune transformation avant `staging` |
| Pouvoir retraiter sans rappeler les API | Tout est retraité à partir de `raw` et des fichiers archivés ; dbt reconstruit `staging`, `intermediate` et `marts` sans aucun appel réseau ; les extractions WFS sont enregistrées en GeoPackage |
| Données incomplètes | Règles R1 à R8 : rejet journalisé dans `audit` (bloquer), alerte (alerter) ou tolérance documentée ; les manques connus (2026, seuil actuel, moyens) sont traités par les décisions D02, D04, D05, D15 |
| Accès à une source limité ou interrompu | Chargement idempotent (empreinte SHA-256 : un fichier rechargé n'est pas dupliqué) ; une source indisponible n'empêche pas les autres de se charger ; exemple vécu : EFFIS inaccessible (D06), remplacée par une étude de cas |

## 12. Planning de réalisation

| Jalon | Couche | Responsable | Date | Preuve qu'il est atteint |
|---|---|---|---|---|
| Spécification fusionnée dans `main`, tag `spec-v1` | — | Destiné BEHANZIN | 2026-11-21 | Tag `spec-v1` visible sur GitHub |
| Fichiers bruts téléchargés (BDIFF 2006-2025, Météo des forêts, OFGL, calendrier) et IFM extrait | Sources | Destiné BEHANZIN | 2026-11-25 | Fichiers présents dans `data/incoming/`, listés dans le journal de chargement |
| Table des arrêtés préfectoraux 2024-2026 | Sources | Sandrine YAO | 2026-11-27 | `arretes_prefectoraux_77.csv` dans `data/incoming/` |
| Ingestion de toutes les sources dans `raw` | Données brutes | Audrey MOBOU | 2026-11-28 | `SELECT COUNT(*)` par source dans `raw.csv_records` ; lot réussi dans `audit` |
| Modèles `staging` et tests R1 à R8 | Données nettoyées | Audrey MOBOU (modèles), Sandrine YAO (tests) | 2026-12-02 | `dbt test` passe ; rejets visibles dans `audit` |
| Tables `intermediate` (jour × département, commune, département × année) | Données consolidées | Audrey MOBOU | 2026-12-04 | `dbt run` réussi ; contrôle : 55 feux du 77 en 2025 retrouvés |
| `marts` et indicateurs | Données prêtes pour l'analyse | Audrey MOBOU, Sandrine YAO | 2026-12-07 | Une requête par question (Q1 à Q4) renvoie un résultat |
| Restitution | Restitution | Destiné BEHANZIN | 2026-12-09 | Application ou rapport qui affiche les indicateurs de Q1 à Q4 |
| Répétition de la soutenance | — | Groupe | 2026-12-10 | Support relu par les trois membres |

Exemple de preuve : une table qui se charge, un test qui passe, une table prête pour l'analyse.
Ce qui est prévu pendant les trois semaines sans cours : téléchargements et ingestion (jalons du 25 au 28/11), puis `staging` et tests (02/12), en se coordonnant par les tickets et les pull requests. *Dates proposées, à valider par le chef de projet.*

## 13. Glossaire

Lien : `docs/glossaire.md` · Nombre de termes : 46 · Termes encore « à vérifier » : 5 (massif de Fontainebleau, grand feu, CODIS, CCF, PDPFCI)

## 14. Limites connues

Ce que cette spécification ne permettra pas de dire au commanditaire, et pourquoi :

- **L'efficacité du dispositif** : un jour sans feu peut être un jour où les patrouilles ont empêché un départ ; ce n'est pas mesurable.
- **Le jugement du seuil actuel** : il n'est pas public (D02, D15) ; on compare des seuils sans savoir lequel est appliqué.
- **Le nombre de départs de feu en 2026** : la BDIFF s'arrête en 2025 (D05) ; l'été 2026 est une étude de cas.
- **Un seuil validé sur des feux réels** : la Météo des forêts n'a qu'un jour orange croisable avec des feux en 2024-2025 ; le seuil repose sur l'IFM (D04).
- **La répartition des moyens en pompiers, engins ou casernes** : données non publiques ; on parle en euros (D08).
- **Où, à l'intérieur du massif de Fontainebleau** : grain communal (D07).
- **Pourquoi les feux se concentrent à Fontainebleau** : la fréquentation n'est pas mesurée (D18).
- **La comparaison avec Paris et la petite couronne** : la BSPP est absente des comptes des SDIS.
