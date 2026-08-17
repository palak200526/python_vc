import argparse
import csv
import boto3
import io
import json
from datetime import datetime
from collections import Counter


BUCKET_NAME = "csvstatpractice"
OUTPUT_PREFIX = "output/"

s3 = boto3.client("s3")


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
        help="S3 URI of the CSV file"
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

    # Validate S3 path
    if not args.file.startswith("s3://"):
        parser.error("Input must be an S3 URI, e.g. s3://csvstatpractice/input/test1.csv")

    s3_path = args.file[5:]
    bucket, key = s3_path.split("/", 1)

    # Read CSV from S3
    try:
        response = s3.get_object(
            Bucket=bucket,
            Key=key
        )

        content = response["Body"].read().decode("utf-8")

        reader = csv.DictReader(
            io.StringIO(content)
        )

        rows = list(reader)

    except Exception as error:
        print(f"Error reading S3 file: {error}")
        return

    columns = reader.fieldnames

    if not columns:
        print("Error: CSV file has no columns.")
        return

    print("CSV file:", args.file)
    print("Rows:", len(rows))
    print("Columns:", len(columns))
    print()

    report = {
        "csv_file": args.file,
        "rows": len(rows),
        "columns": len(columns),
        "column_details": {}
    }

    for column in columns:
        values = [row[column] for row in rows]

        missing = sum(
            1
            for value in values
            if value.strip() == ""
        )

        missing_percentage = (
            missing / len(values) * 100
            if values
            else 0
        )

        column_type = infer_type(values)

        column_report = {
            "type": column_type,
            "missing": missing,
            "missing_percentage": round(
                missing_percentage, 2
            )
        }

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

            column_report["min"] = minimum
            column_report["mean"] = round(mean, 2)
            column_report["max"] = maximum

        if column_type == "text":
            text_values = [
                value.strip()
                for value in values
                if value.strip() != ""
            ]

            frequencies = Counter(text_values)

            print(f"  Top {args.top} values:")

            top_values = []

            for value, count in frequencies.most_common(args.top):
                print(f"    {value}: {count}")

                top_values.append({
                    "value": value,
                    "count": count
                })

            column_report["top_values"] = top_values

        report["column_details"][column] = column_report

        print()

    # Create a unique output filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    output_key = (
        f"{OUTPUT_PREFIX}report_{timestamp}.json"
    )

    # Upload report to S3
    try:
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=output_key,
            Body=json.dumps(
                report,
                indent=2
            ),
            ContentType="application/json"
        )

        print(
            f"Report uploaded to: "
            f"s3://{BUCKET_NAME}/{output_key}"
        )

    except Exception as error:
        print(f"Error uploading report to S3: {error}")


if __name__ == "__main__":
    main()