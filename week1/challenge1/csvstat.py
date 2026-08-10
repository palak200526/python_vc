import argparse
import csv
from datetime import datetime
from collections import Counter  


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
            continue

    return False


def infer_type(values):
    """Infer whether a column is numeric, date, or text."""

    # Remove missing values
    values = [
        value.strip()
        for value in values
        if value.strip() != ""
    ]

    if not values:
        return "text"

    if all(is_numeric(value) for value in values):
        return "numeric"

    if all(is_date(value) for value in values):
        return "date"

    return "text"

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
        parser.error("--top must be a positive integer")

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
        if column_type == "numeric":
            minimum, mean, maximum = numeric_stats(values)

            print(f"  Min: {minimum}")
            print(f"  Mean: {mean:.2f}")
            print(f"  Max: {maximum}")
        if column_type == "text":
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