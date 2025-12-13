import pytest
from src.widget import mask_account_card, get_date


@pytest.fixture
def sample_card_data():
    """икстура с тестовыми данными карт."""
    return "Visa Platinum 7000792289606361"


@pytest.fixture
def sample_account_data():
    """икстура с тестовыми данными счетов."""
    return "Счет 73654108430135874305"


@pytest.fixture
def sample_dates():
    """икстура с тестовыми датами."""
    return [
        "2023-10-01T12:00:00.000000",
        "2024-01-15T08:30:00.000000",
        "2023-12-31T23:59:59.999999",
    ]


def test_mask_account_card_card(sample_card_data):
    """Тест маскирования карты."""
    result = mask_account_card(sample_card_data)
    assert result == "Visa Platinum 7000 79** **** 6361"


def test_mask_account_card_account(sample_account_data):
    """Тест маскирования счета."""
    result = mask_account_card(sample_account_data)
    assert result == "Счет **4305"


def test_get_date():
    """Тест преобразования даты."""
    result = get_date("2023-10-01T12:00:00.000000")
    assert result == "01.10.2023"


def test_get_date_with_z(sample_dates):
    """Тест преобразования даты с разными форматами."""
    result = get_date(sample_dates[0])
    assert result == "01.10.2023"
    
    result = get_date(sample_dates[1])
    assert result == "15.01.2024"
