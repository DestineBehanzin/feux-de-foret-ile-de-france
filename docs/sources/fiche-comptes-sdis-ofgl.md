# Fiche d'identité – Comptes des SDIS 2012-2025 (OFGL)

> Fiche rédigée le 20/11/2026. Les valeurs ont été vérifiées dans le fichier ou dans sa documentation ; sinon, la rubrique indique « non vérifiée » et la raison. Questions numérotées comme dans la spécification du groupe (Q1 : où concentrer les moyens · Q2 : quel seuil de la Météo des forêts · Q3 : le seuil actuel convient-il · Q4 : comment se situe le 77).

| Rubrique | Valeur |
|:---|:---|
| Propriétaire et système | OFGL (Observatoire des Finances et de la Gestion publique Locales), à partir des balances comptables des SDIS publiées par la DGFiP |
| Mode d'accès (export, API, téléchargement) et format | Téléchargement direct, sans compte : CSV (<https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/ofgl-base-sdis/exports/csv?use_labels=true>) ou JSON ; page <https://www.data.gouv.fr/datasets/comptes-des-sdis-2012-2025>. CSV séparateur `;`, UTF-8 |
| Grain (une ligne = ?) | **Une ligne = un budget de SDIS × un exercice × un agrégat financier** (format long) |
| Emprise géographique | 97 départements : métropole sans le 75, 92, 93 et 94 (BSPP), et outre-mer (971, 972, 973, 974, 976) |
| Période réellement couverte par les données | **2012 → 2025** (vérifié dans le fichier). La couverture affichée sur data.gouv.fr (2012-2023) n'est pas à jour |
| Date de dernière mise à jour affichée sur la fiche | 13/08/2026 |
| Fréquence de mise à jour | Non renseignée par le producteur |
| Volumétrie | **84 420 lignes**, 21 colonnes, 63 agrégats, 14 exercices ; budget principal (`CBUDG` = `1`) présent pour les 97 départements chaque année ; aucune valeur vide |
| Clés disponibles (sur quoi pourra-t-on joindre ?) | `Code Département` + `Exercice` : jointure avec la BDIFF, la Météo des forêts et Admin Express |
| Données personnelles | Aucune (comptes d'établissements publics) |
| Licence | Licence Ouverte / Open Licence v2.0 |
| Questions de votre analyse auxquelles elle pourrait répondre | **Q1** (moyens financiers : `Frais de personnel`, `Dépenses d'équipement - véhicules`, `Epargne nette`…), **Q4** (comparaison avec les SDIS de même catégorie ; population pour les ratios) |

## Conclusion

Source **retenue** : seule source publique sur les moyens financiers.
- Transformation : filtrer `CBUDG` = `1`, garder 8 agrégats, pivoter.
- Profil du SDIS 77 : catégorie A, non rural.
- Limites : pas de coût par type d'intervention ; trois colonnes figées sur 2025 à écarter ; BSPP absente.
