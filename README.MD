# Виджет банковских операций клиента

Данный виджет получает данные о карте или счете от клиента, обрабатывает и возвращает редактированную информацию.
Виды обработки информации представлены ниже в разделе **"Реализованные функции"**
Запуск программы происходит через запуск main.py

## Статус проекта:
+ Статус разработки: готов.

## Технологии: 
+ Python
+ GitHub
+ PyCharm

## Реализованные функции
### Модуль masks.py


1. ***get_mask_card_number*** - маскирует номер банковской карты. Вызов функции:\
`print(get_mask_card_number("1111222233334444"))` -> `1111 22** **** 4444`

2. ***get_mask_account*** - vаскирует номер банковского счета. Вызов функции:\
`print(get_mask_account("88897745"))` -> `**7745`


### Модуль processing.py
1. ***filter_by_state*** - принимает словарь с данными об операции и значение ключа state.
    Возвращает инфо об операции в зависимости от выбранного ключа. Вызов функции:\
`print(
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
        )
    )` \
-> \
`[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 
'date': '2018-06-30T02:08:58.425572'}]`

2. ***sort_by_date*** - Получает список словарей операций по картам/счетам клиента.
    Возвращает отсортированный список словарей по датам. Вызов функции:\
`print(
        filter_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
        )
    )`\
-> \
`[{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
`
3. ***search_transaction*** - Принимает список словарей с данными о банковских операциях и строку поиска.
    Возвращает список словарей, у которых в описании есть данная строка. Вызов функции:\
`search_transaction(dict_transactions, str_search)`\
-> \
[{'price': 15, 'description': 'Перевод'}, {'price': 2323, 'description': 'Перевод в банк'}]

4. ***get_count_category*** - Принимает список словарей с данными о банковских операциях и список категорий операций.
    Возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    Категории операций хранятся в поле description. Вызов функции:\
`get_count_category(dict_transactions, []`\
-> \
[{'price': 15, 'description': 'Перевод'}, {'price': 30, 'description': 'Перевод', }]
 


### Модуль widget.py
1. ***mask_account_card*** - маскировка номера карты или счета. Вызов функции:\
`    with open(PATH_TO_DATA + name_file, "r", encoding="utf-8") as file:
        for line in file:
            print(mask_account_card(line))`\
-> \
`1596 83** **** 5199 |
**9589 |
7158 30** **** 6758 |
**5560 |
6831 98** **** 7658 |
8990 92** **** 5229 |
5999 41** **** 6353 |
**4305`

2. ***get_date*** - оставляет только дату из даты и времени. Вызов функции:\
`print(get_date("2024-03-11T02:26:56"))` -> `11.03.2024`


### Модуль generators.py
1. ***filter_by_currency*** - принимает список словарей ->
    возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD). Вызов функции:\
`usd_transactions = filter_by_currency(transactions, "USD")
    try:
        for _ in transactions:
            print(next(usd_transactions))
    except StopIteration:
        pass`

2. ***transaction_descriptions*** - принимает список словарей с транзакциями и
    возвращает описание каждой операции по очереди. Вызов функции:\
`descriptions = transaction_descriptions(transactions)
    for description in descriptions:
        print(description)` -> Перевод организации

3. ***card_number_generator*** - выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где
    X — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор принимает начальное и конечное значения для генерации диапазона номеров. Вызов функции:\
`for card_number in card_number_generator(10, 13):
        print(card_number)` -> \
0000 0000 0000 0010 \
0000 0000 0000 0011 \
0000 0000 0000 0012


### Модуль generators.py
1. ***log*** - декоратор, который выводит логи декорируемой функции в консоль
    или записывает их в файл. Декоратор принимает необязательный аргумент filename - имя файла,
    в который будут записаны логи. Если имя файла не указано, логи будут выведены в консоль. Вызов функции:\
Декорируем функцию с помощью декоратора log -> \
`@log(filename="FILENAME")
def get_func_to_log(func, *args, **kwargs):
    return func(*args, **kwargs)`
Вызываем функцию, которую декорировали и передаем ей значения -> \
`get_func_to_log(func, args)`, где \
*func* - функция, из которой нужно извлечь логи \
*args* - аргументы функции, из которой нужно извлечь логи \

Вывод, если ошибки не было -> \
*2025-03-21 17:03:27: Name functions: *NAME_FUNC* -> ok.\
2025-03-21 17:03:27: Result functions: *RESULT_FUNC**

Вывод, если произошла ошибка в функции -> \
*2025-03-21 17:04:19: \
Function stopped.\
Name function: summ_\
Error: TypeError.\
Сообщение исключения: unsupported operand type(s) for +: 'int' and 'str'.\
Inputs: ((2, '4'), {})*


### Модуль utils.py
1. ***get_info_transactions_json*** - функция, которая возвращает список словарей из 
json-файла с данными о финансовых транзакциях пользователей. Вызов функции ->\
`get_info_transactions_json(path: str)`, где *path* - абсолютный путь к файлу json.\
Вывод функции ->\
`{
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }`


### Модуль external_api.py
1. ***convert_amount*** - функция, которая принимает сумму транзакции и код валюты (например, USD) и
    возвращает сумму транзакции в рублях. Для работы функции используется API APILAYER. Ссыла на API
https://apilayer.com/marketplace/exchangerates_data-api. 
Для работы функции необходимо зарегистрироваться на сайте API и скопировать API ключ. Далее, ключ, 
необходимо добавить в файл .env *API_KEY=your api key*. Вызов функции ->\
`transactions = get_info_transactions_json(path)
print(convert_amount(transactions[0]))`, где path - путь к json-файлу со списком словарей 
транзакций, которые необходимо конвертировать. Вывод функции -> \
`*200.00*` - сумма транзакций в рублях.



### Модуль read_file_from_pandas.py
1. ***read_cvs_files*** - функция для считывания финансовых операций из CSV принимает путь
    к файлу CSV в качестве аргумента выдает список словарей с транзакциями. Вызов функции ->\
`print(read_cvs_files(path_to_file))`, где path_to_file - путь до файла csv. Вывод функции ->\
`[{'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': '16210', 'currency_name': 'Sol',
      'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
      'description': 'Перевод организации'}]`
2. ***read_excel_files*** - функция для считывания финансовых операций из Excel, 
которая принимает путь к файлу Excel в качестве аргумента и выдает список словарей 
с транзакциями. Вызов функции ->\
`print(read_excel_files('path_to_file'))`, где path_to_file - путь до файла csv. Вывод функции ->\
`[{'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': '16210', 'currency_name': 'Sol',
   'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
   'description': 'Перевод организации'}]`

## Добавлены тесты для pytest. Список тестов:
- Модуль test_masks.py
    - test_card_mask
    - test_mask_account
  
- Модуль test_processing.py
    - test_filter_by_state
    - test_sort_by_date
    - test_sort_date_false_key
    - test_sort_date
  
- Модуль test_widget.py
    - test_mask_account_card
    - test_get_date

- Модуль test_generators.py

    - test_filter_by_currency
    - test_transaction_descriptions
    - test_param_transaction_descriptions
    - test_card_number_generator

- Модуль test_decorators.py
    - test_decorator_log_not_error
    - test_decorator_log_with_error

- Модуль test_utils.py
    - test_get_info_transactions_json

- Модуль test_external.py
    - test_convert_amount
    - test_convert_amount_type

- Модуль test_read_file_pd.py
    - test_read_cvs_files
    - test_read_cvs_file_empty
    - test_read_excel_files_success
    - test_read_excel_files_file_not_found
    - test_read_excel_files_invalid_data

- Модуль test_categories.py
  - test_count_existing_categories
  - test_count_with_missing_category
  - test_empty_categories_list
  - test_empty_transactions
  - test_case_sensitivity

- Модуль test_transactions.py
  - test_find_full_match
  - test_find_partial_match
  - test_no_matches
  - test_empty_search


***Для хранения фикстур создан файл conftest.py***

***Для хранения секретных данных используейте .env.example, предварительно сменив расширение 
на .env.***


## Установка:
*Не требует обязательных условий.*
* Установить Poetry `pip install poetry`
* Установить завиимости проекта.
+ Слить проект из GitHub https://github.com/Fidjio/bank_history_widget.git
+ Запуск программы выполняестя из файла main.py в корне каталога *python main.py*


## Команда проекта
Сергей Карсканов - Junior Python developer
