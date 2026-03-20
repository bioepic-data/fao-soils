

# Slot: share 


_Percentage share in Soil Mapping Unit_





URI: [hwsd2:share](https://w3id.org/bioepic-data/fao-soils/hwsd2/share)
Alias: share

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoilMappingUnit](SoilMappingUnit.md) | A Soil Mapping Unit (SMU) represents a distinct area with relatively homogene... |  no  |
| [SoilLayer](SoilLayer.md) | Detailed soil properties at a specific depth layer |  no  |






## Properties

* Range: [Float](Float.md)

* Minimum Value: 0

* Maximum Value: 100




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/bioepic-data/fao-soils/hwsd2




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | hwsd2:share |
| native | hwsd2:share |




## LinkML Source

<details>
```yaml
name: share
description: Percentage share in Soil Mapping Unit
from_schema: https://w3id.org/bioepic-data/fao-soils/hwsd2
rank: 1000
alias: share
domain_of:
- SoilMappingUnit
- SoilLayer
range: float
minimum_value: 0
maximum_value: 100
unit:
  ucum_code: '%'

```
</details>