#!/usr/bin/env python
"""
Load HWSD2 CSV files into DuckDB database.

This script creates a DuckDB database from the HWSD2 CSV files using the
schema defined in hwsd2_duckdb_schema.sql.

Usage:
    uv run python load_hwsd2.py [--force] [--csv-dir PATH] [output_db_path]

Default output: hwsd2.db
"""

import argparse
import sys
from pathlib import Path
import duckdb


def prepare_output_path(db_path: str, force: bool = False) -> Path:
    """
    Validate the output database path and optionally remove an existing file.

    Args:
        db_path: Path to output DuckDB database file
        force: Whether to overwrite an existing database

    Returns:
        Normalized output path

    Raises:
        FileExistsError: If the database already exists and force is False
    """
    output_path = Path(db_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if output_path.exists():
        if not force:
            raise FileExistsError(
                f"Output database already exists: {output_path}. "
                "Use --force to overwrite it."
            )
        output_path.unlink()
        print(f"Removed existing database: {output_path}")

    return output_path


def load_hwsd2(db_path: str = "hwsd2.db", csv_dir: str = "HWSD2_csv", force: bool = False) -> None:
    """
    Load HWSD2 CSV files into a DuckDB database.

    Args:
        db_path: Path to output DuckDB database file
        csv_dir: Path to directory containing CSV files
        force: Whether to overwrite an existing database

    Examples:
        >>> # This will create hwsd2.db in current directory
        >>> load_hwsd2()
        >>> # Use custom paths
        >>> load_hwsd2("my_hwsd.db", "data/HWSD2_csv")
        >>> # Overwrite an existing database
        >>> load_hwsd2("my_hwsd.db", "data/HWSD2_csv", force=True)
    """
    csv_path = Path(csv_dir)
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV directory not found: {csv_path}")

    output_path = prepare_output_path(db_path, force=force)

    print(f"Creating DuckDB database: {output_path}")
    print(f"Loading from CSV directory: {csv_path}")

    # Connect to database (creates if doesn't exist)
    conn = duckdb.connect(str(output_path))

    # Load schema from SQL file
    script_dir = Path(__file__).parent

    # Try to find schema file in standard locations
    # First try: data/hwsd2/ (fao-soils repo structure)
    schema_file = script_dir.parent / "data" / "hwsd2" / "hwsd2_duckdb_schema.sql"

    # Second try: same directory as script (ecosim-co-scientist structure)
    if not schema_file.exists():
        schema_file = script_dir / "hwsd2_duckdb_schema.sql"

    if not schema_file.exists():
        raise FileNotFoundError(f"Schema file not found. Tried: {schema_file}")

    print("\nReading schema...")
    with open(schema_file) as f:
        schema_sql = f.read()

    # Split SQL into statements and execute
    # We need to modify the COPY statements to use absolute paths
    statements = [s.strip() for s in schema_sql.split(';') if s.strip()]

    print("\nCreating tables...")
    table_count = 0
    copy_count = 0

    for stmt in statements:
        if not stmt:
            continue

        # Modify COPY statements to use the correct path
        # Check if COPY appears in the statement (might have comments before it)
        if 'COPY ' in stmt and ' FROM ' in stmt:
            # Extract the CSV filename
            parts = stmt.split("'")
            if len(parts) >= 2:
                csv_file = parts[1]
                # Only process if it's a CSV file path
                if csv_file.endswith('.csv'):
                    # Replace with absolute path
                    full_path = csv_path / csv_file.replace('HWSD2_csv/', '')
                    stmt = stmt.replace(f"'{csv_file}'", f"'{full_path}'")
                    print(f"  Loading: {full_path.name}")
                    copy_count += 1
        elif 'CREATE TABLE' in stmt:
            # Extract table name (might have comments before it)
            for line in stmt.split('\n'):
                if line.strip().startswith('CREATE TABLE'):
                    table_name = line.split()[2]
                    print(f"  Creating: {table_name}")
                    table_count += 1
                    break
        elif 'CREATE INDEX' in stmt:
            continue  # Skip printing indexes

        try:
            conn.execute(stmt)
        except Exception as e:
            snippet = stmt[:160].replace("\n", " ")
            raise RuntimeError(
                f"Failed to execute SQL statement: {e}\nStatement: {snippet}..."
            ) from e

    print(f"\nComplete!")
    print(f"  Tables created: {table_count}")
    print(f"  Files loaded: {copy_count}")

    # Print some basic statistics
    print("\nDatabase statistics:")
    print(f"  HWSD2_LAYERS rows: {conn.execute('SELECT COUNT(*) FROM HWSD2_LAYERS').fetchone()[0]:,}")
    print(f"  HWSD2_SMU rows: {conn.execute('SELECT COUNT(*) FROM HWSD2_SMU').fetchone()[0]:,}")
    domain_count = conn.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_name LIKE 'D_%'").fetchone()[0]
    print(f"  Domain tables: {domain_count}")

    # Show a sample query
    print("\nSample data from HWSD2_LAYERS:")
    result = conn.execute("""
        SELECT
            HWSD2_SMU_ID,
            LAYER,
            TOPDEP,
            BOTDEP,
            SAND,
            SILT,
            CLAY,
            ORG_CARBON,
            PH_WATER
        FROM HWSD2_LAYERS
        LIMIT 5
    """).fetchdf()
    print(result.to_string())

    conn.close()
    print(f"\nDatabase saved to: {output_path}")


def parse_args(argv: list[str]) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Load HWSD2 CSV files into DuckDB.")
    parser.add_argument(
        "db_path",
        nargs="?",
        default="hwsd2.ddb",
        help="Path to output DuckDB database file",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite the output database if it already exists",
    )
    parser.add_argument(
        "--csv-dir",
        help="Path to the HWSD2_csv directory",
    )
    return parser.parse_args(argv)


def main():
    """Main entry point for command-line usage."""
    args = parse_args(sys.argv[1:])

    if args.csv_dir:
        csv_dir = Path(args.csv_dir)
    else:
        # Determine CSV directory relative to this script
        script_dir = Path(__file__).parent

        # Try to find HWSD2_csv in standard locations
        # First try: data/hwsd2/HWSD2_csv (fao-soils repo structure)
        csv_dir = script_dir.parent / "data" / "hwsd2" / "HWSD2_csv"

        # Second try: same directory as script (ecosim-co-scientist structure)
        if not csv_dir.exists():
            csv_dir = script_dir / "HWSD2_csv"

        # Third try: current working directory
        if not csv_dir.exists():
            csv_dir = Path.cwd() / "HWSD2_csv"

    try:
        load_hwsd2(str(args.db_path), str(csv_dir), force=args.force)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
