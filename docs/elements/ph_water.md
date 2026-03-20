

# Slot: ph_water 


_pH measured in water_





URI: [hwsd2:ph_water](https://w3id.org/bioepic-data/fao-soils/hwsd2/ph_water)
Alias: ph_water

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoilLayer](SoilLayer.md) | Detailed soil properties at a specific depth layer |  no  |






## Properties

* Range: [Float](Float.md)

* Minimum Value: 0

* Maximum Value: 14




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/bioepic-data/fao-soils/hwsd2




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | hwsd2:ph_water |
| native | hwsd2:ph_water |




## LinkML Source

<details>
```yaml
name: ph_water
description: pH measured in water
from_schema: https://w3id.org/bioepic-data/fao-soils/hwsd2
rank: 1000
alias: ph_water
domain_of:
- SoilLayer
range: float
minimum_value: 0
maximum_value: 14
unit:
  ucum_code: -log(H+)

```
</details>