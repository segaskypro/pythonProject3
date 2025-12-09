import pytest


# икстура для тестовых транзакций
@pytest.fixture
def sample_transactions():
    """Тестовые данные для обработки транзакций"""
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2023-10-01T12:00:00.000000",
            "description": "Payment 1",
            "from": "Visa Platinum 7000792289606361",
            "to": "Счет 73654108430135874305",
            "amount": "100.00",
            "currency": {"name": "USD", "code": "USD"}
        },
        {
            "id": 2,
            "state": "PENDING",
            "date": "2023-09-15T08:30:00.000000",
            "description": "Payment 2",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
            "amount": "50.00",
            "currency": {"name": "EUR", "code": "EUR"}
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2023-11-20T14:45:00.000000",
            "description": "Payment 3",
            "from": "Счет 12345678901234567890",
            "to": "Visa Classic 1234567812345678",
            "amount": "200.00",
            "currency": {"name": "RUB", "code": "RUB"}
        },
    ]

# икстура для номеров карт
@pytest.fixture(params=[
    ("7000792289606361", "7000 79** **** 6361"),
    ("7158300734726758", "7158 30** **** 6758"),
    ("1234567812345678", "1234 56** **** 5678"),
])
def card_number_data(request):
    """араметризованная фикстура для номеров карт"""
    return request.param

# икстура для номеров счетов
@pytest.fixture(params=[
    ("73654108430135874305", "**4305"),
    ("35383033474447895560", "**5560"),
    ("12345678901234567890", "**7890"),
])
def account_number_data(request):
    """араметризованная фикстура для номеров счетов"""
    return request.param
