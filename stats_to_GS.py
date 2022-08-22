import glob
import os
import csv
from time import sleep


def get_latest_file() -> str:
    os_file = os.path.abspath(__file__)
    size: int = len(os_file)
    os_file = os_file[: size - 29]
    list_of_files = glob.glob(f"{os_file}Overwatch/Workshop/*")
    latest_file: str = max(list_of_files, key=os.path.getctime)
    return latest_file


def read_csv_file(file_to_read: str):
    with open(file_to_read) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count: int = 0
        for row in csv_reader:
            print(row)
            line_count += 1
            if line_count == 12:
                break


def remove_lines(file_to_read: str):
    with open(file_to_read) as old, open("newfile.txt", "w") as new:
        lines = old.readlines()
        new.writelines(lines[12:])
    os.replace("newfile.txt", file_to_read)


if __name__ == "__main__":
    file = get_latest_file()
    while True:
        read_csv_file(file)
        remove_lines(file)
        file = get_latest_file()
        print("Running")
        sleep(1)
