from src.external_api import get_exchange_rate, convert_transaction_to_rub


def test_get_exchange_rate_usd():
    """Тест курса USD."""
    rate = get_exchange_rate("USD")
    assert rate == 75.5


def test_get_exchange_rate_eur():
    """Тест курса EUR."""
    rate = get_exchange_rate("EUR")
    assert rate == 85.0


def test_get_exchange_rate_rub():
    """Тест курса RUB."""
    rate = get_exchange_rate("RUB")
    assert rate == 1.0


def test_get_exchange_rate_unknown():
    """Тест неизвестной валюты."""
    rate = get_exchange_rate("UNKNOWN")
    assert rate == 1.0


def test_convert_transaction_to_rub_rub():
    """Тест конвертации RUB -> RUB."""
    transaction = {
        "operationAmount": {
            "amount": "1000.50",
            "currency": {"code": "RUB"}
        }
    }
    
    result = convert_transaction_to_rub(transaction)
    assert result == 1000.5


def test_convert_transaction_to_rub_usd():
    """Тест конвертации USD -> RUB."""
    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"code": "USD"}
        }
    }
    
    result = convert_transaction_to_rub(transaction)
    assert result == 7550.0


def test_convert_transaction_to_rub_eur():
    """Тест конвертации EUR -> RUB."""
    transaction = {
        "operationAmount": {
            "amount": "50.0",
            "currency": {"code": "EUR"}
        }
    }
    
    result = convert_transaction_to_rub(transaction)
    assert result == 4250.0
