import os

from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

# Переменные
PATH_TO_DATA = os.path.join(os.path.dirname(__file__), "data\\")
name_file = "numbers_card_or_check.txt"

if __name__ == "__main__":
    print("Hello! It's my project!")

    """Функции модуля masks.py"""
    # Функция get_mask_card_number
    print("\nФункция get_mask_card_number:")
    print(get_mask_card_number("1111222233334444"))

    # Функция get_mask_account
    print("\nФункция get_mask_account:")
    print(get_mask_account("88897745"))

    """Функции модуля processing.py"""
    # Функция filter_by_state
    print("\nФункция filter_by_state:")
    print(
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
        )
    )

    # Функция sort_by_date
    print("\nФункция sort_by_date:")
    sorted_list_dict = sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        False,
    )
    for dict_date in sorted_list_dict:
        print(dict_date)

    """Функции модуля widget.py"""
    # Функция mask_account_card
    print("\nФункция mask_account_card:")
    with open(PATH_TO_DATA + name_file, "r", encoding="utf-8") as file:
        for line in file:
            print(mask_account_card(line))

        # Функция get_date
    print("\nФункция get_date:")
    print(get_date("2024-03-11T02:26:56"))
