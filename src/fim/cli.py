#command-line Interface

import argparse
from pathlib import Path

from fim.scanner import scan_directory
from fim.baseline import save_baseline, load_baseline
from fim.monitor import compare_scans


def main():
    parser = argparse.ArgumentParser(
        description="File Integrity Manager"
    )

    parser.add_argument(
        "command",
        choices=["scan", "baseline", "check"],
        help="Command to execute",
    )

    parser.add_argument(
        "directory",
        help="Directory to scan",
    )

    args = parser.parse_args()
    directory = Path(args.directory)

    if not directory.exists():
        parser.error(f"Directory does not exist: {directory}")

    if not directory.is_dir():
        parser.error(f"Path is not a directory: {directory}")

    results = scan_directory(str(directory))

    if args.command == "scan":
        for item in results:
            print(f"File: {item['path']}")
            print(f"SHA-256: {item['sha256']}")
            print("-" * 50)

    elif args.command == "baseline":
        save_baseline(results, "baseline.json")
        print(f"Baseline saved successfully for: {directory}")

    elif args.command == "check":
        baseline_path = Path("baseline.json")

        if not baseline_path.exists():
            parser.error(
                "Baseline file not found. "
                "Create one first using: python -m fim.cli baseline <directory>"
            )

        baseline = load_baseline(str(baseline_path))
        changes = compare_scans(results, baseline)

        for status, paths in changes.items():
            print(f"\n{status.upper()}:")

            if paths:
                for path in paths:
                    print(f"  - {path}")
            else:
                print("  None")


if __name__ == "__main__":
    main()
