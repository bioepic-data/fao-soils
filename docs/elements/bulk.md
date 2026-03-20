

# Slot: bulk 


_Bulk density_





URI: [hwsd2:bulk](https://w3id.org/bioepic-data/fao-soils/hwsd2/bulk)
Alias: bulk

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoilLayer](SoilLayer.md) | Detailed soil properties at a specific depth layer |  no  |






## Properties

* Range: [Float](Float.md)

* Minimum Value: 0

* Maximum Value: 3




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/bioepic-data/fao-soils/hwsd2




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | hwsd2:bulk |
| native | hwsd2:bulk |




## LinkML Source

<details>
```yaml
name: bulk
description: Bulk density
from_schema: https://w3id.org/bioepic-data/fao-soils/hwsd2
rank: 1000
alias: bulk
domain_of:
- SoilLayer
range: float
minimum_value: 0
maximum_value: 3
unit:
  ucum_code: g/cm3

```
</details>