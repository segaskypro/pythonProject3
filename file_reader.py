"""
одуль для чтения финансовых операций из CSV и Excel файлов.
"""
import pandas as pd
from typing import List, Dict
import logging

# астройка логгера
logger = logging.getLogger(__name__)


def read_csv_transactions(file_path: str) -> List[Dict]:
    """
    итает финансовые операции из CSV-файла.
    
    Args:
        file_path (str): уть к CSV-файлу
        
    Returns:
        List[Dict]: Список словарей с транзакциями
        
    Raises:
        FileNotFoundError: сли файл не найден
        Exception: ри других ошибках чтения
    """
    try:
        logger.info(f"тение CSV файла: {file_path}")
        
        # итаем CSV файл (разделитель - точка с запятой ";")
        df = pd.read_csv(file_path, delimiter=';')
        
        # реобразуем DataFrame в список словарей
        transactions = df.to_dict('records')
        
        logger.info(f"спешно прочитано {len(transactions)} транзакций из CSV")
        return transactions
        
    except FileNotFoundError:
        logger.error(f"айл не найден: {file_path}")
        raise
    except Exception as e:
        logger.error(f"шибка при чтении CSV файла {file_path}: {e}")
        raise


def read_excel_transactions(file_path: str) -> List[Dict]:
    """
    итает финансовые операции из Excel-файла.
    
    Args:
        file_path (str): уть к Excel-файлу
        
    Returns:
        List[Dict]: Список словарей с транзакцииями
        
    Raises:
        FileNotFoundError: сли файл не найден
        Exception: ри других ошибках чтения
    """
    try:
        logger.info(f"тение Excel файла: {file_path}")
        
        # итаем Excel файл
        df = pd.read_excel(file_path)
        
        # реобразуем DataFrame в список словарей
        transactions = df.to_dict('records')
        
        logger.info(f"спешно прочитано {len(transactions)} транзакций из Excel")
        return transactions
        
    except FileNotFoundError:
        logger.error(f"айл не найден: {file_path}")
        raise
    except Exception as e:
        logger.error(f"шибка при чтении Excel файла {file_path}: {e}")
        raise


# Тестовый запуск
if __name__ == "__main__":
    # астройка базового логирования
    logging.basicConfig(level=logging.INFO)
    
    try:
        # Тестируем чтение CSV
        csv_transactions = read_csv_transactions("data/transactions.csv")
        print(f"✅ рочитано {len(csv_transactions)} транзакций из CSV")
        if csv_transactions:
            print("📋 ервая транзакция из CSV:")
            for key, value in csv_transactions[0].items():
                print(f"   {key}: {value}")
        
        print("\n" + "="*50 + "\n")
        
        # Тестируем чтение Excel
        excel_transactions = read_excel_transactions("data/transactions_excel.xlsx")
        print(f"✅ рочитано {len(excel_transactions)} транзакций из Excel")
        if excel_transactions:
            print("📋 ервая транзакция из Excel:")
            for key, value in excel_transactions[0].items():
                print(f"   {key}: {value}")
            
    except Exception as e:
        print(f"❌ шибка при тестировании: {e}")
