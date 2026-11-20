# Fiche d'identité – BD Forêt® V2

> Fiche rédigée le 20/11/2026. Les valeurs ont été vérifiées dans le fichier ou dans sa documentation ; sinon, la rubrique indique « non vérifiée » et la raison. Questions numérotées comme dans la spécification du groupe (Q1 : où concentrer les moyens · Q2 : quel seuil de la Météo des forêts · Q3 : le seuil actuel convient-il · Q4 : comment se situe le 77).

| Rubrique | Valeur |
|:---|:---|
| Propriétaire et système | IGN (Institut national de l'information géographique et forestière) |
| Mode d'accès (export, API, téléchargement) et format | Page data.gouv.fr <https://www.data.gouv.fr/datasets/bd-foret-r> : ses ressources sont des **liens vers le site de l'IGN** (aucun fichier direct). Accès retenu : **service WFS** de la Géoplateforme, sans compte (`https://data.geopf.fr/wfs/ows`, couche `LANDCOVER.FORESTINVENTORY.V2:formation_vegetale`), récupéré en GeoJSON et enregistré en GeoPackage |
| Grain (une ligne = ?) | **Une ligne = un polygone de végétation homogène** d'au moins 5 000 m² ; colonnes `id`, `code_tfv`, `tfv`, `tfv_g11`, `essence`, `geom` |
| Emprise géographique | France métropolitaine, par emprises départementales ; extraction : Seine-et-Marne |
| Période réellement couverte par les données | Élaborée entre 2007 et 2018 par photo-interprétation ; couverture affichée sur data.gouv.fr : 2006 → 2022. Millésime du 77 : non vérifié |
| Date de dernière mise à jour affichée sur la fiche | 20/11/2026 (métadonnées data.gouv.fr) |
| Fréquence de mise à jour | Irrégulière |
| Volumétrie | 77 : **13 194 polygones**, **151 101 ha de forêt** (hors landes et formations herbacées), 26 codes `code_tfv`, aucune valeur vide |
| Clés disponibles (sur quoi pourra-t-on joindre ?) | Géométrie : intersection avec les communes d'Admin Express, puis jointure par `code_insee` |
| Données personnelles | Aucune (occupation du sol) |
| Licence | Licence Ouverte / Open Licence v2.0 |
| Questions de votre analyse auxquelles elle pourrait répondre | **Q1** (feux pour 1 000 ha de forêt par commune), **Q3** (poids du massif de Fontainebleau), **Q4** (comparaison entre départements) |

## Conclusion

Source **retenue, indispensable** pour rapporter les feux à la forêt.
- Règle retenue : forêt = tous les `code_tfv` sauf ceux commençant par `LA` (lande, formation herbacée).
- Fichier dérivé : `surface_foret_par_commune_77.csv` (script `extraire_bdforet_77.py`).
- Limite : photographie ancienne, qui ne tient pas compte des incendies récents (Fontainebleau 2026).
