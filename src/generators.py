from typing import Any, Dict, Iterator


def filter_by_currency(transactions: list[dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """Принимает список словарей ->
    возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)"""
    try:
        for dict_ in transactions:
            if dict_["operationAmount"]["currency"]["code"] == currency:
                yield dict_
    except KeyError:
        pass
