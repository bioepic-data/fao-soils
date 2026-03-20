

# Slot: org_carbon 


_Organic carbon content percentage by weight_





URI: [hwsd2:org_carbon](https://w3id.org/bioepic-data/fao-soils/hwsd2/org_carbon)
Alias: org_carbon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
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
| self | hwsd2:org_carbon |
| native | hwsd2:org_carbon |




## LinkML Source

<details>
```yaml
name: org_carbon
description: Organic carbon content percentage by weight
from_schema: https://w3id.org/bioepic-data/fao-soils/hwsd2
rank: 1000
alias: org_carbon
domain_of:
- SoilLayer
range: float
minimum_value: 0
maximum_value: 100
unit:
  ucum_code: '% weight'

```
</details>