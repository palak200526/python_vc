"""
CSVStat: A command-line tool for profiling CSV files.

The tool reports dataset dimensions, column types,
missing values, numeric statistics, and frequent values.
"""


# Used to parse command-line arguments.
import argparse

# Used to read and process CSV files.
import csv

# Used to parse and validate date values.
from datetime import datetime

# Used to count the frequency of values in a column.
from collections import Counter  


TYPE_NUMERIC = "numeric"
TYPE_DATE = "date"
TYPE_TEXT = "text"


def is_numeric(value):
    """Return True if the value can be converted to a number."""
    try:
        float(value)
        return True
    except ValueError:
        return False


def is_date(value):
    """Return True if the value matches a supported date format."""
    date_formats = [
        "%Y-%m-%d",
        "%d-%m-%Y",
        "%Y/%m/%d"
    ]

    for date_format in date_formats:
        try:
            datetime.strptime(value, date_format)
            return True
        except ValueError:
            print(f"'{value}' is not in {date_format} format.")
            continue

    return False


def infer_type(values):
    """Infer whether a column is numeric, date, or text."""

    values = [
        value.strip()
        for value in values
        if value.strip() != ""
    ]

    if not values:
        return TYPE_TEXT

    if all(is_numeric(value) for value in values):
        return TYPE_NUMERIC

    if all(is_date(value) for value in values):
        return TYPE_DATE
    print("Values do not match numeric or date format.") 
    return TYPE_TEXT


def numeric_stats(values):
    """Calculate min, mean, and max for numeric values."""
    
    numbers = [
        float(value.strip())
        for value in values
        if value.strip() != ""
    ]

    return min(numbers), sum(numbers) / len(numbers), max(numbers)

def main():
    parser = argparse.ArgumentParser(
        description="A simple CSV data profiling tool"
    )

    parser.add_argument(
        "file",
        help="Path to the CSV file"
    )

    parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="Show the N most frequent values for text columns (default: 5)"
    )

    args = parser.parse_args()
    if args.top < 1:
        parser.error("--top must be greater than or equal to 1")

    try:
        with open(
            args.file,
            "r",
            newline="",
            encoding="utf-8"
        ) as file:
            reader = csv.DictReader(file)
            rows = list(reader)

    except FileNotFoundError:
        print(f"Error: File '{args.file}' was not found.")
        return

    except csv.Error:
        print(f"Error: '{args.file}' is not a valid CSV file.")
        return

    columns = reader.fieldnames

    print("CSV file:", args.file)
    print("Rows:", len(rows))
    print("Columns:", len(columns))
    print()

    for column in columns:
        values = [row[column] for row in rows]

        missing = sum(
            1
            for value in values
            if value.strip() == ""
        )

        missing_percentage = (
            missing / len(values)
        ) * 100

        column_type = infer_type(values)

        print(f"{column}:")
        print(f"  Type: {column_type}")
        print(f"  Missing: {missing}")
        print(
            f"  Missing percentage: "
            f"{missing_percentage:.2f}%"
        )
        if column_type == TYPE_NUMERIC:
            minimum, mean, maximum = numeric_stats(values)

            print(f"  Min: {minimum}")
            print(f"  Mean: {mean:.2f}")
            print(f"  Max: {maximum}")
        if column_type == TYPE_TEXT:
            text_values = [
                value.strip()
                for value in values
                if value.strip() != ""
            ]

            frequencies = Counter(text_values)

            print(f"  Top {args.top} values:")

            for value, count in frequencies.most_common(args.top):
                print(f"    {value}: {count}")
        print()


if __name__ == "__main__":
    main()