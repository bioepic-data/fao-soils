#!/usr/bin/env python
"""
Export HWSD2 DuckDB tables to Parquet files.

Usage:
    uv run python scripts/export_hwsd2_parquet.py [--force] [db_path] [output_dir]
"""

import argparse
import sys
from pathlib import Path

import duckdb


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

    conn = duckdb.connect(str(database_path), read_only=True)
    try:
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

        for (table_name,) in tables:
            parquet_path = parquet_dir / f"{table_name}.parquet"
            print(f"  Exporting: {table_name} -> {parquet_path.name}")
            conn.execute(
                f"COPY (SELECT * FROM {table_name}) TO ? (FORMAT PARQUET, COMPRESSION ZSTD)",
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
