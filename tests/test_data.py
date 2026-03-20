"""Data test."""
import os
import glob
import pytest
from pathlib import Path

import fao_soils.datamodel.fao_soils
from linkml_runtime.loaders import yaml_loader

DATA_DIR_VALID = Path(__file__).parent / "data" / "valid"
DATA_DIR_INVALID = Path(__file__).parent / "data" / "invalid"

VALID_EXAMPLE_FILES = sorted(glob.glob(os.path.join(DATA_DIR_VALID, "*.yaml")))
INVALID_EXAMPLE_FILES = sorted(
    glob.glob(os.path.join(DATA_DIR_INVALID, "*.yaml")))

ENUM_BOUNDARY_CASES = [
    ("SoilMappingUnit", "coverage", "NONE", "TURKEY"),
    ("SoilMappingUnit", "wrb2", "AC", "ND"),
    ("SoilMappingUnit", "koppen", "A", "E"),
    ("SoilMappingUnit", "texture_usda", "NONE", "LOAM"),
    ("SoilMappingUnit", "drainage", "E", "VP"),
    ("SoilMappingUnit", "root_depth", "DEEP", "VERY_SHALLOW"),
    ("SoilMappingUnit", "phase1", "NONE", "FRAGIPAN"),
    ("SoilMappingUnit", "phase2", "NONE", "FRAGIPAN"),
    ("SoilMappingUnit", "roots", "NONE", "0_20"),
    ("SoilMappingUnit", "il", "NONE", "40_80"),
    ("SoilMappingUnit", "add_prop", "NONE", "VERTIC"),
    ("SoilLayer", "coverage", "NONE", "TURKEY"),
    ("SoilLayer", "wrb2", "AC", "ND"),
    ("SoilLayer", "phase1", "NONE", "FRAGIPAN"),
    ("SoilLayer", "phase2", "NONE", "FRAGIPAN"),
    ("SoilLayer", "roots", "NONE", "0_20"),
    ("SoilLayer", "il", "NONE", "40_80"),
    ("SoilLayer", "swr", "NONE", "VERY_WET"),
    ("SoilLayer", "drainage", "E", "VP"),
    ("SoilLayer", "add_prop", "NONE", "VERTIC"),
    ("SoilLayer", "texture_usda", "NONE", "LOAM"),
    ("SoilLayer", "texture_soter", "C", "Z"),
]


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files(filepath):
    """Test loading of all valid data files."""
    target_class_name = Path(filepath).stem.split("-")[0]
    tgt_class = getattr(
        fao_soils.datamodel.fao_soils,
        target_class_name,
    )
    obj = yaml_loader.load(filepath, target_class=tgt_class)
    assert obj


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES)
def test_invalid_data_files(filepath):
    """Test loading of invalid data files fails."""
    target_class_name = Path(filepath).stem.split("-")[0]
    tgt_class = getattr(
        fao_soils.datamodel.fao_soils,
        target_class_name,
    )
    with pytest.raises(ValueError):
        yaml_loader.load(filepath, target_class=tgt_class)


@pytest.mark.parametrize(
    "class_name,field_name,first_value,last_value",
    ENUM_BOUNDARY_CASES,
)
def test_enum_fields_accept_boundary_values(
    class_name,
    field_name,
    first_value,
    last_value,
):
    """Test enum-backed fields accept first and last permissible values."""
    tgt_class = getattr(fao_soils.datamodel.fao_soils, class_name)
    base_kwargs = {
        "id": 1,
        "hwsd2_smu_id": 1,
    }

    for offset, value in enumerate((first_value, last_value), start=1):
        obj = tgt_class(**{**base_kwargs, "id": offset, field_name: value})
        assert obj
