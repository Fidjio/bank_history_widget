from src.masks import get_mask_account, get_mask_card_number
from datetime import datetime as dt


def mask_account_card(info_from_the_client: str) -> str:
    """ Маскировка номера карты или счета """

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
        is_check = True
    else:
        is_check = False

    if is_check:
        # Маскировка номера счета
        result = get_mask_account(number_card_or_check)
    else:
        # Маскировка номера карты
        result = get_mask_card_number(number_card_or_check)
    return result


def get_date(date: str) -> str:
    """ Оставляет только дату из даты и времени """
    date_time = dt.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    date_time_str = dt.strftime(date_time, '%d.%m.%Y')

    return date_time_str
