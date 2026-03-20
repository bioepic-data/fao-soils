#!/usr/bin/env python
"""
Export HWSD2 DuckDB tables to Parquet files.

Usage:
    uv run python scripts/export_hwsd2_parquet.py [--force] [db_path] [output_dir]
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

import duckdb

SAFE_TABLE_NAME = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def prepare_output_dir(output_dir: str, force: bool = False) -> Path:
    """
    Validate the Parquet output directory and optionally clear existing files.

    Args:
        output_dir: Directory where Parquet files will be written
        force: Whether to overwrite existing Parquet files

    Returns:
        Normalized output directory path

    Raises:
        FileExistsError: If Parquet files already exist and force is False
    """
    parquet_dir = Path(output_dir)
    parquet_dir.mkdir(parents=True, exist_ok=True)

    existing_files = sorted(parquet_dir.glob("*.parquet"))
    if existing_files:
        if not force:
            raise FileExistsError(
                f"Parquet output already exists in {parquet_dir}. "
                "Use --force to overwrite it."
            )
        for parquet_file in existing_files:
            parquet_file.unlink()
        print(f"Removed {len(existing_files)} existing Parquet files from: {parquet_dir}")

    return parquet_dir


def validate_table_name(table_name: str) -> str:
    """
    Validate that a DuckDB table name is safe to interpolate into SQL.

    Args:
        table_name: Table name to validate

    Returns:
        The validated table name

    Raises:
        ValueError: If the table name contains unsafe characters
    """
    if not SAFE_TABLE_NAME.fullmatch(table_name):
        raise ValueError(f"Invalid table name: {table_name}")
    return table_name


def ensure_sufficient_disk_space(output_dir: Path, database_path: Path) -> None:
    """
    Perform a rough disk-space preflight for Parquet export.

    Uses a conservative estimate of twice the DuckDB database size to leave room
    for exported Parquet files and temporary write overhead.
    """
    required_bytes = max(database_path.stat().st_size * 2, 100 * 1024 * 1024)
    free_bytes = shutil.disk_usage(output_dir).free
    if free_bytes < required_bytes:
        raise RuntimeError(
            f"Insufficient disk space in {output_dir}: "
            f"need at least {required_bytes:,} bytes free, found {free_bytes:,}."
        )


def export_hwsd2_parquet(
    db_path: str = "export/hwsd2.ddb",
    output_dir: str = "export/hwsd2_parquet",
    force: bool = False,
) -> None:
    """
    Export all tables from the HWSD2 DuckDB database to Parquet.

    Args:
        db_path: Path to the DuckDB database
        output_dir: Directory where Parquet files will be written
        force: Whether to overwrite existing Parquet files
    """
    database_path = Path(db_path)
    if not database_path.exists():
        raise FileNotFoundError(f"DuckDB database not found: {database_path}")

    parquet_dir = prepare_output_dir(output_dir, force=force)
    print(f"Exporting Parquet files from database: {database_path}")
    print(f"Writing Parquet files to: {parquet_dir}")
    ensure_sufficient_disk_space(parquet_dir, database_path)

    conn = duckdb.connect(str(database_path), read_only=True)
    try:
        try:
            conn.execute("SELECT 1").fetchone()
        except Exception as e:
            raise RuntimeError(f"Cannot access database {database_path}: {e}") from e

        tables = conn.execute(
            """
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'main'
            ORDER BY table_name
            """
        ).fetchall()

        if not tables:
            raise RuntimeError(f"No tables found in database: {database_path}")

        for index, (table_name,) in enumerate(tables, start=1):
            safe_table_name = validate_table_name(table_name)
            parquet_path = parquet_dir / f"{safe_table_name}.parquet"
            print(f"  Exporting: {safe_table_name} -> {parquet_path.name} ({index}/{len(tables)})")
            conn.execute(
                f"COPY (SELECT * FROM {safe_table_name}) TO ? (FORMAT PARQUET, COMPRESSION ZSTD)",
                [str(parquet_path)],
            )

        print(f"\nComplete! Exported {len(tables)} tables to Parquet.")
    finally:
        conn.close()


def parse_args(argv: list[str]) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Export HWSD2 DuckDB tables to Parquet.")
    parser.add_argument(
        "db_path",
        nargs="?",
        default="export/hwsd2.ddb",
        help="Path to the DuckDB database file",
    )
    parser.add_argument(
        "output_dir",
        nargs="?",
        default="export/hwsd2_parquet",
        help="Directory where Parquet files should be written",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing Parquet files in the output directory",
    )
    return parser.parse_args(argv)


def main() -> None:
    """Main entry point for command-line usage."""
    args = parse_args(sys.argv[1:])
    try:
        export_hwsd2_parquet(args.db_path, args.output_dir, force=args.force)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
