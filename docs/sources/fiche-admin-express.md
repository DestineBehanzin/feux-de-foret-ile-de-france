# Fiche d'identité – Admin Express (IGN)

> Fiche rédigée le 20/11/2026. Les valeurs ont été vérifiées dans le fichier ou dans sa documentation ; sinon, la rubrique indique « non vérifiée » et la raison. Questions numérotées comme dans la spécification du groupe (Q1 : où concentrer les moyens · Q2 : quel seuil de la Météo des forêts · Q3 : le seuil actuel convient-il · Q4 : comment se situe le 77).

| Rubrique | Valeur |
|:---|:---|
| Propriétaire et système | IGN (Institut national de l'information géographique et forestière) |
| Mode d'accès (export, API, téléchargement) et format | Page data.gouv.fr <https://www.data.gouv.fr/datasets/admin-express/> : ses ressources sont des **liens vers le site de l'IGN** et des services cartographiques. Accès retenu : **service WFS** de la Géoplateforme, sans compte (couches `ADMINEXPRESS-COG.LATEST:commune` et `:departement`), récupéré en GeoJSON, enregistré en GeoPackage et en CSV |
| Grain (une ligne = ?) | **Une ligne = une commune** (couche commune) ; **une ligne = un département** (couche département) |
| Emprise géographique | France métropolitaine et départements d'outre-mer ; extraction : Île-de-France (communes), France (départements) |
| Période réellement couverte par les données | Éditions du 01/01/2017 au 15/11/2026 ; version utilisée : la dernière (`LATEST`). Population : recensement au 01/01/2023 (2022 pour quelques communes) |
| Date de dernière mise à jour affichée sur la fiche | 19/11/2026 (métadonnées data.gouv.fr) |
| Fréquence de mise à jour | Mensuelle |
| Volumétrie | **1 266 communes** en Île-de-France, dont **507 dans le 77** (1 468 108 habitants) ; **101 départements** ; aucune valeur vide sur les colonnes retenues |
| Clés disponibles (sur quoi pourra-t-on joindre ?) | `code_insee` (commune, jointure avec le `Code INSEE` de la BDIFF), `code_insee_du_departement` ; géométrie (jointure spatiale avec la BD Forêt) |
| Données personnelles | Aucune (données administratives ; la population est un total communal) |
| Licence | Licence Ouverte / Open Licence v2.0 |
| Questions de votre analyse auxquelles elle pourrait répondre | **Q1** (rattacher les feux aux communes, cartes), **Q3** (délimiter le massif de Fontainebleau), **Q4** (feux par habitant et par hectare) |

## Conclusion

Source **retenue, indispensable** : c'est le référentiel des communes et la clé de toutes les jointures.
- Colonnes utiles : `code_insee`, `nom_officiel`, `code_insee_du_departement`, `population`, `date_du_recensement`, `geometrie`.
- Contrôle : les 25 communes à feux du 77 en 2025 ont toutes un code reconnu.
- Point d'attention : des communes fusionnées depuis 2006 peuvent porter un ancien code INSEE dans la BDIFF.
