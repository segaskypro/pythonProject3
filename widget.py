import re
from datetime import datetime

from masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: str) -> str:
    """пределяет тип (карта или счёт) и маскирует номер."""
    if not account_info:
        return ""

    text_lower = account_info.lower()

    if "счет" in text_lower or "счёт" in text_lower or "account" in text_lower:
        digits = re.sub(r'\D', '', account_info)
        if len(digits) == 20:
            masked = get_mask_account(digits)
            return re.sub(r'\d{20}', masked, account_info)
    else:
        digits = re.sub(r'\D', '', account_info)
        if len(digits) == 16:
            masked = get_mask_card_number(digits)
            return re.sub(r'\d{16}', masked, account_info)

    return account_info


def get_date(date_str: str) -> str:
    """реобразует дату в формат DD.MM.YYYY."""
    if not date_str:
        return ""

    try:
        if date_str.endswith('Z'):
            date_str = date_str[:-1] + '+00:00'
        dt = datetime.fromisoformat(date_str)
        return dt.strftime("%d.%m.%Y")
    except (ValueError, TypeError):
        return date_str
