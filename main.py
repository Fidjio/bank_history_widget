import os

from src.processing import filter_by_state
from src.widget import get_date, mask_account_card

# Переменные
PATH_TO_DATA = os.path.join(os.path.dirname(__file__), "data\\")
name_file = "numbers_card_or_check.txt"

if __name__ == "__main__":
    with open(PATH_TO_DATA + name_file, "r", encoding="utf-8") as file:
        for line in file:
            print(mask_account_card(line))

    print(get_date("2024-03-11T02:26:18.671407"))

    print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                           {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                           {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], "CANCELED"))