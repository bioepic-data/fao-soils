# Enum: ILEnum 




_Impermeable layer depth ranges (ESDB)_



URI: [hwsd2:ILEnum](https://w3id.org/bioepic-data/fao-soils/hwsd2/ILEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| NONE | None | No impermeable layer |
| GT_150 | None | > 150 cm |
| 80_150 | None | 80-150 cm |
| 40_80 | None | 40-80 cm |
| LT_40 | None | < 40 cm |




## Slots

| Name | Description |
| ---  | --- |
| [il](il.md) | Impermeable layer depth in cm (ESDB) |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/bioepic-data/fao-soils/hwsd2






## LinkML Source

<details>
```yaml
name: ILEnum
description: Impermeable layer depth ranges (ESDB)
from_schema: https://w3id.org/bioepic-data/fao-soils/hwsd2
rank: 1000
permissible_values:
  NONE:
    text: NONE
    description: No impermeable layer
  GT_150:
    text: GT_150
    description: '> 150 cm'
  '80_150':
    text: '80_150'
    description: 80-150 cm
  '40_80':
    text: '40_80'
    description: 40-80 cm
  LT_40:
    text: LT_40
    description: < 40 cm

```
</details>