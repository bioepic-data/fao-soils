# Auto generated from fao_soils.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-11-10T17:07:48
# Schema: hwsd2
#
# id: https://w3id.org/bioepic-data/fao-soils/hwsd2
# description: LinkML schema for the FAO Harmonized World Soil Database (HWSD) version 2.0.
#
#   The HWSD v2.0 provides comprehensive soil data including physical and chemical properties
#   at multiple soil layers for global coverage. This database is essential for ecosystem
#   modeling, climate modeling, and agricultural applications.
#
#   Main components:
#   - Soil Mapping Units (SMU): Summary-level soil characteristics
#   - Soil Layers: Detailed physical and chemical properties at different depths
#   - Classification systems: WRB, FAO-90, USDA taxonomy
#   - Domain tables: Lookup tables for codes and classifications
# license: CC-BY-4.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Float, Integer, String

metamodel_version = "1.7.0"
version = "2.0.0"

# Namespaces
FAO_SOILS = CurieNamespace('fao_soils', 'https://w3id.org/bioepic-data/fao-soils/')
HWSD2 = CurieNamespace('hwsd2', 'https://w3id.org/bioepic-data/fao-soils/hwsd2/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
QUDT = CurieNamespace('qudt', 'http://qudt.org/schema/qudt/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = HWSD2


# Types

# Class references
class SoilMappingUnitId(extended_int):
    pass


class SoilLayerId(extended_int):
    pass


class WRBClassId(extended_int):
    pass


@dataclass(repr=False)
class SoilMappingUnit(YAMLRoot):
    """
    A Soil Mapping Unit (SMU) represents a distinct area with relatively homogeneous
    soil characteristics. Each SMU may contain multiple soil types with their
    proportional shares.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = HWSD2["SoilMappingUnit"]
    class_class_curie: ClassVar[str] = "hwsd2:SoilMappingUnit"
    class_name: ClassVar[str] = "SoilMappingUnit"
    class_model_uri: ClassVar[URIRef] = HWSD2.SoilMappingUnit

    id: Union[int, SoilMappingUnitId] = None
    hwsd2_smu_id: int = None
    wise30s_smu_id: Optional[str] = None
    hwsd1_smu_id: Optional[int] = None
    coverage: Optional[Union[str, "CoverageEnum"]] = None
    share: Optional[float] = None
    wrb4: Optional[str] = None
    wrb_phases: Optional[str] = None
    wrb2: Optional[str] = None
    wrb2_code: Optional[str] = None
    fao90: Optional[str] = None
    koppen: Optional[Union[str, "KoppenEnum"]] = None
    texture_usda: Optional[Union[str, "TextureUSDAEnum"]] = None
    ref_bulk_density: Optional[float] = None
    bulk_density: Optional[float] = None
    drainage: Optional[Union[str, "DrainageEnum"]] = None
    root_depth: Optional[Union[str, "RootDepthEnum"]] = None
    awc: Optional[float] = None
    phase1: Optional[Union[str, "PhaseEnum"]] = None
    phase2: Optional[Union[str, "PhaseEnum"]] = None
    roots: Optional[Union[str, "RootsEnum"]] = None
    il: Optional[Union[str, "ILEnum"]] = None
    add_prop: Optional[Union[str, "AddPropEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SoilMappingUnitId):
            self.id = SoilMappingUnitId(self.id)

        if self._is_empty(self.hwsd2_smu_id):
            self.MissingRequiredField("hwsd2_smu_id")
        if not isinstance(self.hwsd2_smu_id, int):
            self.hwsd2_smu_id = int(self.hwsd2_smu_id)

        if self.wise30s_smu_id is not None and not isinstance(self.wise30s_smu_id, str):
            self.wise30s_smu_id = str(self.wise30s_smu_id)

        if self.hwsd1_smu_id is not None and not isinstance(self.hwsd1_smu_id, int):
            self.hwsd1_smu_id = int(self.hwsd1_smu_id)

        if self.coverage is not None and not isinstance(self.coverage, CoverageEnum):
            self.coverage = CoverageEnum(self.coverage)

        if self.share is not None and not isinstance(self.share, float):
            self.share = float(self.share)

        if self.wrb4 is not None and not isinstance(self.wrb4, str):
            self.wrb4 = str(self.wrb4)

        if self.wrb_phases is not None and not isinstance(self.wrb_phases, str):
            self.wrb_phases = str(self.wrb_phases)

        if self.wrb2 is not None and not isinstance(self.wrb2, str):
            self.wrb2 = str(self.wrb2)

        if self.wrb2_code is not None and not isinstance(self.wrb2_code, str):
            self.wrb2_code = str(self.wrb2_code)

        if self.fao90 is not None and not isinstance(self.fao90, str):
            self.fao90 = str(self.fao90)

        if self.koppen is not None and not isinstance(self.koppen, KoppenEnum):
            self.koppen = KoppenEnum(self.koppen)

        if self.texture_usda is not None and not isinstance(self.texture_usda, TextureUSDAEnum):
            self.texture_usda = TextureUSDAEnum(self.texture_usda)

        if self.ref_bulk_density is not None and not isinstance(self.ref_bulk_density, float):
            self.ref_bulk_density = float(self.ref_bulk_density)

        if self.bulk_density is not None and not isinstance(self.bulk_density, float):
            self.bulk_density = float(self.bulk_density)

        if self.drainage is not None and not isinstance(self.drainage, DrainageEnum):
            self.drainage = DrainageEnum(self.drainage)

        if self.root_depth is not None and not isinstance(self.root_depth, RootDepthEnum):
            self.root_depth = RootDepthEnum(self.root_depth)

        if self.awc is not None and not isinstance(self.awc, float):
            self.awc = float(self.awc)

        if self.phase1 is not None and not isinstance(self.phase1, PhaseEnum):
            self.phase1 = PhaseEnum(self.phase1)

        if self.phase2 is not None and not isinstance(self.phase2, PhaseEnum):
            self.phase2 = PhaseEnum(self.phase2)

        if self.roots is not None and not isinstance(self.roots, RootsEnum):
            self.roots = RootsEnum(self.roots)

        if self.il is not None and not isinstance(self.il, ILEnum):
            self.il = ILEnum(self.il)

        if self.add_prop is not None and not isinstance(self.add_prop, AddPropEnum):
            self.add_prop = AddPropEnum(self.add_prop)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SoilLayer(YAMLRoot):
    """
    Detailed soil properties at a specific depth layer. Each Soil Mapping Unit
    can have multiple layers (typically D1 through D7) representing different
    soil horizons from surface to depth.

    Contains comprehensive physical properties (texture, bulk density), chemical
    properties (pH, organic carbon, nutrients), and cation exchange characteristics.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = HWSD2["SoilLayer"]
    class_class_curie: ClassVar[str] = "hwsd2:SoilLayer"
    class_name: ClassVar[str] = "SoilLayer"
    class_model_uri: ClassVar[URIRef] = HWSD2.SoilLayer

    id: Union[int, SoilLayerId] = None
    hwsd2_smu_id: int = None
    nsc_mu_source1: Optional[str] = None
    nsc_mu_source2: Optional[str] = None
    wise30s_smu_id: Optional[str] = None
    hwsd1_smu_id: Optional[int] = None
    coverage: Optional[Union[str, "CoverageEnum"]] = None
    sequence: Optional[int] = None
    share: Optional[float] = None
    nsc: Optional[str] = None
    wrb_phases: Optional[str] = None
    wrb4: Optional[str] = None
    wrb2: Optional[str] = None
    fao90: Optional[str] = None
    root_depth_layer: Optional[str] = None
    phase1: Optional[Union[str, "PhaseEnum"]] = None
    phase2: Optional[Union[str, "PhaseEnum"]] = None
    roots: Optional[Union[str, "RootsEnum"]] = None
    il: Optional[Union[str, "ILEnum"]] = None
    swr: Optional[Union[str, "SWREnum"]] = None
    drainage: Optional[Union[str, "DrainageEnum"]] = None
    awc_layer: Optional[str] = None
    add_prop: Optional[Union[str, "AddPropEnum"]] = None
    layer: Optional[str] = None
    topdep: Optional[int] = None
    botdep: Optional[int] = None
    coarse: Optional[float] = None
    sand: Optional[float] = None
    silt: Optional[float] = None
    clay: Optional[float] = None
    texture_usda: Optional[Union[str, "TextureUSDAEnum"]] = None
    texture_soter: Optional[Union[str, "TextureSOTEREnum"]] = None
    bulk: Optional[float] = None
    ref_bulk: Optional[float] = None
    org_carbon: Optional[float] = None
    ph_water: Optional[float] = None
    total_n: Optional[float] = None
    cn_ratio: Optional[float] = None
    cec_soil: Optional[float] = None
    cec_clay: Optional[float] = None
    cec_eff: Optional[float] = None
    teb: Optional[float] = None
    bsat: Optional[float] = None
    alum_sat: Optional[float] = None
    esp: Optional[float] = None
    tcarbon_eq: Optional[float] = None
    gypsum: Optional[float] = None
    elec_cond: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SoilLayerId):
            self.id = SoilLayerId(self.id)

        if self._is_empty(self.hwsd2_smu_id):
            self.MissingRequiredField("hwsd2_smu_id")
        if not isinstance(self.hwsd2_smu_id, int):
            self.hwsd2_smu_id = int(self.hwsd2_smu_id)

        if self.nsc_mu_source1 is not None and not isinstance(self.nsc_mu_source1, str):
            self.nsc_mu_source1 = str(self.nsc_mu_source1)

        if self.nsc_mu_source2 is not None and not isinstance(self.nsc_mu_source2, str):
            self.nsc_mu_source2 = str(self.nsc_mu_source2)

        if self.wise30s_smu_id is not None and not isinstance(self.wise30s_smu_id, str):
            self.wise30s_smu_id = str(self.wise30s_smu_id)

        if self.hwsd1_smu_id is not None and not isinstance(self.hwsd1_smu_id, int):
            self.hwsd1_smu_id = int(self.hwsd1_smu_id)

        if self.coverage is not None and not isinstance(self.coverage, CoverageEnum):
            self.coverage = CoverageEnum(self.coverage)

        if self.sequence is not None and not isinstance(self.sequence, int):
            self.sequence = int(self.sequence)

        if self.share is not None and not isinstance(self.share, float):
            self.share = float(self.share)

        if self.nsc is not None and not isinstance(self.nsc, str):
            self.nsc = str(self.nsc)

        if self.wrb_phases is not None and not isinstance(self.wrb_phases, str):
            self.wrb_phases = str(self.wrb_phases)

        if self.wrb4 is not None and not isinstance(self.wrb4, str):
            self.wrb4 = str(self.wrb4)

        if self.wrb2 is not None and not isinstance(self.wrb2, str):
            self.wrb2 = str(self.wrb2)

        if self.fao90 is not None and not isinstance(self.fao90, str):
            self.fao90 = str(self.fao90)

        if self.root_depth_layer is not None and not isinstance(self.root_depth_layer, str):
            self.root_depth_layer = str(self.root_depth_layer)

        if self.phase1 is not None and not isinstance(self.phase1, PhaseEnum):
            self.phase1 = PhaseEnum(self.phase1)

        if self.phase2 is not None and not isinstance(self.phase2, PhaseEnum):
            self.phase2 = PhaseEnum(self.phase2)

        if self.roots is not None and not isinstance(self.roots, RootsEnum):
            self.roots = RootsEnum(self.roots)

        if self.il is not None and not isinstance(self.il, ILEnum):
            self.il = ILEnum(self.il)

        if self.swr is not None and not isinstance(self.swr, SWREnum):
            self.swr = SWREnum(self.swr)

        if self.drainage is not None and not isinstance(self.drainage, DrainageEnum):
            self.drainage = DrainageEnum(self.drainage)

        if self.awc_layer is not None and not isinstance(self.awc_layer, str):
            self.awc_layer = str(self.awc_layer)

        if self.add_prop is not None and not isinstance(self.add_prop, AddPropEnum):
            self.add_prop = AddPropEnum(self.add_prop)

        if self.layer is not None and not isinstance(self.layer, str):
            self.layer = str(self.layer)

        if self.topdep is not None and not isinstance(self.topdep, int):
            self.topdep = int(self.topdep)

        if self.botdep is not None and not isinstance(self.botdep, int):
            self.botdep = int(self.botdep)

        if self.coarse is not None and not isinstance(self.coarse, float):
            self.coarse = float(self.coarse)

        if self.sand is not None and not isinstance(self.sand, float):
            self.sand = float(self.sand)

        if self.silt is not None and not isinstance(self.silt, float):
            self.silt = float(self.silt)

        if self.clay is not None and not isinstance(self.clay, float):
            self.clay = float(self.clay)

        if self.texture_usda is not None and not isinstance(self.texture_usda, TextureUSDAEnum):
            self.texture_usda = TextureUSDAEnum(self.texture_usda)

        if self.texture_soter is not None and not isinstance(self.texture_soter, TextureSOTEREnum):
            self.texture_soter = TextureSOTEREnum(self.texture_soter)

        if self.bulk is not None and not isinstance(self.bulk, float):
            self.bulk = float(self.bulk)

        if self.ref_bulk is not None and not isinstance(self.ref_bulk, float):
            self.ref_bulk = float(self.ref_bulk)

        if self.org_carbon is not None and not isinstance(self.org_carbon, float):
            self.org_carbon = float(self.org_carbon)

        if self.ph_water is not None and not isinstance(self.ph_water, float):
            self.ph_water = float(self.ph_water)

        if self.total_n is not None and not isinstance(self.total_n, float):
            self.total_n = float(self.total_n)

        if self.cn_ratio is not None and not isinstance(self.cn_ratio, float):
            self.cn_ratio = float(self.cn_ratio)

        if self.cec_soil is not None and not isinstance(self.cec_soil, float):
            self.cec_soil = float(self.cec_soil)

        if self.cec_clay is not None and not isinstance(self.cec_clay, float):
            self.cec_clay = float(self.cec_clay)

        if self.cec_eff is not None and not isinstance(self.cec_eff, float):
            self.cec_eff = float(self.cec_eff)

        if self.teb is not None and not isinstance(self.teb, float):
            self.teb = float(self.teb)

        if self.bsat is not None and not isinstance(self.bsat, float):
            self.bsat = float(self.bsat)

        if self.alum_sat is not None and not isinstance(self.alum_sat, float):
            self.alum_sat = float(self.alum_sat)

        if self.esp is not None and not isinstance(self.esp, float):
            self.esp = float(self.esp)

        if self.tcarbon_eq is not None and not isinstance(self.tcarbon_eq, float):
            self.tcarbon_eq = float(self.tcarbon_eq)

        if self.gypsum is not None and not isinstance(self.gypsum, float):
            self.gypsum = float(self.gypsum)

        if self.elec_cond is not None and not isinstance(self.elec_cond, float):
            self.elec_cond = float(self.elec_cond)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WRBClass(YAMLRoot):
    """
    World Reference Base (WRB) soil classification with RGB color codes
    for visualization and mapping purposes.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = HWSD2["WRBClass"]
    class_class_curie: ClassVar[str] = "hwsd2:WRBClass"
    class_name: ClassVar[str] = "WRBClass"
    class_model_uri: ClassVar[URIRef] = HWSD2.WRBClass

    id: Union[int, WRBClassId] = None
    id_class: Optional[int] = None
    class_number: Optional[int] = None
    divider: Optional[int] = None
    label: Optional[str] = None
    symbol: Optional[str] = None
    red: Optional[int] = None
    green: Optional[int] = None
    blue: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WRBClassId):
            self.id = WRBClassId(self.id)

        if self.id_class is not None and not isinstance(self.id_class, int):
            self.id_class = int(self.id_class)

        if self.class_number is not None and not isinstance(self.class_number, int):
            self.class_number = int(self.class_number)

        if self.divider is not None and not isinstance(self.divider, int):
            self.divider = int(self.divider)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.symbol is not None and not isinstance(self.symbol, str):
            self.symbol = str(self.symbol)

        if self.red is not None and not isinstance(self.red, int):
            self.red = int(self.red)

        if self.green is not None and not isinstance(self.green, int):
            self.green = int(self.green)

        if self.blue is not None and not isinstance(self.blue, int):
            self.blue = int(self.blue)

        super().__post_init__(**kwargs)


# Enumerations
class CoverageEnum(EnumDefinitionImpl):
    """
    Data source coverage codes
    """
    NONE = PermissibleValue(
        text="NONE",
        description="None")
    ESDB = PermissibleValue(
        text="ESDB",
        description="European Soil Database")
    CHINA = PermissibleValue(
        text="CHINA",
        description="China soil database")
    SOTWIS = PermissibleValue(
        text="SOTWIS",
        description="Soil and Terrain Database")
    DSMW = PermissibleValue(
        text="DSMW",
        description="Digital Soil Map of the World")
    WISE30s = PermissibleValue(
        text="WISE30s",
        description="World Inventory of Soil Emission Potentials (30 arcsec)")
    AFGHANISTAN = PermissibleValue(
        text="AFGHANISTAN",
        description="Afghanistan soil database")
    GHANA = PermissibleValue(
        text="GHANA",
        description="Ghana soil database")
    TURKEY = PermissibleValue(
        text="TURKEY",
        description="Turkey soil database")

    _defn = EnumDefinition(
        name="CoverageEnum",
        description="Data source coverage codes",
    )

class DrainageEnum(EnumDefinitionImpl):
    """
    Soil drainage classes
    """
    E = PermissibleValue(
        text="E",
        description="Excessively drained")
    SE = PermissibleValue(
        text="SE",
        description="Somewhat excessively drained")
    W = PermissibleValue(
        text="W",
        description="Well drained")
    MW = PermissibleValue(
        text="MW",
        description="Moderately well drained")
    I = PermissibleValue(
        text="I",
        description="Imperfectly drained")
    P = PermissibleValue(
        text="P",
        description="Poorly drained")
    VP = PermissibleValue(
        text="VP",
        description="Very poorly drained")

    _defn = EnumDefinition(
        name="DrainageEnum",
        description="Soil drainage classes",
    )

class RootDepthEnum(EnumDefinitionImpl):
    """
    Root depth categories
    """
    DEEP = PermissibleValue(
        text="DEEP",
        description="Deep (> 100cm)")
    MODERATELY_DEEP = PermissibleValue(
        text="MODERATELY_DEEP",
        description="Moderately Deep (< 100cm)")
    SHALLOW = PermissibleValue(
        text="SHALLOW",
        description="Shallow (< 50cm)")
    VERY_SHALLOW = PermissibleValue(
        text="VERY_SHALLOW",
        description="Very shallow (< 10cm)")

    _defn = EnumDefinition(
        name="RootDepthEnum",
        description="Root depth categories",
    )

class RootsEnum(EnumDefinitionImpl):
    """
    Obstacle to roots depth ranges (ESDB)
    """
    NONE = PermissibleValue(
        text="NONE",
        description="No obstacle")
    GT_80 = PermissibleValue(
        text="GT_80",
        description="> 80 cm")

    _defn = EnumDefinition(
        name="RootsEnum",
        description="Obstacle to roots depth ranges (ESDB)",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "60_80",
            PermissibleValue(
                text="60_80",
                description="60-80 cm"))
        setattr(cls, "40_60",
            PermissibleValue(
                text="40_60",
                description="40-60 cm"))
        setattr(cls, "20_40",
            PermissibleValue(
                text="20_40",
                description="20-40 cm"))
        setattr(cls, "0_80",
            PermissibleValue(
                text="0_80",
                description="0-80 cm"))
        setattr(cls, "0_20",
            PermissibleValue(
                text="0_20",
                description="0-20 cm"))

class ILEnum(EnumDefinitionImpl):
    """
    Impermeable layer depth ranges (ESDB)
    """
    NONE = PermissibleValue(
        text="NONE",
        description="No impermeable layer")
    GT_150 = PermissibleValue(
        text="GT_150",
        description="> 150 cm")
    LT_40 = PermissibleValue(
        text="LT_40",
        description="< 40 cm")

    _defn = EnumDefinition(
        name="ILEnum",
        description="Impermeable layer depth ranges (ESDB)",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "80_150",
            PermissibleValue(
                text="80_150",
                description="80-150 cm"))
        setattr(cls, "40_80",
            PermissibleValue(
                text="40_80",
                description="40-80 cm"))

class SWREnum(EnumDefinitionImpl):
    """
    Soil Water Regime classes (ESDB)
    """
    NONE = PermissibleValue(
        text="NONE",
        description="Not applicable")
    SLIGHTLY_WET = PermissibleValue(
        text="SLIGHTLY_WET",
        description="Slightly wet")
    MODERATELY_WET = PermissibleValue(
        text="MODERATELY_WET",
        description="Moderately wet")
    WET = PermissibleValue(
        text="WET",
        description="Wet")
    VERY_WET = PermissibleValue(
        text="VERY_WET",
        description="Very wet")

    _defn = EnumDefinition(
        name="SWREnum",
        description="Soil Water Regime classes (ESDB)",
    )

class PhaseEnum(EnumDefinitionImpl):
    """
    Soil phase modifiers
    """
    NONE = PermissibleValue(
        text="NONE",
        description="No phase")
    STONY = PermissibleValue(
        text="STONY",
        description="Stony phase")
    LITHIC = PermissibleValue(
        text="LITHIC",
        description="Lithic phase (shallow to bedrock)")
    PETRIC = PermissibleValue(
        text="PETRIC",
        description="Petric phase (cemented layer)")
    PETROCALCIC = PermissibleValue(
        text="PETROCALCIC",
        description="Petrocalcic phase (cemented carbonate)")
    PETROGYPSIC = PermissibleValue(
        text="PETROGYPSIC",
        description="Petrogypsic phase (cemented gypsum)")
    PETROFERRIC = PermissibleValue(
        text="PETROFERRIC",
        description="Petroferric phase (cemented iron)")
    PHREATIC = PermissibleValue(
        text="PHREATIC",
        description="Phreatic phase (groundwater influenced)")
    FRAGIPAN = PermissibleValue(
        text="FRAGIPAN",
        description="Fragipan phase (dense subsurface layer)")

    _defn = EnumDefinition(
        name="PhaseEnum",
        description="Soil phase modifiers",
    )

class AddPropEnum(EnumDefinitionImpl):
    """
    Additional soil properties
    """
    NONE = PermissibleValue(
        text="NONE",
        description="No additional properties")
    GELIC = PermissibleValue(
        text="GELIC",
        description="Gelic (permafrost influenced)")
    VERTIC = PermissibleValue(
        text="VERTIC",
        description="Vertic (high shrink-swell)")

    _defn = EnumDefinition(
        name="AddPropEnum",
        description="Additional soil properties",
    )

class KoppenEnum(EnumDefinitionImpl):
    """
    Köppen-Geiger climate classification
    """
    A = PermissibleValue(
        text="A",
        description="Tropical")
    B = PermissibleValue(
        text="B",
        description="Arid")
    C = PermissibleValue(
        text="C",
        description="Temperate")
    D = PermissibleValue(
        text="D",
        description="Cold")
    E = PermissibleValue(
        text="E",
        description="Polar")

    _defn = EnumDefinition(
        name="KoppenEnum",
        description="Köppen-Geiger climate classification",
    )

class TextureUSDAEnum(EnumDefinitionImpl):
    """
    USDA soil texture classes
    """
    NONE = PermissibleValue(
        text="NONE",
        description="Not classified")
    CLAY_HEAVY = PermissibleValue(
        text="CLAY_HEAVY",
        description="Clay (heavy)")
    SILTY_CLAY = PermissibleValue(
        text="SILTY_CLAY",
        description="Silty clay")
    CLAY_LIGHT = PermissibleValue(
        text="CLAY_LIGHT",
        description="Clay (light)")
    SILTY_CLAY_LOAM = PermissibleValue(
        text="SILTY_CLAY_LOAM",
        description="Silty clay loam")
    CLAY_LOAM = PermissibleValue(
        text="CLAY_LOAM",
        description="Clay loam")
    SILT = PermissibleValue(
        text="SILT",
        description="Silt")
    SILT_LOAM = PermissibleValue(
        text="SILT_LOAM",
        description="Silt loam")
    SANDY_CLAY = PermissibleValue(
        text="SANDY_CLAY",
        description="Sandy clay")
    LOAM = PermissibleValue(
        text="LOAM",
        description="Loam")

    _defn = EnumDefinition(
        name="TextureUSDAEnum",
        description="USDA soil texture classes",
    )

class TextureSOTEREnum(EnumDefinitionImpl):
    """
    SOTER soil texture classes
    """
    C = PermissibleValue(
        text="C",
        description="Coarse")
    M = PermissibleValue(
        text="M",
        description="Medium")
    F = PermissibleValue(
        text="F",
        description="Fine")
    V = PermissibleValue(
        text="V",
        description="Very Fine")
    Z = PermissibleValue(
        text="Z",
        description="Medium Fine")

    _defn = EnumDefinition(
        name="TextureSOTEREnum",
        description="SOTER soil texture classes",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=HWSD2.id, name="id", curie=HWSD2.curie('id'),
                   model_uri=HWSD2.id, domain=None, range=URIRef)

slots.hwsd2_smu_id = Slot(uri=HWSD2.hwsd2_smu_id, name="hwsd2_smu_id", curie=HWSD2.curie('hwsd2_smu_id'),
                   model_uri=HWSD2.hwsd2_smu_id, domain=None, range=int)

slots.wise30s_smu_id = Slot(uri=HWSD2.wise30s_smu_id, name="wise30s_smu_id", curie=HWSD2.curie('wise30s_smu_id'),
                   model_uri=HWSD2.wise30s_smu_id, domain=None, range=Optional[str])

slots.hwsd1_smu_id = Slot(uri=HWSD2.hwsd1_smu_id, name="hwsd1_smu_id", curie=HWSD2.curie('hwsd1_smu_id'),
                   model_uri=HWSD2.hwsd1_smu_id, domain=None, range=Optional[int])

slots.nsc_mu_source1 = Slot(uri=HWSD2.nsc_mu_source1, name="nsc_mu_source1", curie=HWSD2.curie('nsc_mu_source1'),
                   model_uri=HWSD2.nsc_mu_source1, domain=None, range=Optional[str])

slots.nsc_mu_source2 = Slot(uri=HWSD2.nsc_mu_source2, name="nsc_mu_source2", curie=HWSD2.curie('nsc_mu_source2'),
                   model_uri=HWSD2.nsc_mu_source2, domain=None, range=Optional[str])

slots.nsc = Slot(uri=HWSD2.nsc, name="nsc", curie=HWSD2.curie('nsc'),
                   model_uri=HWSD2.nsc, domain=None, range=Optional[str])

slots.coverage = Slot(uri=HWSD2.coverage, name="coverage", curie=HWSD2.curie('coverage'),
                   model_uri=HWSD2.coverage, domain=None, range=Optional[Union[str, "CoverageEnum"]])

slots.sequence = Slot(uri=HWSD2.sequence, name="sequence", curie=HWSD2.curie('sequence'),
                   model_uri=HWSD2.sequence, domain=None, range=Optional[int])

slots.share = Slot(uri=HWSD2.share, name="share", curie=HWSD2.curie('share'),
                   model_uri=HWSD2.share, domain=None, range=Optional[float])

slots.wrb4 = Slot(uri=HWSD2.wrb4, name="wrb4", curie=HWSD2.curie('wrb4'),
                   model_uri=HWSD2.wrb4, domain=None, range=Optional[str])

slots.wrb_phases = Slot(uri=HWSD2.wrb_phases, name="wrb_phases", curie=HWSD2.curie('wrb_phases'),
                   model_uri=HWSD2.wrb_phases, domain=None, range=Optional[str])

slots.wrb2 = Slot(uri=HWSD2.wrb2, name="wrb2", curie=HWSD2.curie('wrb2'),
                   model_uri=HWSD2.wrb2, domain=None, range=Optional[str])

slots.wrb2_code = Slot(uri=HWSD2.wrb2_code, name="wrb2_code", curie=HWSD2.curie('wrb2_code'),
                   model_uri=HWSD2.wrb2_code, domain=None, range=Optional[str])

slots.fao90 = Slot(uri=HWSD2.fao90, name="fao90", curie=HWSD2.curie('fao90'),
                   model_uri=HWSD2.fao90, domain=None, range=Optional[str])

slots.koppen = Slot(uri=HWSD2.koppen, name="koppen", curie=HWSD2.curie('koppen'),
                   model_uri=HWSD2.koppen, domain=None, range=Optional[Union[str, "KoppenEnum"]])

slots.root_depth = Slot(uri=HWSD2.root_depth, name="root_depth", curie=HWSD2.curie('root_depth'),
                   model_uri=HWSD2.root_depth, domain=None, range=Optional[Union[str, "RootDepthEnum"]])

slots.root_depth_layer = Slot(uri=HWSD2.root_depth_layer, name="root_depth_layer", curie=HWSD2.curie('root_depth_layer'),
                   model_uri=HWSD2.root_depth_layer, domain=None, range=Optional[str])

slots.roots = Slot(uri=HWSD2.roots, name="roots", curie=HWSD2.curie('roots'),
                   model_uri=HWSD2.roots, domain=None, range=Optional[Union[str, "RootsEnum"]])

slots.il = Slot(uri=HWSD2.il, name="il", curie=HWSD2.curie('il'),
                   model_uri=HWSD2.il, domain=None, range=Optional[Union[str, "ILEnum"]])

slots.drainage = Slot(uri=HWSD2.drainage, name="drainage", curie=HWSD2.curie('drainage'),
                   model_uri=HWSD2.drainage, domain=None, range=Optional[Union[str, "DrainageEnum"]])

slots.swr = Slot(uri=HWSD2.swr, name="swr", curie=HWSD2.curie('swr'),
                   model_uri=HWSD2.swr, domain=None, range=Optional[Union[str, "SWREnum"]])

slots.awc = Slot(uri=HWSD2.awc, name="awc", curie=HWSD2.curie('awc'),
                   model_uri=HWSD2.awc, domain=None, range=Optional[float])

slots.awc_layer = Slot(uri=HWSD2.awc_layer, name="awc_layer", curie=HWSD2.curie('awc_layer'),
                   model_uri=HWSD2.awc_layer, domain=None, range=Optional[str])

slots.phase1 = Slot(uri=HWSD2.phase1, name="phase1", curie=HWSD2.curie('phase1'),
                   model_uri=HWSD2.phase1, domain=None, range=Optional[Union[str, "PhaseEnum"]])

slots.phase2 = Slot(uri=HWSD2.phase2, name="phase2", curie=HWSD2.curie('phase2'),
                   model_uri=HWSD2.phase2, domain=None, range=Optional[Union[str, "PhaseEnum"]])

slots.add_prop = Slot(uri=HWSD2.add_prop, name="add_prop", curie=HWSD2.curie('add_prop'),
                   model_uri=HWSD2.add_prop, domain=None, range=Optional[Union[str, "AddPropEnum"]])

slots.layer = Slot(uri=HWSD2.layer, name="layer", curie=HWSD2.curie('layer'),
                   model_uri=HWSD2.layer, domain=None, range=Optional[str],
                   pattern=re.compile(r'^D[1-7]$'))

slots.topdep = Slot(uri=HWSD2.topdep, name="topdep", curie=HWSD2.curie('topdep'),
                   model_uri=HWSD2.topdep, domain=None, range=Optional[int])

slots.botdep = Slot(uri=HWSD2.botdep, name="botdep", curie=HWSD2.curie('botdep'),
                   model_uri=HWSD2.botdep, domain=None, range=Optional[int])

slots.coarse = Slot(uri=HWSD2.coarse, name="coarse", curie=HWSD2.curie('coarse'),
                   model_uri=HWSD2.coarse, domain=None, range=Optional[float])

slots.sand = Slot(uri=HWSD2.sand, name="sand", curie=HWSD2.curie('sand'),
                   model_uri=HWSD2.sand, domain=None, range=Optional[float])

slots.silt = Slot(uri=HWSD2.silt, name="silt", curie=HWSD2.curie('silt'),
                   model_uri=HWSD2.silt, domain=None, range=Optional[float])

slots.clay = Slot(uri=HWSD2.clay, name="clay", curie=HWSD2.curie('clay'),
                   model_uri=HWSD2.clay, domain=None, range=Optional[float])

slots.texture_usda = Slot(uri=HWSD2.texture_usda, name="texture_usda", curie=HWSD2.curie('texture_usda'),
                   model_uri=HWSD2.texture_usda, domain=None, range=Optional[Union[str, "TextureUSDAEnum"]])

slots.texture_soter = Slot(uri=HWSD2.texture_soter, name="texture_soter", curie=HWSD2.curie('texture_soter'),
                   model_uri=HWSD2.texture_soter, domain=None, range=Optional[Union[str, "TextureSOTEREnum"]])

slots.bulk = Slot(uri=HWSD2.bulk, name="bulk", curie=HWSD2.curie('bulk'),
                   model_uri=HWSD2.bulk, domain=None, range=Optional[float])

slots.ref_bulk = Slot(uri=HWSD2.ref_bulk, name="ref_bulk", curie=HWSD2.curie('ref_bulk'),
                   model_uri=HWSD2.ref_bulk, domain=None, range=Optional[float])

slots.bulk_density = Slot(uri=HWSD2.bulk_density, name="bulk_density", curie=HWSD2.curie('bulk_density'),
                   model_uri=HWSD2.bulk_density, domain=None, range=Optional[float])

slots.ref_bulk_density = Slot(uri=HWSD2.ref_bulk_density, name="ref_bulk_density", curie=HWSD2.curie('ref_bulk_density'),
                   model_uri=HWSD2.ref_bulk_density, domain=None, range=Optional[float])

slots.org_carbon = Slot(uri=HWSD2.org_carbon, name="org_carbon", curie=HWSD2.curie('org_carbon'),
                   model_uri=HWSD2.org_carbon, domain=None, range=Optional[float])

slots.total_n = Slot(uri=HWSD2.total_n, name="total_n", curie=HWSD2.curie('total_n'),
                   model_uri=HWSD2.total_n, domain=None, range=Optional[float])

slots.cn_ratio = Slot(uri=HWSD2.cn_ratio, name="cn_ratio", curie=HWSD2.curie('cn_ratio'),
                   model_uri=HWSD2.cn_ratio, domain=None, range=Optional[float])

slots.ph_water = Slot(uri=HWSD2.ph_water, name="ph_water", curie=HWSD2.curie('ph_water'),
                   model_uri=HWSD2.ph_water, domain=None, range=Optional[float])

slots.cec_soil = Slot(uri=HWSD2.cec_soil, name="cec_soil", curie=HWSD2.curie('cec_soil'),
                   model_uri=HWSD2.cec_soil, domain=None, range=Optional[float])

slots.cec_clay = Slot(uri=HWSD2.cec_clay, name="cec_clay", curie=HWSD2.curie('cec_clay'),
                   model_uri=HWSD2.cec_clay, domain=None, range=Optional[float])

slots.cec_eff = Slot(uri=HWSD2.cec_eff, name="cec_eff", curie=HWSD2.curie('cec_eff'),
                   model_uri=HWSD2.cec_eff, domain=None, range=Optional[float])

slots.teb = Slot(uri=HWSD2.teb, name="teb", curie=HWSD2.curie('teb'),
                   model_uri=HWSD2.teb, domain=None, range=Optional[float])

slots.bsat = Slot(uri=HWSD2.bsat, name="bsat", curie=HWSD2.curie('bsat'),
                   model_uri=HWSD2.bsat, domain=None, range=Optional[float])

slots.alum_sat = Slot(uri=HWSD2.alum_sat, name="alum_sat", curie=HWSD2.curie('alum_sat'),
                   model_uri=HWSD2.alum_sat, domain=None, range=Optional[float])

slots.esp = Slot(uri=HWSD2.esp, name="esp", curie=HWSD2.curie('esp'),
                   model_uri=HWSD2.esp, domain=None, range=Optional[float])

slots.tcarbon_eq = Slot(uri=HWSD2.tcarbon_eq, name="tcarbon_eq", curie=HWSD2.curie('tcarbon_eq'),
                   model_uri=HWSD2.tcarbon_eq, domain=None, range=Optional[float])

slots.gypsum = Slot(uri=HWSD2.gypsum, name="gypsum", curie=HWSD2.curie('gypsum'),
                   model_uri=HWSD2.gypsum, domain=None, range=Optional[float])

slots.elec_cond = Slot(uri=HWSD2.elec_cond, name="elec_cond", curie=HWSD2.curie('elec_cond'),
                   model_uri=HWSD2.elec_cond, domain=None, range=Optional[float])

slots.id_class = Slot(uri=HWSD2.id_class, name="id_class", curie=HWSD2.curie('id_class'),
                   model_uri=HWSD2.id_class, domain=None, range=Optional[int])

slots.class_number = Slot(uri=HWSD2.class_number, name="class_number", curie=HWSD2.curie('class_number'),
                   model_uri=HWSD2.class_number, domain=None, range=Optional[int])

slots.divider = Slot(uri=HWSD2.divider, name="divider", curie=HWSD2.curie('divider'),
                   model_uri=HWSD2.divider, domain=None, range=Optional[int])

slots.label = Slot(uri=HWSD2.label, name="label", curie=HWSD2.curie('label'),
                   model_uri=HWSD2.label, domain=None, range=Optional[str])

slots.symbol = Slot(uri=HWSD2.symbol, name="symbol", curie=HWSD2.curie('symbol'),
                   model_uri=HWSD2.symbol, domain=None, range=Optional[str])

slots.red = Slot(uri=HWSD2.red, name="red", curie=HWSD2.curie('red'),
                   model_uri=HWSD2.red, domain=None, range=Optional[int])

slots.green = Slot(uri=HWSD2.green, name="green", curie=HWSD2.curie('green'),
                   model_uri=HWSD2.green, domain=None, range=Optional[int])

slots.blue = Slot(uri=HWSD2.blue, name="blue", curie=HWSD2.curie('blue'),
                   model_uri=HWSD2.blue, domain=None, range=Optional[int])
