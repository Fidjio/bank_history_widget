import pytest

from src.processing import sort_by_date


def test_sort_by_date(dict_for_sort, result_sort_date):
    """Проверка функции sort_by_date с помощью фикстур"""
    assert sort_by_date(dict_for_sort) == result_sort_date


def test_sort_date_false_key(dict_for_sort, result_sort_date_reverse):
    """Проверка функции sort_by_date с помощью фикстур c ключем sort_key=false"""
    assert sort_by_date(dict_for_sort, False) == result_sort_date_reverse


@pytest.mark.parametrize(
    "dict_sort, result",
    [
        (
            # Тест №1: проверка сортировки
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2020-09-12T21:27:25.241689"},
            ],
            [
                {"id": 594226727, "state": "CANCELED", "date": "2020-09-12T21:27:25.241689"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        # Тест №2: пустой словарь
        ([{}], "Данного ключа не существует"),
        # Тест №3: другой вариант даты
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30"},
            ],
        ),
        # Тест №4: одинаковые даты
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30"},
            ],
        ),
    ],
)
def test_sort_date(dict_sort, result):
    assert sort_by_date(dict_sort) == result
