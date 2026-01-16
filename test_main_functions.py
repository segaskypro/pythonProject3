"""
Тесты для функций домашнего задания.
"""

import sys

sys.path.insert(0, 'src')

from masks import mask_account, mask_card_number
from processing import (
    filter_by_state,
    sort_by_date,
    process_bank_search,
    process_bank_operations
)


def get_test_transactions():
    """Возвращает тестовые транзакции."""
    return [
        {"id": 1, "date": "2024-01-15", "description": "Перевод организации", "state": "EXECUTED"},
        {"id": 2, "date": "2024-01-14", "description": "Открытие вклада", "state": "EXECUTED"},
        {"id": 3, "date": "2024-01-13", "description": "Перевод организации", "state": "CANCELED"},
        {"id": 4, "date": "2024-01-12", "description": "Оплата услуг", "state": "PENDING"},
        {"id": 5, "date": "2024-01-11", "description": "Перевод организации", "state": "EXECUTED"}
    ]


def test_masking_functions():
    """Тестирует функции маскировки."""
    print("=" * 40)
    print("ТЕСТ МАСКИРОВКИ")
    print("=" * 40)

    # Тест карты
    card = "7000792289606361"
    result = mask_card_number(card)
    expected = "7000 79** **** 6361"
    assert result == expected, f"Карта: {result} != {expected}"
    print(f"✅ Карта: {result}")

    # Тест счета
    account = "73654108430135874305"
    result = mask_account(account)
    expected = "**4305"
    assert result == expected, f"Счет: {result} != {expected}"
    print(f"✅ Счет: {result}")

    print("✅ Все тесты маскировки пройдены")


def test_search_functions():
    """Тестирует функции поиска."""
    print("\n" + "=" * 40)
    print("ТЕСТ ПОИСКА")
    print("=" * 40)

    data = get_test_transactions()

    # Тест 1: Поиск "перевод"
    result = process_bank_search(data, "перевод")
    assert len(result) == 3, f"Ожидалось 3, найдено {len(result)}"
    print(f"✅ Найдено переводов: {len(result)}")

    # Тест 2: Поиск "вклад"
    result = process_bank_search(data, "вклад")
    assert len(result) == 1, f"Ожидалось 1, найдено {len(result)}"
    print(f"✅ Найдено вкладов: {len(result)}")

    print("✅ Все тесты поиска пройдены")


def test_count_functions():
    """Тестирует функции подсчёта."""
    print("\n" + "=" * 40)
    print("ТЕСТ ПОДСЧЕТА")
    print("=" * 40)

    data = get_test_transactions()
    categories = ["Перевод организации", "Открытие вклада", "Оплата услуг"]

    result = process_bank_operations(data, categories)

    assert result["Перевод организации"] == 3, f"Ожидалось 3 переводов"
    assert result["Открытие вклада"] == 1, f"Ожидалось 1 вклад"
    assert result["Оплата услуг"] == 1, f"Ожидалось 1 оплата услуг"

    print(f"✅ Перевод организации: {result['Перевод организации']}")
    print(f"✅ Открытие вклада: {result['Открытие вклада']}")
    print(f"✅ Оплата услуг: {result['Оплата услуг']}")

    print("✅ Все тесты подсчёта пройдены")


def test_filter_and_sort():
    """Тестирует фильтрацию и сортировку."""
    print("\n" + "=" * 40)
    print("ТЕСТ ФИЛЬТРАЦИИ И СОРТИРОВКИ")
    print("=" * 40)

    data = get_test_transactions()

    # Фильтрация
    executed = filter_by_state(data, "EXECUTED")
    assert len(executed) == 2, f"Ожидалось 2 EXECUTED"
    print(f"✅ EXECUTED транзакций: {len(executed)}")

    # Сортировка
    sorted_desc = sort_by_date(data, reverse=True)
    assert sorted_desc[0]["date"] == "2024-01-15", "Сортировка по убыванию не работает"
    print(f"✅ Сортировка по убыванию работает")

    sorted_asc = sort_by_date(data, reverse=False)
    assert sorted_asc[0]["date"] == "2024-01-11", "Сортировка по возрастанию не работает"
    print(f"✅ Сортировка по возрастанию работает")

    print("✅ Все тесты фильтрации и сортировки пройдены")


if __name__ == "__main__":
    print("ЗАПУСК ТЕСТОВ ДОМАШНЕГО ЗАДАНИЯ")
    print("=" * 50)

    try:
        test_masking_functions()
        test_search_functions()
        test_count_functions()
        test_filter_and_sort()

        print("\n" + "=" * 50)
        print("🎉 ВСЕ ТЕСТЫ УСПЕШНО ПРОЙДЕНЫ!")
        print("=" * 50)

    except AssertionError as e:
        print(f"\n❌ ТЕСТ ПРОВАЛЕН: {e}")
        raise