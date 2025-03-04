from src.widget import get_date


def filter_by_state(list_of_operation_dictionaries: list[dict], state: str = "EXECUTED") -> list[dict] | str:
    """Принимает словарь с данными об операции и значение ключа state.
    Возвращает инфо об операции в зависимости от выбранного ключа"""
    new_list_user_operations = list()

    for user_operation in list_of_operation_dictionaries:
        if user_operation["state"] == state:
            new_list_user_operations.append(user_operation)
    if not new_list_user_operations:
        return "Значений с заданным ключом нет в списке словарей"

    return new_list_user_operations


def sort_by_date(list_dict: list[dict], sort_key: bool = True) -> str | list[dict]:
    """Получает список словарей операций по картам/счетам клиента.
    Возвращает отсортированный список словарей по датам"""
    message_error = (
        "Ошибка полученных данных. Введите дату в одном из форматов: \n"
        "ГГ-мм-ддTчас:минута:секунда.миллисекунда\n"
        "ГГ-мм-ддTчас:минута:секунда\n"
        "ГГ-мм-дд"
    )

    try:
        new_list_dict = list()

        for dict_date in list_dict:
            # Проверка на соответствие формата полученной даты с датой в функции get_date
            if get_date(dict_date["date"]) == message_error:
                return message_error
            # Добавляем словарь с датой в новый список словарей
            new_list_dict.append(dict_date)

        new_list = sorted(new_list_dict, key=lambda list_dict: list_dict["date"], reverse=sort_key)
        return new_list

    except KeyError:
        return "Данного ключа не существует"
