def get_mask_card_number(card_number):
    card_number = str(card_number).replace(" ", "")
    if not card_number.isdigit() or len(card_number) < 10:
        return ""

    first_six = card_number[:6]
    last_four = card_number[-4:]
    masked_number = f"{first_six[:4]} {first_six[4:6]}** **** {last_four}"
    return masked_number


def get_mask_account(account_number):
    account_number = str(account_number).replace(" ", "")
    if not account_number.isdigit() or len(account_number) < 4:
        return ""

    last_four = account_number[-4:]
    masked_part = "*" * (len(account_number) - 4)
    masked_account = masked_part + last_four
    return masked_account

 #bebra