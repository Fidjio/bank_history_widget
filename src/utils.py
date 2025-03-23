import json
from typing import Any


def get_info_transactions_json(path: str) -> list[dict[Any, Any]] | Any:
    """Возвращает список словарей из json-файла с данными
    о финансовых транзакциях пользователей"""
    try:
        with open(path, "r", encoding="utf-8") as json_f:
            info_json = json.load(json_f)

            if info_json:
                return info_json
            else:
                return list()

    except TypeError:
        return list()
    except Exception:
        return list()
