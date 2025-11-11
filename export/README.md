# Export Directory

This directory contains pre-built, ready-to-use database files exported from the FAO soils data.

## Files

### `hwsd2.ddb`

**DuckDB database for HWSD v2.0** (32 MB)

A compact, high-performance database containing all HWSD2 soil data:
- 408,835 soil layer records (7 layers × 58,405 sequences)
- 29,538 soil mapping unit summaries
- 18 lookup/domain tables
- 5 metadata and classification tables

**Why DuckDB?**
- **Fast**: 10-100x faster than CSV for queries
- **Compact**: Efficient compression (32 MB vs 100+ MB CSV)
- **Standard SQL**: Works with any SQL tool
- **Embeddable**: No server needed, just a file
- **Suffix**: We use `.ddb` to distinguish from SQLite `.db` files

## Usage

### Python with DuckDB

```python
import duckdb

# Connect to the database
conn = duckdb.connect('export/hwsd2.ddb', read_only=True)

# Query soil properties
result = conn.execute("""
    SELECT
        l.HWSD2_SMU_ID,
        l.LAYER,
        l.TOPDEP,
        l.BOTDEP,
        l.SAND,
        l.CLAY,
        l.ORG_CARBON,
        d.VALUE as DRAINAGE_CLASS
    FROM HWSD2_LAYERS l
    LEFT JOIN D_DRAINAGE d ON l.DRAINAGE = d.CODE
    WHERE l.HWSD2_SMU_ID = 4726
    ORDER BY l.TOPDEP
""").fetchdf()

print(result)
```

### Python with Pandas

```python
import duckdb
import pandas as pd

conn = duckdb.connect('export/hwsd2.ddb', read_only=True)

# Load entire tables into pandas DataFrames
layers = conn.execute("SELECT * FROM HWSD2_LAYERS").fetchdf()
smu = conn.execute("SELECT * FROM HWSD2_SMU").fetchdf()

# Or use SQL for filtered queries
phaeozems = conn.execute("""
    SELECT * FROM HWSD2_LAYERS
    WHERE WRB2 = 'PH'
    ORDER BY TOPDEP
""").fetchdf()
```

### R with DuckDB

```r
library(duckdb)

# Connect to database
con <- dbConnect(duckdb::duckdb(), dbdir="export/hwsd2.ddb", read_only=TRUE)

# Query data
layers <- dbGetQuery(con, "
  SELECT * FROM HWSD2_LAYERS
  WHERE HWSD2_SMU_ID = 4726
  ORDER BY TOPDEP
")

# Clean up
dbDisconnect(con, shutdown=TRUE)
```

### Command Line

```bash
# Install DuckDB CLI
# macOS: brew install duckdb
# Or download from https://duckdb.org/docs/installation/

# Query from command line
duckdb export/hwsd2.ddb "SELECT COUNT(*) FROM HWSD2_LAYERS"

# Interactive mode
duckdb export/hwsd2.ddb
```

## Building from Scratch

If you need to rebuild the database (e.g., after updating CSV data):

```bash
# From repository root
python scripts/load_hwsd2.py export/hwsd2.ddb
```

The script will:
1. Automatically find CSV files in `data/hwsd2/HWSD2_csv/`
2. Create all tables with proper schema
3. Load all 25 CSV files
4. Create indexes for performance
5. Validate data integrity

**Requirements:**
- Python 3.8+
- duckdb package (`pip install duckdb` or `uv add duckdb`)

## Alternative: CSV Files

If you prefer to work directly with CSV files instead of a database:

```python
import pandas as pd

# Load from CSV
layers = pd.read_csv('data/hwsd2/HWSD2_csv/HWSD2_LAYERS.csv')
drainage = pd.read_csv('data/hwsd2/HWSD2_csv/D_DRAINAGE.csv')

# Join tables manually
merged = layers.merge(drainage, left_on='DRAINAGE', right_on='CODE')
```

**Trade-offs:**
- **CSV**: Human-readable, easy to inspect, works anywhere
- **DuckDB**: Much faster queries, automatic indexing, efficient storage

## Schema

The database follows the HWSD2 schema defined in `src/fao_soils/schema/hwsd2.yaml` (LinkML format).

Key tables:
- `HWSD2_LAYERS` - Detailed soil properties at 7 depth layers
- `HWSD2_SMU` - Soil Mapping Unit summaries
- `D_*` tables - Lookup tables for codes (drainage, texture, classification, etc.)
- `WRB_*` tables - World Reference Base classification

Full schema documentation: See `data/hwsd2/hwsd2_duckdb_schema.sql`

## File Size

- **hwsd2.ddb**: 32 MB (compressed)
- **Source CSVs**: ~100 MB (uncompressed text)
- **Raster data** (not included): ~1.7 GB

The database is small enough to include in version control if desired, or can be rebuilt from CSVs in seconds.

## Updating

To update the database when source CSVs change:

```bash
# Remove old database
rm export/hwsd2.ddb

# Rebuild from CSVs
python scripts/load_hwsd2.py export/hwsd2.ddb
```

The rebuild process takes ~5-10 seconds on modern hardware.

## License

- **Database structure and schema**: BSD-3-Clause (this repository)
- **HWSD v2.0 data content**: CC-BY-4.0 (FAO)

When using this data, please cite:
```bibtex
@misc{hwsd2,
  title = {Harmonized World Soil Database version 2.0},
  author = {{FAO}},
  year = {2023},
  publisher = {Food and Agriculture Organization of the United Nations},
  url = {https://www.fao.org/soils-portal/data-hub/soil-maps-and-databases/harmonized-world-soil-database-v20/en/}
}
```

## Support

For issues with:
- **Database generation**: Check `scripts/README.md`
- **Data quality**: See original FAO documentation
- **Schema questions**: See `docs/hwsd2.md` or GitHub issues
