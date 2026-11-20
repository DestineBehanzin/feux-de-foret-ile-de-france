# Matrice questions × sources (groupe)

> Projet : feux de forêt en Île-de-France (commande du SDIS 77, saison 2027)
> Version du 20/11/2026 · Proposition de Sandrine YAO, à valider par le responsable sources
> Chaque degré cite la colonne du fichier ou la rubrique de la fiche (`docs/sources/fiche-*.md`) qui le justifie.
> Légende : **complet** · **partiel** · **absent** · **inconnu** (non vérifié dans le fichier ou sa documentation)

## Questions retenues par le groupe

| N° | Question |
|---|---|
| Q1 | Où faut-il concentrer nos moyens, humains comme financiers, pour lutter au mieux contre les départs de feu ? |
| Q2 | À partir de quel niveau de la Météo des forêts devons-nous déclencher le dispositif renforcé (patrouilles, guet) ? |
| Q3 | Le seuil actuel convient-il (fausses alertes, feux partis par indice bas) ? |
| Q4 | Comment se comporte l'indice dans le 77 et la région, et comment le 77 se situe-t-il par rapport au reste du territoire ? |

## 1. Sources retenues

| Question | BDIFF | IFM Copernicus | Météo des forêts | BD Forêt V2 | Admin Express | Comptes des SDIS (OFGL) | Calendrier (fériés, vacances) | Arrêtés préfectoraux 77 |
|---|---|---|---|---|---|---|---|---|
| Q1 | **Partiel** : `Code INSEE`, `Date de première alerte`, `Nature` disent où, quand et pourquoi partent les feux, au grain du feu ; rien sur les moyens, et pas de 2026 (fiche, rubrique « Période ») | **Absent** : maille de 0,25° (fiche, rubrique « Grain ») ; ne localise pas les feux | **Absent** : un seul niveau par département (`num_dep`) | **Partiel** : `code_tfv`, `geom` donnent la surface forestière par commune, pour rapporter les feux à la forêt (donnée indirecte) | **Partiel** : `code_insee`, `population`, `geometrie` : référentiel des communes, sans feux ni moyens | **Partiel** : `Agrégat` (« Frais de personnel », « Dépenses d'équipement - véhicules ») et `Montant` : moyens financiers du SDIS, sans répartition à l'intérieur du département | **Partiel** : `date`, `nom_jour_ferie`, `vacances_zone_c` : moments de forte fréquentation, à croiser avec les feux | **Inconnu** : table pas encore constituée (fiche, rubriques « Période » et « Volumétrie » non vérifiées) |
| Q2 | **Partiel** : `Date de première alerte` permet de dater chaque feu, mais 2024-2025 ne comptent qu'un seul jour orange dans le 77, et 2026 est absent | **Partiel** : `Fire weather index` quotidien depuis 1940 (fiche, rubrique « Période ») : permet un seuil sur 20 ans, mais c'est un IFM, pas un niveau de la Météo des forêts ; fichier pas encore téléchargé | **Partiel** : `niveau_j1` complet pour le 77 (120, 120 et 131 jours, profil) mais seulement 1 jour orange en 2024-2025, les saisons croisables avec des feux | **Absent** : pas de dimension temporelle | **Absent** : référentiel sans dimension temporelle | **Absent** : comptes annuels | **Partiel** : `date` permet de tester une règle « niveau + week-end ou jour férié » | **Inconnu** : table pas encore constituée |
| Q3 | **Partiel** : feux datés et localisés 2006-2025 ; ne dit pas quel était le seuil appliqué | **Partiel** : seule source qui couvre le printemps (`Fire weather index` toute l'année) | **Partiel** : `niveau_j1`, `niveau_j2` disent ce qui était annoncé, pas le seuil du SDIS ; saison juin-septembre seulement (profil : 03/06 → 30/09 en 2024 et 2025) | **Partiel** : `code_tfv`, `geom` : poids du massif de Fontainebleau (16 162 ha de forêt) | **Partiel** : `code_insee` : délimiter le massif par communes | **Absent** : comptes annuels | **Partiel** : `date` : feux par indice bas un jour de forte fréquentation | **Inconnu** : table pas encore constituée |
| Q4 | **Complet** : `Département`, `Date de première alerte`, `Surface parcourue (m2)` ; export France entière (2 541 feux, 90 départements en 2025, profil) ; historique 2006-2025 à exporter | **Partiel** : grille mondiale, comparaison possible, mais fichier pas encore téléchargé | **Complet** : `num_dep`, `niveau_j1` pour les 96 départements métropolitains, chaque jour des saisons 2024, 2025, 2026 (profil) | **Partiel** : la couche couvre la France, mais l'extraction est limitée au 77 pour l'instant | **Partiel** : `population` et `geometrie` pour les ratios ; couche département pour la France entière | **Partiel** : `Population totale SDIS`, `Montant en € par habitant` pour 97 départements ; la BSPP (75, 92, 93, 94) est absente | **Absent** | **Absent** : 77 seulement |

## 2. Sources de l'inventaire écartées

| Question | Interventions SDIS | Statistiques nationales des SDIS | Forêts publiques | PPFCI / PDPFCI | Stratégie nationale / moyens de lutte | Pyronear |
|---|---|---|---|---|---|---|
| Q1 | **Partiel** : `Feux de végétations` par SDIS et par an : grain trop large, végétation ≠ forêt | **Partiel** : `Effectif SPP-SPM`, `Effectif SPV-SPR` par département, 2024 seulement, en PDF | **Inconnu** : fiche, rubrique « Grain : Inconnu » | **Inconnu** : fiche, rubrique « Grain : Non vérifié » | **Partiel** : moyens décrits à l'échelle nationale, sans tableau par département | **Partiel** : `partner` = « SDIS 77 » et `camera` montrent l'existence de caméras de détection, sans inventaire des moyens |
| Q2 | **Absent** : grain annuel | **Absent** | **Inconnu** | **Inconnu** | **Inconnu** | **Absent** : images |
| Q3 | **Absent** : grain annuel | **Absent** | **Inconnu** | **Inconnu** | **Inconnu** | **Absent** : images |
| Q4 | **Partiel** : `Feux de végétations` comparable entre SDIS, mais végétation ≠ forêt | **Partiel** : effectifs comparables entre départements, 2024 seulement | **Inconnu** | **Inconnu** | **Inconnu** | **Absent** |

## 3. Questions sans source « complet » et décisions

Détail, raisons et coûts : `docs/journal-des-decisions.md`.

| Question | Ce qui manque | Décision | Journal |
|---|---|---|---|
| Q1 | La localisation des moyens (casernes, engins) et leur coût par type d'intervention | **Approximer** : « où » par BDIFF × BD Forêt × Admin Express ; « moyens » par l'OFGL (euros) | D07, D08 |
| Q2 | Assez de jours orange croisables avec des feux | **Approximer** : seuil cherché sur l'IFM 2006-2025, puis traduit en niveau avec la Météo des forêts 2024-2026 | D04 |
| Q2 | Les dates d'activation et le coût du dispositif actuel | **Renoncer** (données internes du SDIS, non publiques) : coût exprimé en nombre de jours d'activation | D02 |
| Q3 | Le seuil actuellement appliqué par le SDIS 77 | **Renoncer** à le connaître : on teste tous les seuils possibles | D15 |
| Q2, Q3 | Les feux de l'été 2026 | **Approximer** : étude de cas (Météo des forêts, arrêtés préfectoraux) | D05 |
| Q1, Q2, Q3 | Contenu réel de la table des arrêtés préfectoraux | **Collecter** : relevé manuel 2024-2026 | D09 |

**Cellules « inconnu » à vérifier d'abord :** Forêts publiques, PPFCI / PDPFCI de Seine-et-Marne, Stratégie nationale (D10).

## 4. Questions écartées

| Question écartée | Proposée dans | Raison | Journal |
|---|---|---|---|
| « Quels sont les niveaux d'indice disponibles ? » | Analyse de Sandrine (Q3) | Question de découverte des sources, pas de décision à la clé ; réponse : niveaux 1 à 4 de la Météo des forêts | D14 |
| « Où peut-on avoir les données sur les indices ? » | Analyse de Sandrine (Q4) | Question de découverte des sources ; réponse : archives data.gouv.fr et API Météo-France | D14 |
| « Quels sont les indicateurs de feux de forêt ? » | Analyse de Sandrine (Q1) | Reformulée et intégrée à Q1 et Q4 du groupe | D14 |
| « Quels sont les moyens mis en place ? » | Analyse de Sandrine (Q2) | Reformulée et intégrée à Q1 du groupe | D14 |
