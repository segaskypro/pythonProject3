import pytest

from widget import get_date, mask_account_card


def test_mask_account_card_card():
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"

def test_mask_account_card_account():
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"

def test_get_date():
    assert get_date("2023-10-01T12:00:00.000000") == "01.10.2023"

def test_get_date_with_z():
    assert get_date("2023-10-01T12:00:00Z") == "01.10.2023"
