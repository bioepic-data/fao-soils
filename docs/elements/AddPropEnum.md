# Enum: AddPropEnum 




_Additional soil properties_



URI: [hwsd2:AddPropEnum](https://w3id.org/bioepic-data/fao-soils/hwsd2/AddPropEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| NONE | None | No additional properties |
| GELIC | None | Gelic (permafrost influenced) |
| VERTIC | None | Vertic (high shrink-swell) |




## Slots

| Name | Description |
| ---  | --- |
| [add_prop](add_prop.md) | Additional soil properties (Gelic, Vertic) |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/bioepic-data/fao-soils/hwsd2






## LinkML Source

<details>
```yaml
name: AddPropEnum
description: Additional soil properties
from_schema: https://w3id.org/bioepic-data/fao-soils/hwsd2
rank: 1000
permissible_values:
  NONE:
    text: NONE
    description: No additional properties
  GELIC:
    text: GELIC
    description: Gelic (permafrost influenced)
  VERTIC:
    text: VERTIC
    description: Vertic (high shrink-swell)

```
</details>