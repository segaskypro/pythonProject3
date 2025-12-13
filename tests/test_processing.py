import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_operations():
    """икстура с тестовыми операциями для фильтрации."""
    return [
        {"state": "EXECUTED", "id": 1},
        {"state": "EXECUTED", "id": 2},
        {"state": "PENDING", "id": 3},
    ]


@pytest.fixture
def sample_operations_with_dates():
    """икстура с тестовыми операциями для сортировки."""
    return [
        {"date": "2023-09-01T12:00:00.000000", "id": 2},
        {"date": "2023-10-01T12:00:00.000000", "id": 1},
    ]


@pytest.mark.parametrize("state, expected_count", [
    ("EXECUTED", 2),
    ("PENDING", 1),
    ("CANCELED", 0),
])
def test_filter_by_state_parametrized(sample_operations, state, expected_count):
    """араметризованный тест фильтрации по статусу."""
    result = filter_by_state(sample_operations, state)
    assert len(result) == expected_count


def test_filter_by_state_empty():
    """Тест фильтрации пустого списка."""
    result = filter_by_state([], "EXECUTED")
    assert result == []


def test_sort_by_date_descending(sample_operations_with_dates):
    """Тест сортировки по убыванию (новые первыми)."""
    result = sort_by_date(sample_operations_with_dates, descending=True)
    assert result[0]["id"] == 1
    assert result[1]["id"] == 2


def test_sort_by_date_ascending(sample_operations_with_dates):
    """Тест сортировки по возрастанию (старые первыми)."""
    result = sort_by_date(sample_operations_with_dates, descending=False)
    assert result[0]["id"] == 2
    assert result[1]["id"] == 1
