def filter_by_state(list_of_operation_dictionaries: list[dict], state: str ='EXECUTED') -> list[dict]:
    """ Принимает словарь с данными об операции и значение ключа state.
    Возвращает инфо об операции в зависимости от выбранного ключа """
    new_list_user_operations = list()

    for user_operation in list_of_operation_dictionaries:
        if user_operation['state'] == state:
            new_list_user_operations.append(user_operation)

    return new_list_user_operations
