from typing import Any, Generator, Iterator, LiteralString, Optional


def filter_by_currency(
    transactions: list[dict[str, Any]], currency: str
) -> Generator[str | dict[str, Any], None, None]:
    """Принимает список словарей ->
    возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)"""
    try:
        count_transactions = len(transactions)
        if count_transactions == 0:
            yield ""
        for dict_ in transactions:
            if dict_.get("operationAmount", {}).get("currency", {}).get("code", {}) == currency:
                yield dict_
    except KeyError:
        pass


def transaction_descriptions(transactions: list[dict[str, Any]]) -> Iterator[Optional[str]]:
    """Принимает список словарей с транзакциями и
    возвращает описание каждой операции по очереди"""
    count_transactions = len(transactions)

    if count_transactions == 0:
        yield "Нет транзакций"
        return

    for dict_ in transactions:
        if "description" not in dict_.keys():
            yield "Нет транзакции или описания транзакции!"
        else:
            yield dict_.get("description")


def card_number_generator(start_num: int, stop_num: int) -> Generator[str | LiteralString, Any, None]:
    """выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где
    X — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор принимает начальное и конечное значения для генерации диапазона номеров."""

    number_card = "0000000000000000"
    for i in range(start_num, stop_num):
        if stop_num > 9999999999999999:
            yield "Вы вышли за рамки диапазона"
            return
        number_card = number_card[: -len(str(i))] + str(i)
        num_card_result = " ".join([number_card[i: i + 4] for i in range(0, len(number_card), 4)])
        yield num_card_result
