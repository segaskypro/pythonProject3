def mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты.

    Args:
        card_number (str): Номер карты (16 цифр)

    Returns:
        str: Замаскированный номер в формате XXXX XX** **** XXXX
    """
    # Преобразуем в строку если пришел int (для обратной совместимости)
    card_str = str(card_number)

    # Проверяем что номер состоит из 16 цифр
    if len(card_str) != 16 or not card_str.isdigit():
        return card_str

    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета.

    Args:cat src/processing.py
        account_number (str): Номер счета

    Returns:
        str: Замаскированный номер в формате **XXXX
    """
    # Преобразуем в строку если пришел int
    account_str = str(account_number)

    # Проверяем что номер достаточно длинный
    if len(account_str) < 4 or not account_str.isdigit():
        return account_str

    return f"**{account_str[-4:]}"
