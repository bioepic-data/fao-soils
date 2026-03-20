"""Tests for the HWSD2 Parquet export script."""

from pathlib import Path
import subprocess
import sys

import duckdb


def test_export_hwsd2_parquet_refuses_to_overwrite_existing_output(tmp_path):
    """The exporter should fail fast when Parquet output already exists."""
    db_path = tmp_path / "test.ddb"
    conn = duckdb.connect(str(db_path))
    conn.execute("CREATE TABLE example (id INTEGER)")
    conn.execute("INSERT INTO example VALUES (1)")
    conn.close()

    output_dir = tmp_path / "parquet"
    output_dir.mkdir()
    (output_dir / "example.parquet").write_text("placeholder")

    script_path = Path(__file__).resolve().parent.parent / "scripts" / "export_hwsd2_parquet.py"
    result = subprocess.run(
        [sys.executable, str(script_path), str(db_path), str(output_dir)],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 1
    assert "Use --force to overwrite it." in result.stderr
