# from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date
import os

# Переменные
PATH_TO_DATA = os.path.join(os.path.dirname(__file__), "data\\")
name_file = "numbers_card_or_check.txt"

if __name__ == "__main__":
    with open(PATH_TO_DATA + name_file, "r", encoding="utf-8") as file:
        for line in file:
            print(mask_account_card(line))

    print(get_date("2024-03-11T02:26:18.671407"))
