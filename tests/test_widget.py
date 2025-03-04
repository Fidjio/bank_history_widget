import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("data_info_account, mask_info", [
    ("", "Неверный номер карты!"),
    ("123123123123123", "Неверный номер карты!"),
    ("счет 789654455", "**4455"),
    ("счет 8888 5555 4444 7777", "**7777"),
    ("карта 8888 5555 4444 7777", "8888 55** **** 7777"),
    ("Карта 5489789 9999 ", "Неверный номер карты!"),
    ("                ", "Неверный номер карты!"),
    ("счет                 ", "Введите корректный номер счета!")
])
def test_mask_account_card(data_info_account, mask_info):
    assert mask_account_card(data_info_account) == mask_info
