from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(operations: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """ильтрует операции по статусу."""
    if not operations:
        return []

    return [op for op in operations if op.get("state") == state]


def sort_by_date(operations: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """Сортирует операции по дате."""
    if not operations:
        return []

    def get_date(op: Dict[str, Any]) -> datetime:
        date_str = op.get("date", "")
        try:
            if date_str.endswith('Z'):
                date_str = date_str[:-1] + '+00:00'
            return datetime.fromisoformat(date_str)
        except (ValueError, TypeError):
            return datetime.min

    return sorted(operations, key=get_date, reverse=descending)
