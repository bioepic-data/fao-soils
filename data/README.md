# FAO Soils Data

This directory contains data files from FAO soil databases in various formats.

## Directory Structure

```
data/
└── hwsd2/                      # HWSD v2.0 data
    ├── HWSD2_csv/              # CSV exports of database tables
    ├── HWSD2_RASTER/           # Spatial raster files (not in repo)
    ├── hwsd2.db                # DuckDB database (not in repo)
    ├── hwsd2_duckdb_schema.sql # SQL schema for DuckDB
    └── README.md               # HWSD2-specific documentation
```

## Data Files

### CSV Files (Included)

The `hwsd2/HWSD2_csv/` directory contains:

- **Main tables** (2 files):
  - `HWSD2_LAYERS.csv` - 408,835 records of soil layer properties
  - `HWSD2_SMU.csv` - 29,538 soil mapping unit summaries

- **Lookup tables** (18 files):
  - `D_*.csv` - Domain tables for codes and classifications
  - Examples: `D_DRAINAGE.csv`, `D_TEXTURE_USDA.csv`, `D_WRB2.csv`

- **Metadata tables** (2 files):
  - `HWSD2_LAYERS_METADATA.csv` - Column documentation for layers
  - `HWSD2_SMU_METADATA.csv` - Column documentation for SMUs

- **Classification tables** (3 files):
  - `WRB_*.csv` - World Reference Base classification tables

**Total size**: ~100 MB (compressed)

### Large Files (Not in Repository)

These files are too large for Git and must be generated locally:

- **`HWSD2_RASTER/HWSD2.bil`** - Global soil raster (~1.7 GB)
  - 30 arc-second resolution (43,200 × 21,600 pixels)
  - Links geographic locations to soil mapping units
  - Download using `scripts/fetch_fao_soil_database.py`

- **`../export/hwsd2.ddb`** - DuckDB database (~32 MB)
  - Fast SQL queries on soil data
  - Pre-built version available in `export/` directory
  - Can be regenerated using `scripts/load_hwsd2.py`

## Getting the Data

### Option 1: Use Pre-built Database (Recommended)

**The fastest way to start!** A pre-built DuckDB database is available in `export/hwsd2.ddb` (~32 MB).

```bash
# From repository root
cd export/
python -c "import duckdb; conn = duckdb.connect('hwsd2.ddb'); print(conn.execute('SELECT COUNT(*) FROM HWSD2_LAYERS').fetchone())"
```

See [export/README.md](../export/README.md) for usage examples.

### Option 2: Build from CSVs (Included in Repo)

CSVs are included in this repository (in `hwsd2/HWSD2_csv/`). Build the database:

```bash
# From repository root
python scripts/load_hwsd2.py export/hwsd2.ddb
```

This takes ~10 seconds and creates a 32 MB database.

### Option 3: Download from FAO (Original Source)

Download the complete dataset including raster files:

```bash
# From repository root
cd scripts/
python fetch_fao_soil_database.py
```

This downloads:
- Original Microsoft Access database (.mdb)
- Raster files (.bil, ~1.7 GB)
- Technical documentation (PDF)
- Converts database to CSV and SQLite

## Data Formats

### CSV Format

**Advantages:**
- Human-readable
- Easy to inspect and version control
- Import into any tool (Python, R, Excel, etc.)
- Small enough to include in Git repositories

**Disadvantages:**
- Slower for complex queries
- No built-in indexes
- Must handle joins manually

### DuckDB Format

**Advantages:**
- Very fast SQL queries (10-100x faster than CSV)
- Supports complex joins and aggregations
- Small memory footprint
- Standard SQL interface

**Disadvantages:**
- Binary format (not human-readable)
- Large file size (~2.6 GB)
- Not suitable for version control

### Raster Format

**Advantages:**
- Links spatial locations to soil data
- Standard geospatial format
- Works with GIS tools (QGIS, ArcGIS)

**Disadvantages:**
- Very large file (~1.7 GB)
- Requires GIS libraries to read
- Binary format

## Usage Examples

### Query CSV with Pandas

```python
import pandas as pd

# Load main soil layer data
layers = pd.read_csv('hwsd2/HWSD2_csv/HWSD2_LAYERS.csv')

# Load lookup table
drainage = pd.read_csv('hwsd2/HWSD2_csv/D_DRAINAGE.csv')

# Join to get drainage class names
merged = layers.merge(drainage, left_on='DRAINAGE', right_on='CODE')

# Filter for a specific soil type
phaeozems = layers[layers['WRB2'] == 'PH']
```

### Query DuckDB

```python
import duckdb

# Connect to database
conn = duckdb.connect('hwsd2/hwsd2.db')

# SQL query with joins
result = conn.execute("""
    SELECT
        l.HWSD2_SMU_ID,
        l.LAYER,
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

### Extract by Coordinates

```python
from scripts.hwsd2_extractor import get_soil_profile

# Get soil profile for a location
profile = get_soil_profile(lat=40.0, lon=-105.0)

if profile:
    print(f"Soil type: {profile['metadata']['WRB2_NAME']}")

    # Access 7-layer profile
    for _, layer in profile['layers'].iterrows():
        print(f"Layer {layer['LAYER']}: {layer['TOPDEP']}-{layer['BOTDEP']} cm")
        print(f"  Organic C: {layer['ORG_CARBON']}%, pH: {layer['PH_WATER']}")
```

## Data Quality

### Completeness

- **Complete coverage**: All 58,405 soil mapping units have 7 layers
- **Missing values**: Indicated by -9 or NULL
- **No data areas**: Oceans, ice, water bodies (raster value 65535)

### Accuracy

- **Spatial resolution**: 30 arc-seconds (~1 km)
- **Mapping scales**: Original sources vary from 1:250,000 to 1:5,000,000
- **Temporal**: Represents soil conditions circa 1960-2020

### Sources

Data compiled from:
- European Soil Database (ESDB) - high detail
- China soil database - 1:1M scale
- SOTWIS - global coverage
- DSMW - 1:5M global baseline
- WISE30s - 30 arc-second global
- Various national databases

## Size Information

| File/Directory | Compressed | Uncompressed | In Repo? | Location |
|---------------|-----------|--------------|----------|----------|
| HWSD2_csv/ | ~20 MB | ~100 MB | ✓ Yes | data/hwsd2/ |
| hwsd2.ddb | N/A | ~32 MB | ✓ Yes | export/ |
| HWSD2_RASTER/ | ~500 MB | ~1.7 GB | ✗ No | Download separately |
| Schema files | <1 MB | <1 MB | ✓ Yes | src/fao_soils/schema/ |

**Total repo size**: ~120 MB (CSV + database + schemas)
**Total after full download**: ~1.9 GB (+ raster files)

## Git LFS Configuration

Large files are excluded from the repository via `.gitignore`:

```gitignore
# Large data files (download separately)
data/**/*.db
data/**/*.bil
data/**/*.hdr
data/**/*.stx
data/**/*.prj
data/**/*.mdb
data/**/*.zip
```

To download large files, use the scripts in `scripts/`.

## License

### Data License

The HWSD v2.0 data is licensed under **CC-BY-4.0** by FAO.

**Citation:**
```bibtex
@misc{hwsd2,
  title = {Harmonized World Soil Database version 2.0},
  author = {{FAO}},
  year = {2023},
  publisher = {Food and Agriculture Organization of the United Nations},
  url = {https://www.fao.org/soils-portal/data-hub/soil-maps-and-databases/harmonized-world-soil-database-v20/en/}
}
```

### Schema License

The LinkML schemas in `src/fao_soils/schema/` are licensed under **BSD-3-Clause**.

## Further Documentation

- **HWSD2 data structure**: See `hwsd2/README.md`
- **Schema documentation**: See `src/fao_soils/schema/`
- **Processing scripts**: See `scripts/README.md`
- **Web documentation**: https://bioepic-data.github.io/fao-soils

## Support

For issues with:
- **Data download**: Check scripts/README.md troubleshooting section
- **Schema questions**: See docs/ or open an issue on GitHub
- **Original FAO data**: Contact FAO Soils Portal

## Contributing

To contribute data or corrections:
1. Ensure data conforms to the LinkML schema
2. Document data sources and processing steps
3. Add examples showing data usage
4. Submit a pull request

For large datasets, provide scripts to generate them rather than committing the raw files.
