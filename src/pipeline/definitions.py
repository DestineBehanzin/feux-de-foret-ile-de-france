from dagster import Definitions
from pipeline.assets.csv_assets import ingest_csv_sources

defs = Definitions(assets=[ingest_csv_sources])
