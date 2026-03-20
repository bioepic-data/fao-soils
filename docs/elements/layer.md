

# Slot: layer 


_Depth layer code (D1 through D7)_





URI: [hwsd2:layer](https://w3id.org/bioepic-data/fao-soils/hwsd2/layer)
Alias: layer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoilLayer](SoilLayer.md) | Detailed soil properties at a specific depth layer |  no  |






## Properties

* Range: [String](String.md)

* Regex pattern: `^D[1-7]$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/bioepic-data/fao-soils/hwsd2




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | hwsd2:layer |
| native | hwsd2:layer |




## LinkML Source

<details>
```yaml
name: layer
description: Depth layer code (D1 through D7)
from_schema: https://w3id.org/bioepic-data/fao-soils/hwsd2
rank: 1000
alias: layer
domain_of:
- SoilLayer
range: string
pattern: ^D[1-7]$

```
</details>