from glob import glob
from os.path import abspath, getctime
from csv import reader
from time import sleep
from typing import NoReturn

from google_sheets_push import update_sheet

def get_latest_file() -> str:
    os_file: str = abspath(__file__)
    size: int = len(os_file)
    os_file = os_file[: size - 29]
    list_of_files: list[str] = glob(f"{os_file}Overwatch/Workshop/*")
    latest_file: str = max(list_of_files, key=getctime)
    return latest_file


def read_csv_file(file_to_read: str) -> list:
    row_data: list[list] = []
    t1: list = []
    t2: list = []
    file_length: int = file_len(file_to_read)

    with open(file_to_read) as csv_file:
        csv_reader = reader(csv_file, delimiter=",")
        for numbers in range(file_length - 11, file_length + 1):
            for rows in csv_reader:
                if csv_reader.line_num == numbers:
                    rows.pop(0)
                    if rows[1] == "LÃºcio":
                        rows[1] = "Lucio"
                    elif rows[1] == "TorbjÃ¶rn":
                        rows[1] = "Torbjorn"
                    if rows[len(rows) - 1] == "Team 1":
                        t1.append(rows)
                    else:
                        t2.append(rows)
                    break

    row_data.insert(
        0,
        [
            "Player Name",
            "Hero Name",
            "Damage Dealt",
            "Barrier Damage",
            "Damage Blocked",
            "Damage Taken",
            "Deaths",
            "Elims",
            "Final Blows",
            "Env Deaths",
            "Env Kills",
            "Healing",
            "Obj Kills",
            "solo kills",
            "Ults Earned",
            "Ults Used",
            "Healing Recived",
            "Team",
        ],
    )
    for t1_rows in t1:
        row_data.append(t1_rows)
    for t2_rows in t2:
        row_data.append(t2_rows)
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
        sleep(2)


if __name__ == "__main__":
    main()
