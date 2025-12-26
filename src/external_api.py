# Файл: src/external_api_new.py
# ШАГ 1: Импорты
import os
import requests
import json
from typing import Dict, Any, Optional
from dotenv import load_dotenv
from datetime import datetime, timedelta

# ШАГ 2: Загружаем переменные окружения
load_dotenv()


# ШАГ 3: Класс для работы с API
class ExchangeRateAPI:
    """Класс для работы с API курсов валют с кэшированием"""

    def __init__(self):
        self.api_key = os.getenv("EXCHANGE_RATE_API_KEY", "")
        self.cache_duration = timedelta(hours=1)
        self.cache = {}
        self.last_update = {}

    def _is_cache_valid(self, from_currency: str) -> bool:
        """Проверяет, действителен ли кэш для валюты"""
        if from_currency not in self.last_update:
            return False
        return datetime.now() - self.last_update[from_currency] < self.cache_duration

    def _get_from_cache(self, from_currency: str) -> Optional[Dict]:
        """Получает данные из кэша"""
        if self._is_cache_valid(from_currency):
            return self.cache.get(from_currency)
        return None

    def _save_to_cache(self, from_currency: str, data: Dict):
        """Сохраняет данные в кэш"""
        self.cache[from_currency] = data
        self.last_update[from_currency] = datetime.now()

    def get_exchange_rates(self, from_currency: str) -> Dict:
        """
        Получает курсы валют из API с кэшированием.

        Args:
            from_currency: Базовая валюта (например, "USD")

        Returns:
            Словарь с курсами валют
        """
        # Проверяем кэш
        cached_data = self._get_from_cache(from_currency)
        if cached_data:
            print(f"Использую кэшированные данные для {from_currency}")
            return cached_data

        print(f"Запрашиваю курсы из API для {from_currency}...")

        try:
            # Используем бесплатный API
            url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

            # Делаем запрос с таймаутом
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            data = response.json()

            # Сохраняем в кэш
            self._save_to_cache(from_currency, data)

            return data

        except requests.exceptions.Timeout:
            print("Ошибка: таймаут при запросе к API")
            return self._get_fallback_rates(from_currency)
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе к API: {e}")
            return self._get_fallback_rates(from_currency)
        except (ValueError, KeyError, json.JSONDecodeError) as e:
            print(f"Ошибка обработки данных API: {e}")
            return self._get_fallback_rates(from_currency)

    def _get_fallback_rates(self, from_currency: str) -> Dict:
        """Возвращает резервные тестовые данные при ошибке API"""
        print(f"Использую резервные данные для {from_currency}")

        fallback_rates = {
            "USD": {
                "rates": {"USD": 1.0, "EUR": 0.92, "RUB": 75.5},
                "base": "USD",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "EUR": {
                "rates": {"USD": 1.09, "EUR": 1.0, "RUB": 85.0},
                "base": "EUR",
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "RUB": {
                "rates": {"USD": 0.013, "EUR": 0.012, "RUB": 1.0},
                "base": "RUB",
                "date": datetime.now().strftime("%Y-%m-%d")
            }
        }

        return fallback_rates.get(from_currency.upper(), {
            "rates": {from_currency.upper(): 1.0, "RUB": 1.0},
            "base": from_currency.upper(),
            "date": datetime.now().strftime("%Y-%m-%d")
        })


# ШАГ 4: Создаем глобальный экземпляр API
_exchange_api = ExchangeRateAPI()


# ШАГ 5: Основная функция для получения курса
def get_exchange_rate(from_currency: str, to_currency: str = "RUB") -> float:
    """
    Получает текущий курс обмена валют через внешнее API.

    Args:
        from_currency: Исходная валюта (например, "USD", "EUR")
        to_currency: Целевая валюта (по умолчанию "RUB")

    Returns:
        Курс обмена
    """
    try:
        # Получаем данные из API
        data = _exchange_api.get_exchange_rates(from_currency.upper())

        # Извлекаем нужный курс
        rates = data.get("rates", {})
        target_currency = to_currency.upper()

        if target_currency not in rates:
            print(f"Валюта {target_currency} не найдена в ответе API")
            return _get_fallback_rate(from_currency.upper(), target_currency)

        rate = rates[target_currency]
        return float(rate)

    except Exception as e:
        print(f"Критическая ошибка при получении курса: {e}")
        return _get_fallback_rate(from_currency.upper(), to_currency.upper())


# ШАГ 6: Резервная функция
def _get_fallback_rate(from_currency: str, to_currency: str) -> float:
    """Резервная функция с тестовыми данными"""
    fallback_matrix = {
        "USD": {"RUB": 75.5, "EUR": 0.92, "USD": 1.0},
        "EUR": {"RUB": 85.0, "USD": 1.09, "EUR": 1.0},
        "RUB": {"USD": 0.013, "EUR": 0.012, "RUB": 1.0}
    }

    if from_currency in fallback_matrix and to_currency in fallback_matrix[from_currency]:
        return fallback_matrix[from_currency][to_currency]

    print(f"Внимание: курс {from_currency}->{to_currency} не найден, использую 1.0")
    return 1.0


# ШАГ 7: Функция конвертации транзакций (оставляем почти без изменений)
def convert_transaction_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли через реальный API.

    Args:
        transaction: Словарь с данными о транзакции

    Returns:
        Сумма транзакции в рублях
    """
    try:
        # 1. Получаем сумму
        amount_str = transaction["operationAmount"]["amount"]
        amount = float(amount_str)

        # 2. Получаем валюту
        currency = transaction["operationAmount"]["currency"]["code"]

        # 3. Проверяем валюту
        if currency.upper() == "RUB":
            return amount

        # 4. Конвертируем через реальный API
        rate = get_exchange_rate(currency, "RUB")
        converted = round(amount * rate, 2)

        print(f"Конвертация: {amount} {currency} -> {converted} RUB (курс: {rate})")

        return converted

    except KeyError as e:
        print(f"Ошибка: в транзакции нет ключа {e}")
        return 0.0
    except ValueError as e:
        print(f"Ошибка: не могу преобразовать сумму в число: {e}")
        return 0.0
    except Exception as e:
        print(f"Неожиданная ошибка при конвертации: {e}")
        return 0.0