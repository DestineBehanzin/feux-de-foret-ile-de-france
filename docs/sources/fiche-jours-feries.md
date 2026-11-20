# Fiche d'identité – Jours fériés en France

> Fiche rédigée le 20/11/2026. Les valeurs ont été vérifiées dans le fichier ou dans sa documentation ; sinon, la rubrique indique « non vérifiée » et la raison. Questions numérotées comme dans la spécification du groupe (Q1 : où concentrer les moyens · Q2 : quel seuil de la Météo des forêts · Q3 : le seuil actuel convient-il · Q4 : comment se situe le 77).

| Rubrique | Valeur |
|:---|:---|
| Propriétaire et système | data.gouv.fr (Etalab) |
| Mode d'accès (export, API, téléchargement) et format | Téléchargement direct, sans compte : <https://etalab.github.io/jours-feries-france-data/csv/jours_feries_metropole.csv> (CSV, séparateur `,`, UTF-8) ; aussi en JSON, ICS, API (<https://calendrier.api.gouv.fr/jours-feries/>) et bibliothèque Python. Page : <https://www.data.gouv.fr/datasets/jours-feries-en-france> |
| Grain (une ligne = ?) | **Une ligne = un jour férié** : colonnes `date`, `annee`, `zone`, `nom_jour_ferie` |
| Emprise géographique | France métropolitaine (fichier « Métropole ») |
| Période réellement couverte par les données | Fichier CSV : **2006 → 2031** (vérifié) ; le producteur garde 20 ans de passé et 5 ans de futur. La période 1950-2050 affichée sur data.gouv.fr concerne la bibliothèque et l'API |
| Date de dernière mise à jour affichée sur la fiche | 13/10/2026 (fichier CSV) |
| Fréquence de mise à jour | Non renseignée ; la fenêtre glisse chaque année |
| Volumétrie | **286 lignes**, 11 jours fériés par an, aucune valeur vide ; 11 Ko |
| Clés disponibles (sur quoi pourra-t-on joindre ?) | `date` : jointure avec la date d'alerte de la BDIFF et la date cible de la Météo des forêts |
| Données personnelles | Aucune |
| Licence | Licence Ouverte / Open Licence v2.0 |
| Questions de votre analyse auxquelles elle pourrait répondre | **Q1** (moments de forte fréquentation), **Q2** (règle « niveau + week-end ou jour férié »), **Q3** (feux par indice vert un jour férié) |

## Conclusion

Source **retenue** (avec les vacances scolaires, elle forme la table calendrier).
- Doublon : le 01/05/2008 apparaît deux fois (1er mai et Ascension) ; dédoublonner avant la jointure.
- Archiver le fichier téléchargé : 2006 sortira de la fenêtre dans quelques années.
