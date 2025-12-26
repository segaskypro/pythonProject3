import json
import os
from typing import List, Dict, Any


def load_json_data(
    file_path: str
) -> List[Dict[str, Any]]:
    """
    агружает данные из JSON-файла.

    сли файл не найден, пустой, содержит не-список или 
    произошла ошибка декодирования, возвращает пустой список.

    :param file_path: уть к JSON-файлу
    :return: Список словарей с данными о транзакциях или пустой список
    """
    # роверяем существование файла
    if not os.path.exists(file_path):
        return []

    try:
        # ткрываем и читаем файл
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

    except (json.JSONDecodeError, UnicodeDecodeError):
        # сли файл поврежден или не в UTF-8
        return []

    # роверяем, что данные - это список
    if not isinstance(data, list):
        return []

    return data
