

# Slot: wrb2 


_Dominant WRB 2022 soil group code (2-character HWSD/WRB symbol)._

__

_Example usage:_

_wrb2: FR  # Ferralsols - tropical weathered soils_

_wrb2: CR  # Cryosols - permafrost soils_

_wrb2: GG  # Glaciers - non-soil areas_





URI: [hwsd2:wrb2](https://w3id.org/bioepic-data/fao-soils/hwsd2/wrb2)
Alias: wrb2

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoilMappingUnit](SoilMappingUnit.md) | A Soil Mapping Unit (SMU) represents a distinct area with relatively homogene... |  no  |
| [SoilLayer](SoilLayer.md) | Detailed soil properties at a specific depth layer |  no  |






## Properties

* Range: [FAOSoilTypeEnum](FAOSoilTypeEnum.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/bioepic-data/fao-soils/hwsd2




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | hwsd2:wrb2 |
| native | hwsd2:wrb2 |




## LinkML Source

<details>
```yaml
name: wrb2
description: 'Dominant WRB 2022 soil group code (2-character HWSD/WRB symbol).


  Example usage:

  wrb2: FR  # Ferralsols - tropical weathered soils

  wrb2: CR  # Cryosols - permafrost soils

  wrb2: GG  # Glaciers - non-soil areas'
from_schema: https://w3id.org/bioepic-data/fao-soils/hwsd2
rank: 1000
alias: wrb2
domain_of:
- SoilMappingUnit
- SoilLayer
range: FAOSoilTypeEnum

```
</details>