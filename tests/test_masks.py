import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("number, mask_number", [
    ("2565789514963258", "2565 78** **** 3258"),
    ("55858748965154789", "Неверный номер карты!"),
    ("a789b879b112d478", "Неверный номер карты!"),
    ("", "Неверный номер карты!"),
    ("5856 7895 1496 3258", "5856 78** **** 3258")]
                         )
def test_card_mask(number, mask_number):
    assert get_mask_card_number(number) == mask_number


@pytest.mark.parametrize("number, mask_number", [
    ("1556666532121", "**2121"),
    ("", "Введите корректный номер счета!"),
    ("hshsahdfh", "**hdfh"),
    ("123", "Введите корректный номер счета!"),
])
def test_mask_account(number, mask_number):
    assert get_mask_account(number) == mask_number
