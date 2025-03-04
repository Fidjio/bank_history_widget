import pytest


@pytest.fixture
def dict_list_state():
    """Список словарей для проверки функции filter_by_state"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

@pytest.fixture
def return_dict_by_executed():
    """Результат работы функции filter_by_state при выбранном ключе state EXECUTED"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
    ]

@pytest.fixture
def return_dict_by_canceled():
    """Результат работы функции filter_by_state при выбранном ключе state CANCELED"""
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
    ]

@pytest.fixture
def dict_for_sort():
    """Cписок словарей для сортировки с помощью функции sort_by_date"""
    return [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2020-09-12T21:27:25.241689'},
    ]

@pytest.fixture
def result_sort_date():
    """Результат работы функции sort_by_date с фикстурой dict_for_sort"""
    return [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2020-09-12T21:27:25.241689'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]

@pytest.fixture
def result_sort_date_reverse():
    """Результат работы функции sort_by_date с фикстурой dict_for_sort"""
    return [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2020-09-12T21:27:25.241689'}
    ]
