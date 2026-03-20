

# Slot: bsat 


_Base saturation percentage_





URI: [hwsd2:bsat](https://w3id.org/bioepic-data/fao-soils/hwsd2/bsat)
Alias: bsat

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
| self | hwsd2:bsat |
| native | hwsd2:bsat |




## LinkML Source

<details>
```yaml
name: bsat
description: Base saturation percentage
from_schema: https://w3id.org/bioepic-data/fao-soils/hwsd2
rank: 1000
alias: bsat
domain_of:
- SoilLayer
range: float
minimum_value: 0
maximum_value: 100
unit:
  ucum_code: '% CECsoil'

```
</details>