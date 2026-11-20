CREATE SCHEMA IF NOT EXISTS raw;

CREATE TABLE IF NOT EXISTS raw.csv_records (
    ingestion_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    source_name TEXT NOT NULL,
    source_file TEXT NOT NULL,
    source_row_number INTEGER NOT NULL,
    payload JSONB NOT NULL,
    row_hash CHAR(64) NOT NULL,
    batch_id UUID NOT NULL,
    ingested_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uq_raw_csv_record UNIQUE (source_name, source_file, row_hash)
);

CREATE INDEX IF NOT EXISTS idx_csv_records_source
    ON raw.csv_records(source_name, ingested_at);
CREATE INDEX IF NOT EXISTS idx_csv_records_batch
    ON raw.csv_records(batch_id);
