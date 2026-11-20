# Fiche d'identité – Archives de la Météo des forêts

> Fiche rédigée le 20/11/2026. Les valeurs ont été vérifiées dans le fichier ou dans sa documentation ; sinon, la rubrique indique « non vérifiée » et la raison. Questions numérotées comme dans la spécification du groupe (Q1 : où concentrer les moyens · Q2 : quel seuil de la Météo des forêts · Q3 : le seuil actuel convient-il · Q4 : comment se situe le 77).

| Rubrique | Valeur |
|:---|:---|
| Propriétaire et système | Météo-France |
| Mode d'accès (export, API, téléchargement) et format | Téléchargement direct sur <https://www.data.gouv.fr/datasets/archives-de-la-meteo-des-forets> : un fichier CSV compressé par saison (`mdf_2024.csv.gz`, `mdf_2025.csv.gz`, `mdf_2026.csv.gz`), plus une documentation (PDF, échantillons zip, GeoJSON des départements). Flux quotidien aussi disponible par l'API Météo des forêts (compte gratuit sur le portail Météo-France) |
| Grain (une ligne = ?) | **Une ligne = un département × un bulletin quotidien** : colonnes `date` (date et heure de publication), `num_dep`, `niveau_j1` (niveau du lendemain), `niveau_j2` (niveau du surlendemain), `dep_nom` (2024-2025) / `nom_dep` (2026) |
| Emprise géographique | France métropolitaine : 96 départements |
| Période réellement couverte par les données | Saisons seulement : 03/06/2024 → 30/09/2024 ; 03/06/2025 → 30/09/2025 ; 28/05/2026 → 05/10/2026 (lu dans les fichiers) |
| Date de dernière mise à jour affichée sur la fiche | 05/10/2026 (dernière mise à jour du jeu de données) |
| Fréquence de mise à jour | Quotidienne pendant la saison |
| Volumétrie | 2024 : 11 520 lignes · 2025 : 11 520 lignes · 2026 : 12 576 lignes. Seine-et-Marne : 120, 120 et 131 jours |
| Clés disponibles (sur quoi pourra-t-on joindre ?) | `num_dep` (département) et date cible (`date` + 1 jour pour `niveau_j1`). Jointure avec la BDIFF (`Département`, date de `Date de première alerte`), l'OFGL (`Code Département`) et le calendrier |
| Données personnelles | Aucune |
| Licence | Licence Ouverte / Open Licence v2.0 |
| Questions de votre analyse auxquelles elle pourrait répondre | **Q2** (niveau du jour de chaque feu, traduction du seuil d'IFM en niveau), **Q3** (feux par niveau vert, stabilité J+2 → J+1), **Q4** (nombre de jours orange par département) |

## Conclusion

Source **retenue, indispensable**.
- Niveaux annoncés pour le 77 : 2024 = 120 jours verts ; 2025 = 98 verts, 21 jaunes, 1 orange ; 2026 = 42 verts, 62 jaunes, 27 orange (dont le 12 juillet 2026).
- Pièges : `date` est la date de **publication** ; le format change en 2026 (séparateur `;`, `num_dep` sur 2 caractères, `nom_dep`).
- Limite : pas d'indice au printemps ni en automne, ni à l'intérieur du département.
