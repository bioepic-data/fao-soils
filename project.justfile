## Add your own just recipes here. This is imported by the main justfile.

[group('data maintenance')]
update-data:
  uv run python scripts/fetch_fao_soil_database.py --data-dir data/hwsd2

[group('data maintenance')]
refresh-data-downloads:
  uv run python scripts/fetch_fao_soil_database.py --data-dir data/hwsd2 --force-download

[group('data maintenance')]
update-export:
  uv run python scripts/load_hwsd2.py --force export/hwsd2.ddb

[group('data maintenance')]
update-parquet:
  uv run python scripts/export_hwsd2_parquet.py --force export/hwsd2.ddb export/hwsd2_parquet

[group('data maintenance')]
update-artifacts: update-data update-export update-parquet
