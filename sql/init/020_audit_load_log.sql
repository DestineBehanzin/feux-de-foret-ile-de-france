CREATE SCHEMA IF NOT EXISTS audit;

CREATE TABLE IF NOT EXISTS audit.load_log (
    batch_id UUID PRIMARY KEY,
    pipeline_name TEXT NOT NULL,
    source_name TEXT NOT NULL,
    source_file TEXT NOT NULL,
    started_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMPTZ,
    status TEXT NOT NULL
        CHECK (
            status IN (
                'RUNNING',
                'SUCCESS',
                'FAILED'
            )
        ),
    rows_read INTEGER NOT NULL DEFAULT 0,
    rows_inserted INTEGER NOT NULL DEFAULT 0,
    rows_rejected INTEGER NOT NULL DEFAULT 0,
    error_message TEXT
);

ALTER TABLE audit.load_log
    ADD COLUMN IF NOT EXISTS source_file TEXT;

ALTER TABLE audit.load_log
    ADD COLUMN IF NOT EXISTS rows_read INTEGER NOT NULL DEFAULT 0;

ALTER TABLE audit.load_log
    ADD COLUMN IF NOT EXISTS rows_inserted INTEGER NOT NULL DEFAULT 0;

ALTER TABLE audit.load_log
    ADD COLUMN IF NOT EXISTS rows_rejected INTEGER NOT NULL DEFAULT 0;

ALTER TABLE audit.load_log
    ADD COLUMN IF NOT EXISTS completed_at TIMESTAMPTZ;

ALTER TABLE audit.load_log
    ADD COLUMN IF NOT EXISTS error_message TEXT;
