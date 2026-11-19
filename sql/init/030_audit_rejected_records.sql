CREATE TABLE IF NOT EXISTS audit.rejected_records (
  rejection_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  batch_id UUID NOT NULL,
  source_name TEXT NOT NULL,
  source_file TEXT NOT NULL,
  source_row_number INTEGER,
  raw_payload TEXT,
  reason TEXT NOT NULL,
  rejected_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_rejected_batch ON audit.rejected_records(batch_id);
