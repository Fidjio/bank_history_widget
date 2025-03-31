import pytest

from src.widget import get_date, mask_account_card

message_of_error_date = (
    "Ошибка полученных данных. Введите дату в одном из форматов: \n"
    "ГГ-мм-ддTчас:минута:секунда.миллисекунда\n"
    "ГГ-мм-ддTчас:минута:секунда\n"
    "ГГ-мм-дд"
)


@pytest.mark.parametrize(
    "data_info_account, mask_info",
    [
        ("", " Неверный номер карты!"),
        ("123123123123123", " Неверный номер карты!"),
        ("счет 789654455", "счет **4455"),
        ("счет 8888 5555 4444 7777", "счет **7777"),
        ("карта 8888 5555 4444 7777", "карта 8888 55** **** 7777"),
        ("Карта 5489789 9999 ", "Карта Неверный номер карты!"),
        ("счет 444", "счет Введите корректный номер счета!"),
    ],
)
def test_mask_account_card(data_info_account, mask_info):
    assert mask_account_card(data_info_account) == mask_info


@pytest.mark.parametrize(
    "user_date, fix_date",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("", message_of_error_date),
        (" ", message_of_error_date),
        ("2024-03-11T02:26:18", "11.03.2024"),
        ("2024-03-11", "11.03.2024"),
        ("11.03.2024", message_of_error_date),
        ("2024-03-11T02:26", message_of_error_date),
        ("2024-03-1102:26", message_of_error_date),
    ],
)
def test_get_date(user_date, fix_date):
    assert get_date(user_date) == fix_date
