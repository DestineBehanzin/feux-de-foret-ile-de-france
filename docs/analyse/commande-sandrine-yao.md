---
updated: 2026-11-13T12:32:19.918+01:00
edited_seconds: 6
---
# Analyse de la commande - Sandrine YAO

## 1. Les questions

Quatre questions dont la réponse aiderait la direction à trancher.

> [!test] Test
> Le test : si la réponse est X, la direction fait A ; si elle est Y, elle fait B. Si A et B sont identiques, ce n'est pas une question analytique pertinente.

1.Quels sont les indicateurs de feux de forêt?
2. Quels sont les moyens mis en place pour mieux lutter contre les départs de feu?
3. Quels sont les niveaux d'indice disponible? Il y a t-il des données disponibles?
4. Ou peut- on avoir les données sur les indices?

## 2. Les termes inconnus

Les mots de la commande que vous ne savez pas définir précisément, ou qui peuvent se comprendre de plusieurs façons.

| Terme | Ce que je crois qu'il veut dire | Ce qu'il faudrait vérifier |
|---|---|---|
| | | |

## 3. Les besoins

La décision à éclairer, en une phrase :

Ce qui manque dans la commande pour y répondre (une information, une précision, une hypothèse à confirmer) :
-

## 4. Les données

Pour chaque question, la donnée qu'il vous faudrait idéalement pour répondre.

| Question | Donnée idéale | Grain (une ligne = ?) | Période | Fraîcheur | Emprise géographique |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |

## 5. Confrontation aux sources

> Rédigée le 20/11/2026. Les sections 1 à 4 n'ont pas été modifiées.
> Sources : les 9 sources de l'inventaire du groupe (`docs/sources/inventaire.md`). Chaque degré cite la colonne du fichier ou la rubrique de la fiche qui le justifie.

### Matrice

| Question | BDIFF | Interventions SDIS | Météo des forêts | Statistiques nationales des SDIS | BD Forêt V2 | Forêts publiques | PPFCI / PDPFCI | Stratégie nationale / moyens de lutte | Pyronear |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **Partiel** : `Date de première alerte`, `Code INSEE`, `Surface parcourue (m2)`, `Surface forêt (m2)` et `Nature` donnent le nombre, les surfaces et les causes des feux, au grain du feu ; mais l'export s'arrête en 2025, l'été 2026 de la commande est absent | **Partiel** : `Feux de végétations` est un total par SDIS et par an (grain trop large), et la végétation inclut champs et broussailles | **Partiel** : `niveau_j1` est un niveau de danger (1 à 4), pas une mesure des feux survenus | **Absent** : les annexes par département (édition 2025, p. 68-69) ne contiennent que `Interventions` et les effectifs, aucune colonne sur les feux de forêt | **Partiel** : aucun feu, mais `code_tfv` et `geom` donnent la surface forestière (151 101 ha dans le 77) pour rapporter les feux à la forêt (donnée indirecte) | **Inconnu** : fiche du groupe, rubrique « Grain : Inconnu » | **Inconnu** : fiche du groupe, rubrique « Grain : Non vérifié » ; plan de la Seine-et-Marne non vérifié | **Inconnu** : ma fiche, rubriques « Grain » et « Volumétrie » à compléter | **Absent** : ma fiche, rubrique « Grain : une ligne = une image » ; images de fumée pour entraîner des modèles, pas des mesures de feux |
| 2 | **Absent** : aucune des 24 colonnes ne décrit des moyens (date, lieu, surfaces, cause, dégâts) | **Partiel** : `Total interventions`, `Incendies` mesurent l'activité du SDIS, pas ses moyens (donnée indirecte) | **Absent** : `date`, `num_dep`, `niveau_j1`, `niveau_j2` donnent seulement le niveau de danger | **Partiel** : `Effectif SPP-SPM` et `Effectif SPV-SPR` par département donnent les moyens humains pour 2024 ; ni engins, ni casernes, ni dispositif feux de forêt | **Absent** : `code_tfv`, `tfv`, `tfv_g11`, `essence`, `geom` décrivent la végétation | **Inconnu** : fiche du groupe, rubrique « Grain : Inconnu » | **Inconnu** : fiche du groupe, rubrique « Mode d'accès : Documents, Article » ; plan de la Seine-et-Marne non vérifié | **Partiel** : ma fiche, rubrique « Mode d'accès : page web » ; moyens décrits à l'échelle nationale, sans tableau par département | **Partiel** : ma fiche, rubrique « Clés disponibles » ; `partner` (« SDIS 77 ») et `camera` montrent que le SDIS 77 a des caméras de détection Pyronear, sans inventaire des moyens |
| 3 | **Absent** : aucune colonne d'indice | **Absent** : aucune colonne d'indice | **Complet** : `niveau_j1` et `niveau_j2` valent 1 à 4 (lu dans `mdf_2024`, `mdf_2025`, `mdf_2026`) ; `num_dep` = `77` présent chaque jour de saison ; `date` du 03/06/2024 au 05/10/2026 | **Absent** : aucune colonne d'indice dans les annexes par département | **Absent** : aucune colonne d'indice | **Inconnu** : fiche du groupe, rubrique « Grain : Inconnu » | **Inconnu** : le plan peut citer l'indice sans fournir de données ; non vérifié | **Inconnu** : non vérifié | **Absent** : images, pas d'indice |
| 4 | **Absent** : ne diffuse pas l'indice | **Absent** : ne diffuse pas l'indice | **Complet** : archives data.gouv.fr (`mdf_2024.csv.gz`, `mdf_2025.csv.gz`, `mdf_2026.csv.gz`) et API Météo-France (fiche du groupe, rubrique « Mode d'accès : API gratuite ») | **Absent** : ne diffuse pas l'indice | **Absent** : ne diffuse pas l'indice | **Absent** : ne diffuse pas l'indice | **Absent** : ne diffuse pas l'indice | **Absent** : ne diffuse pas l'indice | **Absent** : ne diffuse pas l'indice |

### Écarts avec la section 4

Pour chaque question, comparez la donnée idéale (section 4) à la meilleure source disponible, critère par critère : écrivez « idéal → réel », ou « = » si les deux correspondent.

Ma section 4 n'a pas été remplie avant l'exploration des sources : c'est le premier écart. J'écris donc « non défini → réel ».

| Question | Meilleure source | Grain | Période | Fraîcheur | Emprise |
| -------- | ---------------- | ----- | ------- | --------- | ------- |
| 1        | BDIFF | non défini → un feu de forêt (commune, date et heure d'alerte) | non défini → jusqu'en 2025 | non défini → annuelle (dernière mise à jour affichée : 01/12/2025) | non défini → France, filtrable sur le 77 (`Département`, `Code INSEE`) |
| 2        | Statistiques nationales des SDIS | non défini → un département | non défini → 2024 (édition 2025) | non défini → annuelle | non défini → France, par département |
| 3        | Météo des forêts | non défini → un département × un jour | non défini → saisons 2024, 2025 et 2026 | non défini → quotidienne, publiée la veille vers 17 h | non défini → France métropolitaine, par département |
| 4        | Météo des forêts | non défini → un département × un jour | non défini → depuis le 03/06/2024 | non défini → quotidienne | non défini → France métropolitaine |

### Décisions

Q1 et Q2 n'ont aucune source « complet ». Les cellules « inconnu » (Forêts publiques, PPFCI, Stratégie nationale) appellent d'abord une vérification.

| Question | Ce qui manque | Décision | Pourquoi | Ce que la décision coûte |
|---|---|---|---|---|
| Q1 | Les feux de l'été 2026 (la BDIFF s'arrête en 2025) | approximer | La BDIFF est complète de 2006 à 2025 au grain du feu. 2026 est traité comme une étude de cas : Météo des forêts (orange pour le 77 du 8 au 13 juillet 2026) et arrêtés préfectoraux | Aucune statistique de feux pour 2026 : impossible de dire si 2026 a compté plus ou moins de départs de feu |
| Q1 | Rapporter les feux à la surface de forêt | collecter | La BD Forêt V2 donne la surface forestière par commune (jointure par `code_insee` via Admin Express) | Une source et une jointure spatiale de plus |
| Q2 | Les moyens financiers du SDIS 77 | collecter | Source publique hors inventaire : Comptes des SDIS (OFGL), colonnes `Agrégat` et `Montant` | Une source de plus à ajouter à l'inventaire |
| Q2 | Les mesures prises pendant les périodes de danger | collecter | Les arrêtés préfectoraux du 77 sont publics ; on les relève dans une table (date, zone, mesure) | Relevé manuel, sans garantie d'exhaustivité |
| Q2 | Engins, casernes, dates d'activation et coût du dispositif renforcé | renoncer (au détail) | Données non publiques ; la règle du projet interdit de les demander. On garde effectifs (Statistiques des SDIS) et dépenses (OFGL) | Les moyens ne seront exprimés qu'en effectifs et en euros |
| Q2, Q3 | Contenu réel de Forêts publiques, du PDPFCI du 77 et de la Stratégie nationale | vérifier d'abord | Les fiches indiquent « Grain : Inconnu » ou « Non vérifié » | Temps de vérification ; écartées si rien d'exploitable |

### Ce que la confrontation m'apprend

- Mes questions 3 et 4 sont couvertes par la Météo des forêts, mais elles ne passent pas le test de la section 1 : savoir quels niveaux existent et où trouver les données ne fait pas trancher la direction. Ce sont des questions de découverte des sources.
- Mes questions 1 et 2 portent sur la bonne matière (les feux, les moyens) mais doivent être reformulées pour mener à une décision, comme « où concentrer les moyens » ou « à partir de quel niveau déclencher le dispositif ». Je propose de les fusionner dans les questions du groupe.
- Ma fiche Pyronear indiquait « Grain : Pays » : c'était inexact. Je l'ai corrigée (une ligne = une image), et la vérification a montré que le SDIS 77 est partenaire de Pyronear.
