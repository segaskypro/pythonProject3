import logging
import os


def setup_logger(name: str, log_file: str) -> logging.Logger:
    """
    Создает и настраивает логер для модуля.

    Args:
        name: Имя логера (обычно __name__ модуля)
        log_file: Имя файла для записи логов

    Returns:
        Настроенный объект логера
    """
    # Создаём папку logs, если её нет
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    # Создаём логер
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Уровень не ниже DEBUG

    # Создаём file handler (пишет в файл) с кодировкой UTF-8
    file_path = os.path.join(log_dir, log_file)
    file_handler = logging.FileHandler(
        file_path, mode="w", encoding="utf-8"
    )  # ← Разбили длинную строку
    file_handler.setLevel(logging.DEBUG)

    # Создаём formatter
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Применяем formatter к handler
    file_handler.setFormatter(formatter)

    # Добавляем handler к логеру
    logger.addHandler(file_handler)

    return logger
