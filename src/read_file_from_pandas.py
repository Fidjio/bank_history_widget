import csv
from typing import Any

import pandas as pd


def read_cvs_files(f_path: str) -> str | list[dict[str | Any, str | Any]]:
    """Функция для считывания финансовых операций из CSV принимает путь
    к файлу CSV в качестве аргумента выдает список словарей с транзакциями."""
    try:
        with open(f_path, "r", encoding="utf-8") as file:
            reader = list(csv.DictReader(file, delimiter=";"))
            return reader

    except Exception as ex:
        return f"Ошибка: {ex}"


def read_excel_files(f_path: str) -> str | list[dict[str | Any, str | Any]]:
    """Функция для считывания финансовых операций из Excel, которая принимает путь
    к файлу Excel в качестве аргумента и выдает список словарей с транзакциями."""
    try:
        df = pd.read_excel(f_path)
        return df.to_dict("records")

    except Exception as ex:
        return f"Ошибка: {ex}"
