import csv
import json
import os

from src.generators import filter_by_currency
from src.processing import filter_by_state, search_transaction, sort_by_date
from src.read_file_from_pandas import read_cvs_files, read_excel_files
from src.utils import get_info_transactions_json
from src.widget import get_date, mask_account_card
from tests.conftest import result_sort_date


def main() -> None:
    list_files = ["JSON", "CSV", "XLSX"]
    path_to_files = {
        "JSON": "data\\operations.json",
        "CSV": "data\\transactions.csv",
        "XLSX": "data\\transactions_excel.xlsx",
    }
    path_to_file = str()
    func_to_open_file = {"JSON": get_info_transactions_json, "CSV": read_cvs_files, "XLSX": read_excel_files}
    states = ["EXECUTED", "CANCELED", "PENDING"]
    filter_transactions_dict = dict

    ####################################################################################################

    # Выбор файла для обработки транзакций
    print("    Программа: Привет! Добро пожаловать в программу работы" "с банковскими транзакциями.")
    while True:
        try:
            user_num_file = input(
                """
        Выберите необходимый пункт меню:
        
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
    
    Пользователь: """
            )
            extension_file_user = list_files[int(user_num_file) - 1]
            print(f"Программа: Для обработки выбран {extension_file_user}-файл")
            for extension, path_ in path_to_files.items():
                if extension == extension_file_user:
                    path_to_file = path_
            break

        except (TypeError, IndexError, ValueError):
            print(f"\nВведите цифру от 1 до 3.")

    # Выбор статуса для фильтрации транзакций и фильтрация файла
    while True:
        try:
            state = (
                input(
                    "Программа: Введите статус, по которому необходимо выполнить фильтрацию.\n"
                    "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
                    "Пользователь: "
                )
                .upper()
                .strip()
            )

            if state in states:
                for extension, func_reader in func_to_open_file.items():
                    if extension == extension_file_user:
                        info_in_file = func_reader(path_to_file)
                        filter_transactions_dict = filter_by_state(info_in_file, str(state))
                        print(f'Программа: Операции отфильтрованы по статусу "{state}"')
                break
            else:
                print(f"Программа: Статус операции {state} недоступен.")
        except Exception as ex:
            print(f"Произошло исключение: {ex}")

    # Выбор сортировки полученного словаря filter_transactions_dict
    while True:
        user_input = input("Программа: Отсортировать операции по дате? Да/Нет\nПользователь: ")
        if user_input.lower() == "да":
            flag_ = input("Программа: Отсортировать по возрастанию или по убыванию?\nПользователь: ")
            if flag_.lower() == "по убыванию":
                filter_transactions_dict = sort_by_date(filter_transactions_dict)
            elif flag_.lower() == "по возрастанию":
                filter_transactions_dict = sort_by_date(filter_transactions_dict, False)

        user_input = input("Программа: Выводить только рублевые транзакции? Да/Нет\nПользователь: ")
        if user_input.lower() == "да":
            filter_transactions_dict = list(filter_by_currency(filter_transactions_dict, "RUB"))

        user_input = input(
            "Программа: Отфильтровать список транзакций по определенному слову " "в описании? Да/Нет\nПользователь: "
        )
        if user_input.lower() == "да":
            description = input("Программа: Введите слово для поиска.\nПользователь: ")
            filter_transactions_dict = search_transaction(filter_transactions_dict, description)
        break

    print("Программа: Распечатываю итоговый список транзакций...\n")

    # Вывод транзакций
    print(f"Программа: Всего банковских операций в выборке: {len(filter_transactions_dict)}")
    # if extension_file_user == 'JSON':
    for dict_ in filter_transactions_dict:
        print(f"\n{get_date(dict_.get('date'))} {dict_.get('description')}")
        if dict_.get("description").split()[0] == "Перевод":
            print(f"{mask_account_card(dict_.get('from'))} -> {mask_account_card(dict_.get('to'))}")
            print(
                f"Сумма: {dict_.get('operationAmount').get('amount')} "
                f"{dict_.get('operationAmount').get('currency').get('name')}"
            )
        else:
            print(f"{mask_account_card(dict_.get('to'))}")
            print(
                f"Сумма: {dict_.get('operationAmount').get('amount')} "
                f"{dict_.get('operationAmount').get('currency').get('name')}"
            )


if __name__ == "__main__":
    print(main())
