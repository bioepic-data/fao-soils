# Enum: FAOSoilTypeEnum 




_FAO World Reference Base (WRB) soil classification codes used in HWSD2. This enum is adapted from the LinkML valuesets FAO soil valueset, but uses the 2-character HWSD/WRB symbols as permissible values so it can type the existing `wrb2` field directly._



URI: [hwsd2:FAOSoilTypeEnum](https://w3id.org/bioepic-data/fao-soils/hwsd2/FAOSoilTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| AC | None | Acrisols - soils with subsurface accumulation of low-activity clays and low b... |
| AL | None | Alisols - soils with high aluminium saturation and low base saturation |
| AN | ENVO:00002232 | Andosols - soils developed from volcanic ash with unique physical and chemica... |
| AR | ENVO:00002229 | Arenosols - sandy soils with weak horizon development |
| AT | None | Anthrosols - soils strongly modified by human activities |
| CH | None | Chernozems - very dark, fertile soils with thick mollic horizon |
| CL | None | Calcisols - soils with secondary calcium carbonate accumulation |
| CM | None | Cambisols - soils with beginning of horizon differentiation |
| CR | ENVO:00002236 | Cryosols - soils formed under permafrost conditions |
| FL | ENVO:00002273 | Fluvisols - soils developed from recent alluvial deposits |
| FR | None | Ferralsols - highly weathered soils with low-activity clay minerals |
| GG | ENVO:00000133 | Glaciers - areas covered by permanent ice (non-soil land cover category carri... |
| GL | ENVO:00002244 | Gleysols - soils with permanent or temporary waterlogging |
| GY | None | Gypsisols - soils with secondary gypsum accumulation |
| HS | ENVO:00005774 | Histosols - soils formed from organic materials (peat soils) |
| KS | None | Kastanozems - soils with chestnut-colored mollic horizon |
| LP | None | Leptosols - shallow soils over hard rock or highly calcareous material |
| LV | None | Luvisols - soils with clay illuviation and high base saturation |
| LX | None | Lixisols - soils with clay illuviation and low base saturation |
| NT | None | Nitisols - soils with deep, well-structured clay horizons |
| PH | None | Phaeozems - soils with dark mollic horizon and high base saturation |
| PL | None | Planosols - soils with abrupt textural change and impermeable subsoil |
| PT | None | Plinthosols - soils with iron-rich, humus-poor mixture that hardens irreversi... |
| PZ | None | Podzols - soils with subsurface accumulation of aluminium and iron complexes ... |
| RG | None | Regosols - weakly developed soils without significant horizon differentiation |
| RT | None | Retisols - soils with clay migration and tonguing of overlying material |
| SC | ENVO:00002252 | Solonchaks - soils with high salt content |
| SN | None | Solonetz - soils with high exchangeable sodium content |
| ST | None | Stagnosols - soils with seasonal waterlogging in upper horizons |
| TC | None | Technosols - soils containing significant amounts of technical artifacts |
| UM | None | Umbrisols - soils with dark acidic surface horizon |
| VR | ENVO:00002254 | Vertisols - clay-rich soils with shrink-swell properties |
| WR | ENVO:01001320 | Open inland water - areas covered by permanent water bodies (non-soil land co... |
| ND | None | No data - areas where soil data is not available |




## Slots

| Name | Description |
| ---  | --- |
| [wrb2](wrb2.md) | Dominant WRB 2022 soil group code (2-character HWSD/WRB symbol) |





## See Also

* [https://github.com/linkml/valuesets/pull/26](https://github.com/linkml/valuesets/pull/26)
* [https://raw.githubusercontent.com/linkml/valuesets/main/src/valuesets/schema/earth_science/fao_soil.yaml](https://raw.githubusercontent.com/linkml/valuesets/main/src/valuesets/schema/earth_science/fao_soil.yaml)
* [https://www.fao.org/soils-portal/data-hub/soil-classification/world-reference-base/en/](https://www.fao.org/soils-portal/data-hub/soil-classification/world-reference-base/en/)
* [https://www.isric.org/explore/hwsd](https://www.isric.org/explore/hwsd)

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/bioepic-data/fao-soils/hwsd2






## LinkML Source

<details>
```yaml
name: FAOSoilTypeEnum
description: FAO World Reference Base (WRB) soil classification codes used in HWSD2.
  This enum is adapted from the LinkML valuesets FAO soil valueset, but uses the 2-character
  HWSD/WRB symbols as permissible values so it can type the existing `wrb2` field
  directly.
from_schema: https://w3id.org/bioepic-data/fao-soils/hwsd2
see_also:
- https://github.com/linkml/valuesets/pull/26
- https://raw.githubusercontent.com/linkml/valuesets/main/src/valuesets/schema/earth_science/fao_soil.yaml
- https://www.fao.org/soils-portal/data-hub/soil-classification/world-reference-base/en/
- https://www.isric.org/explore/hwsd
rank: 1000
permissible_values:
  AC:
    text: AC
    description: Acrisols - soils with subsurface accumulation of low-activity clays
      and low base saturation
    annotations:
      soil_name:
        tag: soil_name
        value: Acrisols
      fao_id:
        tag: fao_id
        value: 1
      color_rgb:
        tag: color_rgb
        value: 247,152,4
  AL:
    text: AL
    description: Alisols - soils with high aluminium saturation and low base saturation
    annotations:
      soil_name:
        tag: soil_name
        value: Alisols
      fao_id:
        tag: fao_id
        value: 2
      color_rgb:
        tag: color_rgb
        value: 255,255,190
  AN:
    text: AN
    description: Andosols - soils developed from volcanic ash with unique physical
      and chemical properties
    meaning: ENVO:00002232
    annotations:
      soil_name:
        tag: soil_name
        value: Andosols
      fao_id:
        tag: fao_id
        value: 3
      color_rgb:
        tag: color_rgb
        value: 254,0,0
  AR:
    text: AR
    description: Arenosols - sandy soils with weak horizon development
    meaning: ENVO:00002229
    annotations:
      soil_name:
        tag: soil_name
        value: Arenosols
      fao_id:
        tag: fao_id
        value: 4
      color_rgb:
        tag: color_rgb
        value: 245,212,161
  AT:
    text: AT
    description: Anthrosols - soils strongly modified by human activities
    annotations:
      soil_name:
        tag: soil_name
        value: Anthrosols
      fao_id:
        tag: fao_id
        value: 5
      color_rgb:
        tag: color_rgb
        value: 207,152,4
  CH:
    text: CH
    description: Chernozems - very dark, fertile soils with thick mollic horizon
    annotations:
      soil_name:
        tag: soil_name
        value: Chernozems
      fao_id:
        tag: fao_id
        value: 6
      color_rgb:
        tag: color_rgb
        value: 145,77,53
  CL:
    text: CL
    description: Calcisols - soils with secondary calcium carbonate accumulation
    annotations:
      soil_name:
        tag: soil_name
        value: Calcisols
      fao_id:
        tag: fao_id
        value: 7
      color_rgb:
        tag: color_rgb
        value: 254,244,0
  CM:
    text: CM
    description: Cambisols - soils with beginning of horizon differentiation
    annotations:
      soil_name:
        tag: soil_name
        value: Cambisols
      fao_id:
        tag: fao_id
        value: 8
      color_rgb:
        tag: color_rgb
        value: 254,190,0
  CR:
    text: CR
    description: Cryosols - soils formed under permafrost conditions
    meaning: ENVO:00002236
    annotations:
      soil_name:
        tag: soil_name
        value: Cryosols
      fao_id:
        tag: fao_id
        value: 9
      color_rgb:
        tag: color_rgb
        value: 75,61,172
  FL:
    text: FL
    description: Fluvisols - soils developed from recent alluvial deposits
    meaning: ENVO:00002273
    annotations:
      soil_name:
        tag: soil_name
        value: Fluvisols
      fao_id:
        tag: fao_id
        value: 10
      color_rgb:
        tag: color_rgb
        value: 0,254,253
  FR:
    text: FR
    description: Ferralsols - highly weathered soils with low-activity clay minerals
    annotations:
      soil_name:
        tag: soil_name
        value: Ferralsols
      fao_id:
        tag: fao_id
        value: 11
      color_rgb:
        tag: color_rgb
        value: 255,135,33
  GG:
    text: GG
    description: Glaciers - areas covered by permanent ice (non-soil land cover category
      carried in HWSD2)
    meaning: ENVO:00000133
    annotations:
      soil_name:
        tag: soil_name
        value: Glaciers
      fao_id:
        tag: fao_id
        value: 12
      color_rgb:
        tag: color_rgb
        value: 212,212,212
  GL:
    text: GL
    description: Gleysols - soils with permanent or temporary waterlogging
    meaning: ENVO:00002244
    annotations:
      soil_name:
        tag: soil_name
        value: Gleysols
      fao_id:
        tag: fao_id
        value: 13
      color_rgb:
        tag: color_rgb
        value: 128,131,217
  GY:
    text: GY
    description: Gypsisols - soils with secondary gypsum accumulation
    annotations:
      soil_name:
        tag: soil_name
        value: Gypsisols
      fao_id:
        tag: fao_id
        value: 14
      color_rgb:
        tag: color_rgb
        value: 254,246,164
  HS:
    text: HS
    description: Histosols - soils formed from organic materials (peat soils)
    meaning: ENVO:00005774
    annotations:
      soil_name:
        tag: soil_name
        value: Histosols
      fao_id:
        tag: fao_id
        value: 15
      color_rgb:
        tag: color_rgb
        value: 112,107,102
  KS:
    text: KS
    description: Kastanozems - soils with chestnut-colored mollic horizon
    annotations:
      soil_name:
        tag: soil_name
        value: Kastanozems
      fao_id:
        tag: fao_id
        value: 17
      color_rgb:
        tag: color_rgb
        value: 202,147,127
  LP:
    text: LP
    description: Leptosols - shallow soils over hard rock or highly calcareous material
    annotations:
      soil_name:
        tag: soil_name
        value: Leptosols
      fao_id:
        tag: fao_id
        value: 18
      color_rgb:
        tag: color_rgb
        value: 209,209,209
  LV:
    text: LV
    description: Luvisols - soils with clay illuviation and high base saturation
    annotations:
      soil_name:
        tag: soil_name
        value: Luvisols
      fao_id:
        tag: fao_id
        value: 19
      color_rgb:
        tag: color_rgb
        value: 250,132,132
  LX:
    text: LX
    description: Lixisols - soils with clay illuviation and low base saturation
    annotations:
      soil_name:
        tag: soil_name
        value: Lixisols
      fao_id:
        tag: fao_id
        value: 20
      color_rgb:
        tag: color_rgb
        value: 255,190,190
  NT:
    text: NT
    description: Nitisols - soils with deep, well-structured clay horizons
    annotations:
      soil_name:
        tag: soil_name
        value: Nitisols
      fao_id:
        tag: fao_id
        value: 21
      color_rgb:
        tag: color_rgb
        value: 255,167,127
  PH:
    text: PH
    description: Phaeozems - soils with dark mollic horizon and high base saturation
    annotations:
      soil_name:
        tag: soil_name
        value: Phaeozems
      fao_id:
        tag: fao_id
        value: 22
      color_rgb:
        tag: color_rgb
        value: 189,100,70
  PL:
    text: PL
    description: Planosols - soils with abrupt textural change and impermeable subsoil
    annotations:
      soil_name:
        tag: soil_name
        value: Planosols
      fao_id:
        tag: fao_id
        value: 23
      color_rgb:
        tag: color_rgb
        value: 247,125,58
  PT:
    text: PT
    description: Plinthosols - soils with iron-rich, humus-poor mixture that hardens
      irreversibly
    annotations:
      soil_name:
        tag: soil_name
        value: Plinthosols
      fao_id:
        tag: fao_id
        value: 24
      color_rgb:
        tag: color_rgb
        value: 115,0,0
  PZ:
    text: PZ
    description: Podzols - soils with subsurface accumulation of aluminium and iron
      complexes with organic matter (spodic horizon)
    annotations:
      soil_name:
        tag: soil_name
        value: Podzols
      fao_id:
        tag: fao_id
        value: 25
      color_rgb:
        tag: color_rgb
        value: 12,217,0
  RG:
    text: RG
    description: Regosols - weakly developed soils without significant horizon differentiation
    annotations:
      soil_name:
        tag: soil_name
        value: Regosols
      fao_id:
        tag: fao_id
        value: 26
      color_rgb:
        tag: color_rgb
        value: 254,227,164
  RT:
    text: RT
    description: Retisols - soils with clay migration and tonguing of overlying material
    annotations:
      soil_name:
        tag: soil_name
        value: Retisols
      fao_id:
        tag: fao_id
        value: 27
      color_rgb:
        tag: color_rgb
        value: 254,194,194
  SC:
    text: SC
    description: Solonchaks - soils with high salt content
    meaning: ENVO:00002252
    annotations:
      soil_name:
        tag: soil_name
        value: Solonchaks
      fao_id:
        tag: fao_id
        value: 28
      color_rgb:
        tag: color_rgb
        value: 254,0,250
  SN:
    text: SN
    description: Solonetz - soils with high exchangeable sodium content
    annotations:
      soil_name:
        tag: soil_name
        value: Solonetz
      fao_id:
        tag: fao_id
        value: 29
      color_rgb:
        tag: color_rgb
        value: 249,194,254
  ST:
    text: ST
    description: Stagnosols - soils with seasonal waterlogging in upper horizons
    annotations:
      soil_name:
        tag: soil_name
        value: Stagnosols
      fao_id:
        tag: fao_id
        value: 30
      color_rgb:
        tag: color_rgb
        value: 64,192,233
  TC:
    text: TC
    description: Technosols - soils containing significant amounts of technical artifacts
    annotations:
      soil_name:
        tag: soil_name
        value: Technosols
      fao_id:
        tag: fao_id
        value: 31
      color_rgb:
        tag: color_rgb
        value: 145,0,157
  UM:
    text: UM
    description: Umbrisols - soils with dark acidic surface horizon
    annotations:
      soil_name:
        tag: soil_name
        value: Umbrisols
      fao_id:
        tag: fao_id
        value: 32
      color_rgb:
        tag: color_rgb
        value: 115,142,127
  VR:
    text: VR
    description: Vertisols - clay-rich soils with shrink-swell properties
    meaning: ENVO:00002254
    annotations:
      soil_name:
        tag: soil_name
        value: Vertisols
      fao_id:
        tag: fao_id
        value: 33
      color_rgb:
        tag: color_rgb
        value: 197,0,255
  WR:
    text: WR
    description: Open inland water - areas covered by permanent water bodies (non-soil
      land cover category carried in HWSD2)
    meaning: ENVO:01001320
    annotations:
      soil_name:
        tag: soil_name
        value: Open inland water
      fao_id:
        tag: fao_id
        value: 34
      color_rgb:
        tag: color_rgb
        value: 0,0,255
  ND:
    text: ND
    description: No data - areas where soil data is not available
    annotations:
      soil_name:
        tag: soil_name
        value: No data
      fao_id:
        tag: fao_id
        value: 35
      color_rgb:
        tag: color_rgb
        value: 255,255,255

```
</details>