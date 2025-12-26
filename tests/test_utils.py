import os
import json
import tempfile
from src.utils import load_json_data


def test_load_json_data_valid_file():
    """Тест загрузки корректного JSON файла."""
    test_data = [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 200}
    ]
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump(test_data, f)
        temp_path = f.name
    
    try:
        result = load_json_data(temp_path)
        assert result == test_data
        assert len(result) == 2
    finally:
        os.unlink(temp_path)


def test_load_json_data_file_not_found():
    """Тест когда файл не существует."""
    result = load_json_data("nonexistent_file.json")
    assert result == []
    assert len(result) == 0


def test_load_json_data_empty_file():
    """Тест пустого файла."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_path = f.name
    
    try:
        result = load_json_data(temp_path)
        assert result == []
    finally:
        os.unlink(temp_path)


def test_load_json_data_invalid_json():
    """Тест файла с некорректным JSON."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        f.write("то не JSON файл")
        temp_path = f.name
    
    try:
        result = load_json_data(temp_path)
        assert result == []
    finally:
        os.unlink(temp_path)


def test_load_json_data_not_a_list():
    """Тест когда JSON не список."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump({"key": "value"}, f)
        temp_path = f.name
    
    try:
        result = load_json_data(temp_path)
        assert result == []
    finally:
        os.unlink(temp_path)
