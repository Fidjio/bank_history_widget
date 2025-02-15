def mask_account_card(info_from_the_client: str) -> str:
    """ Маскировка номера карты или счета """

    # Извлечение номера карты/счета из строки
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

    # Маскировка номера счета
    if is_check:
        if len(number_card_or_check) < 6:
            return "Введите корректный номер счета!"
        else:
            return f"**{number_card_or_check[-4:]}"

    else:
        # Маскировка номера карты
        if len(number_card_or_check) != 16:
            return "Неверный номер карты!"
        else:
            return f"{number_card_or_check[:4]} {number_card_or_check[4:6]}** **** {number_card_or_check[-4:]}"


def get_date(date: str) -> str:
    """ Оставляет только дату из даты и времени """

    return ".".join(reversed(date[0:10].split("-")))
