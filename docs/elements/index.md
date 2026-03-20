# FAO Harmonized World Soil Database v2.0 Schema

LinkML schema for the FAO Harmonized World Soil Database (HWSD) version 2.0.

The HWSD v2.0 provides comprehensive soil data including physical and chemical properties
at multiple soil layers for global coverage. This database is essential for ecosystem
modeling, climate modeling, and agricultural applications.

Main components:
- Soil Mapping Units (SMU): Summary-level soil characteristics
- Soil Layers: Detailed physical and chemical properties at different depths
- Classification systems: WRB, FAO-90, USDA taxonomy
- Domain tables: Lookup tables for codes and classifications

URI: https://w3id.org/bioepic-data/fao-soils/hwsd2

Name: hwsd2



## Classes

| Class | Description |
| --- | --- |
| [SoilLayer](SoilLayer.md) | Detailed soil properties at a specific depth layer |
| [SoilMappingUnit](SoilMappingUnit.md) | A Soil Mapping Unit (SMU) represents a distinct area with relatively homogene... |
| [WRBClass](WRBClass.md) | World Reference Base (WRB) soil classification with RGB color codes |



## Slots

| Slot | Description |
| --- | --- |
| [add_prop](add_prop.md) | Additional soil properties (Gelic, Vertic) |
| [alum_sat](alum_sat.md) | Aluminium saturation percentage |
| [awc](awc.md) | Available Water Capacity |
| [awc_layer](awc_layer.md) | Available Water Capacity for rootable soil depth |
| [blue](blue.md) | Blue RGB color component (0-255) |
| [botdep](botdep.md) | Depth of bottom of layer |
| [bsat](bsat.md) | Base saturation percentage |
| [bulk](bulk.md) | Bulk density |
| [bulk_density](bulk_density.md) | Bulk density (SMU level) |
| [cec_clay](cec_clay.md) | Cation Exchange Capacity of clay fraction |
| [cec_eff](cec_eff.md) | Effective Cation Exchange Capacity (ECEC) |
| [cec_soil](cec_soil.md) | Cation Exchange Capacity of soil |
| [class_number](class_number.md) | Class number |
| [clay](clay.md) | Clay content percentage by weight |
| [cn_ratio](cn_ratio.md) | Carbon to nitrogen ratio (C/N) |
| [coarse](coarse.md) | Coarse fragments percentage by volume |
| [coverage](coverage.md) | Data source coverage (ESDB, CHINA, SOTWIS, etc |
| [divider](divider.md) | Divider value |
| [drainage](drainage.md) | Reference soil drainage class |
| [elec_cond](elec_cond.md) | Electric conductivity |
| [esp](esp.md) | Exchangeable Sodium Percentage |
| [fao90](fao90.md) | Soil Unit Symbol from FAO 1990 classification |
| [green](green.md) | Green RGB color component (0-255) |
| [gypsum](gypsum.md) | Gypsum content percentage by weight |
| [hwsd1_smu_id](hwsd1_smu_id.md) | Soil Mapping Unit identifier from HWSD version 1 |
| [hwsd2_smu_id](hwsd2_smu_id.md) | Soil Mapping Unit identifier in HWSD version 2 |
| [id](id.md) | Database internal ID |
| [id_class](id_class.md) | Class identifier |
| [il](il.md) | Impermeable layer depth in cm (ESDB) |
| [koppen](koppen.md) | Köppen-Geiger climate classification |
| [label](label.md) | Full label for WRB class |
| [layer](layer.md) | Depth layer code (D1 through D7) |
| [nsc](nsc.md) | National Soil Classification code |
| [nsc_mu_source1](nsc_mu_source1.md) | National Soil Classification source 1 |
| [nsc_mu_source2](nsc_mu_source2.md) | National Soil Classification source 2 |
| [org_carbon](org_carbon.md) | Organic carbon content percentage by weight |
| [ph_water](ph_water.md) | pH measured in water |
| [phase1](phase1.md) | Primary soil phase (Stony, Lithic, Petric, etc |
| [phase2](phase2.md) | Secondary soil phase |
| [red](red.md) | Red RGB color component (0-255) |
| [ref_bulk](ref_bulk.md) | Reference bulk density |
| [ref_bulk_density](ref_bulk_density.md) | Reference bulk density (SMU level) |
| [root_depth](root_depth.md) | Rooting depth category |
| [root_depth_layer](root_depth_layer.md) | Rootable soil depth for specific layer |
| [roots](roots.md) | Obstacle to roots depth in cm (ESDB) |
| [sand](sand.md) | Sand content percentage by weight |
| [sequence](sequence.md) | Sequence number in Soil Mapping Unit |
| [share](share.md) | Percentage share in Soil Mapping Unit |
| [silt](silt.md) | Silt content percentage by weight |
| [swr](swr.md) | Soil Water Regime (ESDB) |
| [symbol](symbol.md) | Symbol code for WRB class |
| [tcarbon_eq](tcarbon_eq.md) | Calcium carbonate equivalent percentage by weight |
| [teb](teb.md) | Total Exchangeable Bases |
| [texture_soter](texture_soter.md) | SOTER soil texture class |
| [texture_usda](texture_usda.md) | USDA soil texture class |
| [topdep](topdep.md) | Depth of top of layer |
| [total_n](total_n.md) | Total nitrogen content |
| [wise30s_smu_id](wise30s_smu_id.md) | Soil Mapping Unit identifier from WISE30s database |
| [wrb2](wrb2.md) | Dominant WRB 2022 soil group code (2-character HWSD/WRB symbol) |
| [wrb2_code](wrb2_code.md) | Numeric code for WRB2 dominant soil group |
| [wrb4](wrb4.md) | Soil Unit Symbol from World Reference Base 2022 (4-character code) |
| [wrb_phases](wrb_phases.md) | Detailed Soil Unit Symbol from WRB 2022 with phases |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AddPropEnum](AddPropEnum.md) | Additional soil properties |
| [CoverageEnum](CoverageEnum.md) | Data source coverage codes |
| [DrainageEnum](DrainageEnum.md) | Soil drainage classes |
| [FAOSoilTypeEnum](FAOSoilTypeEnum.md) | FAO World Reference Base (WRB) soil classification codes used in HWSD2 |
| [ILEnum](ILEnum.md) | Impermeable layer depth ranges (ESDB) |
| [KoppenEnum](KoppenEnum.md) | Köppen-Geiger climate classification |
| [PhaseEnum](PhaseEnum.md) | Soil phase modifiers |
| [RootDepthEnum](RootDepthEnum.md) | Root depth categories |
| [RootsEnum](RootsEnum.md) | Obstacle to roots depth ranges (ESDB) |
| [SWREnum](SWREnum.md) | Soil Water Regime classes (ESDB) |
| [TextureSOTEREnum](TextureSOTEREnum.md) | SOTER soil texture classes |
| [TextureUSDAEnum](TextureUSDAEnum.md) | USDA soil texture classes |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
