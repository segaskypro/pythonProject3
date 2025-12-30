from logger_config import setup_logger


logger = setup_logger("utils", "utils.log")


def filter_by_state(operations, state: str = "EXECUTED"):
    """Фильтрует операции по статусу."""
    logger.debug(f"Начата фильтрация операций по статусу: {state}")

    filtered = [op for op in operations if op.get("state") == state]

    logger.debug(f"Фильтрация завершена. Найдено операций: {len(filtered)}")
    return filtered


def sort_by_date(operations, descending: bool = True):
    """Сортирует операции по дате."""
    logger.debug(f"Начата сортировка операций. Убывание: {descending}")

    try:
        sorted_ops = sorted(
            operations,
            key=lambda x: x.get("date", ""),
            reverse=descending
        )
        logger.debug(
            f"Сортировка завершена. Обработано операций: {len(sorted_ops)}"
        )  # ← Разбили длинную строку
        return sorted_ops
    except Exception as e:
        logger.error(f"Ошибка при сортировке: {e}")
        raise


# Пример использования (для тестирования)
if __name__ == "__main__":
    test_operations = [
        {"id": 1, "state": "EXECUTED", "date": "2023-10-01"},
        {"id": 2, "state": "PENDING", "date": "2023-10-02"},
        {"id": 3, "state": "EXECUTED", "date": "2023-09-30"},
    ]

    filtered = filter_by_state(test_operations, "EXECUTED")
    print(f"Отфильтровано: {len(filtered)} операций")

    sorted_ops = sort_by_date(filtered)
    print(f"Первая операция после сортировки: {sorted_ops[0]}")
