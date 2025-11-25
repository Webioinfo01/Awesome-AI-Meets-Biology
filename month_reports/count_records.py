#!/usr/bin/env python3
"""
Count records in each category of a JSON file
"""
import json
import argparse
from pathlib import Path


def count_records(json_file: str) -> None:
    """Count records in each category of a JSON file"""
    json_path = Path(json_file)
    
    if not json_path.exists():
        print(f"Error: File not found: {json_file}")
        return
    
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format: {e}")
        return
    except Exception as e:
        print(f"Error: Cannot read file: {e}")
        return
    
    print("=" * 50)
    print(f"JSON File Record Count: {json_path.name}")
    print("=" * 50)
    
    total = 0
    for category, records in data.items():
        count = len(records) if isinstance(records, list) else 0
        total += count
        print(f"{category:20s}: {count:3d} records")
    
    print("-" * 50)
    print(f"{'Total':20s}: {total:3d} records")
    print("=" * 50)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Count records in each category of a JSON file",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s updater_filter.json
  %(prog)s /path/to/your/file.json
  %(prog)s ../2505/updater_filter.json
        """
    )
    parser.add_argument(
        "json_file",
        type=str,
        help="Path to the JSON file to count records"
    )
    
    args = parser.parse_args()
    count_records(args.json_file)

