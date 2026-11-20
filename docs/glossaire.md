# Glossaire

> Projet : feux de forêt en Île-de-France (commande du SDIS 77, saison 2027)
> Version du 20/11/2026 · Contribution de Sandrine YAO au ticket #28
> Tout terme employé dans la spécification ou le rapport doit figurer ici.
> **Statut :** « vérifié » = définition reprise d'une source citée ; « choix du projet » = définition fixée par le groupe ; « à vérifier » = définition non confirmée.

## Feux et surfaces

| Terme | Définition | Source | Statut |
|---|---|---|---|
| Incendie de forêt | Incendie qui démarre en forêt, ou qui se propage en forêt ou au sein de terres boisées au cours de son évolution | `Définitions.pdf` (export BDIFF) | vérifié |
| Départ de feu | Un incendie enregistré dans la BDIFF, compté une fois, à la date de son alerte | Choix du projet | choix du projet |
| Date d'alerte | Date et heure où l'information d'un départ de feu parvient au CODIS ; colonne `Date de première alerte` | `Définitions.pdf` | vérifié |
| Surface parcourue | Surface totale parcourue par le feu, quelle que soit la végétation touchée ; colonne `Surface parcourue (m2)` | `Définitions.pdf` | vérifié |
| Surface de forêt (BDIFF) | Surface touchée située uniquement en forêt : milieu boisé avec un couvert arboré de plus de 10 %, d'un seul tenant de plus de 0,5 ha et large de plus de 20 m | `Définitions.pdf` | vérifié |
| Surfaces estimées / mesurées | Estimées : non issues de mesures. Mesurées : issues de mesures sur le terrain ou d'un SIG ; colonne `Précision des surfaces` | `Définitions.pdf` | vérifié |
| Nature (de l'incendie) | Origine de l'incendie, quand elle est connue : naturelle (foudre…), accidentelle (ligne électrique, échappement…), malveillance (volontaire), involontaire (travaux), involontaire (particulier) | `Définitions.pdf` | vérifié |
| Cause humaine | Toutes les natures sauf « naturelle » | Choix du projet | choix du projet |
| Forêt (BD Forêt) | Polygone de la BD Forêt V2 dont le `code_tfv` ne commence pas par `LA` (lande, formation herbacée) | Journal D07 | choix du projet |
| Massif de Fontainebleau | Ensemble des communes du 77 couvrant le massif ; liste exacte à fixer | — | à vérifier |
| Grand feu | Seuil de surface à partir duquel un feu est considéré comme grand | — | à vérifier |

## Indice de danger

| Terme | Définition | Source | Statut |
|---|---|---|---|
| IFM (Indice Forêt Météo) | Indice de danger météorologique de feu de forêt (en anglais *Fire Weather Index*), calculé à partir de la température, de l'humidité de l'air, du vent et des précipitations ; méthode canadienne | Météo-France ; Ressources naturelles Canada | vérifié |
| Seuil IFM 20 | Valeur de l'IFM au-delà de laquelle le risque de départ de feu est considéré comme réel | ORCAE (indicateurs risque feux de forêt) | vérifié |
| Météo des forêts | Niveau de danger de feu publié par Météo-France pour chaque département, à partir de l'IFM, du stress hydrique de la végétation, de l'occupation des sols et des zones sensibles | Communiqué Météo-France 2026 | vérifié |
| Niveau de danger | 1 = faible (vert), 2 = modéré (jaune), 3 = élevé (orange), 4 = très élevé (rouge) ; colonnes `niveau_j1`, `niveau_j2` | Archives de la Météo des forêts | vérifié |
| Niveau J+1 / J+2 | Niveau annoncé pour le lendemain / le surlendemain de la publication | Archives de la Météo des forêts | vérifié |
| Date de publication | Colonne `date` des archives : horodatage du bulletin, la veille vers 17 h | Fichiers `mdf_*.csv.gz` | vérifié |
| Date cible | Jour auquel s'applique un niveau : date de publication + 1 jour pour `niveau_j1` | Journal D16 | choix du projet |
| Saison de la Météo des forêts | Période de publication : 3 juin - 30 septembre en 2024 et 2025, 28 mai - 5 octobre en 2026 | Profil des sources | vérifié |
| Seuil de déclenchement | Niveau de la Météo des forêts à partir duquel le dispositif renforcé est activé | Commande | vérifié |
| Fausse alerte | Jour où le niveau est supérieur ou égal au seuil sans qu'aucun feu de forêt ne parte dans le département | Choix du projet | choix du projet |
| Feu non annoncé | Feu parti un jour où le niveau était inférieur au seuil, ou un jour sans niveau publié (hors saison) | Choix du projet | choix du projet |
| Jour d'activation | Jour où le niveau est supérieur ou égal au seuil testé ; unité de coût du dispositif (journal D02) | Choix du projet | choix du projet |

## Moyens et organisation

| Terme | Définition | Source | Statut |
|---|---|---|---|
| SDIS | Service départemental d'incendie et de secours | — | vérifié |
| SDIS 77 | Service départemental d'incendie et de secours de Seine-et-Marne ; commanditaire du projet | Commande | vérifié |
| BSPP | Brigade de sapeurs-pompiers de Paris : défend Paris et la petite couronne (75, 92, 93, 94) ; absente des comptes OFGL | Comptes des SDIS (OFGL) | vérifié |
| CODIS | Centre opérationnel départemental d'incendie et de secours, qui reçoit les alertes | `Définitions.pdf` (date d'alerte) | à vérifier |
| Dispositif renforcé | Moyens supplémentaires activés en période de danger (patrouilles, guet, etc.) | Commande | vérifié |
| CCF | Camion-citerne feux de forêt | AAFF, questions-réponses août 2026 | à vérifier |
| Catégorie de SDIS | Catégorie A, B ou C selon la population ; colonne `Catégorie population du SDIS` ; le SDIS 77 est en catégorie A | Comptes des SDIS (OFGL) | vérifié |
| Budget principal | Budget général du SDIS (`CBUDG` = `1`), par opposition aux budgets annexes (restauration, hébergement…) | Comptes des SDIS (OFGL) | vérifié |
| Agrégat | Regroupement comptable calculé par l'OFGL (exemple : « Frais de personnel ») ; colonne `Agrégat` | Méthodologie OFGL | vérifié |
| Arrêté préfectoral | Décision du préfet (fermeture de massif, interdiction du feu…), publiée au recueil des actes administratifs | Préfecture de Seine-et-Marne | vérifié |
| PDPFCI | Plan départemental de protection des forêts contre les incendies | Fiche PPFCI du groupe | à vérifier |

## Territoire et calendrier

| Terme | Définition | Source | Statut |
|---|---|---|---|
| Code INSEE | Code officiel à 5 caractères d'une commune (exemple : `77186` Fontainebleau) ; clé de jointure BDIFF × Admin Express | Admin Express | vérifié |
| Code département | Code à 2 caractères (`01`, `2A`, `77`) ; clé de jointure entre la BDIFF, la Météo des forêts et l'OFGL | Choix du projet (harmonisation) | choix du projet |
| Zone C | Zone de vacances scolaires qui comprend l'académie de Créteil, donc la Seine-et-Marne | Vacances scolaires par zones | vérifié |
| Jour de forte fréquentation | Samedi, dimanche, jour férié ou jour de vacances scolaires en zone C | Choix du projet | choix du projet |
| Lambert-93 | Système de coordonnées officiel de la France métropolitaine (EPSG:2154), utilisé pour calculer les surfaces | IGN | vérifié |
| WFS | Service web normalisé qui renvoie des objets géographiques (utilisé pour la BD Forêt et Admin Express) | IGN, Géoplateforme | vérifié |

## Vocabulaire de la donnée

| Terme | Définition | Source | Statut |
|---|---|---|---|
| Grain | Ce que représente une ligne d'une table (exemple : un feu, un département × un jour) | Cours | vérifié |
| Emprise | Territoire couvert par une source | Cours | vérifié |
| Fraîcheur | Délai entre un événement et sa disponibilité dans la source | Cours | vérifié |
| Millésime | Année de référence d'une donnée (exemple : population au 1er janvier 2023) | — | vérifié |
| Source de référence | Source qui fait foi quand une même donnée existe dans plusieurs sources (spécification, section 4) | Cours | vérifié |
| Taux de remplissage | Part des lignes où un champ n'est pas vide | Profil des sources | vérifié |
