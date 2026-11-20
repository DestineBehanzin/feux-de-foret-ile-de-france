# Fiche d'identité – Images de départs de feux, Pyro-SDIS (Pyronear)

> Fiche corrigée le 20/11/2026 après vérification de la page data.gouv.fr et de la fiche du jeu de données sur Hugging Face.

| Rubrique | Valeur |
|:---|:---|
| Propriétaire et système | Association **Pyronear**, avec les SDIS partenaires (Force 06, SDIS 07, SDIS 12, **SDIS 77**). Les images viennent des caméras Pyronear installées avec ces SDIS, et ont été annotées par les bénévoles de l'association |
| Mode d'accès (export, API, téléchargement) et format | Page data.gouv.fr : <https://www.data.gouv.fr/datasets/679123b6ef0f97629ae0d5e1> (« Images de départs de feux - SDIS - 2024 »). Sa seule ressource renvoie vers Hugging Face : <https://huggingface.co/datasets/pyronear/pyro-sdis>. Téléchargement de **fichiers Parquet** (3 pour l'entraînement, 1 pour la validation) ou chargement avec la bibliothèque Python `datasets`. Annotations au format YOLO |
| Grain (une ligne = ?) | **Une ligne = une image** issue d'une caméra, avec ses annotations de fumée (cadres au format YOLO) et ses métadonnées : `partner`, `camera`, `date`, `image_name` |
| Emprise géographique | Départements des SDIS partenaires : au moins 06, 07, 12 et 77 (zones déclarées sur data.gouv.fr). La version 2.0 annonce de nouveaux partenaires, non listés. Aucune coordonnée ni commune dans les métadonnées |
| Période réellement couverte par les données | Page data.gouv.fr : 01/01/2024 → 31/12/2024 (version 1.0). Version actuelle sur Hugging Face (v2.0) : images de **2023 à 2025** |
| Date de dernière mise à jour affichée sur la fiche | data.gouv.fr : 19/11/2026 · Hugging Face : 23/09/2026 |
| Fréquence de mise à jour | Ponctuelle (data.gouv.fr) ; publication par versions (v1.0 en 2024, v2.0 en 2026) |
| Volumétrie | Version 2.0 : **12 378 images** (11 249 pour l'entraînement, 1 129 pour la validation), dont 10 744 avec de la fumée et 1 634 fausses alertes du système Pyronear ; environ **1,3 Go** à télécharger. Version 1.0 : 33 636 images |
| Clés disponibles (sur quoi pourra-t-on joindre ?) | `partner` (exemple : « SDIS 77 ») et `date` (format `AAAA-MM-JJTHH-MM-SS`). Pas de code commune ni de coordonnées : **aucune jointure possible avec la BDIFF** au grain de la commune ; au mieux département + jour |
| Données personnelles | **Non vérifiée** : les images n'ont pas été ouvertes. Ce sont des vues de paysage prises par des caméras de surveillance ; la présence éventuelle de personnes ou de véhicules identifiables n'a pas été contrôlée |
| Licence | **Divergence entre les deux pages** : Licence Ouverte 2.0 sur data.gouv.fr, Apache-2.0 sur Hugging Face. À clarifier avant toute réutilisation |
| Questions de votre analyse auxquelles elle pourrait répondre | **Aucune directement.** Le jeu sert à entraîner des modèles de détection de fumée. Il montre seulement que le SDIS 77 dispose de caméras de détection Pyronear (`partner`, `camera`), ce qui touche marginalement la question des moyens mis en place |

## Conclusion

Source **non retenue** pour le projet :
- elle contient des **images**, pas des mesures de feux ni d'indice ;
- elle ne se joint pas aux autres sources au grain de la commune ;
- son volume (environ 1,3 Go d'images) est disproportionné pour ce qu'elle apporterait à nos questions.

Piste éventuelle, hors socle : compter les caméras du SDIS 77 à partir des métadonnées `partner` et `camera`, comme indicateur d'existence d'un moyen de détection.

## Correction par rapport à la version précédente

| Rubrique | Avant | Après | Raison |
|---|---|---|---|
| Grain | Pays | Une image | Vérifié dans la fiche Hugging Face (champs `image`, `annotations`, `partner`, `camera`, `date`) |
| Emprise | Communes et département | Départements 06, 07, 12, 77 (au moins) | Zones déclarées sur data.gouv.fr ; pas de commune dans les métadonnées |
| Période | 2026 | 2024 (data.gouv.fr) ; 2023-2025 (v2.0) | 2026 était la date de mise à jour, pas la période couverte |
| Volumétrie | À compléter | 12 378 images, environ 1,3 Go | Fiche Hugging Face |
| Licence | Licence Ouverte 2.0 | Divergence Licence Ouverte 2.0 / Apache-2.0 | Les deux pages ne disent pas la même chose |
