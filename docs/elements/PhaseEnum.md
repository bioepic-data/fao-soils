# Enum: PhaseEnum 




_Soil phase modifiers_



URI: [hwsd2:PhaseEnum](https://w3id.org/bioepic-data/fao-soils/hwsd2/PhaseEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| NONE | None | No phase |
| STONY | None | Stony phase |
| LITHIC | None | Lithic phase (shallow to bedrock) |
| PETRIC | None | Petric phase (cemented layer) |
| PETROCALCIC | None | Petrocalcic phase (cemented carbonate) |
| PETROGYPSIC | None | Petrogypsic phase (cemented gypsum) |
| PETROFERRIC | None | Petroferric phase (cemented iron) |
| PHREATIC | None | Phreatic phase (groundwater influenced) |
| FRAGIPAN | None | Fragipan phase (dense subsurface layer) |




## Slots

| Name | Description |
| ---  | --- |
| [phase1](phase1.md) | Primary soil phase (Stony, Lithic, Petric, etc |
| [phase2](phase2.md) | Secondary soil phase |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/bioepic-data/fao-soils/hwsd2






## LinkML Source

<details>
```yaml
name: PhaseEnum
description: Soil phase modifiers
from_schema: https://w3id.org/bioepic-data/fao-soils/hwsd2
rank: 1000
permissible_values:
  NONE:
    text: NONE
    description: No phase
  STONY:
    text: STONY
    description: Stony phase
  LITHIC:
    text: LITHIC
    description: Lithic phase (shallow to bedrock)
  PETRIC:
    text: PETRIC
    description: Petric phase (cemented layer)
  PETROCALCIC:
    text: PETROCALCIC
    description: Petrocalcic phase (cemented carbonate)
  PETROGYPSIC:
    text: PETROGYPSIC
    description: Petrogypsic phase (cemented gypsum)
  PETROFERRIC:
    text: PETROFERRIC
    description: Petroferric phase (cemented iron)
  PHREATIC:
    text: PHREATIC
    description: Phreatic phase (groundwater influenced)
  FRAGIPAN:
    text: FRAGIPAN
    description: Fragipan phase (dense subsurface layer)

```
</details>