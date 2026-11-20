import os
import shutil
import uuid
from pathlib import Path
from dagster import asset, AssetExecutionContext, MaterializeResult, MetadataValue
from pipeline.config.source_loader import load_csv_sources
from pipeline.connectors.csv_connector import iter_csv_rows
from pipeline.repositories.csv_repository import CsvRepository
from pipeline.validators.bdiff_validator import validate_bdiff


@asset(group_name="ingestion", compute_kind="python")
def ingest_csv_sources(context: AssetExecutionContext):
    incoming = Path(os.getenv("CSV_INCOMING_DIR", "/app/data/incoming"))
    archive = Path(os.getenv("CSV_ARCHIVE_DIR", "/app/data/archive"))
    repository = CsvRepository(os.environ["DATABASE_URL"])
    totals = {"read": 0, "inserted": 0, "rejected": 0}
    processed = []

    for source in load_csv_sources():
        path = incoming / source["file_name"]
        if not path.is_file():
            raise FileNotFoundError(f"Fichier introuvable: {path}")
        batch_id = uuid.uuid4()
        read = inserted = rejected = 0
        encoding_used = None
        repository.start_batch(batch_id, source["name"], path.name)
        try:
            rows = iter_csv_rows(
                path=path,
                delimiter=source["delimiter"],
                encoding=source["encoding"],
                fallback_encodings=source["fallback_encodings"],
                header_row=source["header_row"],
                skip_blank_rows=source.get("skip_blank_rows", True),
            )
            for row_number, payload, row_hash, encoding_used, column_count in rows:
                read += 1
                errors = validate_bdiff(
                    payload,
                    source.get("expected_column_count"),
                    source.get("required_positions", []),
                ) if source.get("domain") == "bdiff" else []
                if errors:
                    rejected += 1
                    repository.reject_row(batch_id, source["name"], path.name,
                                          row_number, payload, "; ".join(errors))
                    continue
                inserted += repository.insert_row(source["name"], path.name,
                                                  row_number, payload, row_hash, batch_id)
            repository.finish_batch(batch_id, "SUCCESS", read, inserted, rejected)
        except Exception as exc:
            repository.finish_batch(batch_id, "FAILED", read, inserted, rejected, str(exc))
            raise

        totals["read"] += read
        totals["inserted"] += inserted
        totals["rejected"] += rejected
        processed.append(path.name)
        if source.get("archive_after_success", True):
            archive.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, archive / f"{batch_id}_{path.name}")
        context.log.info(f"{source['name']}: encodage={encoding_used}, lues={read}, inserees={inserted}, rejetees={rejected}")

    return MaterializeResult(metadata={
        "files": MetadataValue.json(processed),
        "rows_read": totals["read"],
        "rows_inserted": totals["inserted"],
        "rows_rejected": totals["rejected"],
    })
