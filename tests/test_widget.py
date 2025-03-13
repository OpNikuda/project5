import pytest
from src.widget import mask_card_number, mask_account_number, mask_account_card

def test_mask_card_number():
    # Тест для маскирования номера карты
    assert mask_card_number("1234567890123456") == "************3456", "Ошибка в маскировании номера карты"
    assert mask_card_number("1111222233334444") == "************4444", "Ошибка в маскировании номера карты"
    assert mask_card_number("9999888877776666") == "************6666", "Ошибка в маскировании номера карты"

def test_mask_account_number():
    # Тест для маскирования номера счёта
    assert mask_account_number("12345678901234567890") == "1234********7890", "Ошибка в маскировании номера счёта"
    assert mask_account_number("98765432109876543210") == "9876********3210", "Ошибка в маскировании номера счёта"
    assert mask_account_number("11112222333344445555") == "1111********5555", "Ошибка в маскировании номера счёта"

def test_mask_account_card():
    # Тест для функции, которая определяет тип номера и маскирует его
    assert mask_account_card("1234567890123456") == "************3456", "Ошибка в маскировании номера карты"
    assert mask_account_card("12345678901234567890") == "1234********7890", "Ошибка в маскировании номера счёта"

    # Тест на невалидный формат (содержит нецифровые символы)
    try:
        mask_account_card("1234abc567890123456")
        assert False, "Ожидалось исключение ValueError"
    except ValueError:
        pass  # Ожидаемое поведение

def test_edge_cases():
    # Тест на граничные случаи
    assert mask_card_number("1234") == "1234", "Ошибка в маскировании короткого номера карты"
    assert mask_account_number("12345678901234567") == "1234********567", "Ошибка в маскировании короткого номера счёта"

    # Тест на пустую строку
    try:
        mask_account_card("")
        assert False, "Ожидалось исключение ValueError"
    except ValueError:
        pass  # Ожидаемое поведение

