# Fiche d'identité – Arrêtés préfectoraux de Seine-et-Marne (risque incendie)

> Fiche rédigée le 20/11/2026. Les valeurs ont été vérifiées dans le fichier ou dans sa documentation ; sinon, la rubrique indique « non vérifiée » et la raison. Questions numérotées comme dans la spécification du groupe (Q1 : où concentrer les moyens · Q2 : quel seuil de la Météo des forêts · Q3 : le seuil actuel convient-il · Q4 : comment se situe le 77).

| Rubrique | Valeur |
|:---|:---|
| Propriétaire et système | Préfecture de Seine-et-Marne (cabinet du préfet, SIDPC) ; publication au recueil des actes administratifs |
| Mode d'accès (export, API, téléchargement) et format | Pages web de la préfecture (<https://www.seine-et-marne.gouv.fr/Actualites/Incendies-points-de-situation-et-arretes-prefectoraux>) avec des arrêtés en **PDF**. Exemple vérifié : arrêté du 21/08/2026 n° 2026/CAB/SIDPC/1349 (interdiction d'accès à des secteurs de Fontainebleau et des Trois Pignons). **Pas de fichier de données** : table à construire à la main |
| Grain (une ligne = ?) | **Une ligne = un arrêté** (à construire : `id_arrete`, `date_signature`, `date_debut`, `date_fin`, `perimetre`, `type_mesure`, `plage_horaire`, `url_source`) |
| Emprise géographique | Seine-et-Marne (communes ou massifs cités dans chaque arrêté) |
| Période réellement couverte par les données | Non vérifiée : liste complète des arrêtés 2024-2026 non encore relevée (la page de la préfecture n'a pas pu être ouverte depuis notre outil) |
| Date de dernière mise à jour affichée sur la fiche | Non vérifiée : même raison |
| Fréquence de mise à jour | Ponctuelle : un arrêté à chaque mesure |
| Volumétrie | Non vérifiée : nombre d'arrêtés à établir lors du relevé |
| Clés disponibles (sur quoi pourra-t-on joindre ?) | Dates d'application (jointure par jour avec la Météo des forêts et la BDIFF) ; périmètre (communes, via Admin Express) |
| Données personnelles | Non vérifiée : à contrôler arrêté par arrêté (un arrêté peut nommer des personnes ou des entreprises ; on ne garderait que dates, zones et mesures) |
| Licence | Non vérifiée : documents administratifs publics, licence de réutilisation non indiquée |
| Questions de votre analyse auxquelles elle pourrait répondre | **Q2** (ce qui a été déclenché, face au niveau du jour), **Q3** (étude de cas de l'été 2026 : 27 jours orange) |

## Conclusion

Source **retenue, à collecter** : c'est la seule trace publique de ce qui a été déclenché.
- Relevé manuel : sans garantie d'exhaustivité.
- Étape suivante : lister les arrêtés 2024-2026 sur le site de la préfecture et dans le recueil des actes administratifs, puis compléter les rubriques « non vérifiée ».
