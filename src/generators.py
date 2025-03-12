from typing import Any, Dict, Iterator, Optional, Generator, LiteralString


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


def card_number_generator(start_num: int, stop_num: int) -> Generator[LiteralString, Any, str | None]:
    """выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где
    X — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор должен принимать начальное и конечное значения для генерации диапазона номеров."""
    if stop_num >= 9999999999999999:
        return "Вы вышли за рамки диапазона"
    number_card = "0000000000000000"
    for i in range(start_num, stop_num):
        number_card = number_card[:-len(str(i))] + str(i)
        # Результат выводится с помощью генератора списков
        num_card_result = " ".join([number_card[i:i + 4] for i in range(0, len(number_card), 4)])
        yield num_card_result

    return None
