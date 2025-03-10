import pytest
from your_module import (  # Замените your_module на название вашего модуля
    get_mask_card_number,
    get_mask_account,
    mask_account_card,
    get_date,
    filter_by_state,
    sort_by_date,
)

# Фикстуры для тестов
@pytest.fixture
def card_numbers():
    return [
        '1234567812345678',
        '9876543210123456',
        '1234',  # короткий номер
        '',  # пустая строка
        'abc1234567890123',  # невалидный номер
    ]

@pytest.fixture
def account_numbers():
    return [
        '12345678901234567890',
        '98765432101234567890',
        '1234',  # короткий номер
        '',  # пустая строка
    ]

@pytest.fixture
def sample_data():
    return [
        {'state': 'EXECUTED', 'date': '2023-01-01'},
        {'state': 'PENDING', 'date': '2023-01-02'},
        {'state': 'EXECUTED', 'date': '2023-01-03'},
    ]

@pytest.fixture
def date_strings():
    return [
        '2023-01-01',
        '01/01/2023',
        'Invalid Date',
        '',  # пустая строка
    ]

# Тесты для get_mask_card_number
@pytest.mark.parametrize("card_number, expected", [
    ('1234567812345678', '************5678'),
    ('9876543210123456', '************3456'),
    ('1234', ''),  # короткий номер
    ('', ''),  # пустая строка
    ('abc1234567890123', ''),  # невалидный номер
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected

# Тесты для get_mask_account
@pytest.mark.parametrize("account_number, expected", [
    ('12345678901234567890', '1234********7890'),
    ('98765432101234567890', '9876********7890'),
    ('1234', ''),  # короткий номер
    ('', ''),  # пустая строка
])
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected

# Тесты для mask_account_card
@pytest.mark.parametrize("payment_info, expected", [
    ('1234567812345678', '************5678'),
    ('12345678901234567890', '1234********7890'),
    ('1234', ''),  # короткий номер
    ('', ''),  # пустая строка
    ('abc1234567890123', ''),  # невалидный номер
])
def test_mask_account_card(payment_info, expected):
    assert mask_account_card(payment_info) == expected

# Тесты для get_date
@pytest.mark.parametrize("date_string, expected", [
    ('2023-01-01', '2023-01-01'),
    ('01/01/2023', '2023-01-01'),  # Преобразование формата
    ('Invalid Date', None),  # Некорректная дата
    ('', None),  # Пустая строка
])
def test_get_date(date_string, expected):
    assert get_date(date_string) == expected

# Тесты для filter_by_state
@pytest.mark.parametrize("state, expected_count", [
    ('EXECUTED', 2),
    ('PENDING', 1),
    ('FAILED', 0),  # Нет таких статусов
])
def test_filter_by_state(sample_data, state, expected_count):
    result = filter_by_state(sample_data, state)
    assert len(result) == expected_count

# Тесты для sort_by_date
def test_sort_by_date(sample_data):
    sorted_data = sort_by_date(sample_data)
    assert sorted_data[0]['date'] == '2023-01-03'  # Проверка на убывание
    assert sorted_data[1]['date'] == '2023-01-01'

# Тесты на некорректные форматы дат
def test_sort_by_date_invalid(sample_data):
    sample_data.append({'state': 'EXECUTED', 'date': 'Invalid Date'})
    sorted_data = sort_by_date(sample_data)
    assert sorted_data[0]['date'] == '
