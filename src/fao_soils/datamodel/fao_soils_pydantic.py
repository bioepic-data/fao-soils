from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "None"
version = "2.0.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )

    @model_serializer(mode='wrap', when_used='unless-none')
    def treat_empty_lists_as_none(
            self, handler: SerializerFunctionWrapHandler,
            info: SerializationInfo) -> dict[str, Any]:
        if info.exclude_none:
            _instance = self.model_copy()
            for field, field_info in type(_instance).model_fields.items():
                if getattr(_instance, field) == [] and not(
                        field_info.is_required()):
                    setattr(_instance, field, None)
        else:
            _instance = self
        return handler(_instance, info)



class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'hwsd2',
     'default_range': 'string',
     'description': 'LinkML schema for the FAO Harmonized World Soil Database '
                    '(HWSD) version 2.0.\n'
                    '\n'
                    'The HWSD v2.0 provides comprehensive soil data including '
                    'physical and chemical properties\n'
                    'at multiple soil layers for global coverage. This database is '
                    'essential for ecosystem\n'
                    'modeling, climate modeling, and agricultural applications.\n'
                    '\n'
                    'Main components:\n'
                    '- Soil Mapping Units (SMU): Summary-level soil '
                    'characteristics\n'
                    '- Soil Layers: Detailed physical and chemical properties at '
                    'different depths\n'
                    '- Classification systems: WRB, FAO-90, USDA taxonomy\n'
                    '- Domain tables: Lookup tables for codes and classifications',
     'id': 'https://w3id.org/bioepic-data/fao-soils/hwsd2',
     'imports': ['linkml:types'],
     'license': 'CC-BY-4.0',
     'name': 'hwsd2',
     'prefixes': {'fao_soils': {'prefix_prefix': 'fao_soils',
                                'prefix_reference': 'https://w3id.org/bioepic-data/fao-soils/'},
                  'hwsd2': {'prefix_prefix': 'hwsd2',
                            'prefix_reference': 'https://w3id.org/bioepic-data/fao-soils/hwsd2/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'qudt': {'prefix_prefix': 'qudt',
                           'prefix_reference': 'http://qudt.org/schema/qudt/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'see_also': ['https://bioepic-data.github.io/fao-soils',
                  'https://www.fao.org/soils-portal/data-hub/soil-maps-and-databases/harmonized-world-soil-database-v20/en/'],
     'source_file': 'src/fao_soils/schema/fao_soils.yaml',
     'title': 'FAO Harmonized World Soil Database v2.0 Schema'} )

class CoverageEnum(str, Enum):
    """
    Data source coverage codes
    """
    NONE = "NONE"
    """
    None
    """
    ESDB = "ESDB"
    """
    European Soil Database
    """
    CHINA = "CHINA"
    """
    China soil database
    """
    SOTWIS = "SOTWIS"
    """
    Soil and Terrain Database
    """
    DSMW = "DSMW"
    """
    Digital Soil Map of the World
    """
    WISE30s = "WISE30s"
    """
    World Inventory of Soil Emission Potentials (30 arcsec)
    """
    AFGHANISTAN = "AFGHANISTAN"
    """
    Afghanistan soil database
    """
    GHANA = "GHANA"
    """
    Ghana soil database
    """
    TURKEY = "TURKEY"
    """
    Turkey soil database
    """


class DrainageEnum(str, Enum):
    """
    Soil drainage classes
    """
    E = "E"
    """
    Excessively drained
    """
    SE = "SE"
    """
    Somewhat excessively drained
    """
    W = "W"
    """
    Well drained
    """
    MW = "MW"
    """
    Moderately well drained
    """
    I = "I"
    """
    Imperfectly drained
    """
    P = "P"
    """
    Poorly drained
    """
    VP = "VP"
    """
    Very poorly drained
    """


class RootDepthEnum(str, Enum):
    """
    Root depth categories
    """
    DEEP = "DEEP"
    """
    Deep (> 100cm)
    """
    MODERATELY_DEEP = "MODERATELY_DEEP"
    """
    Moderately Deep (< 100cm)
    """
    SHALLOW = "SHALLOW"
    """
    Shallow (< 50cm)
    """
    VERY_SHALLOW = "VERY_SHALLOW"
    """
    Very shallow (< 10cm)
    """


class RootsEnum(str, Enum):
    """
    Obstacle to roots depth ranges (ESDB)
    """
    NONE = "NONE"
    """
    No obstacle
    """
    GT_80 = "GT_80"
    """
    > 80 cm
    """
    number_60_80 = "60_80"
    """
    60-80 cm
    """
    number_40_60 = "40_60"
    """
    40-60 cm
    """
    number_20_40 = "20_40"
    """
    20-40 cm
    """
    number_0_80 = "0_80"
    """
    0-80 cm
    """
    number_0_20 = "0_20"
    """
    0-20 cm
    """


class ILEnum(str, Enum):
    """
    Impermeable layer depth ranges (ESDB)
    """
    NONE = "NONE"
    """
    No impermeable layer
    """
    GT_150 = "GT_150"
    """
    > 150 cm
    """
    number_80_150 = "80_150"
    """
    80-150 cm
    """
    number_40_80 = "40_80"
    """
    40-80 cm
    """
    LT_40 = "LT_40"
    """
    < 40 cm
    """


class SWREnum(str, Enum):
    """
    Soil Water Regime classes (ESDB)
    """
    NONE = "NONE"
    """
    Not applicable
    """
    SLIGHTLY_WET = "SLIGHTLY_WET"
    """
    Slightly wet
    """
    MODERATELY_WET = "MODERATELY_WET"
    """
    Moderately wet
    """
    WET = "WET"
    """
    Wet
    """
    VERY_WET = "VERY_WET"
    """
    Very wet
    """


class PhaseEnum(str, Enum):
    """
    Soil phase modifiers
    """
    NONE = "NONE"
    """
    No phase
    """
    STONY = "STONY"
    """
    Stony phase
    """
    LITHIC = "LITHIC"
    """
    Lithic phase (shallow to bedrock)
    """
    PETRIC = "PETRIC"
    """
    Petric phase (cemented layer)
    """
    PETROCALCIC = "PETROCALCIC"
    """
    Petrocalcic phase (cemented carbonate)
    """
    PETROGYPSIC = "PETROGYPSIC"
    """
    Petrogypsic phase (cemented gypsum)
    """
    PETROFERRIC = "PETROFERRIC"
    """
    Petroferric phase (cemented iron)
    """
    PHREATIC = "PHREATIC"
    """
    Phreatic phase (groundwater influenced)
    """
    FRAGIPAN = "FRAGIPAN"
    """
    Fragipan phase (dense subsurface layer)
    """


class AddPropEnum(str, Enum):
    """
    Additional soil properties
    """
    NONE = "NONE"
    """
    No additional properties
    """
    GELIC = "GELIC"
    """
    Gelic (permafrost influenced)
    """
    VERTIC = "VERTIC"
    """
    Vertic (high shrink-swell)
    """


class KoppenEnum(str, Enum):
    """
    Köppen-Geiger climate classification
    """
    A = "A"
    """
    Tropical
    """
    B = "B"
    """
    Arid
    """
    C = "C"
    """
    Temperate
    """
    D = "D"
    """
    Cold
    """
    E = "E"
    """
    Polar
    """


class TextureUSDAEnum(str, Enum):
    """
    USDA soil texture classes
    """
    NONE = "NONE"
    """
    Not classified
    """
    CLAY_HEAVY = "CLAY_HEAVY"
    """
    Clay (heavy)
    """
    SILTY_CLAY = "SILTY_CLAY"
    """
    Silty clay
    """
    CLAY_LIGHT = "CLAY_LIGHT"
    """
    Clay (light)
    """
    SILTY_CLAY_LOAM = "SILTY_CLAY_LOAM"
    """
    Silty clay loam
    """
    CLAY_LOAM = "CLAY_LOAM"
    """
    Clay loam
    """
    SILT = "SILT"
    """
    Silt
    """
    SILT_LOAM = "SILT_LOAM"
    """
    Silt loam
    """
    SANDY_CLAY = "SANDY_CLAY"
    """
    Sandy clay
    """
    LOAM = "LOAM"
    """
    Loam
    """


class TextureSOTEREnum(str, Enum):
    """
    SOTER soil texture classes
    """
    C = "C"
    """
    Coarse
    """
    M = "M"
    """
    Medium
    """
    F = "F"
    """
    Fine
    """
    V = "V"
    """
    Very Fine
    """
    Z = "Z"
    """
    Medium Fine
    """



class SoilMappingUnit(ConfiguredBaseModel):
    """
    A Soil Mapping Unit (SMU) represents a distinct area with relatively homogeneous
    soil characteristics. Each SMU may contain multiple soil types with their
    proportional shares.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'hwsd2:SoilMappingUnit',
         'from_schema': 'https://w3id.org/bioepic-data/fao-soils/hwsd2'})

    id: int = Field(default=..., description="""Database internal ID""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer', 'WRBClass']} })
    hwsd2_smu_id: int = Field(default=..., description="""Soil Mapping Unit identifier in HWSD version 2""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer']} })
    wise30s_smu_id: Optional[str] = Field(default=None, description="""Soil Mapping Unit identifier from WISE30s database""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer']} })
    hwsd1_smu_id: Optional[int] = Field(default=None, description="""Soil Mapping Unit identifier from HWSD version 1""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer']} })
    coverage: Optional[CoverageEnum] = Field(default=None, description="""Data source coverage (ESDB, CHINA, SOTWIS, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer']} })
    share: Optional[float] = Field(default=None, description="""Percentage share in Soil Mapping Unit""", ge=0, le=100, json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer'], 'unit': {'ucum_code': '%'}} })
    wrb4: Optional[str] = Field(default=None, description="""Soil Unit Symbol from World Reference Base 2022 (4-character code)""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer']} })
    wrb_phases: Optional[str] = Field(default=None, description="""Detailed Soil Unit Symbol from WRB 2022 with phases""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer']} })
    wrb2: Optional[str] = Field(default=None, description="""Soil Unit Symbol from WRB 2022 (2-character code)""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer']} })
    wrb2_code: Optional[str] = Field(default=None, description="""Numeric code for WRB2 dominant soil group""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit']} })
    fao90: Optional[str] = Field(default=None, description="""Soil Unit Symbol from FAO 1990 classification""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer']} })
    koppen: Optional[KoppenEnum] = Field(default=None, description="""Köppen-Geiger climate classification""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit']} })
    texture_usda: Optional[TextureUSDAEnum] = Field(default=None, description="""USDA soil texture class""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer']} })
    ref_bulk_density: Optional[float] = Field(default=None, description="""Reference bulk density (SMU level)""", ge=0, le=3, json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit'], 'unit': {'ucum_code': 'g/cm3'}} })
    bulk_density: Optional[float] = Field(default=None, description="""Bulk density (SMU level)""", ge=0, le=3, json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit'], 'unit': {'ucum_code': 'g/cm3'}} })
    drainage: Optional[DrainageEnum] = Field(default=None, description="""Reference soil drainage class""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer']} })
    root_depth: Optional[RootDepthEnum] = Field(default=None, description="""Rooting depth category""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit']} })
    awc: Optional[float] = Field(default=None, description="""Available Water Capacity""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit'], 'unit': {'ucum_code': 'mm/m'}} })
    phase1: Optional[PhaseEnum] = Field(default=None, description="""Primary soil phase (Stony, Lithic, Petric, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer']} })
    phase2: Optional[PhaseEnum] = Field(default=None, description="""Secondary soil phase""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer']} })
    roots: Optional[RootsEnum] = Field(default=None, description="""Obstacle to roots depth in cm (ESDB)""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer']} })
    il: Optional[ILEnum] = Field(default=None, description="""Impermeable layer depth in cm (ESDB)""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer']} })
    add_prop: Optional[AddPropEnum] = Field(default=None, description="""Additional soil properties (Gelic, Vertic)""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer']} })


class SoilLayer(ConfiguredBaseModel):
    """
    Detailed soil properties at a specific depth layer. Each Soil Mapping Unit
    can have multiple layers (typically D1 through D7) representing different
    soil horizons from surface to depth.

    Contains comprehensive physical properties (texture, bulk density), chemical
    properties (pH, organic carbon, nutrients), and cation exchange characteristics.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'hwsd2:SoilLayer',
         'from_schema': 'https://w3id.org/bioepic-data/fao-soils/hwsd2'})

    id: int = Field(default=..., description="""Database internal ID""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer', 'WRBClass']} })
    hwsd2_smu_id: int = Field(default=..., description="""Soil Mapping Unit identifier in HWSD version 2""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer']} })
    nsc_mu_source1: Optional[str] = Field(default=None, description="""National Soil Classification source 1""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilLayer']} })
    nsc_mu_source2: Optional[str] = Field(default=None, description="""National Soil Classification source 2""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilLayer']} })
    wise30s_smu_id: Optional[str] = Field(default=None, description="""Soil Mapping Unit identifier from WISE30s database""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer']} })
    hwsd1_smu_id: Optional[int] = Field(default=None, description="""Soil Mapping Unit identifier from HWSD version 1""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer']} })
    coverage: Optional[CoverageEnum] = Field(default=None, description="""Data source coverage (ESDB, CHINA, SOTWIS, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer']} })
    sequence: Optional[int] = Field(default=None, description="""Sequence number in Soil Mapping Unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilLayer']} })
    share: Optional[float] = Field(default=None, description="""Percentage share in Soil Mapping Unit""", ge=0, le=100, json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer'], 'unit': {'ucum_code': '%'}} })
    nsc: Optional[str] = Field(default=None, description="""National Soil Classification code""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilLayer']} })
    wrb_phases: Optional[str] = Field(default=None, description="""Detailed Soil Unit Symbol from WRB 2022 with phases""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer']} })
    wrb4: Optional[str] = Field(default=None, description="""Soil Unit Symbol from World Reference Base 2022 (4-character code)""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer']} })
    wrb2: Optional[str] = Field(default=None, description="""Soil Unit Symbol from WRB 2022 (2-character code)""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer']} })
    fao90: Optional[str] = Field(default=None, description="""Soil Unit Symbol from FAO 1990 classification""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer']} })
    root_depth_layer: Optional[str] = Field(default=None, description="""Rootable soil depth for specific layer""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilLayer']} })
    phase1: Optional[PhaseEnum] = Field(default=None, description="""Primary soil phase (Stony, Lithic, Petric, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer']} })
    phase2: Optional[PhaseEnum] = Field(default=None, description="""Secondary soil phase""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer']} })
    roots: Optional[RootsEnum] = Field(default=None, description="""Obstacle to roots depth in cm (ESDB)""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer']} })
    il: Optional[ILEnum] = Field(default=None, description="""Impermeable layer depth in cm (ESDB)""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer']} })
    swr: Optional[SWREnum] = Field(default=None, description="""Soil Water Regime (ESDB)""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilLayer']} })
    drainage: Optional[DrainageEnum] = Field(default=None, description="""Reference soil drainage class""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer']} })
    awc_layer: Optional[str] = Field(default=None, description="""Available Water Capacity for rootable soil depth""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilLayer'], 'unit': {'ucum_code': 'mm'}} })
    add_prop: Optional[AddPropEnum] = Field(default=None, description="""Additional soil properties (Gelic, Vertic)""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer']} })
    layer: Optional[str] = Field(default=None, description="""Depth layer code (D1 through D7)""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilLayer']} })
    topdep: Optional[int] = Field(default=None, description="""Depth of top of layer""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['SoilLayer'], 'unit': {'ucum_code': 'cm'}} })
    botdep: Optional[int] = Field(default=None, description="""Depth of bottom of layer""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['SoilLayer'], 'unit': {'ucum_code': 'cm'}} })
    coarse: Optional[float] = Field(default=None, description="""Coarse fragments percentage by volume""", ge=0, le=100, json_schema_extra = { "linkml_meta": {'domain_of': ['SoilLayer'], 'unit': {'ucum_code': '% volume'}} })
    sand: Optional[float] = Field(default=None, description="""Sand content percentage by weight""", ge=0, le=100, json_schema_extra = { "linkml_meta": {'domain_of': ['SoilLayer'], 'unit': {'ucum_code': '% weight'}} })
    silt: Optional[float] = Field(default=None, description="""Silt content percentage by weight""", ge=0, le=100, json_schema_extra = { "linkml_meta": {'domain_of': ['SoilLayer'], 'unit': {'ucum_code': '% weight'}} })
    clay: Optional[float] = Field(default=None, description="""Clay content percentage by weight""", ge=0, le=100, json_schema_extra = { "linkml_meta": {'domain_of': ['SoilLayer'], 'unit': {'ucum_code': '% weight'}} })
    texture_usda: Optional[TextureUSDAEnum] = Field(default=None, description="""USDA soil texture class""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer']} })
    texture_soter: Optional[TextureSOTEREnum] = Field(default=None, description="""SOTER soil texture class""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilLayer']} })
    bulk: Optional[float] = Field(default=None, description="""Bulk density""", ge=0, le=3, json_schema_extra = { "linkml_meta": {'domain_of': ['SoilLayer'], 'unit': {'ucum_code': 'g/cm3'}} })
    ref_bulk: Optional[float] = Field(default=None, description="""Reference bulk density""", ge=0, le=3, json_schema_extra = { "linkml_meta": {'domain_of': ['SoilLayer'], 'unit': {'ucum_code': 'g/cm3'}} })
    org_carbon: Optional[float] = Field(default=None, description="""Organic carbon content percentage by weight""", ge=0, le=100, json_schema_extra = { "linkml_meta": {'domain_of': ['SoilLayer'], 'unit': {'ucum_code': '% weight'}} })
    ph_water: Optional[float] = Field(default=None, description="""pH measured in water""", ge=0, le=14, json_schema_extra = { "linkml_meta": {'domain_of': ['SoilLayer'], 'unit': {'ucum_code': '-log(H+)'}} })
    total_n: Optional[float] = Field(default=None, description="""Total nitrogen content""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['SoilLayer'], 'unit': {'ucum_code': 'g/kg'}} })
    cn_ratio: Optional[float] = Field(default=None, description="""Carbon to nitrogen ratio (C/N)""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['SoilLayer']} })
    cec_soil: Optional[float] = Field(default=None, description="""Cation Exchange Capacity of soil""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['SoilLayer'], 'unit': {'ucum_code': 'cmolc/kg'}} })
    cec_clay: Optional[float] = Field(default=None, description="""Cation Exchange Capacity of clay fraction""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['SoilLayer'], 'unit': {'ucum_code': 'cmolc/kg'}} })
    cec_eff: Optional[float] = Field(default=None, description="""Effective Cation Exchange Capacity (ECEC)""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['SoilLayer'], 'unit': {'ucum_code': 'cmolc/kg'}} })
    teb: Optional[float] = Field(default=None, description="""Total Exchangeable Bases""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['SoilLayer'], 'unit': {'ucum_code': 'cmolc/kg'}} })
    bsat: Optional[float] = Field(default=None, description="""Base saturation percentage""", ge=0, le=100, json_schema_extra = { "linkml_meta": {'domain_of': ['SoilLayer'], 'unit': {'ucum_code': '% CECsoil'}} })
    alum_sat: Optional[float] = Field(default=None, description="""Aluminium saturation percentage""", ge=0, le=100, json_schema_extra = { "linkml_meta": {'domain_of': ['SoilLayer'], 'unit': {'ucum_code': '% ECEC'}} })
    esp: Optional[float] = Field(default=None, description="""Exchangeable Sodium Percentage""", ge=0, le=100, json_schema_extra = { "linkml_meta": {'domain_of': ['SoilLayer'], 'unit': {'ucum_code': '%'}} })
    tcarbon_eq: Optional[float] = Field(default=None, description="""Calcium carbonate equivalent percentage by weight""", ge=0, le=100, json_schema_extra = { "linkml_meta": {'domain_of': ['SoilLayer'], 'unit': {'ucum_code': '% weight'}} })
    gypsum: Optional[float] = Field(default=None, description="""Gypsum content percentage by weight""", ge=0, le=100, json_schema_extra = { "linkml_meta": {'domain_of': ['SoilLayer'], 'unit': {'ucum_code': '% weight'}} })
    elec_cond: Optional[float] = Field(default=None, description="""Electric conductivity""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['SoilLayer'], 'unit': {'ucum_code': 'dS/m'}} })

    @field_validator('layer')
    def pattern_layer(cls, v):
        pattern=re.compile(r"^D[1-7]$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid layer format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid layer format: {v}"
            raise ValueError(err_msg)
        return v


class WRBClass(ConfiguredBaseModel):
    """
    World Reference Base (WRB) soil classification with RGB color codes
    for visualization and mapping purposes.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'hwsd2:WRBClass',
         'from_schema': 'https://w3id.org/bioepic-data/fao-soils/hwsd2'})

    id: int = Field(default=..., description="""Database internal ID""", json_schema_extra = { "linkml_meta": {'domain_of': ['SoilMappingUnit', 'SoilLayer', 'WRBClass']} })
    id_class: Optional[int] = Field(default=None, description="""Class identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['WRBClass']} })
    class_number: Optional[int] = Field(default=None, description="""Class number""", json_schema_extra = { "linkml_meta": {'domain_of': ['WRBClass']} })
    divider: Optional[int] = Field(default=None, description="""Divider value""", json_schema_extra = { "linkml_meta": {'domain_of': ['WRBClass']} })
    label: Optional[str] = Field(default=None, description="""Full label for WRB class""", json_schema_extra = { "linkml_meta": {'domain_of': ['WRBClass']} })
    symbol: Optional[str] = Field(default=None, description="""Symbol code for WRB class""", json_schema_extra = { "linkml_meta": {'domain_of': ['WRBClass']} })
    red: Optional[int] = Field(default=None, description="""Red RGB color component (0-255)""", ge=0, le=255, json_schema_extra = { "linkml_meta": {'domain_of': ['WRBClass']} })
    green: Optional[int] = Field(default=None, description="""Green RGB color component (0-255)""", ge=0, le=255, json_schema_extra = { "linkml_meta": {'domain_of': ['WRBClass']} })
    blue: Optional[int] = Field(default=None, description="""Blue RGB color component (0-255)""", ge=0, le=255, json_schema_extra = { "linkml_meta": {'domain_of': ['WRBClass']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
SoilMappingUnit.model_rebuild()
SoilLayer.model_rebuild()
WRBClass.model_rebuild()
