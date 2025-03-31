from datetime import datetime as dt

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info_from_the_client: str) -> str:
    """Маскировка номера карты или счета"""

    number_card_or_check = ""
    name_operations = ""

    # Получение номера карты/счета из данных пользователя
    for number in info_from_the_client:
        if number.isdigit():
            number_card_or_check += number
        else:
            name_operations += number
    name_operations = name_operations.strip()

    # Выбор способа маскировки (счет/карта)
    if name_operations.lower() == "Счет".lower():
        # Маскировка номера счета
        result = get_mask_account(number_card_or_check)
    else:
        # Маскировка номера карты
        result = get_mask_card_number(number_card_or_check)

    return f'{name_operations} {result}'


def get_date(date: str) -> str:
    """Оставляет только дату из даты и времени"""

    try:
        # Переменная для хранения вариантов форматов дат
        formats_date = ["%Y-%m-%dT%H:%M:%S.%f", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d", "%Y-%m-%dT%H:%M:%SZ"]
        i = 0
        for format_date in formats_date:
            try:
                date_time = dt.strptime(date, format_date)
                date_time_str = dt.strftime(date_time, "%d.%m.%Y")
            except Exception:
                i += 1
                pass
        if i == len(formats_date):
            raise ValueError
        else:
            return date_time_str
    except ValueError:
        return (
            "Ошибка полученных данных. Введите дату в одном из форматов: \n"
            "ГГ-мм-ддTчас:минута:секунда.миллисекунда\n"
            "ГГ-мм-ддTчас:минута:секунда\n"
            "ГГ-мм-дд"
        )
