import glob
import os
import csv
from time import sleep

row_tracker = 1


def get_latest_file() -> str:
    os_file = os.path.abspath(__file__)
    size: int = len(os_file)
    os_file = os_file[: size - 22]
    list_of_files = glob.glob(f"{os_file}Overwatch/Workshop/*")
    latest_file: str = max(list_of_files, key=os.path.getctime)
    return latest_file


def reading(row_tracker, file):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for numbers in range(row_tracker, row_tracker + 12):
            for rows in csv_reader:
                if csv_reader.line_num == numbers:
                    print(rows)
                    break




reading(row_tracker, get_latest_file())
row_tracker += 12
reading(row_tracker, get_latest_file())
