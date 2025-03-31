import csv
from typing import Any, Dict, List, Union

import pandas as pd


def read_cvs_files(f_path: str) -> Union[List[Dict[str, Any]], str]:
    """Функция для считывания финансовых операций из CSV принимает путь
    к файлу CSV в качестве аргумента выдает список словарей с транзакциями."""
    try:
        results = []
        with open(f_path, "r", encoding="utf-8") as file:
            reader = list(csv.DictReader(file, delimiter=";"))
            for dict_ in reader:
                result_dict = {
                    "id": dict_.get('id'),
                    "state": dict_.get('state'),
                    "date": dict_.get('date'),
                    "operationAmount": {
                        "amount": dict_.get('amount'),
                        "currency": {
                            "name": dict_.get('currency_name'),
                            "code": dict_.get('currency_code')
                        }
                    },
                    "description": dict_.get('description'),
                    "from": dict_.get('from'),
                    "to": dict_.get('to')
                }
                results.append(result_dict)
            return results

    except Exception as ex:
        return f"Ошибка: {ex}"


def read_excel_files(f_path: str) -> str | list[dict[str | Any, str | Any]]:
    """Функция для считывания финансовых операций из Excel, которая принимает путь
    к файлу Excel в качестве аргумента и выдает список словарей с транзакциями."""
    try:
        results = []
        reader = pd.read_excel(f_path).to_dict("records")
        for dict_ in reader:
            result_dict = {
                "id": dict_.get('id'),
                "state": dict_.get('state'),
                "date": dict_.get('date'),
                "operationAmount": {
                    "amount": dict_.get('amount'),
                    "currency": {
                        "name": dict_.get('currency_name'),
                        "code": dict_.get('currency_code')
                    }
                },
                "description": dict_.get('description'),
                "from": dict_.get('from'),
                "to": dict_.get('to')
            }
            results.append(result_dict)
        return results

    except Exception as ex:
        return f"Ошибка: {ex}"
