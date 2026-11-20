# Fiche d'identité – Vacances scolaires par zones

> Fiche rédigée le 20/11/2026. Les valeurs ont été vérifiées dans le fichier ou dans sa documentation ; sinon, la rubrique indique « non vérifiée » et la raison. Questions numérotées comme dans la spécification du groupe (Q1 : où concentrer les moyens · Q2 : quel seuil de la Météo des forêts · Q3 : le seuil actuel convient-il · Q4 : comment se situe le 77).

| Rubrique | Valeur |
|:---|:---|
| Propriétaire et système | Antoine Augusti (producteur individuel), d'après le calendrier scolaire officiel ; dépôt GitHub <https://github.com/AntoineAugusti/vacances-scolaires> |
| Mode d'accès (export, API, téléchargement) et format | Téléchargement direct, sans compte : <https://raw.githubusercontent.com/AntoineAugusti/vacances-scolaires/master/data.csv> (CSV, séparateur `,`, UTF-8). Page : <https://www.data.gouv.fr/datasets/5aeb1610c751df5402613fae> |
| Grain (une ligne = ?) | **Une ligne = un jour** : colonnes `date`, `vacances_zone_a`, `vacances_zone_b`, `vacances_zone_c` (booléens), `nom_vacances` |
| Emprise géographique | France, par zone A, B et C. Le 77 dépend de l'académie de Créteil, en **zone C** |
| Période réellement couverte par les données | **01/01/1990 → 31/12/2028** (vérifié dans le fichier) ; la couverture affichée sur data.gouv.fr va jusqu'en 2030 |
| Date de dernière mise à jour affichée sur la fiche | 23/09/2026 (fichier CSV) |
| Fréquence de mise à jour | Annuelle |
| Volumétrie | **14 245 lignes** (une par jour, sans doublon), 5 colonnes ; `nom_vacances` vide les jours hors vacances (8 514 lignes), ce qui est normal ; 6 types de vacances, dont « Pont de l'Ascension » |
| Clés disponibles (sur quoi pourra-t-on joindre ?) | `date` : jointure avec la BDIFF et la Météo des forêts |
| Données personnelles | Aucune |
| Licence | Licence Ouverte v1.0 (code data.gouv.fr : `fr-lo`) |
| Questions de votre analyse auxquelles elle pourrait répondre | **Q1** (moments de forte fréquentation), **Q2** (règle de déclenchement combinée), **Q3** (feux par indice vert pendant les vacances) |

## Conclusion

Source **retenue**.
- Colonnes utiles : `date`, `vacances_zone_c`, `nom_vacances`.
- Exemple 2025, zone C : vacances de printemps du 12/04 au 27/04, vacances d'été du 05/07 au 31/08.
- Limite : producteur individuel, pas un service de l'État ; à recouper avec le calendrier officiel en cas de doute.
