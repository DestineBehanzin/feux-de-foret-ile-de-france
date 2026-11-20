# Hypothèses, objectifs SMART, métriques et KPIs – Sandrine YAO

> Projet : feux de forêt en Île-de-France (commande du SDIS 77, saison 2027)
> Rédigé le 20/11/2026 · Proposition de travail pour le groupe (à reprendre dans `docs/specification.md`, sections « Indicateurs » et « Restitution », au moment du cours de KPI)
> Les chiffres cités ont été calculés sur les fichiers réels ; les seuils de décision sont des **propositions à valider** par le groupe.

## 1. Les questions de la commande

| N° | Question | Décision qu'elle éclaire |
|---|---|---|
| Q1 | Où faut-il concentrer nos moyens, humains comme financiers, pour lutter au mieux contre les départs de feu ? | Zones et périodes où renforcer la prévention, la surveillance et l'intervention |
| Q2 | À partir de quel niveau de la Météo des forêts devons-nous déclencher le dispositif renforcé ? | Seuil de déclenchement des patrouilles et du guet |
| Q3 | Le seuil actuel convient-il (fausses alertes, feux partis par indice bas) ? | Garder, abaisser ou compléter la règle de déclenchement |
| Q4 | Comment se situent le 77 et son indice par rapport à la région et au territoire national ? | Argumenter une demande de renforts ou de cofinancement |

## 2. Métriques et KPIs : la différence

- Une **métrique** est une mesure brute, sans jugement : « 55 feux de forêt dans le 77 en 2025 ».
- Un **KPI** (indicateur clé de performance) rapporte une ou plusieurs métriques à un **objectif** et porte un **seuil qui déclenche une décision** : « part des feux couverts par le seuil orange ; si elle est inférieure à 60 %, on abaisse le seuil ».

---

## 3. Hypothèses par source

Chaque hypothèse est numérotée par question (H1.x pour Q1, etc.). Une hypothèse se teste en général en croisant plusieurs sources ; le tableau indique **ce que chaque source apporte**.

| Source | Hypothèses | Ce que la source permet de tester | Colonnes mobilisées |
|---|---|---|---|
| **BDIFF** | H1.1, H1.2, H1.3, H2.1, H2.2, H3.2, H3.3, H3.4, H4.1, H4.2 | Où, quand et pourquoi partent les feux ; nombre et surface par commune, par mois, par heure, par cause | `Date de première alerte`, `Code INSEE`, `Département`, `Surface parcourue (m2)`, `Surface forêt (m2)`, `Nature` |
| **IFM Copernicus** | H2.1, H3.3 | Le danger météo de chaque jour, **toute l'année et sur 20 ans**, pour chercher un seuil fiable et qualifier les feux de printemps | Fire weather index (temps, latitude, longitude) |
| **Météo des forêts** | H2.1, H3.1, H3.2, H3.4, H4.1 | Le niveau annoncé chaque jour pour le 77 et les autres départements ; traduction du seuil d'IFM en niveau | `date`, `num_dep`, `niveau_j1`, `niveau_j2` |
| **BD Forêt V2** | H1.2, H3.4, H4.1 | La surface de forêt par commune, pour rapporter les feux à la forêt et délimiter le massif de Fontainebleau | `code_tfv`, `geom` |
| **Admin Express** | H1.2, H3.4, H4.1 | Rattacher chaque feu à sa commune, calculer les surfaces, cartographier | `code_insee`, `population`, `geometrie` |
| **Comptes des SDIS (OFGL)** | H1.4, H4.1 | Les moyens financiers du SDIS 77 face aux SDIS comparables ; population pour les ratios | `Agrégat`, `Montant`, `Montant en € par habitant`, `Population totale SDIS`, `Catégorie population du SDIS` |
| **Calendrier** (jours fériés, vacances) | H1.3, H2.2, H3.2 | Le rôle de la fréquentation (week-ends, jours fériés, vacances) dans les départs de feu | `date`, `nom_jour_ferie`, `vacances_zone_c` |
| **Arrêtés préfectoraux** | H2.1, H3.1 | Ce qui a réellement été déclenché (fermetures, interdictions) face au niveau du jour | Table à construire : `date_debut`, `date_fin`, `perimetre`, `type_mesure` |

### Énoncé des hypothèses

| Code | Question | Hypothèse |
|---|---|---|
| H1.1 | Q1 | Au moins 80 % des feux à cause connue sont d'origine humaine (involontaire, accidentelle, malveillance, travaux) |
| H1.2 | Q1 | Au moins 50 % des feux du 77 partent dans moins de 5 % des communes, autour du massif de Fontainebleau |
| H1.3 | Q1 | Au moins 60 % des alertes ont lieu entre 12 h et 19 h, et au moins 30 % des feux partent en avril-mai |
| H1.4 | Q1 | Les dépenses d'équipement par habitant du SDIS 77 sont inférieures à la moyenne des SDIS de catégorie A |
| H2.1 | Q2 | Il existe un seuil d'IFM au-delà duquel la probabilité qu'au moins un feu parte dans la journée **double** dans le 77 ; ce seuil correspond au niveau orange de la Météo des forêts |
| H2.2 | Q2 | Une règle « niveau ≥ jaune **et** week-end ou jour férié » couvre plus de feux qu'un seuil orange seul, pour un nombre de jours d'activation comparable |
| H3.1 | Q3 | La majorité des jours orange de 2026 n'ont donné lieu à aucun grand feu (fausses alertes) — *testable seulement de façon limitée, faute de feux BDIFF en 2026* |
| H3.2 | Q3 | Au moins 25 % des feux de la saison partent un jour de niveau vert |
| H3.3 | Q3 | Au moins 30 % des feux partent hors de la saison de la Météo des forêts, alors que l'IFM y dépasse déjà 20 |
| H3.4 | Q3 | Plus de 50 % des feux partent dans le massif de Fontainebleau : un niveau unique pour tout le département est trop large |
| H4.1 | Q4 | Le 77 a plus de feux pour 1 000 ha de forêt que la moyenne francilienne, mais moins que la moyenne nationale |
| H4.2 | Q4 | Le nombre de feux de forêt du 77 augmente d'au moins 5 % par an sur 2010-2025 |

### Premiers constats sur les fichiers réels

| Constat | Hypothèse concernée | Source |
|---|---|---|
| 55 feux de forêt dans le 77 en 2025, pour 3,7 ha brûlés | H1.2, H4.2 | BDIFF 2025 |
| Fontainebleau : 24 feux sur 55 (44 %) ; la commune compte 16 162 ha de forêt (94 % de sa surface) | H1.2, H3.4 | BDIFF 2025, BD Forêt V2 |
| 20 feux sur 55 en avril-mai 2025, hors saison de la Météo des forêts | H1.3, H3.3 | BDIFF 2025 |
| Niveaux annoncés pour le 77 : 2024 = 120 jours verts sur 120 ; 2025 = 98 verts, 21 jaunes, 1 orange ; 2026 = 42 verts, 62 jaunes, 27 orange | H3.2, H2.1 | Météo des forêts |
| Tous les feux de juin-septembre 2024 dans le 77 sont donc partis un jour **vert** | H3.2 | BDIFF + Météo des forêts |
| Niveau orange annoncé pour le 77 du 8 au 13 juillet 2026, dont le 12 juillet (départ du grand incendie de Fontainebleau) | H3.1 (étude de cas) | Météo des forêts |
| 151 101 ha de forêt dans le 77 (hors landes) | H4.1 | BD Forêt V2 |

---

## 4. Objectifs SMART

L'échéance commune est la **soutenance du 11 décembre 2026**, pour une application à la saison 2027.

### Objectif 1 (Q1) : cibler les zones et les périodes

| Critère | Contenu |
|---|---|
| **Spécifique** | Identifier les communes et les périodes de l'année où concentrer la prévention et la surveillance dans le 77 |
| **Mesurable** | Classement des communes par nombre de feux pour 1 000 ha de forêt ; part des feux par mois, par heure et par type de jour |
| **Atteignable** | BDIFF 2006-2025, BD Forêt V2, Admin Express, calendrier : sources publiques déjà récupérées ou testées |
| **Réaliste** | Livrer une liste de **10 communes prioritaires** maximum et **un calendrier d'activation** (mois et créneaux horaires) |
| **Temporel** | 11 décembre 2026 |

### Objectif 2 (Q2) : recommander un seuil de déclenchement

| Critère | Contenu |
|---|---|
| **Spécifique** | Recommander le niveau de la Météo des forêts (J+1) à partir duquel déclencher le dispositif renforcé dans le 77 |
| **Mesurable** | Pour chaque seuil possible : part des feux couverts, nombre de jours d'activation par saison, taux de départ de feu |
| **Atteignable** | Seuil d'IFM calculé sur BDIFF × IFM 2006-2025, puis traduit en niveau grâce à la Météo des forêts 2024-2026 |
| **Réaliste** | Le seuil retenu doit couvrir **au moins 60 %** des feux de la saison avec **au plus 30 jours** d'activation par saison (valeurs à valider avec la direction) |
| **Temporel** | 11 décembre 2026 |

### Objectif 3 (Q3) : diagnostiquer le seuil actuel

| Critère | Contenu |
|---|---|
| **Spécifique** | Mesurer et expliquer les feux partis par indice bas et les feux partis hors saison de la Météo des forêts |
| **Mesurable** | Part des feux de la saison partis un jour vert ; part des feux de l'année partis hors saison ; part des feux dans le massif de Fontainebleau |
| **Atteignable** | BDIFF 2024-2025 × Météo des forêts ; BDIFF 2006-2025 pour la saisonnalité ; BD Forêt pour le massif |
| **Réaliste** | Confirmer ou infirmer chaque reproche des chefs de centre par un chiffre, et proposer **une piste d'amélioration par défaut constaté** |
| **Temporel** | 11 décembre 2026 |

### Objectif 4 (Q4) : situer le 77

| Critère | Contenu |
|---|---|
| **Spécifique** | Comparer l'exposition du 77 à celle des départements franciliens (78, 91, 95) et à la moyenne nationale |
| **Mesurable** | Feux pour 1 000 ha de forêt, feux pour 100 000 habitants, nombre de jours orange ou rouge par saison, dépenses d'équipement par habitant |
| **Atteignable** | BDIFF France entière, BD Forêt, OFGL, Météo des forêts : toutes publiques |
| **Réaliste** | Placer le 77 dans un **classement** des départements et dire s'il est au-dessus ou au-dessous de la moyenne régionale et nationale |
| **Temporel** | 11 décembre 2026 |

---

## 5. Métriques (mesures brutes)

| Code | Métrique | Définition / formule | Unité | Grain | Sources et colonnes |
|---|---|---|---|---|---|
| M01 | Nombre de feux | Nombre de lignes de la BDIFF | feux | commune, département, jour, mois, année | BDIFF : `Numéro` |
| M02 | Surface brûlée | Somme de `Surface parcourue (m2)` ÷ 10 000 | ha | commune, département, année | BDIFF |
| M03 | Surface de forêt brûlée | Somme de `Surface forêt (m2)` ÷ 10 000 | ha | commune, département, année | BDIFF |
| M04 | Surface de forêt | Surface des polygones forestiers (hors `code_tfv` commençant par `LA`) | ha | commune, département | BD Forêt V2, Admin Express |
| M05 | Population | `population` (commune) ou `Population totale SDIS` (département) | habitants | commune, département | Admin Express, OFGL |
| M06 | Nombre de feux par cause | Nombre de feux par valeur de `Nature` | feux | département, année | BDIFF |
| M07 | Nombre de feux par heure d'alerte | Nombre de feux par heure de `Date de première alerte` | feux | heure | BDIFF |
| M08 | Nombre de feux par mois | Nombre de feux par mois de `Date de première alerte` | feux | mois | BDIFF |
| M09 | Nombre de jours par niveau | Nombre de jours de saison avec `niveau_j1` = 1, 2, 3 ou 4 | jours | département, saison | Météo des forêts |
| M10 | IFM journalier | Valeur de l'IFM du jour (maximum des mailles couvrant le 77, choix à documenter) | indice | département, jour | IFM Copernicus |
| M11 | Nombre de jours avec au moins un feu | Nombre de jours distincts dans `Date de première alerte` | jours | département, saison | BDIFF |
| M12 | Nombre de feux par type de jour | Feux un week-end, un jour férié, en vacances (zone C), un jour ordinaire | feux | type de jour | BDIFF, calendrier |
| M13 | Dépenses du SDIS | `Montant` pour chaque `Agrégat` retenu (budget principal, `CBUDG` = `1`) | € | département, année | OFGL |
| M14 | Dépenses par habitant | `Montant en € par habitant` | €/hab. | département, année | OFGL |
| M15 | Nombre de jours sous arrêté | Nombre de jours couverts par au moins un arrêté de restriction | jours | département, saison | Arrêtés préfectoraux |

---

## 6. KPIs

Format repris de la section « Indicateurs » prévue dans `docs/specification.md`.

| Question | KPI | Formule | Grain | Période | Sources | Seuil qui déclenche une décision |
|---|---|---|---|---|---|---|
| Q1 | **K1.1 Feux pour 1 000 ha de forêt** | M01 ÷ M04 × 1 000 | commune | 2006-2025 (cumul et moyenne annuelle) | BDIFF, BD Forêt, Admin Express | Les communes du premier décile deviennent **zones prioritaires** de patrouille et de guet |
| Q1 | **K1.2 Concentration géographique** | Part des feux du 77 dans les 5 % de communes qui en comptent le plus | département | 2006-2025 | BDIFF, Admin Express | Si > 50 % : dispositif **ciblé** sur ces communes plutôt que départemental |
| Q1 | **K1.3 Part des feux d'origine humaine** | Feux à cause humaine ÷ feux à cause connue (M06) | département | 2006-2025 | BDIFF | Si > 80 % : priorité budgétaire à la **prévention** auprès du public et des travaux |
| Q1 | **K1.4 Part des feux en avril-mai** | Feux d'avril-mai ÷ feux de l'année (M08) | département | 2006-2025 | BDIFF | Si > 30 % : activer le dispositif **dès le printemps** |
| Q1 | **K1.5 Part des alertes entre 12 h et 19 h** | Alertes 12 h-19 h ÷ toutes les alertes (M07) | département | 2006-2025 | BDIFF | Si > 60 % : concentrer les patrouilles sur l'**après-midi** |
| Q1 | **K1.6 Écart de dépenses d'équipement** | (M14 du 77 − moyenne M14 des SDIS de catégorie A) ÷ moyenne | département | 2020-2025 | OFGL | Si < 0 : argument pour un **cofinancement** des équipements |
| Q2 | **K2.1 Taux de départ par niveau d'IFM** | M11 des jours de la classe d'IFM ÷ nombre de jours de la classe | classe d'IFM | 2006-2025 | BDIFF, IFM | La classe où le taux **double** par rapport à la précédente fixe le seuil d'IFM |
| Q2 | **K2.2 Couverture des feux par seuil** | Feux partis un jour ≥ seuil ÷ feux de la saison | seuil | 2006-2025 (IFM) | BDIFF, IFM | Le seuil retenu doit couvrir **≥ 60 %** des feux |
| Q2 | **K2.3 Jours d'activation par seuil** | Nombre de jours de la saison ≥ seuil | seuil, saison | 2006-2025 (IFM) ; 2024-2026 (niveaux) | IFM, Météo des forêts | Le seuil retenu doit rester **≤ 30 jours** par saison (budget) |
| Q2 | **K2.4 Gain de la règle combinée** | K2.2 avec la règle « niveau ≥ jaune et week-end ou férié » − K2.2 avec le seuil orange seul | règle | 2024-2025 | BDIFF, Météo des forêts, calendrier | Si le gain est positif à jours d'activation comparables : adopter la **règle combinée** |
| Q3 | **K3.1 Part des feux par indice vert** | Feux de la saison partis un jour `niveau_j1` = 1 ÷ feux de la saison | saison | 2024-2025 | BDIFF, Météo des forêts | Si > 25 % : l'indice seul ne suffit pas, maintenir une **capacité minimale** en vert |
| Q3 | **K3.2 Part des feux hors saison** | Feux partis hors période de publication ÷ feux de l'année | année | 2006-2025 | BDIFF | Si > 30 % : utiliser l'**IFM** pour piloter le printemps |
| Q3 | **K3.3 Concentration dans le massif** | Feux dans les communes du massif de Fontainebleau ÷ feux du 77 | département | 2006-2025 | BDIFF, BD Forêt, Admin Express | Si > 50 % : proposer un **niveau infra-départemental** (massif) |
| Q3 | **K3.4 Stabilité de la prévision** | Jours où `niveau_j2` = `niveau_j1` du lendemain ÷ jours | saison | 2024-2026 | Météo des forêts | Si > 80 % : préparer les moyens **à J+2** |
| Q4 | **K4.1 Rang du 77 en feux pour 1 000 ha de forêt** | Rang du 77 parmi les départements (M01 ÷ M04) | département | 2006-2025 | BDIFF, BD Forêt | Si le 77 est dans le premier quart national : demande de **renforts** argumentée |
| Q4 | **K4.2 Feux pour 100 000 habitants** | M01 ÷ M05 × 100 000 | département | 2012-2025 | BDIFF, OFGL | Comparaison à la moyenne régionale (78, 91, 95) et nationale |
| Q4 | **K4.3 Jours orange ou rouge par saison** | M09 pour les niveaux 3 et 4 | département, saison | 2024-2026 | Météo des forêts | Si le 77 dépasse la moyenne francilienne : exposition météo plus forte que ses voisins |

### KPIs souhaités mais impossibles à calculer avec des sources publiques

| KPI souhaité | Pourquoi impossible | Ce que l'on fait |
|---|---|---|
| Coût d'un jour de dispositif renforcé | Données internes du SDIS 77, non publiques | On exprime le coût en **nombre de jours d'activation** (K2.3) |
| Taux de fausses alertes du seuil actuel | Le seuil actuel du SDIS 77 n'est pas public, et la BDIFF n'a pas les feux de 2026 (seule saison avec des jours orange) | On teste **tous les seuils** (K2.2, K2.3) et on traite 2026 en étude de cas |
| Délai d'intervention selon la distance aux casernes | Implantation des casernes non publiée par le SDIS 77 | Piste à approfondir (OpenStreetMap), hors du socle de sources |
| Effet du dispositif sur le nombre de feux | Un jour sans feu peut être un jour où le dispositif a empêché un départ : non mesurable | Limite écrite dans le rapport |

---

## 7. Restitution envisagée

| KPI | Lecteur | Décision qu'il éclaire | Forme envisagée | Ce qu'elle laisse invisible |
|---|---|---|---|---|
| K1.1, K1.2, K3.3 | Direction du SDIS 77 | Zones prioritaires | Carte des communes colorée par feux pour 1 000 ha de forêt | Les feux à l'intérieur d'une commune (grain communal) |
| K1.4, K1.5, K3.2 | Direction, chefs de centre | Calendrier d'activation | Barres par mois et par heure | Les années atypiques (moyenne sur 20 ans) |
| K2.1, K2.2, K2.3, K2.4 | Direction | Seuil de déclenchement | Tableau « seuil × part des feux couverts × jours d'activation » | L'effet réel du dispositif |
| K3.1, K3.4 | Chefs de centre | Confiance dans l'indice | Calendrier de la saison coloré par niveau, jours de feu marqués | Les feux de 2026 (absents de la BDIFF) |
| K1.6, K4.1, K4.2, K4.3 | Direction, financeurs | Demande de renforts ou de cofinancement | Classement des départements | La BSPP (75, 92, 93, 94), absente de l'OFGL |
