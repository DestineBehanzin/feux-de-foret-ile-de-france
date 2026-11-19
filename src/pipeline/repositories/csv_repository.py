import json

import psycopg


class CsvRepository:
    PIPELINE_NAME = "ingestion_csv_bdiff"

    def __init__(self, database_url: str):
        self.database_url = database_url.replace(
            "postgresql+psycopg://",
            "postgresql://",
            1,
        )

    def start_batch(
        self,
        batch_id,
        source_name: str,
        source_file: str,
    ) -> None:
        with psycopg.connect(self.database_url) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO audit.load_log (
                        batch_id,
                        pipeline_name,
                        source_name,
                        source_file,
                        status,
                        rows_read,
                        rows_inserted,
                        rows_rejected
                    )
                    VALUES (
                        %s,
                        %s,
                        %s,
                        %s,
                        'RUNNING',
                        0,
                        0,
                        0
                    )
                    """,
                    (
                        batch_id,
                        self.PIPELINE_NAME,
                        source_name,
                        source_file,
                    ),
                )

    def insert_row(
        self,
        source_name: str,
        source_file: str,
        row_number: int,
        payload: dict,
        row_hash: str,
        batch_id,
    ) -> int:
        with psycopg.connect(self.database_url) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO raw.csv_records (
                        source_name,
                        source_file,
                        source_row_number,
                        payload,
                        row_hash,
                        batch_id
                    )
                    VALUES (
                        %s,
                        %s,
                        %s,
                        %s::jsonb,
                        %s,
                        %s
                    )
                    ON CONFLICT (
                        source_name,
                        source_file,
                        row_hash
                    )
                    DO NOTHING
                    """,
                    (
                        source_name,
                        source_file,
                        row_number,
                        json.dumps(
                            payload,
                            ensure_ascii=False,
                        ),
                        row_hash,
                        batch_id,
                    ),
                )

                return cursor.rowcount

    def reject_row(
        self,
        batch_id,
        source_name: str,
        source_file: str,
        row_number: int,
        payload: dict,
        reason: str,
    ) -> None:
        with psycopg.connect(self.database_url) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO audit.rejected_records (
                        batch_id,
                        source_name,
                        source_file,
                        source_row_number,
                        raw_payload,
                        reason
                    )
                    VALUES (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
                    )
                    """,
                    (
                        batch_id,
                        source_name,
                        source_file,
                        row_number,
                        json.dumps(
                            payload,
                            ensure_ascii=False,
                        ),
                        reason,
                    ),
                )

    def finish_batch(
        self,
        batch_id,
        status: str,
        rows_read: int,
        rows_inserted: int,
        rows_rejected: int,
        error_message: str | None = None,
    ) -> None:
        with psycopg.connect(self.database_url) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE audit.load_log
                    SET
                        status = %s,
                        rows_read = %s,
                        rows_inserted = %s,
                        rows_rejected = %s,
                        error_message = %s,
                        completed_at = CURRENT_TIMESTAMP
                    WHERE batch_id = %s
                    """,
                    (
                        status,
                        rows_read,
                        rows_inserted,
                        rows_rejected,
                        error_message,
                        batch_id,
                    ),
                )