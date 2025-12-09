def get_mask_card_number(card_number: str) -> str:
    """аскирует номер карты: XXXX XX** **** XXXX"""
    if not card_number:
        return ""
    # бираем пробелы
    clean = str(card_number).replace(" ", "")
    # роверяем что это 16 цифр
    if len(clean) == 16 and clean.isdigit():
        return f"{clean[:4]} {clean[4:6]}** **** {clean[-4:]}"
    return str(card_number)


def get_mask_account(account_number: str) -> str:
    """аскирует номер счёта: **XXXX"""
    if not account_number:
        return ""
    # бираем пробелы
    clean = str(account_number).replace(" ", "")
    # ужно минимум 4 цифры
    if len(clean) >= 4 and clean.isdigit():
        return f"**{clean[-4:]}"
    return str(account_number)
