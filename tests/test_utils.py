"""
Тесты для модуля utils с использованием mock/patch.
Теперь тесты изолированы от файловой системы.
"""

import pytest
from unittest.mock import patch, mock_open
import json
from src.utils import load_json_data


def test_load_json_data_with_mock_open():
    """Тест с использованием mock_open"""
    test_data = [{"id": 1, "name": "Test"}]
    json_str = json.dumps(test_data)

    # Мокаем И os.path.exists И open
    with patch('os.path.exists', return_value=True):
        with patch('builtins.open', mock_open(read_data=json_str)) as mock_file:
            with patch('json.load') as mock_json:
                mock_json.return_value = test_data

                result = load_json_data("test.json")

                # Проверяем что open вызывался правильно
                mock_file.assert_called_once_with("test.json", 'r', encoding='utf-8')
                assert result == test_data
                print("✓ Тест с mock_open пройден")


def test_load_json_data_file_not_found_with_mock():
    """Тест обработки отсутствующего файла с mock"""
    with patch('os.path.exists', return_value=False):
        result = load_json_data("nonexistent.json")
        assert result == []
        print("✓ Тест отсутствующего файла пройден")


def test_load_json_data_invalid_json_with_mock():
    """Тест невалидного JSON с mock"""
    with patch('os.path.exists', return_value=True):
        with patch('builtins.open', mock_open(read_data="не json")):
            with patch('json.load', side_effect=json.JSONDecodeError("Ошибка", "док", 0)):
                result = load_json_data("bad.json")
                assert result == []
                print("✓ Тест невалидного JSON пройден")


def test_load_json_data_not_a_list_with_mock():
    """Тест когда JSON не список"""
    with patch('os.path.exists', return_value=True):
        with patch('builtins.open', mock_open(read_data='{"not": "a_list"}')):
            with patch('json.load', return_value={"not": "a_list"}):
                result = load_json_data("not_list.json")
                assert result == []
                print("✓ Тест 'не список' пройден")


def test_load_json_data_empty_file_with_mock():
    """Тест пустого файла"""
    with patch('os.path.exists', return_value=True):
        with patch('builtins.open', mock_open(read_data="")):
            with patch('json.load', side_effect=json.JSONDecodeError("EOF", "", 0)):
                result = load_json_data("empty.json")
                assert result == []
                print("✓ Тест пустого файла пройден")


def test_load_json_data_unicode_error_with_mock():
    """Тест ошибки кодирования Unicode"""
    with patch('os.path.exists', return_value=True):
        with patch('builtins.open', side_effect=UnicodeDecodeError('utf-8', b'\xff', 0, 1, 'invalid')):
            result = load_json_data("bad_encoding.json")
            assert result == []
            print("✓ Тест ошибки Unicode пройден")


def test_load_json_data_success_real_example():
    """Тест успешной загрузки реальных данных"""
    real_data = [
        {"id": 1, "amount": 100, "currency": "USD"},
        {"id": 2, "amount": 200, "currency": "EUR"}
    ]
    json_str = json.dumps(real_data)

    with patch('os.path.exists', return_value=True):
        with patch('builtins.open', mock_open(read_data=json_str)):
            with patch('json.load', return_value=real_data):
                result = load_json_data("operations.json")
                assert result == real_data
                assert len(result) == 2
                assert result[0]["currency"] == "USD"
                print("✓ Тест реальных данных пройден")


# Запуск тестов
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("Запуск тестов для utils с mock/patch")
    print("=" * 50)
    pytest.main([__file__, "-v", "--tb=short"])