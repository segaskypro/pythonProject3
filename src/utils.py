import json
from typing import List, Dict, Any


def load_json_data(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает данные из JSON-файла.

    Если файл не найден, пустой, содержит не-список или
    произошла ошибка декодирования, возвращает пустой список.

    :param file_path: Путь к JSON-файлу
    :return: Список словарей с данными о транзакции или пустой список
    """
    try:
        # Открываем и читаем файл
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

    except FileNotFoundError:
        # Файл не найден
        return []
    except (json.JSONDecodeError, UnicodeDecodeError):
        # Файл поврежден или не в UTF-8
        return []

    # Проверяем, что данные - это список
    if not isinstance(data, list):
        return []

    return data