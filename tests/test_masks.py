import pytest

from masks import get_mask_account, get_mask_card_number


def test_card_basic():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"

def test_card_with_spaces():
    assert get_mask_card_number("7000 7922 8960 6361") == "7000 79** **** 6361"

def test_card_short():
    assert get_mask_card_number("1234") == "1234"

def test_card_empty():
    assert get_mask_card_number("") == ""

def test_account_basic():
    assert get_mask_account("73654108430135874305") == "**4305"

def test_account_with_spaces():
    assert get_mask_account("7365 4108 4301 3587 4305") == "**4305"

def test_account_short():
    assert get_mask_account("1234") == "**1234"

def test_account_empty():
    assert get_mask_account("") == ""
