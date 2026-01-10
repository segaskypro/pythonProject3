"""
одуль для чтения финансовых операций из CSV и Excel файлов.
"""
import pandas as pd
from typing import List, Dict
import logging

logger = logging.getLogger(__name__)


def read_csv_transactions(file_path: str) -> List[Dict]:
    """итает финансовые операции из CSV-файла."""
    try:
        logger.info(f"тение CSV файла: {file_path}")
        df = pd.read_csv(file_path, delimiter=';')
        transactions = df.to_dict('records')
        msg = f"спешно прочитано {len(transactions)} транзакций"
        logger.info(msg)
        return transactions
    except FileNotFoundError:
        logger.error(f"айл не найден: {file_path}")
        raise
    except Exception as e:
        logger.error(f"шибка при чтении CSV: {e}")
        raise


def read_excel_transactions(file_path: str) -> List[Dict]:
    """итает финансовые операции из Excel-файла."""
    try:
        logger.info(f"тение Excel файла: {file_path}")
        df = pd.read_excel(file_path)
        transactions = df.to_dict('records')
        msg = f"спешно прочитано {len(transactions)} транзакций"
        logger.info(msg)
        return transactions
    except FileNotFoundError:
        logger.error(f"айл не найден: {file_path}")
        raise
    except Exception as e:
        logger.error(f"шибка при чтении Excel: {e}")
        raise


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        csv_data = read_csv_transactions("data/transactions.csv")
        print(f"рочитано {len(csv_data)} транзакций из CSV")
        excel_data = read_excel_transactions("data/transactions_excel.xlsx")
        print(f"рочитано {len(excel_data)} транзакций из Excel")
    except Exception as e:
        print(f"шибка при тестировании: {e}")
