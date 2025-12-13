from typing import List, Dict


def filter_by_state(transactions: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    ильтрует транзакции по статусу.
    
    Args:
        transactions: Список транзакций
        state: Статус для фильтрации (по умолчанию "EXECUTED")
    
    Returns:
        тфильтрованный список транзакций
    """
    if not transactions:
        return []
    
    filtered_transactions = [
        transaction for transaction in transactions
        if transaction.get("state") == state
    ]
    
    return filtered_transactions


def sort_by_date(transactions: List[Dict], descending: bool = True) -> List[Dict]:
    """Сортирует транзакции по дате."""
    if not transactions:
        return []
    
    valid_transactions = [t for t in transactions if t.get("date")]
    
    sorted_transactions = sorted(
        valid_transactions,
        key=lambda x: x["date"],
        reverse=descending
    )
    
    return sorted_transactions
