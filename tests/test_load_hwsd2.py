"""Tests for the HWSD2 DuckDB loader script."""

from pathlib import Path
import subprocess
import sys


def test_load_hwsd2_refuses_to_overwrite_existing_database(tmp_path):
    """The loader should fail fast when the output database already exists."""
    db_path = tmp_path / "existing.ddb"
    db_path.write_text("placeholder")

    script_path = Path(__file__).resolve().parent.parent / "scripts" / "load_hwsd2.py"
    result = subprocess.run(
        [sys.executable, str(script_path), str(db_path)],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 1
    assert "Use --force to overwrite it." in result.stderr
