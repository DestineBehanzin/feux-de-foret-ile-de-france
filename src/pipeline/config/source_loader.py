import os
from pathlib import Path
import yaml


def load_csv_sources() -> list[dict]:
    path = Path(os.getenv("CSV_SOURCES_CONFIG", "/app/config/sources.yml"))
    with path.open(encoding="utf-8") as stream:
        data = yaml.safe_load(stream) or {}

    sources = [s for s in data.get("csv_sources", []) if s.get("enabled", True)]
    for source in sources:
        missing = [key for key in ("name", "file_name") if not source.get(key)]
        if missing:
            raise ValueError(f"Configuration incomplete: {missing}")
        source.setdefault("delimiter", ";")
        source.setdefault("encoding", "utf-8-sig")
        source.setdefault("fallback_encodings", ["utf-8", "cp1252", "latin-1"])
        source.setdefault("header_row", 1)
    return sources
