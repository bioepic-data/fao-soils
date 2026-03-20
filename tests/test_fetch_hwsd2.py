"""Tests for the HWSD2 fetch script configuration and CLI."""

import importlib.util
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parent.parent / "scripts" / "fetch_fao_soil_database.py"
SPEC = importlib.util.spec_from_file_location("fetch_fao_soil_database", SCRIPT_PATH)
fetch_module = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(fetch_module)


def test_default_hwsd_data_dir_points_to_repo_data_dir():
    """The fetch script should default to the repo-managed data directory."""
    assert fetch_module.default_hwsd_data_dir() == Path("data/hwsd2").resolve()


def test_parse_args_supports_repo_update_flags():
    """The fetch script should expose repo-oriented CLI flags."""
    args = fetch_module.parse_args(["--data-dir", "custom-data", "--force-download"])

    assert args.data_dir == "custom-data"
    assert args.force_download is True


def test_download_all_continues_when_documentation_download_fails(tmp_path):
    """The technical report is optional and should not stop artifact refresh."""

    class Fetcher(fetch_module.HWSDFetcher):
        def download_database(self):
            path = self.data_dir / "HWSD2_DB.zip"
            path.write_text("db")
            return path

        def download_raster(self):
            path = self.data_dir / "HWSD2_RASTER.zip"
            path.write_text("raster")
            return path

        def download_documentation(self):
            raise RuntimeError("pdf unavailable")

    fetcher = Fetcher(data_dir=tmp_path)
    components = fetcher.download_all()

    assert components["database"] == tmp_path / "HWSD2_DB.zip"
    assert components["raster"] == tmp_path / "HWSD2_RASTER.zip"
    assert "documentation" not in components
