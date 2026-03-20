# FAO Soils Scripts

This directory contains scripts for downloading, processing, and extracting data from FAO soil databases.

## Download and Conversion Scripts

### `fetch_fao_soil_database.py`

Downloads and converts the FAO Harmonized World Soil Database (HWSD) v2.0 from its original Microsoft Access format to more accessible formats.

**Features:**
- Downloads HWSD2 database, raster, and documentation from FAO
- Converts Microsoft Access (.mdb) database to SQLite and CSV
- Verifies file integrity with checksums
- Extracts raster spatial data

**Usage:**
```bash
# Refresh repo-managed HWSD2 source artifacts under data/hwsd2/
uv sync --dev
uv run python fetch_fao_soil_database.py --data-dir ../data/hwsd2

# Specify custom output directory
uv run python fetch_fao_soil_database.py --data-dir /path/to/output

# Re-download source archives before refreshing outputs
uv run python fetch_fao_soil_database.py --data-dir ../data/hwsd2 --force-download
```

**Requirements:**
- Python 3.8+
- Project dependencies installed with `uv sync --dev`
- mdb-tools (for .mdb conversion on Unix/Mac)

### `install_mdb_tools.sh`

Helper script to install mdb-tools on Unix-based systems (required for .mdb conversion).

**Usage:**
```bash
# Install mdb-tools
bash install_mdb_tools.sh
```

**Supported systems:**
- macOS (via Homebrew)
- Ubuntu/Debian (via apt)
- Fedora/CentOS (via yum)

## Data Processing Scripts

### `load_hwsd2.py`

Loads HWSD2 CSV files into a DuckDB database for fast SQL queries.

**Features:**
- Creates DuckDB database from CSV exports
- Sets up all tables, indexes, and relationships
- Validates data integrity
- Provides sample queries

**Usage:**
```bash
# Load data into a new DuckDB file
uv sync --dev
uv run python load_hwsd2.py ../data/hwsd2/hwsd2.db

# Use custom CSV directory
uv run python load_hwsd2.py output.db --csv-dir /path/to/HWSD2_csv

# Overwrite an existing DuckDB file
uv run python load_hwsd2.py --force ../data/hwsd2/hwsd2.db
```

For the packaged export in this repo, use:

```bash
just update-export
```

### `export_hwsd2_parquet.py`

Exports each table from the HWSD2 DuckDB database to a Parquet file.

**Usage:**
```bash
# Export all tables from the packaged DuckDB database
uv sync --dev
uv run python export_hwsd2_parquet.py --force ../export/hwsd2.ddb ../export/hwsd2_parquet
```

For the packaged Parquet export in this repo, use:

```bash
just update-parquet
```

**Output:**
- DuckDB database (~2.6 GB)
- 25 tables (2 main + 18 lookup + 5 metadata)
- 408,835 layer records + 29,538 SMU records

## Data Extraction Scripts

### `hwsd2_extractor.py`

Extract soil profiles by geographic coordinates from HWSD2 data.

**Features:**
- Convert lat/lon to HWSD2_SMU_ID from raster
- Query soil properties from database
- Extract full 7-layer soil profiles (0-200 cm)
- Resolve lookup codes to human-readable names

**Usage:**
```bash
# Extract soil profile for specific coordinates
python hwsd2_extractor.py 40.0 -105.0

# Use as Python module
python
>>> from hwsd2_extractor import get_soil_profile
>>> profile = get_soil_profile(lat=40.0, lon=-105.0)
>>> print(profile['metadata']['WRB2_NAME'])
```

**Requirements:**
- DuckDB database (created by `load_hwsd2.py`)
- Raster file (HWSD2.bil)
- Python packages: duckdb, pandas, struct

**Example output:**
```
Location: 40.0°N, -105.0°W
SMU_ID: 4828
Soil Type: Cambisols (WRB)
Drainage: Moderately well drained

7-Layer Soil Profile:
Layer  Depth(cm)  Sand%  Silt%  Clay%   OC%    pH   Bulk(g/cm³)
D1       0- 20      28.0   46.0   26.0   2.06   6.2   1.48
D2      20- 40      28.0   45.0   27.0   1.43   6.4   1.47
...
```

### `test_extractor.py`

Test suite and examples for the HWSD2 extractor.

**Features:**
- Coordinate conversion tests
- SMU extraction tests
- Full profile extraction examples
- Multi-site batch processing

**Usage:**
```bash
# Run all tests
python test_extractor.py

# Tests include:
# - Coordinate to row/col conversion
# - SMU_ID extraction from raster
# - Database queries with joins
# - Multi-site extraction
```

## Workflow

Complete workflow from download to extraction:

```bash
# 1. Install system dependency for .mdb extraction
bash install_mdb_tools.sh

# 2. Install Python dependencies in the project environment
uv sync --dev

# 3. Download and convert HWSD2 data
uv run python fetch_fao_soil_database.py --data-dir ../data/hwsd2

# 4. Load CSV data into DuckDB
uv run python load_hwsd2.py --force ../export/hwsd2.ddb

# 5. Export all tables to Parquet
uv run python export_hwsd2_parquet.py --force ../export/hwsd2.ddb ../export/hwsd2_parquet

# 6. Extract soil profiles
uv run python ../../scripts/hwsd2_extractor.py 40.0 -105.0

# 7. Run tests
uv run python ../../scripts/test_extractor.py
```

## Directory Structure After Running Scripts

```
fao-soils/
├── scripts/
│   ├── fetch_fao_soil_database.py
│   ├── install_mdb_tools.sh
│   ├── load_hwsd2.py
│   ├── hwsd2_extractor.py
│   └── test_extractor.py
├── data/
│   └── hwsd2/
│       ├── HWSD2_csv/          # CSV exports (from fetch script)
│       ├── HWSD2_RASTER/       # Raster files (from fetch script)
│       ├── hwsd2.db            # SQLite database (from fetch script)
│       ├── hwsd2_duckdb_schema.sql
│       └── README.md
├── export/
│   ├── hwsd2.ddb               # DuckDB database (from load script)
│   └── hwsd2_parquet/          # Parquet exports (from Parquet export script)
└── src/fao_soils/schema/
    └── hwsd2.yaml              # LinkML schema
```

## Just Targets

From the repository root:

```bash
just update-data
just refresh-data-downloads
just update-export
just update-parquet
just update-artifacts
```

## Data Sources

All scripts download from official FAO sources:

- **Database**: https://s3.eu-west-1.amazonaws.com/data.gaezdev.aws.fao.org/HWSD/HWSD2_DB.zip
- **Raster**: https://s3.eu-west-1.amazonaws.com/data.gaezdev.aws.fao.org/HWSD/HWSD2_RASTER.zip
- **Documentation**: https://www.fao.org/3/cc3823en/cc3823en.pdf

## Troubleshooting

### mdb-tools not found

If you get errors about mdb-tools:
```bash
# macOS
brew install mdb-tools

# Ubuntu/Debian
sudo apt-get install mdbtools

# Or use the install script
bash install_mdb_tools.sh
```

### Large file warnings

The raster file is ~1.7 GB and the database is ~2.6 GB. Ensure you have at least 5 GB of free disk space.

### Memory issues

For large queries, increase available memory:
```python
import duckdb
conn = duckdb.connect()
conn.execute("SET memory_limit='4GB'")
```

## Contributing

To add new scripts:
1. Follow the naming convention: `verb_noun.py` (e.g., `extract_soil_properties.py`)
2. Include a docstring with usage examples
3. Add error handling for common failure modes
4. Update this README with script documentation
5. Add tests if appropriate

## License

Scripts in this directory are licensed under BSD-3-Clause.

The HWSD v2.0 data accessed by these scripts is licensed under CC-BY-4.0 by FAO.
