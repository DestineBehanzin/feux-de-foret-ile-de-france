
# Analyse de la commande - Fride Audrey MOBOU

## 1. Les questions

Quatre questions dont la réponse aiderait la direction à trancher.

> [!test] Test
> Le test : si la réponse est X, la direction fait A ; si elle est Y, elle fait B. Si A et B sont identiques, ce n'est pas une question analytique pertinente.

1. Quels sont les impacts des moyens utilisés par le SDIS pour lutter contre les feux de forets ?
2. Quelles sont les niveaux de la météo des forets ?
3. Quel est le seuil actuel de la météo des forets à partir duquel sont déclenchés tous les dispositifs ?
4. Qu'est ce qui influence l'indice qui permet de determiner l'appartion ou la non apparition d'un feu de foret ?

## 2. Les termes inconnus

Les mots de la commande que vous ne savez pas définir précisément, ou qui peuvent se comprendre de plusieurs façons.

| Terme | Ce que je crois qu'il veut dire | Ce qu'il faudrait vérifier |
|Météo de foret|Ensemble des temperatures de la foret |Ce que contient cette météo et comment interpreter les temperatures par rapport au risque de feu de foret|
|le seuil | le seuil à partir duquel on considère que le risque de feu de foret est important |Comment ce seuil est calculé et utilisé |
|Indice| L'indice qui résumé le niveau ||


## 3. Les besoins

La décision à éclairer, en une phrase :

Ce qui manque dans la commande pour y répondre (une information, une précision, une hypothèse à confirmer) : Il manque les détails sur les termes inconnus à savoir: la meteo de foret, le seuil, l'indice ainsi que ce qui les influence 


## 4. Les données

Pour chaque question, la donnée qu'il vous faudrait idéalement pour répondre.

| Question | Donnée idéale | Grain (une ligne = ?) | Période | Fraîcheur | Emprise géographique |
|---|---|---|---|---|---|
| 1 | Données des résultats du SDIS|2010-2025 |2026 | |Par département sur toute la métropole française |
| 2 | Données de la météo des forets |2010-2025 |2026 | |Par département sur toute la métropole française |
| 3 | Données de la météo des forets et données des dispositifs mis en place en fonction des indicateurs caractéristiques de cette météo et leurs résultats |2010-2025 |2026 | |Par département sur toute la métropole française |
| 4 |Données des feu de forets et des caractéristiques des forets |2010-2025 |2026 | |Par département sur toute la métropole française |

## 5. Confrontation aux sources

### Matrice

| Question | [BD Foret V2] | [Forets publiques] | [Statistqiues SDIS] | 
|---|---|---|---|---|
| 1 | Absent|Absent|Absent|complet mais inexploitable car on n'arrive à télécharger la source|

| 4 | complet |Inconnu car documentation indisponible |  Inconnu|

### Écarts avec la section 4

Pour chaque question, comparez la donnée idéale (section 4) à la meilleure source disponible, critère par critère : écrivez « idéal → réel », ou « = » si les deux correspondent.

| Question | Meilleure source | Grain | Période | Fraîcheur | Emprise |
| -------- | ---------------- | ----- | ------- | --------- | ------- |
| 1        |Statistiques SDIS |Inconnu|2012-2024|     2024  | Ile de France |

| 4        | BD Foret V2      |Polygone de formation végétale → évènement de feu recherché|2006-2019|   Variable selon département    | Ile de france |

### Décisions

| Question | Ce qui manque | Décision | Pourquoi | Ce que la décision coûte |
|---|---|---|---|---|
| 4| | Les données météorologiques (température, humidité, vitesse du vent, précipitations), les données historiques de feux ainsi que la méthode de calcul de l'indice de risque incendie. La DC_BDForet_2-0 fournit uniquement les caractéristiques de la végétation (essences, peuplements, couvert forestier) / Collecter / La DC_BDForet_2-0 apporte une partie importante des facteurs explicatifs du risque de feu grâce aux variables ESSENCE, TFV et TFV_G11, mais elle ne permet pas à elle seule d'expliquer ou de recalculer l'indice de risque. Pour répondre correctement à la question, il est nécessaire de croiser cette source avec les données de la météo des forêts de Météo-France et les données historiques de départs de feux | Temps supplémentaire de recherche et d'intégration des données externes, mise en place de traitements de croisement spatial entre les données météorologiques, les feux observés et les caractéristiques des forêts. Cela augmente la complexité du pipeline mais améliore fortement la qualité de l'analyse.| 