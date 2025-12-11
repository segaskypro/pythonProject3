from widget import mask_account_card, get_date


def test_mask_account_card_card():
    """Тест маскирования карты."""
    result = mask_account_card("Visa Platinum 7000792289606361")
    assert result == "Visa Platinum 7000 79** **** 6361"


def test_mask_account_card_account():
    """Тест маскирования счета."""
    result = mask_account_card("Счет 73654108430135874305")
    assert result == "Счет **4305"


def test_get_date():
    """Тест преобразования даты."""
    result = get_date("2023-10-01T12:00:00.000000")
    assert result == "01.10.2023"


def test_get_date_with_z():
    """Тест преобразования даты с Z."""
    result = get_date("2023-10-01T12:00:00Z")
    assert result == "01.10.2023"
