# -*- coding: utf-8 -*-
"""Module for processing bank transactions."""

import re
from collections import Counter
from typing import List, Dict


def filter_by_state(transactions: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Filter transactions by state."""
    return [t for t in transactions if t.get("state") == state]


def sort_by_date(transactions: List[Dict], reverse: bool = True) -> List[Dict]:
    """Sort transactions by date."""
    return sorted(transactions, key=lambda x: x.get("date", ""), reverse=reverse)


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """
    Search transactions by description using regular expressions.

    Args:
        data: List of dictionaries with bank operations
        search: String to search in description field

    Returns:
        List of dictionaries with matching operations
    """
    if not data or not search:
        return []

    result = []

    for operation in data:
        description = operation.get('description', '')

        # Use re.search for case-insensitive search
        if re.search(search, description, re.IGNORECASE):
            result.append(operation)

    return result


def process_bank_operations(data: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Count operations by categories.

    Args:
        data: List of dictionaries with bank operations
        categories: List of categories to count

    Returns:
        Dictionary with operation counts per category
    """
    if not data:
        return {category: 0 for category in categories}

    # Collect all descriptions
    descriptions = []
    for operation in data:
        description = operation.get('description', '')
        if description:
            descriptions.append(description)

    # Use Counter for counting
    counter = Counter(descriptions)

    # Filter only needed categories
    result = {}
    for category in categories:
        result[category] = counter.get(category, 0)

    return result
