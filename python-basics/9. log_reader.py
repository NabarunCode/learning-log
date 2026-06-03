"""
log_reader.py
Automation Script 2 — Read a log file and extract lines by keyword.
Author: Nabarun Chakraborty
"""

import os
import sys
from datetime import datetime


def read_log(file_path):
    """Read log file and return all lines."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Log file not found: {file_path}")
    with open(file_path, "r") as f:
        return f.readlines()


def filter_lines(lines, keyword):
    """Return lines containing the keyword (case-insensitive)."""
    keyword_lower = keyword.lower()
    return [line for line in lines if keyword_lower in line.lower()]


def write_report(matches, keyword, output_path):
    """Write matched lines to an output file with a header."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(output_path, "w") as f:
        f.write(f"# Log Report — Keyword: '{keyword}'\n")
        f.write(f"# Generated: {timestamp}\n")
        f.write(f"# Matches found: {len(matches)}\n\n")
        f.writelines(matches)
    print(f"Report saved: {output_path}")


def main():
    # --- Config ---
    log_file = "sample.log"
    keyword = "ERROR"
    output_file = f"report_{keyword.lower()}.txt"

    print(f"Reading: {log_file}")
    print(f"Filtering for: '{keyword}'")

    try:
        lines = read_log(log_file)
        print(f"Total lines read: {len(lines)}")

        matches = filter_lines(lines, keyword)
        print(f"Matching lines: {len(matches)}")

        if matches:
            write_report(matches, keyword, output_file)
        else:
            print("No matches found. No report generated.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
