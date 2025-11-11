# FAO Soils - LinkML Schemas

**Standardized, machine-readable schemas for FAO soil databases**

This documentation site provides comprehensive information about LinkML schemas for FAO (Food and Agriculture Organization) soil databases.

## Schemas

### HWSD2 - Harmonized World Soil Database v2.0

The HWSD v2.0 is a comprehensive global soil dataset with 30 arc-second resolution (~1 km) covering physical, chemical, and hydrological soil properties at 7 depth layers (0-200 cm).

- **[HWSD2 Documentation](hwsd2.md)** - Comprehensive guide to the database and schema
- **[HWSD2 Schema Reference](elements/hwsd2.md)** - Auto-generated schema documentation
- **[Download Data](https://www.fao.org/soils-portal/data-hub/soil-maps-and-databases/harmonized-world-soil-database-v20/en/)** - Official FAO download page

**Key features:**
- 58,405 soil mapping units globally
- 408,835 layer records (7 layers × 58,405 sequences)
- Physical properties: texture, bulk density, coarse fragments
- Chemical properties: organic carbon, pH, nitrogen, CEC
- Multiple classification systems: WRB, FAO-90, USDA

## Using the Schemas

### Installation

```bash
pip install linkml linkml-runtime
```

### Generate Python Dataclasses

```bash
gen-python src/fao_soils/schema/hwsd2.yaml > hwsd2_model.py
```

### Generate Other Formats

```bash
# JSON Schema
gen-json-schema src/fao_soils/schema/hwsd2.yaml > hwsd2.schema.json

# SQL DDL
gen-sqlddl src/fao_soils/schema/hwsd2.yaml > hwsd2.sql

# Markdown documentation
gen-markdown src/fao_soils/schema/hwsd2.yaml > hwsd2_docs.md

# OWL ontology
gen-owl src/fao_soils/schema/hwsd2.yaml > hwsd2.owl
```

## Applications

### Ecosystem Modeling

- Extract soil profiles by geographic coordinates
- Parameterize biogeochemical models (EcoSIM, CENTURY, DayCENT)
- Multi-site comparative studies
- Climate change impact assessments

### Data Integration

- Standardized vocabulary for soil properties
- Validation of soil data quality
- Interoperability with environmental databases
- Reproducible research workflows

## Resources

- **[GitHub Repository](https://github.com/bioepic-data/fao-soils)** - Source code and schemas
- **[Auto-generated Schema Docs](elements/index.md)** - Full schema reference
- **[FAO Soils Portal](https://www.fao.org/soils-portal/en/)** - Official FAO resource
- **[LinkML](https://linkml.io/)** - LinkML framework documentation

## Related Projects

- **[ecosim-co-scientist](https://github.com/bioepic-data/ecosim-co-scientist)** - Tools for ecosystem modeling with HWSD2 data extractors

## Contributing

Contributions are welcome! See our [GitHub repository](https://github.com/bioepic-data/fao-soils) for contribution guidelines.

## License

- **Schema files**: BSD-3-Clause
- **HWSD v2.0 data**: CC-BY-4.0 (provided by FAO)
