import pytest

from src.processing import search_transaction

# Простые тестовые данные
TEST_DATA = [
    {"description": "Покупка в магазине", "amount": 100},
    {"description": "Оплата кафе", "amount": 200},
    {"description": "Перевод другу", "amount": 300},
    {"description": None, "amount": 400},  # Без описания
    {"description": "", "amount": 500},     # Пустое описание
]

def test_find_full_match():
    """Находит полное совпадение"""
    result = search_transaction(TEST_DATA, "Оплата кафе")
    assert len(result) == 1
    assert result[0]["amount"] == 200

def test_find_partial_match():
    """Находит частичное совпадение"""
    result = search_transaction(TEST_DATA, "магазин")
    assert len(result) == 1
    assert result[0]["amount"] == 100

def test_no_matches():
    """Нет совпадений"""
    result = search_transaction(TEST_DATA, "Такси")
    assert len(result) == 0

def test_empty_search():
    """Пустая строка поиска возвращает все с описанием"""
    result = search_transaction(TEST_DATA, "")
    assert len(result) == 3  # 3 элемента с description (не None и не пустой)

def test_case_insensitive():
    """Поиск не зависит от регистра"""
    result = search_transaction(TEST_DATA, "ПЕРЕВОД")
    assert len(result) == 1
    assert result[0]["amount"] == 300
