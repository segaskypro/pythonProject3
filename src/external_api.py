import os
import requests
import json
from typing import Dict, Any, Optional
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()


class ExchangeRateAPI:
    def __init__(self):
        self.api_key = os.getenv("EXCHANGE_RATE_API_KEY", "")
        self.cache_duration = timedelta(hours=1)
        self.cache = {}
        self.last_update = {}

    def _is_cache_valid(self, from_currency: str) -> bool:
        if from_currency not in self.last_update:
            return False
        return datetime.now() - self.last_update[from_currency] < self.cache_duration

    def _get_from_cache(self, from_currency: str) -> Optional[Dict]:
        if self._is_cache_valid(from_currency):
            return self.cache.get(from_currency)
        return None

    def _save_to_cache(self, from_currency: str, data: Dict):
        self.cache[from_currency] = data
        self.last_update[from_currency] = datetime.now()

    def get_exchange_rates(self, from_currency: str) -> Dict:
        cached_data = self._get_from_cache(from_currency)
        if cached_data:
            return cached_data

        try:
            url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            self._save_to_cache(from_currency, data)
            return data

        except requests.exceptions.Timeout:
            return self._get_fallback_rates(from_currency)
        except requests.exceptions.RequestException:
            return self._get_fallback_rates(from_currency)
        except (ValueError, KeyError, json.JSONDecodeError):
            return self._get_fallback_rates(from_currency)

    def _get_fallback_rates(self, from_currency: str) -> Dict:
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


_exchange_api = ExchangeRateAPI()


def get_exchange_rate(from_currency: str, to_currency: str = "RUB") -> float:
    try:
        data = _exchange_api.get_exchange_rates(from_currency.upper())
        rates = data.get("rates", {})
        target_currency = to_currency.upper()

        if target_currency not in rates:
            return _get_fallback_rate(from_currency.upper(), target_currency)

        rate = rates[target_currency]
        return float(rate)

    except Exception:
        return _get_fallback_rate(from_currency.upper(), to_currency.upper())


def _get_fallback_rate(from_currency: str, to_currency: str) -> float:
    fallback_matrix = {
        "USD": {"RUB": 75.5, "EUR": 0.92, "USD": 1.0},
        "EUR": {"RUB": 85.0, "USD": 1.09, "EUR": 1.0},
        "RUB": {"USD": 0.013, "EUR": 0.012, "RUB": 1.0}
    }

    if from_currency in fallback_matrix and to_currency in fallback_matrix[from_currency]:
        return fallback_matrix[from_currency][to_currency]

    return 1.0


def convert_transaction_to_rub(transaction: Dict[str, Any]) -> float:
    try:
        amount_str = transaction["operationAmount"]["amount"]
        amount = float(amount_str)
        currency = transaction["operationAmount"]["currency"]["code"]

        if currency.upper() == "RUB":
            return amount

        rate = get_exchange_rate(currency, "RUB")
        converted = round(amount * rate, 2)
        return converted

    except KeyError:
        return 0.0
    except ValueError:
        return 0.0
    except Exception:
        return 0.0