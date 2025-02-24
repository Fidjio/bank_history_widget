def filter_by_state(list_of_operation_dictionaries: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Принимает словарь с данными об операции и значение ключа state.
    Возвращает инфо об операции в зависимости от выбранного ключа"""
    new_list_user_operations = list()

    for user_operation in list_of_operation_dictionaries:
        if user_operation["state"] == state:
            new_list_user_operations.append(user_operation)

    return new_list_user_operations


def sort_by_date(list_dict: list[dict], sort_key: bool = True) -> list[dict]:
    """Получает список словарей операций по картам/счетам клиента.
    Возвращает отсортированный список словарей по датам"""
    new_list = sorted(list_dict, key=lambda list_dict: list_dict["date"], reverse=sort_key)

    return new_list
