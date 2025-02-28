def mask_card_number(card_number):
    # Маскируем номер карты, оставляя последние 4 цифры открытыми
    return '*' * (len(card_number) - 4) + card_number[-4:]

def mask_account_number(account_number):
    # Маскируем номер счета, оставляя первые 4 и последние 4 цифры открытыми
    return account_number[:4] + '*' * (len(account_number) - 8) + account_number[-4:]

def mask_account_card(payment_info):
    # Определяем, является ли номер картой или счетом
    if payment_info.isdigit():  # Проверяем, состоит ли строка только из цифр
        if len(payment_info) > 16:  # Предположим, что номера счетов длиннее
            return mask_account_number(payment_info)
        else:
            return mask_card_number(payment_info)
    else:
        raise ValueError("Неверный формат номера.")

# Примеры использования
print(mask_account_card('8012841482180128'))  # Вывод: ************0128 (номер карты)
print(mask_account_card('73654108430135874305'))  # Вывод: 7365********8305 (номер счета)
