import csv


def write_to_csv(file_path, rows):
    with open(file=file_path, mode="w", newline="") as f:
        writer = csv.writer(f, delimiter=";", quotechar="'")
        for row in rows:
            writer.writerow(row)
