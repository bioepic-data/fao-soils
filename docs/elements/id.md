

# Slot: id 


_Database internal ID_





URI: [hwsd2:id](https://w3id.org/bioepic-data/fao-soils/hwsd2/id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoilMappingUnit](SoilMappingUnit.md) | A Soil Mapping Unit (SMU) represents a distinct area with relatively homogene... |  no  |
| [SoilLayer](SoilLayer.md) | Detailed soil properties at a specific depth layer |  no  |
| [WRBClass](WRBClass.md) | World Reference Base (WRB) soil classification with RGB color codes |  no  |






## Properties

* Range: [Integer](Integer.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/bioepic-data/fao-soils/hwsd2




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | hwsd2:id |
| native | hwsd2:id |




## LinkML Source

<details>
```yaml
name: id
description: Database internal ID
from_schema: https://w3id.org/bioepic-data/fao-soils/hwsd2
rank: 1000
identifier: true
alias: id
domain_of:
- SoilMappingUnit
- SoilLayer
- WRBClass
range: integer
required: true

```
</details>