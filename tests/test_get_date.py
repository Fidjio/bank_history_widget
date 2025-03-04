import pytest

from src.widget import get_date

message_of_error_date = (
    "Ошибка полученных данных. Введите дату в одном из форматов: \n"
    "ГГ-мм-ддTчас:минута:секунда.миллисекунда\n"
    "ГГ-мм-ддTчас:минута:секунда\n"
    "ГГ-мм-дд"
)


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
