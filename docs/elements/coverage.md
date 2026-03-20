

# Slot: coverage 


_Data source coverage (ESDB, CHINA, SOTWIS, etc.)_





URI: [hwsd2:coverage](https://w3id.org/bioepic-data/fao-soils/hwsd2/coverage)
Alias: coverage

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoilMappingUnit](SoilMappingUnit.md) | A Soil Mapping Unit (SMU) represents a distinct area with relatively homogene... |  no  |
| [SoilLayer](SoilLayer.md) | Detailed soil properties at a specific depth layer |  no  |






## Properties

* Range: [CoverageEnum](CoverageEnum.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/bioepic-data/fao-soils/hwsd2




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | hwsd2:coverage |
| native | hwsd2:coverage |




## LinkML Source

<details>
```yaml
name: coverage
description: Data source coverage (ESDB, CHINA, SOTWIS, etc.)
from_schema: https://w3id.org/bioepic-data/fao-soils/hwsd2
rank: 1000
alias: coverage
domain_of:
- SoilMappingUnit
- SoilLayer
range: CoverageEnum

```
</details>