"""
Profil des sources du projet (section 9 de la spécification) :
taux de remplissage des champs requis, bornes des dates, doublons,
entités présentes comparées au référentiel (Admin Express).

Entrée : un dossier contenant les fichiers bruts (noms ci-dessous).
Sortie : le profil au format Markdown, sur la sortie standard.

Utilisation : python scripts/qualite/profil_sources.py data/incoming > docs/qualite/profil-sources.md
"""

import sys
from pathlib import Path

import pandas as pd

D = Path(sys.argv[1] if len(sys.argv) > 1 else "data/incoming")
out = []


def p(line: str = "") -> None:
    out.append(line)


def pct(x: float) -> str:
    return f"{x * 100:.1f} %".replace(".", ",")


def remplissage(df: pd.DataFrame, cols: list[str]) -> None:
    p("| Champ requis | Lignes remplies | Taux de remplissage |")
    p("|---|---|---|")
    for c in cols:
        s = df[c].astype("string").str.strip()
        n = int((s.notna() & (s != "")).sum())
        p(f"| `{c}` | {n:,} / {len(df):,} |".replace(",", " ") + f" {pct(n / len(df))} |")
    p()


# Référentiel : communes d'Île-de-France (Admin Express)
communes = pd.read_csv(D / "communes_idf.csv", dtype=str)
communes77 = set(communes.loc[communes.code_insee_du_departement == "77", "code_insee"])

# ---------------------------------------------------------------- BDIFF
p("## BDIFF (`bdiff_2025.csv`)")
p()
b = pd.read_csv(D / "bdiff_2025.csv", sep=";", skiprows=2, dtype=str)
b77 = b[b["Département"] == "77"]
p(f"- Lignes : {len(b):,} (France) · {len(b77)} (Seine-et-Marne) · {b.shape[1]} colonnes".replace(",", " "))
dates = pd.to_datetime(b["Date de première alerte"], errors="coerce")
p(f"- Bornes de `Date de première alerte` : {dates.min():%d/%m/%Y %H:%M} → {dates.max():%d/%m/%Y %H:%M} ; dates illisibles : {int(dates.isna().sum())}")
p(f"- Doublons sur (`Département`, `Numéro`) : {int(b.duplicated(['Département', 'Numéro']).sum())}")
p(f"- Départements présents : {b['Département'].nunique()}")
inconnus = sorted(set(b77["Code INSEE"]) - communes77)
p(f"- Communes du 77 présentes : {b77['Code INSEE'].nunique()} sur {len(communes77)} du référentiel ; codes INSEE du 77 absents du référentiel : {len(inconnus)} {inconnus if inconnus else ''}")
p()
p("**France entière**")
p()
remplissage(b, ["Numéro", "Département", "Code INSEE", "Date de première alerte", "Surface parcourue (m2)", "Surface forêt (m2)", "Nature"])
p("**Seine-et-Marne**")
p()
remplissage(b77, ["Code INSEE", "Date de première alerte", "Surface parcourue (m2)", "Surface forêt (m2)", "Nature"])
p("Valeurs de `Précision des surfaces` (77) : " + ", ".join(f"{k} = {v}" for k, v in b77["Précision des surfaces"].fillna("(vide)").value_counts().items()))
p()
p("Valeurs de `Précision de la donnée` (France) : " + ", ".join(f"{k} = {v}" for k, v in b["Précision de la donnée"].fillna("(vide)").value_counts().items()))
p()

# ---------------------------------------------------------------- Météo des forêts
p("## Archives de la Météo des forêts (`mdf_2024.csv.gz`, `mdf_2025.csv.gz`, `mdf_2026.csv.gz`)")
p()
p("| Saison | Séparateur | Lignes | Départements | Première publication | Dernière publication | Jours du 77 | Jours du 77 manquants | Doublons (date, dép.) | Valeurs de `niveau_j1` hors 1-4 | Champs vides |")
p("|---|---|---|---|---|---|---|---|---|---|---|")
for y in (2024, 2025, 2026):
    f = D / f"mdf_{y}.csv.gz"
    sep = ";" if y >= 2026 else ","
    m = pd.read_csv(f, sep=sep, dtype=str)
    m["jour"] = m["date"].str[:10]
    m["num_dep"] = m["num_dep"].str.zfill(2)
    s77 = m[m.num_dep == "77"]
    attendus = pd.date_range(m.jour.min(), m.jour.max()).strftime("%Y-%m-%d")
    manquants = len(set(attendus) - set(s77.jour))
    hors = int((~m["niveau_j1"].isin(["1", "2", "3", "4"])).sum())
    vides = int(m[["date", "num_dep", "niveau_j1", "niveau_j2"]].isna().sum().sum())
    p(f"| {y} | `{sep}` | {len(m):,} | {m.num_dep.nunique()} | {m.jour.min()} | {m.jour.max()} | {len(s77)} | {manquants} | {int(m.duplicated(['jour', 'num_dep']).sum())} | {hors} | {vides} |".replace(",", " ").replace("` `", "`,`"))
p()

# ---------------------------------------------------------------- OFGL
p("## Comptes des SDIS (`ofgl-base-sdis.csv`)")
p()
o = pd.read_csv(D / "ofgl-base-sdis.csv", sep=";", dtype=str)
p(f"- Lignes : {len(o):,} · colonnes : {o.shape[1]} · exercices : {o['Exercice'].min()} → {o['Exercice'].max()}".replace(",", " "))
pp = o[o["CBUDG"] == "1"]
par_an = pp.groupby("Exercice")["Code Département"].nunique()
p(f"- Départements avec un budget principal, par exercice : de {par_an.min()} à {par_an.max()} (attendu : 97, soit 101 départements moins 75, 92, 93, 94)")
dup = int(pp.duplicated(["Exercice", "Code Département", "Agrégat"]).sum())
p(f"- Doublons sur (`Exercice`, `Code Département`, `Agrégat`) pour le budget principal : {dup}")
p()
remplissage(o, ["Exercice", "Code Département", "CBUDG", "Agrégat", "Montant", "Population totale SDIS"])

# ---------------------------------------------------------------- Calendrier
p("## Jours fériés (`jours_feries_metropole.csv`)")
p()
jf = pd.read_csv(D / "jours_feries_metropole.csv", dtype=str)
p(f"- Lignes : {len(jf)} · bornes : {jf.date.min()} → {jf.date.max()} · dates en double : {int(jf.date.duplicated().sum())} ({', '.join(jf.loc[jf.date.duplicated(keep=False), 'date'].unique())})")
p()
remplissage(jf, ["date", "nom_jour_ferie"])

p("## Vacances scolaires (`vacances_scolaires.csv`)")
p()
v = pd.read_csv(D / "vacances_scolaires.csv", dtype=str)
attendus = pd.date_range(v.date.min(), v.date.max()).strftime("%Y-%m-%d")
p(f"- Lignes : {len(v):,} · bornes : {v.date.min()} → {v.date.max()} · jours manquants : {len(set(attendus) - set(v.date))} · dates en double : {int(v.date.duplicated().sum())}".replace(",", " "))
p(f"- `nom_vacances` vide hors vacances (attendu) : {int(v.nom_vacances.isna().sum()):,} lignes ; `nom_vacances` vide un jour de vacances zone C : {int((v.vacances_zone_c.eq('True') & v.nom_vacances.isna()).sum())}".replace(",", " "))
p()
remplissage(v, ["date", "vacances_zone_c"])

# ---------------------------------------------------------------- Référentiels IGN
p("## Admin Express, communes d'Île-de-France (`communes_idf.csv`)")
p()
p(f"- Lignes : {len(communes):,} · codes INSEE en double : {int(communes.code_insee.duplicated().sum())}".replace(",", " "))
p("- Communes par département : " + ", ".join(f"{k} = {v}" for k, v in communes.code_insee_du_departement.value_counts().sort_index().items()))
p()
remplissage(communes, ["code_insee", "nom_officiel", "code_insee_du_departement", "population"])

p("## BD Forêt V2, surface forestière par commune du 77 (`surface_foret_par_commune_77.csv`)")
p()
sf = pd.read_csv(D / "surface_foret_par_commune_77.csv", dtype={"code_insee": str})
p(f"- Communes : {len(sf)} (référentiel : {len(communes77)}) · communes sans forêt : {int((sf.surface_foret_ha == 0).sum())} · surface forestière totale : {sf.surface_foret_ha.sum():,.0f} ha".replace(",", " "))
p(f"- Communes du référentiel absentes : {len(communes77 - set(sf.code_insee))}")
p()

print("\n".join(out))
