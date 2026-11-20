# Fiche d'identité – BDIFF (Base de données sur les incendies de forêt)

> Fiche rédigée le 20/11/2026. Les valeurs ont été vérifiées dans le fichier ou dans sa documentation ; sinon, la rubrique indique « non vérifiée » et la raison. Questions numérotées comme dans la spécification du groupe (Q1 : où concentrer les moyens · Q2 : quel seuil de la Météo des forêts · Q3 : le seuil actuel convient-il · Q4 : comment se situe le 77).

| Rubrique | Valeur |
|:---|:---|
| Propriétaire et système | Ministère de l'Agriculture / IGN ; application web BDIFF de recherche et de consultation des incendies de forêt : <https://bdiff.agriculture.gouv.fr/> |
| Mode d'accès (export, API, téléchargement) et format | **Export** depuis l'application (onglet de recherche, puis export « Incendies »), sans compte. Archive zip contenant `Incendies.csv` (séparateur `;`, UTF-8, **2 lignes d'en-tête** à ignorer : nombre d'incendies et critères de sélection, puis 24 colonnes), `Définitions.pdf` et `Mention légales.pdf` |
| Grain (une ligne = ?) | **Une ligne = un incendie de forêt** (critère d'export « Type de feu : F ») |
| Emprise géographique | France entière (90 départements présents dans l'export 2025), filtrable par `Département` et par commune (`Code INSEE`) |
| Période réellement couverte par les données | Export vérifié : 01/01/2025 → 31/12/2025. Selon l'application, données depuis 2006 ; **pas de données 2026**. Années 2006-2024 : non vérifiées (export à refaire) |
| Date de dernière mise à jour affichée sur la fiche | 01/12/2025 |
| Fréquence de mise à jour | Annuelle |
| Volumétrie | Export 2025 : **2 541 incendies**, 24 colonnes, 1 660 communes ; Seine-et-Marne : **55 incendies** |
| Clés disponibles (sur quoi pourra-t-on joindre ?) | `Code INSEE` (commune), `Département`, `Date de première alerte` (date et heure, à la minute), `Numéro` (identifiant de l'incendie) |
| Données personnelles | Aucune : localisation à la commune, pas de nom ni d'adresse. Les mentions RGPD du site concernent les comptes utilisateurs, pas les données |
| Licence | Conditions de réutilisation fixées dans `Mention légales.pdf` (citation de la source, pas de modification des données ni de vente) ; ce n'est pas une Licence Ouverte |
| Questions de votre analyse auxquelles elle pourrait répondre | **Q1** (où, quand, pourquoi : `Code INSEE`, `Date de première alerte`, `Nature`), **Q2** et **Q3** (croisement avec la Météo des forêts et l'IFM), **Q4** (comparaison entre départements) |

## Conclusion

Source **retenue, indispensable** : c'est la seule source publique qui décrit chaque feu de forêt.
- Colonnes utiles : `Numéro`, `Année`, `Département`, `Code INSEE`, `Nom de la commune`, `Date de première alerte`, `Surface parcourue (m2)`, `Surface forêt (m2)`, `Nature`, `Précision des surfaces`, `Précision de la donnée`.
- Limites : s'arrête en 2025 ; cause (`Nature`) vide pour 55 % des feux du 77 en 2025 ; surfaces estimées (pas mesurées) dans le 77 ; surfaces en m².
