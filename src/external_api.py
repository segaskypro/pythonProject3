from typing import Dict, Any
from dotenv import load_dotenv

# агружаем переменные окружения из .env файла
load_dotenv()


def get_exchange_rate(from_currency: str, to_currency: str = "RUB") -> float:
    """
    олучает текущий курс обмена валют.

    ока используем тестовые курсы, позже подключим API.

    :param from_currency: сходная валюта (например, "USD", "EUR")
    :param to_currency: елевая валюта (по умолчанию "RUB")
    :return: урс обмена (сколько рублей за 1 единицу исходной валюты)
    """
    # Тестовые курсы (пока без реального API)
    test_rates = {
        "USD": 75.5,  # 1 USD = 75.5 RUB
        "EUR": 85.0,  # 1 EUR = 85.0 RUB
        "RUB": 1.0    # 1 RUB = 1 RUB
    }

    # риводим к верхнему регистру для удобства
    currency = from_currency.upper()

    # озвращаем курс или 1.0 если валюта не найдена
    return test_rates.get(currency, 1.0)


def convert_transaction_to_rub(transaction: Dict[str, Any]) -> float:
    """
    онвертирует сумму транзакции в рубли.

    сли транзакция уже в рублях, возвращает сумму как float.
    сли в USD или EUR, конвертирует по тестовому курсу.

    :param transaction: Словарь с данными о транзакции
    :return: Сумма транзакции в рублях (float)
    """
    try:
        # 1. олучаем сумму
        amount_str = transaction["operationAmount"]["amount"]
        amount = float(amount_str)

        # 2. олучаем валюту
        currency = transaction["operationAmount"]["currency"]["code"]

        # 3. роверяем валюту
        if currency.upper() == "RUB":
            # же рубли, ничего не конвертируем
            return amount

        # 4. онвертируем если USD или EUR
        if currency.upper() in ["USD", "EUR"]:
            rate = get_exchange_rate(currency, "RUB")
            return round(amount * rate, 2)

        # 5. ругие валюты (пока не обрабатываем)
        print(
            f"нимание: валюта '{currency}' не поддерживается, "
            f"возвращаем оригинальную сумму"
        )
        return amount

    except KeyError as e:
        print(f"шибка: в транзакции нет ключа {e}")
        return 0.0
    except ValueError as e:
        print(f"шибка: не могу преобразовать сумму в число: {e}")
        return 0.0
