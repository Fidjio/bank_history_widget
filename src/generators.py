from typing import Any, Dict, Iterator, Optional


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

def transaction_descriptions(transactions: list[dict[str, Any]]) -> Iterator[Optional[str]]:
    """Принимает список словарей с транзакциями и
    возвращает описание каждой операции по очереди"""
    try:
        for dict_ in transactions:
            yield dict_.get("description")
    except Exception:
        pass
