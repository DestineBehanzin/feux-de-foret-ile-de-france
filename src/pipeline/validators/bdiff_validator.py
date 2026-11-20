import re
import unicodedata
from datetime import datetime

MEDITERRANEAN_DEPARTMENTS = {"04", "05", "06", "07", "11", "13", "2A", "2B", "26", "30", "34", "48", "66", "83", "84"}
NATURE_VALUES = {"naturelle", "accidentelle", "malveillance", "involontaire travaux", "involontaire particulier"}


def _norm(value):
    text = "" if value is None else str(value).strip().lower()
    text = "".join(c for c in unicodedata.normalize("NFKD", text) if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", " ", text).strip()


def _value_by_position(payload: dict, position: int):
    values = [v for k, v in payload.items() if k != "_extra_columns"]
    return values[position - 1] if 0 < position <= len(values) else ""


def validate_bdiff(payload: dict, expected_column_count=26, required_positions=None) -> list[str]:
    errors = []
    values = [v for k, v in payload.items() if k != "_extra_columns"]
    if expected_column_count and len(values) != int(expected_column_count):
        errors.append(f"nombre de colonnes attendu={expected_column_count}, obtenu={len(values)}")
    for position in required_positions or []:
        if not str(_value_by_position(payload, int(position))).strip():
            errors.append(f"colonne obligatoire vide a la position {position}")

    year = str(_value_by_position(payload, 1)).strip()
    if year and (not year.isdigit() or not 1900 <= int(year) <= 2100):
        errors.append(f"annee invalide: {year}")

    department = str(_value_by_position(payload, 3)).strip().upper()
    if department and not re.fullmatch(r"(?:0[1-9]|[1-8][0-9]|9[0-5]|97[1-6]|2A|2B)", department):
        errors.append(f"departement invalide: {department}")

    insee = str(_value_by_position(payload, 4)).strip().upper()
    if insee and not re.fullmatch(r"(?:\d{5}|2[AB]\d{3})", insee):
        errors.append(f"code INSEE invalide: {insee}")

    alert_date = str(_value_by_position(payload, 6)).strip()

    if alert_date:
        accepted_formats = (
            "%Y-%m-%d %H:%M:%S",
            "%Y-%m-%d %H:%M",
            "%d/%m/%Y %H:%M:%S",
            "%d/%m/%Y %H:%M",
        )

        valid_date = False

        for date_format in accepted_formats:
            try:
                datetime.strptime(alert_date, date_format)
                valid_date = True
                break
            except ValueError:
                continue

        if not valid_date:
            errors.append(
                f"date de premiere alerte invalide: {alert_date}"
            )

    for position in range(7, 17):
        value = str(_value_by_position(payload, position)).strip()
        if value:
            try:
                if float(value.replace(" ", "").replace(",", ".")) < 0:
                    errors.append(f"surface negative a la position {position}")
            except ValueError:
                errors.append(f"surface non numerique a la position {position}: {value}")

    nature = _norm(_value_by_position(payload, 19))
    if nature and nature not in NATURE_VALUES:
        errors.append(f"nature inconnue: {_value_by_position(payload, 19)}")

    for position in (21, 22, 23):
        value = str(_value_by_position(payload, position)).strip()
        if value:
            try:
                n = float(value.replace(",", "."))
                if n < 0 or not n.is_integer():
                    errors.append(f"compteur invalide a la position {position}: {value}")
            except ValueError:
                errors.append(f"compteur non numerique a la position {position}: {value}")
    return errors
