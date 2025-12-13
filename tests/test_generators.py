"""Tests for generators module."""
import pytest
from generators import (filter_by_currency,
                        transaction_descriptions,
                        card_number_generator)


# Test data from assignment
TRANSACTIONS = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"}
        },
        "description": "Transfer to organization",
        "from": "Account 75106830613657916952",
        "to": "Account 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {"name": "USD", "code": "USD"}
        },
        "description": "Transfer between accounts",
        "from": "Account 19708645243227258542",
        "to": "Account 75651667383060284188"
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {"name": "RUB", "code": "RUB"}
        },
        "description": "Transfer between accounts",
        "from": "Account 44812258784861134719",
        "to": "Account 74489636417521191160"
    },
]


@pytest.fixture
def sample_transactions():
    """Fixture with test transactions."""
    return TRANSACTIONS.copy()


@pytest.fixture
def empty_transactions():
    """Fixture with empty transaction list."""
    return []


class TestFilterByCurrency:
    """Tests for filter_by_currency"""

    def test_filter_usd_transactions(self, sample_transactions):
        """Test filtering USD transactions."""
        usd_transactions = filter_by_currency(sample_transactions, "USD")

        first = next(usd_transactions)
        second = next(usd_transactions)

        assert first["id"] == 939719570
        assert second["id"] == 142264268
        assert first["operationAmount"]["currency"]["code"] == "USD"
        assert second["operationAmount"]["currency"]["code"] == "USD"

    def test_filter_rub_transactions(self, sample_transactions):
        """Test filtering RUB transactions."""
        rub_transactions = filter_by_currency(sample_transactions, "RUB")
        transaction = next(rub_transactions)

        assert transaction["id"] == 873106923
        assert transaction["operationAmount"]["currency"]["code"] == "RUB"

    def test_filter_no_transactions(self, sample_transactions):
        """Test filtering when currency is not present."""
        eur_transactions = filter_by_currency(sample_transactions, "EUR")
        with pytest.raises(StopIteration):
            next(eur_transactions)

    def test_empty_list(self, empty_transactions):
        """Test with empty list."""
        result = filter_by_currency(empty_transactions, "USD")
        with pytest.raises(StopIteration):
            next(result)


class TestTransactionDescriptions:
    """Tests for transaction_descriptions"""

    def test_get_descriptions(self, sample_transactions):
        """Test getting descriptions."""
        descriptions = transaction_descriptions(sample_transactions)

        assert next(descriptions) == "Transfer to organization"
        assert next(descriptions) == "Transfer between accounts"
        assert next(descriptions) == "Transfer between accounts"

    def test_empty_transactions(self, empty_transactions):
        """Test with empty list."""
        descriptions = transaction_descriptions(empty_transactions)
        with pytest.raises(StopIteration):
            next(descriptions)


class TestCardNumberGenerator:
    """Tests for card_number_generator"""

    def test_generate_numbers(self):
        """Test generating card numbers."""
        generator = card_number_generator(1, 5)

        expected = [
            "0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003",
            "0000 0000 0000 0004",
            "0000 0000 0000 0005",
        ]

        for i, card_number in enumerate(generator):
            assert card_number == expected[i]

    def test_single_number(self):
        """Test generating single number."""
        generator = card_number_generator(9999999999999999, 9999999999999999)
        assert next(generator) == "9999 9999 9999 9999"

    @pytest.mark.parametrize("start,end,expected_count", [
        (1, 10, 10),
        (100, 105, 6),
        (9999, 10000, 2),
    ])
    def test_parametrized_ranges(self, start, end, expected_count):
        """Parametrized test for different ranges."""
        generator = card_number_generator(start, end)
        count = sum(1 for _ in generator)
        assert count == expected_count
