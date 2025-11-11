<a href="https://github.com/dalito/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# fao-soils

**LinkML schemas and data models for FAO soil databases**

This repository provides standardized, machine-readable schemas for FAO (Food and Agriculture Organization) soil databases using [LinkML](https://linkml.io/).

## Current Schemas

### HWSD2 - Harmonized World Soil Database v2.0

The [Harmonized World Soil Database v2.0](https://www.fao.org/soils-portal/data-hub/soil-maps-and-databases/harmonized-world-soil-database-v20/en/) is a comprehensive global soil dataset that provides:

- **Global coverage** at 30 arc-second resolution (~1 km)
- **7 standardized depth layers** (0-200 cm)
- **Comprehensive soil properties**:
  - Physical: texture (sand/silt/clay), bulk density, coarse fragments
  - Chemical: organic carbon, pH, nitrogen, C/N ratio, calcium carbonate, gypsum
  - Cation exchange: CEC, base saturation, aluminum saturation
  - Hydrological: drainage class, available water capacity
- **Multiple classification systems**: WRB (World Reference Base), FAO-90, USDA
- **Climate context**: Köppen-Geiger climate zones

**Data structure:**
- 408,835 layer records from 58,405 soil mapping units
- Each mapping unit can contain multiple soil sequences (representing spatial heterogeneity)
- Gridded raster data (43,200 × 21,600 pixels) linking locations to soil properties

**Schema file:** [`src/fao_soils/schema/hwsd2.yaml`](src/fao_soils/schema/hwsd2.yaml)

## Documentation Website

[https://bioepic-data.github.io/fao-soils](https://bioepic-data.github.io/fao-soils)

## Repository Structure

* [docs/](docs/) - mkdocs-managed documentation
  * [elements/](docs/elements/) - generated schema documentation
* [examples/](examples/) - Examples of using the schema
* [project/](project/) - project files (these files are auto-generated, do not edit)
* [src/](src/) - source files (edit these)
  * [fao_soils](src/fao_soils)
    * [schema/](src/fao_soils/schema) -- LinkML schemas (edit these)
      * [`hwsd2.yaml`](src/fao_soils/schema/hwsd2.yaml) - HWSD v2.0 schema
      * [`fao_soils.yaml`](src/fao_soils/schema/fao_soils.yaml) - Template schema
    * [datamodel/](src/fao_soils/datamodel) -- generated Python datamodels
* [tests/](tests/) - Python tests
  * [data/](tests/data) - Example data

## Quick Start

### Using the Schema

```python
from linkml_runtime.loaders import yaml_loader
from fao_soils.datamodel.hwsd2 import SoilMappingUnit, SoilLayer

# Load data conforming to the schema
# (After schema is compiled, which generates Python classes)
```

### Generating Schema Artifacts

The LinkML schema can generate multiple formats:

```bash
# Install dependencies
pip install linkml

# Generate Python dataclasses
gen-python src/fao_soils/schema/hwsd2.yaml > hwsd2_datamodel.py

# Generate JSON Schema
gen-json-schema src/fao_soils/schema/hwsd2.yaml > hwsd2.schema.json

# Generate SQL DDL
gen-sqlddl src/fao_soils/schema/hwsd2.yaml > hwsd2.sql

# Generate Markdown documentation
gen-markdown src/fao_soils/schema/hwsd2.yaml > hwsd2_docs.md
```

## Use Cases

### Ecosystem Modeling

The HWSD2 schema enables:
- Extraction of soil profiles by geographic coordinates
- Integration with climate forcing data for ecosystem models
- Parameter calibration for biogeochemical models (e.g., EcoSIM, CENTURY, DayCENT)
- Multi-site comparative studies

### Data Integration

- Standardized vocabulary for soil properties
- Consistent units and value ranges
- Validation of soil data quality
- Interoperability with other environmental databases

### Applications

- Climate change impact assessments
- Agricultural productivity modeling
- Carbon cycle modeling
- Hydrological modeling
- Land use planning

## Related Projects

For data extraction and analysis tools using this schema, see:
- **[ecosim-co-scientist](https://github.com/bioepic-data/ecosim-co-scientist)** - AI-powered tools for ecosystem modeling including HWSD2 data extractors

## Developer Tools

There are several pre-defined command-recipes available.
They are written for the command runner [just](https://github.com/casey/just/). To list all pre-defined commands, run `just` or `just --list`.

Common commands:
```bash
# Generate all schema artifacts
just gen-project

# Run tests
just test

# Build documentation
just gendoc
```

## Data Sources

The schemas in this repository describe the structure of FAO soil databases. The actual data files are maintained by FAO and can be obtained from:

- **HWSD v2.0**: [FAO Soils Portal](https://www.fao.org/soils-portal/data-hub/soil-maps-and-databases/harmonized-world-soil-database-v20/en/)

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

- **Schema files**: BSD-3-Clause (this repository)
- **HWSD v2.0 data**: CC-BY-4.0 (provided by FAO)

See [LICENSE](LICENSE) for details.

## Citation

If you use these schemas in your research, please cite:

```bibtex
@software{fao_soils_schema,
  title = {FAO Soils LinkML Schemas},
  author = {{BioEPIC Data Team}},
  year = {2024},
  url = {https://github.com/bioepic-data/fao-soils},
  note = {LinkML schemas for FAO soil databases}
}
```

For the HWSD v2.0 data itself, please cite:
```bibtex
@misc{hwsd2,
  title = {Harmonized World Soil Database version 2.0},
  author = {{FAO}},
  year = {2023},
  publisher = {Food and Agriculture Organization of the United Nations},
  url = {https://www.fao.org/soils-portal/data-hub/soil-maps-and-databases/harmonized-world-soil-database-v20/en/}
}
```

## Credits

This project uses the template [linkml-project-copier](https://github.com/dalito/linkml-project-copier) published as [doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584).
