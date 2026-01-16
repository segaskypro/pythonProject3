# tests/test_processing_complete.py
"""Полные тесты для модуля processing."""
import sys

sys.path.insert(0, 'src')

from processing import (
    filter_by_state,
    sort_by_date,
    process_bank_search,
    process_bank_operations
)


def test_filter_by_state_edge_cases():
    """Тесты граничных случаев для фильтрации."""
    # Пустой список
    result = filter_by_state([], "EXECUTED")
    assert result == []

    # Нет поля state
    data = [{"id": 1}, {"id": 2, "state": "EXECUTED"}]
    result = filter_by_state(data, "EXECUTED")
    assert len(result) == 1
    assert result[0]["id"] == 2

    # Неверный статус
    data = [{"id": 1, "state": "EXECUTED"}]
    result = filter_by_state(data, "INVALID")
    assert result == []

    print("✅ Граничные случаи фильтрации")


def test_sort_by_date_edge_cases():
    """Тесты граничных случаев для сортировки."""
    # Пустой список
    result = sort_by_date([], reverse=True)
    assert result == []

    # Нет поля date
    data = [
        {"id": 1, "date": "2024-01-15"},
        {"id": 2},  # Нет даты
        {"id": 3, "date": "2024-01-10"}
    ]
    result = sort_by_date(data, reverse=True)
    # Элементы без даты должны быть в конце
    assert result[0]["id"] in [1, 3]
    assert result[2]["id"] == 2

    # Одинаковые даты
    data = [
        {"id": 1, "date": "2024-01-15", "name": "A"},
        {"id": 2, "date": "2024-01-15", "name": "B"}
    ]
    result = sort_by_date(data, reverse=True)
    assert len(result) == 2

    print("✅ Граничные случаи сортировки")


def test_process_bank_search_edge_cases():
    """Тесты граничных случаев для поиска."""
    # Пустые данные
    result = process_bank_search([], "test")
    assert result == []

    # None данные
    result = process_bank_search(None, "test")
    assert result == []

    # Пустая строка поиска
    data = [{"description": "test"}]
    result = process_bank_search(data, "")
    assert result == []

    # Нет поля description
    data = [{"id": 1}, {"id": 2, "description": "test"}]
    result = process_bank_search(data, "test")
    assert len(result) == 1
    assert result[0]["id"] == 2

    # Регистронезависимый поиск
    data = [{"description": "Тестовая Операция"}]
    result = process_bank_search(data, "тестовая")
    assert len(result) == 1
    result = process_bank_search(data, "ОПЕРАЦИЯ")
    assert len(result) == 1

    print("✅ Граничные случаи поиска")


def test_process_bank_operations_edge_cases():
    """Тесты граничных случаев для подсчета операций."""
    # Пустые данные
    result = process_bank_operations([], ["test"])
    assert result == {"test": 0}

    # None данные
    result = process_bank_operations(None, ["test"])
    assert result == {"test": 0}

    # Пустой список категорий
    data = [{"description": "test"}]
    result = process_bank_operations(data, [])
    assert result == {}

    # Нет поля description
    data = [{"id": 1}, {"id": 2, "description": "test"}]
    result = process_bank_operations(data, ["test", "other"])
    assert result["test"] == 1
    assert result["other"] == 0

    # Повторяющиеся описания
    data = [
        {"description": "test"},
        {"description": "test"},
        {"description": "other"}
    ]
    result = process_bank_operations(data, ["test", "other", "missing"])
    assert result["test"] == 2
    assert result["other"] == 1
    assert result["missing"] == 0

    print("✅ Граничные случаи подсчета операций")


def run_all_tests():
    """Запуск всех тестов."""
    print("=" * 60)
    print("ПОЛНЫЕ ТЕСТЫ ДЛЯ MODULE PROCESSING")
    print("=" * 60)

    test_filter_by_state_edge_cases()
    test_sort_by_date_edge_cases()
    test_process_bank_search_edge_cases()
    test_process_bank_operations_edge_cases()

    print("\n" + "=" * 60)
    print("✅ ВСЕ ТЕСТЫ УСПЕШНО ПРОЙДЕНЫ!")
    print("=" * 60)


if __name__ == "__main__":
    run_all_tests()