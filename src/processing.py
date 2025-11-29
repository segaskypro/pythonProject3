# -*- coding: utf-8 -*-
"""Module for processing bank transactions"""

from typing import List, Dict


def filter_by_state(transactions: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Filter transactions by state"""
    return [t for t in transactions if t.get("state") == state]


def sort_by_date(transactions: List[Dict], reverse: bool = True) -> List[Dict]:
    """Sort transactions by date"""
    return sorted(transactions, key=lambda x: x.get("date", ""), reverse=reverse)