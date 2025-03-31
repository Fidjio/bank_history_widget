import pytest

from src.processing import get_count_category  # Замените your_module на имя вашего модуля

# Тестовые данные
TEST_TRANSACTIONS = [
    {"description": "Покупка еды", "amount": 500},
    {"description": "Такси", "amount": 300},
    {"description": "Покупка еды", "amount": 200},
    {"description": "Кино", "amount": 400},
    {"description": None, "amount": 100},  # Транзакция без категории
    {"description": "Такси", "amount": 350},
]


def test_count_existing_categories():
    """Тест подсчета существующих категорий"""
    categories = ["Покупка еды", "Такси"]
    result = get_count_category(TEST_TRANSACTIONS, categories)

    assert result == {"Покупка еды": 2, "Такси": 2}


def test_count_with_missing_category():
    """Тест с категорией, которой нет в транзакциях"""
    categories = ["Покупка еды", "Одежда"]
    result = get_count_category(TEST_TRANSACTIONS, categories)

    assert result == {"Покупка еды": 2, "Одежда": 0}


def test_empty_categories_list():
    """Тест с пустым списком категорий"""
    result = get_count_category(TEST_TRANSACTIONS, [])

    assert result == 'Список транзакций пуст!'


def test_empty_transactions():
    """Тест с пустым списком транзакций"""
    result = get_count_category([], ["Покупка еды"])

    assert result == {'Покупка еды': 0}


def test_case_sensitivity():
    """Тест на чувствительность к регистру"""
    categories = ["покупка еды", "такси"]
    result = get_count_category(TEST_TRANSACTIONS, categories)

    assert result == {"покупка еды": 0, "такси": 0}
