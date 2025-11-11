# Examples of using fao-soils

This folder contains examples using the datamodel.

The source of the data used in the example is [tests/data](../tests/data/).

The command `just test` creates different representations of the data in [tests/data](../tests/data/) and writes them to the subfolder `output`.
It also generates a markdown documentation of the examples which is not very useful in its current form.
Hence, the `output` sub-folder is git-ignored.

## HWSD2 Examples

### `hwsd2_soil_profile.yaml`

A complete soil profile example from the Harmonized World Soil Database v2.0.

**Location**: Konza Prairie, Kansas, USA (39.103°N, 96.563°W)
**Soil Type**: Phaeozem (Haplic) - dark, fertile grassland soil
**SMU_ID**: 4726

This example demonstrates:

- **Soil Mapping Unit** metadata (SMU level properties)
- **7-layer soil profile** (0-200 cm depth)
- All major soil properties:
  - Physical: texture, bulk density, coarse fragments
  - Chemical: organic carbon, pH, nitrogen, CEC
  - Classification: WRB, FAO-90, USDA texture
  - Hydrological: drainage class, available water capacity

**Key features of this soil:**
- High organic carbon in topsoil (2.06%) - typical of grassland Mollisols
- Decreasing organic matter with depth
- Slightly acidic to neutral pH (6.2-7.4)
- High base saturation (80-92%) indicating high fertility
- Silt loam to loam texture with good water holding capacity
- Moderately well drained

This example is based on real HWSD2 data for the Konza Prairie NEON site.

## Using the Examples

### Validate Against Schema

```bash
# Install linkml
pip install linkml

# Validate the example
linkml-validate -s src/fao_soils/schema/hwsd2.yaml examples/hwsd2_soil_profile.yaml
```

### Load in Python

```python
from linkml_runtime.loaders import yaml_loader

# Load the example data
with open('examples/hwsd2_soil_profile.yaml') as f:
    data = yaml.safe_load(f)

# Access properties
print(f"Soil type: {data['soil_mapping_unit']['wrb2']}")
print(f"Layers: {len(data['soil_layers'])}")
```

### Generate Derived Formats

```bash
# Convert to JSON
linkml-convert -s src/fao_soils/schema/hwsd2.yaml -t json \
  examples/hwsd2_soil_profile.yaml > soil_profile.json
```

## Additional Examples

For data extraction tools to create more examples, see the [ecosim-co-scientist](https://github.com/bioepic-data/ecosim-co-scientist/tree/main/hwsd_data) repository which includes Python tools to extract HWSD2 soil profiles by geographic coordinates.
