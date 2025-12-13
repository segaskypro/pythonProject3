def mask_card_number(card_number: str) -> str:
    """аскирует номер банковской карты."""
    clean_number = "".join(card_number.split())
    card_str = str(clean_number)

    if len(card_str) != 16 or not card_str.isdigit():
        return card_number

    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def mask_account(account_number: str) -> str:
    """аскирует номер банковского счета."""
    clean_number = "".join(account_number.split())
    account_str = str(clean_number)

    if len(account_str) < 4 or not account_str.isdigit():
        return account_number

    return f"**{account_str[-4:]}"
