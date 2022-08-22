from glob import glob
from os.path import abspath, getctime
from csv import reader
from time import sleep
from typing import NoReturn

from quickstart import update_sheet


def get_latest_file() -> str:
    os_file = abspath(__file__)
    size: int = len(os_file)
    os_file = os_file[: size - 29]
    list_of_files = glob(f"{os_file}Overwatch/Workshop/*")
    latest_file: str = max(list_of_files, key=getctime)
    return latest_file


def read_csv_file(file_to_read: str) -> list:
    file_length = file_len(file_to_read)
    row_data: list = []

    with open(file_to_read) as csv_file:
        csv_reader = reader(csv_file, delimiter=",")
        for numbers in range(file_length - 11, file_length + 1):
            for rows in csv_reader:
                if csv_reader.line_num == numbers:
                    row_data.append(rows)
                    break
    return row_data


def file_len(file_to_read: str) -> int:
    with open(file_to_read) as fp:
        lines: int = len(fp.readlines())
        return lines


def main() -> NoReturn:
    file: str = get_latest_file()
    while True:
        if 12 <= file_len(file):
            update_sheet(read_csv_file(file))
        else:
            print("File Too Short")
        new_file: str = get_latest_file()
        if file != new_file:
            file = new_file
        print("Running")
        sleep(2)


if __name__ == "__main__":
    main()
