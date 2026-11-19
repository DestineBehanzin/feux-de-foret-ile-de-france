import csv
import hashlib
import json
from pathlib import Path


def _open_with_fallback(path: Path, encodings: list[str]):
    last_error = None
    for encoding in dict.fromkeys(encodings):
        try:
            stream = path.open("r", encoding=encoding, newline="")
            stream.read(4096)
            stream.seek(0)
            return stream, encoding
        except UnicodeDecodeError as exc:
            last_error = exc
            try:
                stream.close()
            except UnboundLocalError:
                pass
    raise ValueError(f"Encodage illisible pour {path.name}: {last_error}")


def _unique_headers(values: list[str]) -> list[str]:
    headers, seen = [], {}
    for index, value in enumerate(values, start=1):
        base = (value or "").strip().lstrip("\ufeff") or f"colonne_{index}"
        seen[base] = seen.get(base, 0) + 1
        headers.append(base if seen[base] == 1 else f"{base}_{seen[base]}")
    return headers


def iter_csv_rows(path: Path, delimiter=";", encoding="utf-8-sig",
                  fallback_encodings=None, header_row=1, skip_blank_rows=True):
    encodings = [encoding] + list(fallback_encodings or [])
    stream, selected_encoding = _open_with_fallback(path, encodings)
    try:
        reader = csv.reader(stream, delimiter=delimiter)
        for _ in range(int(header_row) - 1):
            next(reader, None)
        raw_headers = next(reader, None)
        if not raw_headers:
            raise ValueError(f"Aucun en-tete trouve a la ligne {header_row}.")
        headers = _unique_headers(raw_headers)

        for row_number, values in enumerate(reader, start=int(header_row) + 1):
            if skip_blank_rows and (not values or all(not str(v).strip() for v in values)):
                continue
            if len(values) < len(headers):
                values += [""] * (len(headers) - len(values))
            extra = values[len(headers):]
            payload = {header: value.strip() for header, value in zip(headers, values)}
            if extra:
                payload["_extra_columns"] = [value.strip() for value in extra]
            canonical = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
            row_hash = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
            yield row_number, payload, row_hash, selected_encoding, len(headers)
    finally:
        stream.close()
