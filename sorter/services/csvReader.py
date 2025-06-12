import csv
from pathlib import Path

def read_csv_file(file_path):
    def parse_value(value):
        try:
            num = float(value)
            return num if num >= 0 else 0.0  # Remove negative values
        except (ValueError, TypeError):
            return 0.0  # Treat non-numeric as 0.0

    data = []
    path = Path(file_path).resolve()
    with path.open(mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip header
        for row in reader:
            processed_row = [parse_value(value) for value in row]
            data.append(processed_row)
    return data
