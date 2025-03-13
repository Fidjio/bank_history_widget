# Тестирование функции filter_by_currency
import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(users_transactions, transactions_usd, transactions_none_code):
    """Проверка функции filter_by_currency"""

    gen = filter_by_currency(users_transactions, "USD")
    assert list(gen) == transactions_usd

    gen = filter_by_currency(transactions_none_code, "USD")
    assert list(gen) == []

    gen = filter_by_currency([], "USD")
    assert list(gen) == [""]


def test_transaction_descriptions(users_transactions, result_transaction_descriptions):
    """Проверка функции transaction_descriptions.
    result_transaction_descriptions является списком с ожидаемыми результатами функции"""
    gen = transaction_descriptions(users_transactions)

    assert next(gen) == result_transaction_descriptions[0]
    assert next(gen) == result_transaction_descriptions[1]
    assert next(gen) == result_transaction_descriptions[2]
    assert next(gen) == result_transaction_descriptions[3]
    assert next(gen) == result_transaction_descriptions[4]

    with pytest.raises(StopIteration):
        next(gen)


@pytest.mark.parametrize(
    "transactions, result",
    [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD"}},
                }
            ],
            "Нет транзакции или описания транзакции!",
        ),
        ([], "Нет транзакций"),
        (
            [
                {
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                }
            ],
            "Перевод с карты на карту",
        ),
    ],
)
def test_param_transaction_descriptions(transactions, result):
    gen = transaction_descriptions(transactions)

    assert next(gen) == result

    with pytest.raises(StopIteration):
        next(gen)


@pytest.mark.parametrize(
    "start, stop, result",
    [
        (
            1,
            11,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
                "0000 0000 0000 0006",
                "0000 0000 0000 0007",
                "0000 0000 0000 0008",
                "0000 0000 0000 0009",
                "0000 0000 0000 0010",
            ],
        ),
        (20, 23, ["0000 0000 0000 0020", "0000 0000 0000 0021", "0000 0000 0000 0022"]),
        (9999999999999998, 10000000000000000, ["Вы вышли за рамки диапазона"]),
    ],
)
def test_card_number_generator(start, stop, result):
    gen = card_number_generator(start, stop)
    assert list(gen) == result

    with pytest.raises(StopIteration):
        next(gen)
