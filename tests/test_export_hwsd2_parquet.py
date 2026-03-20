"""Tests for the HWSD2 Parquet export script."""

from pathlib import Path
import subprocess
import sys

import duckdb
import pandas as pd
import pyarrow.parquet as pq


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


def test_exported_parquet_reads_with_pyarrow_and_pandas(tmp_path):
    """Exported Parquet should be readable outside DuckDB."""
    db_path = tmp_path / "test.ddb"
    conn = duckdb.connect(str(db_path))
    conn.execute(
        """
        CREATE TABLE example (
            id INTEGER,
            label VARCHAR,
            value DOUBLE
        )
        """
    )
    conn.execute(
        """
        INSERT INTO example VALUES
            (1, 'alpha', 1.5),
            (2, 'beta', NULL)
        """
    )
    conn.close()

    output_dir = tmp_path / "parquet"
    script_path = Path(__file__).resolve().parent.parent / "scripts" / "export_hwsd2_parquet.py"
    result = subprocess.run(
        [sys.executable, str(script_path), "--force", str(db_path), str(output_dir)],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr

    parquet_path = output_dir / "example.parquet"
    assert parquet_path.exists()

    arrow_table = pq.read_table(parquet_path)
    assert arrow_table.num_rows == 2
    assert arrow_table.num_columns == 3
    assert arrow_table.column("label").to_pylist() == ["alpha", "beta"]

    df = pd.read_parquet(parquet_path)
    assert list(df.columns) == ["id", "label", "value"]
    assert df.to_dict(orient="records")[0] == {"id": 1, "label": "alpha", "value": 1.5}
    assert pd.isna(df.iloc[1]["value"])
