from . import masks


def mask_account_card(account_info: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от типа.

    Args:
        account_info (str): Строка с информацией о карте/счете 
                          (например, "Visa Platinum 7000792289606361")

    Returns:
        str: Строка с замаскированным номером
    """
    # Разделяем строку на части
    parts = account_info.split()

    # Последний элемент - номер, остальное - название
    card_number = parts[-1]
    card_name = " ".join(parts[:-1])

    # Определяем тип и применяем соответствующую маскировку
    if card_name.lower() == "счет":
        masked_number = masks.mask_account(card_number)
    else:
        masked_number = masks.mask_card_number(card_number)

    return f"{card_name} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ.

    Args:
        date_string (str): Дата в формате "2024-03-11T02:26:18.671407"

    Returns:
        str: Дата в формате "11.03.2024"
    """
    # Берем только часть до 'T' (дату)
    date_part = date_string.split('T')[0]

    # Разбиваем на год, месяц, день
    year, month, day = date_part.split('-')

    return f"{day}.{month}.{year}"