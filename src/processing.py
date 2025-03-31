import re
from collections import Counter
from typing import Any

from src.widget import get_date


def filter_by_state(list_of_operation_dictionaries: list[dict], state: str = "EXECUTED") -> list[dict] | str:
    """Принимает словарь с данными об операции и значение ключа state.
    Возвращает инфо об операции в зависимости от выбранного ключа"""
    new_list_user_operations = list()

    for user_operation in list_of_operation_dictionaries:
        if user_operation.get("state") == state:
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
            if get_date(dict_date.get("date", '')) == message_error:
                return message_error
            # Добавляем словарь с датой в новый список словарей
            new_list_dict.append(dict_date)

        new_list = sorted(new_list_dict, key=lambda list_dict: list_dict["date"], reverse=sort_key)
        return new_list

    except KeyError:
        return "Данного ключа не существует"


def search_transaction(list_dict_transactions: list[dict], str_search: str) -> list[Any]:
    """Принимает список словарей с данными о банковских операциях и строку поиска.
    Возвращает список словарей, у которых в описании есть данная строка."""
    result_list_dict = list()

    for dict_ in list_dict_transactions:
        if dict_.get("description"):
            description = str(dict_.get("description"))
            search_describe = re.search(str_search, description)
            if search_describe is None:
                continue
            else:
                if search_describe.group() == str_search:
                    result_list_dict.append(dict_)

    return result_list_dict


def get_count_category(list_dict_transactions: list[dict], categories: list) -> dict[Any, int] | str:
    """Принимает список словарей с данными о банковских операциях и список категорий операций.
    Возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    Категории операций хранятся в поле description.
    """
    if categories:
        # Извлекаем все категории из операций
        operation_categories = [op.get('description') for op in list_dict_transactions]
        # Фильтруем только категории из заданного списка
        filtered_categories = [cat for cat in operation_categories if cat in categories]
        # Считаем количество операций в каждой категории
        counts = Counter(filtered_categories)
        # Создаем результат с нулевыми значениями для отсутствующих категорий
        result = {category: counts.get(category, 0) for category in categories}

        return result
    else:
        return "Список транзакций пуст!"
