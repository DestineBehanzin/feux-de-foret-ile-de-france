# Fiche d'identité – Indice Forêt Météo (IFM) – Fire danger indices historical data (Copernicus)

> Fiche rédigée le 20/11/2026. Les valeurs ont été vérifiées dans le fichier ou dans sa documentation ; sinon, la rubrique indique « non vérifiée » et la raison. Questions numérotées comme dans la spécification du groupe (Q1 : où concentrer les moyens · Q2 : quel seuil de la Météo des forêts · Q3 : le seuil actuel convient-il · Q4 : comment se situe le 77).

| Rubrique | Valeur |
|:---|:---|
| Propriétaire et système | Copernicus Emergency Management Service (CEMS), opéré par l'ECMWF ; jeu `cems-fire-historical-v1` sur l'Early Warning Data Store (EWDS) |
| Mode d'accès (export, API, téléchargement) et format | Téléchargement depuis <https://ewds.climate.copernicus.eu/datasets/cems-fire-historical-v1>, formats **NetCDF** ou **GRIB2**. Création d'un compte : **non vérifiée** (pas encore téléchargé) |
| Grain (une ligne = ?) | **Une valeur = une maille de la grille × un jour** (produit « Reanalysis », grille de 0,25°) |
| Emprise géographique | Monde ; extraction prévue : mailles couvrant la Seine-et-Marne et l'Île-de-France |
| Période réellement couverte par les données | Depuis 1940 jusqu'à aujourd'hui, quotidien (selon la description du jeu de données). Non vérifiée dans un fichier |
| Date de dernière mise à jour affichée sur la fiche | Non vérifiée : non relevée sur la page |
| Fréquence de mise à jour | Quotidienne, avec quelques jours de décalage (selon la documentation du catalogue) |
| Volumétrie | Non vérifiée : dépend de l'emprise et de la période extraites. 15 variables proposées, dont `Fire weather index` |
| Clés disponibles (sur quoi pourra-t-on joindre ?) | Temps et coordonnées (latitude, longitude) : jointure avec la BDIFF par **date** et par **maille contenant la commune** ; avec la Météo des forêts par date et département |
| Données personnelles | Aucune (données météorologiques sur grille) |
| Licence | CC-BY (selon la page du jeu de données) |
| Questions de votre analyse auxquelles elle pourrait répondre | **Q2** (chercher un seuil d'IFM sur 20 ans de feux), **Q3** (danger météo des feux de printemps, hors saison de la Météo des forêts) |

## Conclusion

Source **retenue, indispensable pour Q2** : la Météo des forêts n'a eu qu'un seul jour orange dans le 77 en 2024-2025, et la BDIFF n'a pas 2026. L'IFM permet de travailler sur 2006-2025.
- Variables utiles : `Fire weather index` ; en option `Fine fuel moisture code`.
- À vérifier au téléchargement : nom exact des variables, besoin d'un compte, volume des fichiers.
- Limite : maille d'environ 25 km, quelques mailles seulement pour le 77.
