import pytest
from processing import filter_by_state, sort_by_date


@pytest.mark.parametrize("state, expected_count", [
    ("EXECUTED", 2),
    ("PENDING", 1),
    ("CANCELED", 0),
])
def test_filter_by_state_parametrized(state, expected_count):
    """араметризованный тест фильтрации по статусу."""
    operations = [
        {"state": "EXECUTED", "id": 1},
        {"state": "EXECUTED", "id": 2},
        {"state": "PENDING", "id": 3},
    ]
    result = filter_by_state(operations, state)
    assert len(result) == expected_count


def test_filter_by_state_empty():
    """Тест фильтрации пустого списка."""
    result = filter_by_state([], "EXECUTED")
    assert result == []


def test_sort_by_date_descending():
    """Тест сортировки по убыванию (новые первыми)."""
    operations = [
        {"date": "2023-09-01T12:00:00.000000", "id": 2},
        {"date": "2023-10-01T12:00:00.000000", "id": 1},
    ]
    result = sort_by_date(operations, descending=True)
    assert result[0]["id"] == 1
    assert result[1]["id"] == 2


def test_sort_by_date_ascending():
    """Тест сортировки по возрастанию (старые первыми)."""
    operations = [
        {"date": "2023-10-01T12:00:00.000000", "id": 1},
        {"date": "2023-09-01T12:00:00.000000", "id": 2},
    ]
    result = sort_by_date(operations, descending=False)
    assert result[0]["id"] == 2
    assert result[1]["id"] == 1
