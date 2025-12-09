import pytest

from processing import filter_by_state, sort_by_date


def test_filter_executed():
    operations = [
        {"state": "EXECUTED", "id": 1},
        {"state": "PENDING", "id": 2},
    ]
    result = filter_by_state(operations, "EXECUTED")
    assert len(result) == 1
    assert result[0]["id"] == 1

def test_filter_pending():
    operations = [
        {"state": "EXECUTED", "id": 1},
        {"state": "PENDING", "id": 2},
    ]
    result = filter_by_state(operations, "PENDING")
    assert len(result) == 1
    assert result[0]["id"] == 2

def test_filter_empty():
    result = filter_by_state([], "EXECUTED")
    assert result == []

def test_sort_by_date_desc():
    operations = [
        {"date": "2023-09-01T12:00:00.000000", "id": 2},
        {"date": "2023-10-01T12:00:00.000000", "id": 1},
    ]
    result = sort_by_date(operations)
    assert result[0]["id"] == 1
    assert result[1]["id"] == 2

def test_sort_by_date_asc():
    operations = [
        {"date": "2023-10-01T12:00:00.000000", "id": 1},
        {"date": "2023-09-01T12:00:00.000000", "id": 2},
    ]
    result = sort_by_date(operations, descending=False)
    assert result[0]["id"] == 2
    assert result[1]["id"] == 1
