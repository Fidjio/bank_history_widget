# Виджет банковских операций клиента

Данный виджет получает данные о карте или счете от клиента, обрабатывает и возвращает редактированную информацию.
Виды обработки информации представлены ниже в разделе **"Реализованные функции"**

## Статус проекта:
+ Статус разработки: *в разработке*

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

- Модуль generators.py
    - test_filter_by_currency
    - test_transaction_descriptions
    - test_param_transaction_descriptions
    - test_card_number_generator

***Для хранения фикстур создан файл conftest.py***


## Установка:
*Не требует обязательных условий.*
* Установить Poetry `pip install poetry`
+ Слить проект из GitHub https://github.com/Fidjio/bank_history_widget.git
+ Запуск программы выполняестя из файла main.py в корне каталога *python main.py*


## Команда проекта
Сергей Карсканов - Junior Python developer
