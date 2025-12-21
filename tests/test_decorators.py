"""Тесты для декоратора log."""

import os
import tempfile
from src.decorators import log


def test_log_to_console(capsys):
    """Тест логирования в консоль."""
    @log()
    def add(a, b):
        return a + b

    result = add(1, 2)

    captured = capsys.readouterr()
    assert result == 3
    assert "add ok" in captured.out


def test_log_to_file():
    """Тест логирования в файл."""
    # Создаем временный файл
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.log') as tmp:
        filename = tmp.name

    try:
        @log(filename=filename)
        def multiply(x, y):
            return x * y

        result = multiply(3, 4)

        assert result == 12

        # роверяем запись в файл
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            assert "multiply ok" in content
    finally:
        # даляем временный файл
        os.unlink(filename)


def test_log_error_to_console(capsys):
    """Тест логирования ошибки в консоль."""
    @log()
    def raise_error():
        raise ValueError("Test error")

    try:
        raise_error()
    except ValueError:
        pass

    captured = capsys.readouterr()
    assert "raise_error error" in captured.out
    assert "ValueError" in captured.out


def test_log_error_to_file():
    """Тест логирования ошибки в файл."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.log') as tmp:
        filename = tmp.name

    try:
        @log(filename=filename)
        def divide(a, b):
            return a / b

        try:
            divide(1, 0)
        except ZeroDivisionError:
            pass

        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            assert "divide error" in content
            assert "ZeroDivisionError" in content
            assert "Inputs: (1, 0)" in content
    finally:
        os.unlink(filename)


def test_log_preserves_function_metadata():
    """Тест, что декоратор сохраняет метаданные функции."""
    @log()
    def example_func(a: int, b: int) -> int:
        """Тестовая функция."""
        return a + b

    assert example_func.__name__ == "example_func"
    assert "Тестовая функция" in example_func.__doc__
