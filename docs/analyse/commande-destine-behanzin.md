---
updated: 2026-11-13T12:32:19.918+01:00
edited_seconds: 6
---
# Analyse de la commande - Prénom Nom

## 1. Les questions
Quatre questions dont la réponse aiderait la direction à trancher.

> [!test] Test
> Le test : si la réponse est X, la direction fait A ; si elle est Y, elle fait B. Si A et B sont identiques, ce n'est pas une question analytique pertinente.

1.Quels sont les moyens dont dispose le SDIS de Seine-et-marne pour lutter au mieux contre les départs de feu?
2.Ou sont concentrés ces moyens à ce jour?
3.Comment calcule-t-on l'indice?
4.Quelle est la marge de l'indice actuel?

## 2. Les termes inconnus

Les mots de la commande que vous ne savez pas définir précisément, ou qui peuvent se comprendre de plusieurs façons.

| Terme | Ce que je crois qu'il veut dire | Ce qu'il faudrait vérifier |
|---|---|---|
|météo des forets |c'est la prédiction de la température dans les forets| La définition|
|indice|valeur cible|son périmetre|
|dispositif renforcé|moyens mis en place pour éteindre le feu|ce qu'il en est réellement|
|feux de forets|les feux qui se déclenchent en foret|a partir de quoi un phénomène est considéré comme un feu de foret|
|départ de feu|la source d'un feu de foret||

## 3. Les besoins

La décision à éclairer, en une phrase :

Ce qui manque dans la commande pour y répondre (une information, une précision, une hypothèse à confirmer) :
-Les définitions des termes techniques.
-Les données
-Est ce que le seuil possède une marge?
 Si oui elle est de combien?


## 4. Les données

Pour chaque question, la donnée qu'il vous faudrait idéalement pour répondre.

| Question | Donnée idéale | Grain (une ligne = ?) | Période | Fraîcheur | Emprise géographique |
|---|---|---|---|---|---|
| 1 |Données des moyens | | 2026 ou les années précédentes| |Seine et marne, dans les autres départements autour et sur le territoire nationale  |
| 2 |Données des concentrations des moyens | |2026 ou les années précédentes | | Seine et marne, dans les autres départements autour et sur le territoire nationale|
| 3 |Calcul de l'indice | |2026 ou les années précédentes | |Seine et marne, dans les autres départements autour et sur le territoire nationale |
| 4 |Indice , et ses marges | |2026 ou les années précédentes | |Seine et marne, dans les autres départements autour et sur le territoire nationale |


Section 5
| Question | Source | Dégré | Décision|
|---|---|---|---|
|Q1: Quels sont les moyens dont dispose le SDIS de Seine-et-marne pour lutter au mieux contre les départs de feu?|Interventions SDIS|Partiel: Grace aux colonnes "Secours en piscines ou eaux intérieurs, Secours en mer, Secours a victime, Secours a personnes, Protectioon des biens, opérations diverses et Total Interventions", On connait toutes le nombre d'interventions des SDIS En Ile de france. Grace a toutes les autres clonnes on connait le nombre de départs de feux et leurs sources.|Collecter|
|Q1: Quels sont les moyens dont dispose le SDIS de Seine-et-marne pour lutter au mieux contre les départs de feu?|Les Plans de Protection des Forêts Contre les Incendies (PPFCI/PDPFCI)|Partiel: La période réellement couverte par les données étant de 10ans, elle permet de répondre aux moyens dont on dispose uniquement de 2024-2034|Collecter|
|Q2: Ou sont concentrés ces moyens à ce jour?|Interventions SDIS|Complet: Grace aux colonnes "Secours en piscines ou eaux intérieurs, Secours en mer, Secours a victime, Secours a personnes, Protection des biens, opérations diverses et Total Interventions", On connait toutes le nombre d'interventions des SDIS En Ile de france. Grace a toutes les autres clonnes on connait le nombre de départs de feux et leurs sources. Donc on peut direcetement savoir ou sont concnetrés les moyens|Collecter|
|Q2: Ou sont concentrés ces moyens à ce jour?|Les Plans de Protection des Forêts Contre les Incendies (PPFCI/PDPFCI)|Complet: On connait les différents moyens et on connait les endroit ou ils sotn concenctrés grace aux différentes poltiques. C'est un article dont les colonnes seront a etre crées et remplit plus tard|Collecter|
|Q3: Comment calcule-t-on l'indice?|Météo des forêts|Partiel: on connait les différents indices mais pas le moyen de calcul de ses indices.|Approximer|
|Q4: Quelle est la marge de l'indice actuel?|Météo des forêts|Inconnu|Renoncer|

## 5. Confrontation aux sources

### Matrice

| Question | Interventions SDIS | Météo des forêts | Les Plans de Protection des Forêts Contre les Incendies (PPFCI/PDPFCI)|
|---|---|---|---|---|
| 1 | Partiel: Grace aux colonnes "Secours en piscines ou eaux intérieurs, Secours en mer, Secours a victime, Secours a personnes, Protectioon des biens, opérations diverses et Total Interventions", On connait toutes le nombre d'interventions des SDIS En Ile de france. Grace a toutes les autres clonnes on connait le nombre de départs de feux et leurs sources.|Absent |Complet: La période réellement couverte par les données étant de 10ans, elle permet de répondre aux moyens dont on dispose uniquement de 2024-2034 |
| 2 |Complet: Grace aux colonnes "Secours en piscines ou eaux intérieurs, Secours en mer, Secours a victime, Secours a personnes, Protection des biens, opérations diverses et Total Interventions", On connait toutes le nombre d'interventions des SDIS En Ile de france. Grace a toutes les autres clonnes on connait le nombre de départs de feux et leurs sources. Donc on peut direcetement savoir ou sont concnetrés les moyens |Absent|Complet: On connait les différents moyens et on connait les endroit ou ils sotn concenctrés grace aux différentes poltiques. C'est un article dont les colonnes seront a etre crées et remplit plus tard|
| 3 |Absent|Partiel: Seuil présent mais la méthode de calcul y est pas expliqué |Absent |
| 4 |Absent|Inconnu |Absent|

### Écarts avec la section 4

Pour chaque question, comparez la donnée idéale (section 4) à la meilleure source disponible, critère par critère : écrivez « idéal → réel », ou « = » si les deux correspondent.

| Question | Meilleure source | Grain | Période | Fraîcheur | Emprise |
| -------- | ---------------- | ----- | ------- | --------- | ------- |
| 3        | Météo des forêts | Seuil de risque d'incendies | Jusqu'a 2026 |6 février 2026 |Ile-de-france|
| 4        | Météo des forêts | Seuil de risque d'incendies| Jusqu'a 2026 | 6 février 2026 |Ile-de-france|

### Décisions

| Question | Ce qui manque | Décision | Pourquoi | Ce que la décision coûte |
|---|---|---|---|---|
| Q3| Manque la méthode de calcul de l'indice | Collecter |Les seuils sont affichés directement |Ajuster la question|
|Q4|La marge de l'indice ne figure pas dans la base de données |Renoncer|Les seuils sont affichés directement|Ajuster la question|
