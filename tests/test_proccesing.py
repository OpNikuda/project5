import pytest
from src.proccesing import filter_by_state

@pytest.mark.parametrize("data, state, expected", [
    # Фильтрация по состоянию 'EXECUTED'
    (
        [
            {'state': 'EXECUTED', 'date': '2023-01-01'},
            {'state': 'PENDING', 'date': '2023-01-02'},
            {'state': 'EXECUTED', 'date': '2023-01-03'},
        ],
        'EXECUTED',
        [
            {'state': 'EXECUTED', 'date': '2023-01-01'},
            {'state': 'EXECUTED', 'date': '2023-01-03'},
        ],
    ),
    # Фильтрация по состоянию 'PENDING'
    (
        [
            {'state': 'EXECUTED', 'date': '2023-01-01'},
            {'state': 'PENDING', 'date': '2023-01-02'},
            {'state': 'EXECUTED', 'date': '2023-01-03'},
        ],
        'PENDING',
        [
            {'state': 'PENDING', 'date': '2023-01-02'},
        ],
    ),
    # Фильтрация по несуществующему состоянию
    (
        [
            {'state': 'EXECUTED', 'date': '2023-01-01'},
            {'state': 'PENDING', 'date': '2023-01-02'},
        ],
        'FAILED',
        [],
    ),
    # Пустой список данных
    (
        [],
        'EXECUTED',
        [],
    ),
    # Отсутствие ключа 'state' в некоторых словарях
    (
        [
            {'state': 'EXECUTED', 'date': '2023-01-01'},
            {'date': '2023-01-02'},  # Нет ключа 'state'
            {'state': 'EXECUTED', 'date': '2023-01-03'},
        ],
        'EXECUTED',
        [
            {'state': 'EXECUTED', 'date': '2023-01-01'},
            {'state': 'EXECUTED', 'date': '2023-01-03'},
        ],
    ),
])
def test_filter_by_state(data, state, expected):
    assert filter_by_state(data, state) == expected

from datetime import datetime
from src.proccesing import sort_by_date

@pytest.mark.parametrize("list_of_dicts, reverse, expected", [
    # Сортировка по убыванию (reverse=True)
    (
        [
            {'date': '2023-01-01'},
            {'date': '2023-01-03'},
            {'date': '2023-01-02'},
        ],
        True,
        [
            {'date': '2023-01-03'},
            {'date': '2023-01-02'},
            {'date': '2023-01-01'},
        ],
    ),
    # Сортировка по возрастанию (reverse=False)
    (
        [
            {'date': '2023-01-03'},
            {'date': '2023-01-01'},
            {'date': '2023-01-02'},
        ],
        False,
        [
            {'date': '2023-01-01'},
            {'date': '2023-01-02'},
            {'date': '2023-01-03'},
        ],
    ),
    # Пустой список
    (
        [],
        True,
        [],
    ),
    # Один элемент в списке
    (
        [{'date': '2023-01-01'}],
        True,
        [{'date': '2023-01-01'}],
    ),
    # Некорректные даты (должны быть пропущены или обработаны)
    (
        [
            {'date': '2023-01-01'},
            {'date': 'Invalid Date'},  # Некорректная дата
            {'date': '2023-01-03'},
        ],
        True,
        [
            {'date': '2023-01-03'},
            {'date': '2023-01-01'},
        ],
    ),
])
def test_sort_by_date(list_of_dicts, reverse, expected):
    if any('date' in d and not isinstance(d['date'], str) for d in list_of_dicts):
        with pytest.raises(ValueError):
            sort_by_date(list_of_dicts, reverse)
    else:
        assert sort_by_date(list_of_dicts, reverse) == expected

