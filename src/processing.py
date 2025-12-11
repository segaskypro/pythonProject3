from typing import List, Dict


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
