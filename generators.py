"""Module for transaction generators."""


def filter_by_currency(transactions, currency_code):
    """
    Filters transactions by currency.

    Args:
        transactions: list of transaction dictionaries
        currency_code: currency code (e.g., "USD")

    Yields:
        transactions in specified currency
    """
    for transaction in transactions:
        try:
            code = transaction["operationAmount"]["currency"]["code"]
            if code == currency_code:
                yield transaction
        except (KeyError, TypeError):
            continue


def transaction_descriptions(transactions):
    """
    Generator for transaction descriptions.

    Args:
        transactions: list of transaction dictionaries

    Yields:
        description of each transaction
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start, end):
    """
    Generator for bank card numbers.

    Args:
        start: starting number
        end: ending number

    Yields:
        card number in format "XXXX XXXX XXXX XXXX"
    """
    for number in range(start, end + 1):
        card_str = str(number).zfill(16)
        formatted = (f"{card_str[:4]} {card_str[4:8]} "
                     f"{card_str[8:12]} {card_str[12:]}")
        yield formatted
