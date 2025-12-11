import pytest
from src.masks import mask_card_number, mask_account


@pytest.mark.parametrize("card_number, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("7158300734726758", "7158 30** **** 6758"),
    ("1234567812345678", "1234 56** **** 5678"),
    ("", ""),
    ("1234", "1234"),
])
def test_get_mask_card_number_parametrized(card_number, expected):
    """Параметризованный тест маскирования карт."""
    result = mask_card_number(card_number)
    assert result == expected


@pytest.mark.parametrize("account_number, expected", [
    ("73654108430135874305", "**4305"),
    ("35383033474447895560", "**5560"),
    ("12345678901234567890", "**7890"),
    ("", ""),
    ("1234", "**1234"),
])
def test_get_mask_account_parametrized(account_number, expected):
    """Параметризованный тест маскирования счетов."""
    result = mask_account(account_number)
    assert result == expected


def test_get_mask_card_number_with_spaces():
    """Тест маскирования карты с пробелами."""
    result = mask_card_number("7000 7922 8960 6361")
    assert result == "7000 79** **** 6361"


def test_get_mask_account_with_spaces():
    """Тест маскирования счета с пробелами."""
    result = mask_account("7365 4108 4301 3587 4305")
    assert result == "**4305"


def test_get_mask_card_number_short():
    """Тест маскирования короткого номера карты."""
    result = mask_card_number("12345")
    assert result == "12345"


def test_get_mask_account_short():
    """Тест маскирования короткого номера счета."""
    result = mask_account("123")
    assert result == "123"