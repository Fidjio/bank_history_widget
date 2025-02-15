import os

from src.widget import get_date, mask_account_card

# Переменные
PATH_TO_DATA = os.path.join(os.path.dirname(__file__), "data\\")
name_file = "numbers_card_or_check.txt"

if __name__ == "__main__":
    with open(PATH_TO_DATA + name_file, "r", encoding="utf-8") as file:
        for line in file:
            print(mask_account_card(line))

    print(get_date("2024-03-11T02:26:18.671407"))
