# HWSD2 - Harmonized World Soil Database v2.0

## Overview

The Harmonized World Soil Database (HWSD) version 2.0 is a comprehensive global soil dataset published by the Food and Agriculture Organization (FAO) of the United Nations. It provides detailed soil physical and chemical properties at multiple depth layers with global coverage.

## Dataset Specifications

### Spatial Coverage

- **Resolution**: 30 arc-seconds (~1 km at the equator)
- **Grid dimensions**: 43,200 columns × 21,600 rows
- **Geographic extent**: Global (-180° to 180°, -90° to 90°)
- **Projection**: WGS84 Geographic (EPSG:4326)
- **Format**: Binary raster (.bil) with attribute database

### Temporal Coverage

- HWSD v2.0 represents contemporary soil conditions
- Based on soil surveys conducted primarily between 1960-2020
- Periodic updates incorporate new national soil databases

### Vertical Resolution

The database provides soil properties at **7 standardized depth layers**:

| Layer | Top (cm) | Bottom (cm) | Thickness (cm) |
|-------|----------|-------------|----------------|
| D1    | 0        | 20          | 20             |
| D2    | 20       | 40          | 20             |
| D3    | 40       | 60          | 20             |
| D4    | 60       | 80          | 20             |
| D5    | 80       | 100         | 20             |
| D6    | 100      | 150         | 50             |
| D7    | 150      | 200         | 50             |

Total profile depth: 0-200 cm (surface to 2 meters)

## Database Structure

### Soil Mapping Units (SMUs)

Each location on the global grid is assigned to a **Soil Mapping Unit (SMU)**. An SMU represents a geographic area with relatively homogeneous soil characteristics.

- **Total SMUs**: 58,405
- **Unique identifiers**: HWSD2_SMU_ID (1 to ~43,000 range)
- **Legacy IDs**: Links to HWSD v1.0 and WISE30s databases

### Soil Sequences

To represent spatial heterogeneity, each SMU can contain **multiple soil sequences**:

- **Sequence 1**: Usually the dominant soil type (highest share %)
- **Sequence 2-N**: Secondary and minor soil types
- **Share**: Percentage of the SMU area covered by each sequence (sum = 100%)

Example: SMU 4726 (Konza Prairie, Kansas)
- Sequence 1: 60% - Loamy Phaeozem
- Sequence 2: 30% - Sandy Phaeozem
- Sequence 3: 10% - Clayey Phaeozem

### Data Records

- **Total layer records**: 408,835
- **Layers per SMU**: 7 (D1 through D7)
- **Records per layer**: ~58,405 (one per SMU sequence)

## Soil Properties

### Physical Properties

#### Particle Size Distribution
- **Sand** (% by weight): 2.0 - 0.05 mm diameter
- **Silt** (% by weight): 0.05 - 0.002 mm diameter
- **Clay** (% by weight): < 0.002 mm diameter
- **Coarse fragments** (% by volume): > 2 mm diameter

Constraint: Sand + Silt + Clay = 100%

#### Texture Classifications
- **USDA texture class**: 14 classes (Clay, Silty clay, Loam, etc.)
- **SOTER texture class**: 5 classes (Coarse, Medium, Fine, Very Fine, Medium Fine)

#### Bulk Density
- **Bulk density** (g/cm³): Mass of dry soil per unit volume
- **Reference bulk density** (g/cm³): Estimated from texture and organic matter
- **Typical range**: 1.0 - 1.8 g/cm³

### Chemical Properties

#### Carbon and Nitrogen
- **Organic carbon** (% by weight): 0 - 100%
- **Total nitrogen** (g/kg): Total N content
- **C/N ratio**: Carbon to nitrogen ratio
  - Typical range: 8-15 (mineral soils), 20-30 (organic soils)

#### Acidity
- **pH (water)**: Measured in water suspension
  - Range: 0-14 (typically 3.5-9.0)
  - < 5.5: Acidic
  - 5.5-7.0: Slightly acidic
  - 7.0-8.5: Neutral to alkaline
  - > 8.5: Strongly alkaline

#### Cation Exchange Capacity (CEC)
- **CEC soil** (cmolc/kg): Total exchange capacity of the soil
- **CEC clay** (cmolc/kg): Exchange capacity of clay fraction
- **Effective CEC (ECEC)** (cmolc/kg): Exchange capacity at current pH

#### Base Status
- **Total Exchangeable Bases (TEB)** (cmolc/kg): Sum of base cations
- **Base saturation** (% of CEC): Percentage of exchange sites occupied by base cations
- **Aluminum saturation** (% of ECEC): Percentage occupied by Al³⁺ (acidic soils)
- **Exchangeable Sodium Percentage (ESP)** (%): Na saturation (sodic soils)

#### Other Chemical Properties
- **Calcium carbonate equivalent** (% by weight): CaCO₃ content (calcareous soils)
- **Gypsum** (% by weight): CaSO₄·2H₂O content (gypsic soils)
- **Electrical conductivity** (dS/m): Salinity indicator
  - < 2 dS/m: Non-saline
  - 2-4 dS/m: Slightly saline
  - 4-8 dS/m: Moderately saline
  - > 8 dS/m: Highly saline

### Hydrological Properties

#### Drainage Class
Seven classes from excessively drained to very poorly drained:
- **E**: Excessively drained (rapid percolation)
- **SE**: Somewhat excessively drained
- **W**: Well drained
- **MW**: Moderately well drained
- **I**: Imperfectly drained (seasonal saturation)
- **P**: Poorly drained (frequent saturation)
- **VP**: Very poorly drained (permanent saturation)

#### Water Capacity
- **Available Water Capacity (AWC)**: mm/m or mm (depending on table)
  - Amount of water available to plants between field capacity and wilting point
  - Typical range: 50-200 mm/m

#### Root and Water Limitations
- **Root depth**: Deep (>100 cm), Moderately deep (<100 cm), Shallow (<50 cm), Very shallow (<10 cm)
- **Obstacle to roots**: Depth to restrictive layer (cm)
- **Impermeable layer**: Depth to impermeable horizon (cm)
- **Soil water regime**: Wetness duration (ESDB)

### Soil Classifications

#### World Reference Base (WRB) 2022
The primary classification system with multiple levels of detail:

- **WRB2**: 2-character codes (32 reference soil groups)
  - Examples: AC (Acrisols), CH (Chernozems), PT (Plinthosols)
- **WRB4**: 4-character codes with qualifier
  - Examples: ACfr (Ferric Acrisols), CHha (Haplic Chernozems)
- **WRB Phases**: Detailed classification with multiple qualifiers
  - Examples: ACfrkk (Akroskeletic Ferric Acrisols)

Common WRB soil groups:
- **Acrisols**: Acidic, clay-rich, weathered tropical soils
- **Chernozems**: Deep, dark, fertile grassland soils
- **Ferralsols**: Highly weathered tropical soils with oxides
- **Luvisols**: Clay-enriched temperate forest soils
- **Phaeozems**: Dark, humus-rich grassland soils
- **Podzols**: Acidic forest soils with leached surface layer

#### FAO-90 Classification
Legacy FAO classification (1990 system):
- Similar to WRB but older version
- 194 soil units in the database

#### Climate Classification
- **Köppen-Geiger zones**: A (Tropical), B (Arid), C (Temperate), D (Cold), E (Polar)

## Data Quality and Limitations

### Data Sources and Coverage

The HWSD v2.0 integrates multiple national and regional databases:

- **ESDB**: European Soil Database (high detail)
- **CHINA**: China soil database (1:1M scale)
- **SOTWIS**: Soil and Terrain Database (global)
- **DSMW**: Digital Soil Map of the World (1:5M scale)
- **WISE30s**: World Inventory of Soil Emission Potentials (30 arcsec)
- **National databases**: Afghanistan, Ghana, Turkey, etc.

### Missing Data Indicators

- **Value -9**: Missing or not applicable
- **NODATA (65535)**: No soil data (oceans, ice, water bodies)

### Uncertainty

- **Scale**: Original mapping scales vary (1:250,000 to 1:5,000,000)
- **Heterogeneity**: Single SMU values represent area averages
- **Temporal**: Soil properties change over time; database is a snapshot
- **Analytical**: Different labs and methods used for soil analysis

### Recommended Usage

**Appropriate for:**
- Global and continental-scale modeling
- Regional assessments (>100 km²)
- Initial parameterization of ecosystem models
- Comparative studies across climates/biomes
- Educational purposes

**Not appropriate for:**
- Site-specific predictions (< 1 km²)
- Precision agriculture (< 1 ha)
- Regulatory decisions
- Construction planning

**Best practices:**
- Validate with local soil data when available
- Perform sensitivity analysis on soil parameters
- Use dominant sequence or weighted averages
- Consider uncertainty in model results
- Cite the database properly

## Using the Schema

### Loading the Schema

```python
from linkml_runtime import SchemaView

schema_view = SchemaView("src/fao_soils/schema/hwsd2.yaml")

# Explore the schema
print(schema_view.all_classes())
print(schema_view.all_slots())
print(schema_view.all_enums())
```

### Key Classes

- **SoilMappingUnit**: Summary properties for an SMU
- **SoilLayer**: Detailed properties for a single depth layer
- **WRBClass**: World Reference Base soil classification with colors for mapping

### Key Slots (Properties)

Soil layers have ~47 properties including:
- Identifiers: `hwsd2_smu_id`, `sequence`, `layer`
- Depths: `topdep`, `botdep`
- Texture: `sand`, `silt`, `clay`, `texture_usda`, `texture_soter`
- Carbon/N: `org_carbon`, `total_n`, `cn_ratio`
- Chemistry: `ph_water`, `cec_soil`, `bsat`, `esp`
- Physical: `bulk`, `coarse`

### Enumerations

- **DrainageEnum**: 7 drainage classes (E, SE, W, MW, I, P, VP)
- **TextureUSDAEnum**: 14 USDA texture classes
- **TextureSOTEREnum**: 5 SOTER texture classes
- **KoppenEnum**: 5 climate zones (A, B, C, D, E)
- **RootDepthEnum**: 4 root depth categories
- **PhaseEnum**: 9 soil phase modifiers

## Data Access

### Official Source

Download the HWSD v2.0 database from the FAO Soils Portal:
- [HWSD v2.0 Download Page](https://www.fao.org/soils-portal/data-hub/soil-maps-and-databases/harmonized-world-soil-database-v20/en/)

The download includes:
- Raster files (HWSD2.bil, .hdr, .prj, .stx)
- Access database (HWSD2.mdb) or CSV exports
- Documentation (PDF)

### Processing Tools

For tools to work with HWSD2 data, see:
- [ecosim-co-scientist](https://github.com/bioepic-data/ecosim-co-scientist/tree/main/hwsd_data) - Python extraction tools
  - DuckDB database loader
  - Geographic coordinate to soil profile extractor
  - Example queries and visualizations

## References

### Primary Citation

```bibtex
@misc{hwsd2,
  title = {Harmonized World Soil Database version 2.0},
  author = {{FAO}},
  year = {2023},
  publisher = {Food and Agriculture Organization of the United Nations},
  url = {https://www.fao.org/soils-portal/data-hub/soil-maps-and-databases/harmonized-world-soil-database-v20/en/}
}
```

### Related Publications

- FAO/IIASA/ISRIC/ISS-CAS/JRC (2012). Harmonized World Soil Database (version 1.2). FAO, Rome, Italy and IIASA, Laxenburg, Austria.
- Fischer, G., et al. (2008). Global Agro-ecological Zones Assessment for Agriculture (GAEZ 2008). IIASA, Laxenburg, Austria and FAO, Rome, Italy.

### Schema Citation

```bibtex
@software{hwsd2_schema,
  title = {HWSD2 LinkML Schema},
  author = {{BioEPIC Data Team}},
  year = {2024},
  url = {https://github.com/bioepic-data/fao-soils},
  note = {LinkML schema for FAO HWSD v2.0}
}
```

## See Also

- [FAO Soils Portal](https://www.fao.org/soils-portal/en/)
- [World Reference Base (WRB)](https://www.fao.org/soils-portal/data-hub/soil-classification/world-reference-base/en/)
- [LinkML Documentation](https://linkml.io/)
- [ISRIC World Soil Information](https://www.isric.org/)
