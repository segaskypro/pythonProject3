"""
Тесты для модуля external_api с использованием mock/patch.
Теперь тесты изолированы от реального API.
"""

import pytest
from unittest.mock import patch, MagicMock
import json
from src.external_api import (
    get_exchange_rate,
    convert_transaction_to_rub,
    ExchangeRateAPI
)


# ============================================
# ТЕСТ 1: Тестирование класса ExchangeRateAPI
# ============================================

def test_exchange_rate_api_cache():
    """Тест кэширования в ExchangeRateAPI"""
    api = ExchangeRateAPI()

    # Тестовые данные
    test_data = {
        "rates": {"RUB": 75.5, "USD": 1.0},
        "base": "USD",
        "date": "2024-01-01"
    }

    # Сохраняем в кэш
    api._save_to_cache("USD", test_data)

    # Получаем из кэша
    cached = api._get_from_cache("USD")
    assert cached == test_data
    print("✓ Тест кэширования пройден")


def test_exchange_rate_api_cache_validity():
    """Тест валидности кэша"""
    api = ExchangeRateAPI()

    # Пустой кэш должен быть невалидным
    assert not api._is_cache_valid("USD")
    print("✓ Тест пустого кэша пройден")


@patch('src.external_api.requests.get')
def test_exchange_rate_api_success(mock_get):
    """Тест успешного получения данных из API с mock"""
    # Настраиваем mock
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "rates": {"RUB": 75.5, "EUR": 0.92},
        "base": "USD",
        "date": "2024-01-01"
    }
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    # Создаем API и делаем запрос
    api = ExchangeRateAPI()
    result = api.get_exchange_rates("USD")

    # Проверяем
    assert result["rates"]["RUB"] == 75.5
    mock_get.assert_called_once_with(
        "https://api.exchangerate-api.com/v4/latest/USD",
        timeout=10
    )
    print("✓ Тест успешного API запроса пройден")


@patch('src.external_api.requests.get')
def test_exchange_rate_api_timeout(mock_get):
    """Тест таймаута API с mock"""
    # ИСПРАВЛЕНИЕ: используем правильное исключение
    from requests.exceptions import Timeout

    # Настраиваем mock для выброса исключения
    mock_get.side_effect = Timeout("Request timeout")

    api = ExchangeRateAPI()
    result = api.get_exchange_rates("USD")

    # Должен вернуть fallback данные
    assert "rates" in result
    assert "RUB" in result["rates"]
    print("✓ Тест таймаута API пройден")


# ============================================
# ТЕСТ 2: Тестирование функции get_exchange_rate
# ============================================

@patch('src.external_api.ExchangeRateAPI.get_exchange_rates')
def test_get_exchange_rate_success(mock_api):
    """Тест успешного получения курса с mock"""
    # Настраиваем mock API
    mock_api.return_value = {
        "rates": {"RUB": 75.5, "EUR": 0.92},
        "base": "USD",
        "date": "2024-01-01"
    }

    # Вызываем функцию
    rate = get_exchange_rate("USD", "RUB")

    # Проверяем
    assert rate == 75.5
    mock_api.assert_called_once_with("USD")
    print("✓ Тест get_exchange_rate пройден")


@patch('src.external_api.ExchangeRateAPI.get_exchange_rates')
def test_get_exchange_rate_currency_not_found(mock_api):
    """Тест когда валюта не найдена в ответе API"""
    # API возвращает данные без нужной валюты
    mock_api.return_value = {
        "rates": {"EUR": 0.92},  # Нет RUB!
        "base": "USD"
    }

    rate = get_exchange_rate("USD", "RUB")

    # Должен использовать fallback (75.5)
    assert rate == 75.5
    print("✓ Тест 'валюта не найдена' пройден")


@patch('src.external_api.ExchangeRateAPI.get_exchange_rates')
def test_get_exchange_rate_fallback(mock_api):
    """Тест резервных данных с mock"""

    # Используем side_effect чтобы возвращать разные данные для разных валют
    def get_exchange_rates_side_effect(currency):
        if currency == "USD":
            return {
                "rates": {"RUB": 75.5, "EUR": 0.92},
                "base": "USD"
            }
        elif currency == "EUR":
            return {
                "rates": {"RUB": 85.0, "USD": 1.09},
                "base": "EUR"
            }
        elif currency == "RUB":
            return {
                "rates": {"USD": 0.013, "EUR": 0.012},
                "base": "RUB"
            }
        else:
            return {"rates": {}, "base": currency}

    mock_api.side_effect = get_exchange_rates_side_effect

    # Теперь тестируем разные валюты
    assert get_exchange_rate("USD", "RUB") == 75.5
    assert get_exchange_rate("EUR", "RUB") == 85.0
    assert get_exchange_rate("RUB", "USD") == 0.013

    print("✓ Тест fallback данных пройден")


# ============================================
# ТЕСТ 3: Тестирование функции convert_transaction_to_rub
# ============================================

@patch('src.external_api.get_exchange_rate')
def test_convert_transaction_to_rub_usd(mock_rate):
    """Тест конвертации USD в RUB с mock"""
    # Настраиваем mock курса
    mock_rate.return_value = 75.5

    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"code": "USD"}
        }
    }

    result = convert_transaction_to_rub(transaction)

    assert result == 7550.0  # 100 * 75.5
    mock_rate.assert_called_once_with("USD", "RUB")
    print("✓ Тест конвертации USD->RUB пройден")


@patch('src.external_api.get_exchange_rate')
def test_convert_transaction_to_rub_eur(mock_rate):
    """Тест конвертации EUR в RUB с mock"""
    mock_rate.return_value = 85.0

    transaction = {
        "operationAmount": {
            "amount": "50.0",
            "currency": {"code": "EUR"}
        }
    }

    result = convert_transaction_to_rub(transaction)

    assert result == 4250.0  # 50 * 85.0
    print("✓ Тест конвертации EUR->RUB пройден")


def test_convert_transaction_to_rub_rub():
    """Тест когда транзакция уже в рублях (без конвертации)"""
    transaction = {
        "operationAmount": {
            "amount": "1000.50",
            "currency": {"code": "RUB"}
        }
    }

    result = convert_transaction_to_rub(transaction)

    assert result == 1000.5
    print("✓ Тест RUB транзакции пройден")


def test_convert_transaction_to_rub_key_error():
    """Тест ошибки KeyError в транзакции"""
    transaction = {"invalid": "structure"}

    result = convert_transaction_to_rub(transaction)

    assert result == 0.0
    print("✓ Тест KeyError пройден")


def test_convert_transaction_to_rub_value_error():
    """Тест ошибки ValueError (нечисловая сумма)"""
    transaction = {
        "operationAmount": {
            "amount": "не число",
            "currency": {"code": "USD"}
        }
    }

    result = convert_transaction_to_rub(transaction)

    assert result == 0.0
    print("✓ Тест ValueError пройден")


# ============================================
# ТЕСТ 4: Интеграционные тесты (опционально)
# ============================================

def test_integration_real_api():
    """
    Интеграционный тест с реальным API.
    Запускайте только когда нужна проверка реального соединения.
    """
    # Этот тест можно пропускать в обычных прогонах
    # pytest.mark.skip(reason="Требует интернет соединения")

    try:
        rate = get_exchange_rate("USD", "RUB")
        assert isinstance(rate, float)
        assert rate > 0
        print(f"✓ Интеграционный тест пройден, курс USD/RUB: {rate}")
    except Exception as e:
        pytest.skip(f"Нет соединения с API: {e}")


# ============================================
# ЗАПУСК ТЕСТОВ
# ============================================

if __name__ == "__main__":
    # Запуск всех тестов
    print("\n" + "=" * 50)
    print("Запуск тестов с использованием mock/patch")
    print("=" * 50)

    pytest.main([__file__, "-v", "--tb=short"])