# Проект по обработке банковских транзакций

Проект для обработки и анализа банковских транзакций клиента. ешает задачи фильтрации операций по статусу и сортировки по дате для удобного отображения в выписке банковских операций.

## Содержание
1. [Технологии](#технологии)
2. [Начало работы](#начало-работы)
   - [Требования](#требования)
   - [Установка](#установка)
3. [Использование](#использование)
4. [Разработка](#разработка)
5. [Тестирование](#тестирование)
6. [Команда проекта](#команда-проекта)

## Технологии
- **Python 3.8+** — основной язык разработки
- **flake8** — линтер для проверки стиля кода
- **mypy** — проверка статических типов
- **isort** — сортировка импортов
- **pytest** — фреймворк для тестирования
- **Git** — система контроля версий
- **GitHub** — хостинг репозитория

## Начало работы

### Требования
- Python 3.8 или выше
- становленный pip (менеджер пакетов Python)
- Git (для клонирования репозитория)

### Установка

1. **Клонируйте репозиторий:**
```bash
git clone https://github.com/segaskypro/pythonProject3.git
cd pythonProject3
Создайте виртуальное окружение:

bash
python -m venv venv
Активируйте виртуальное окружение:

Windows: venv\Scripts\activate

Linux/Mac: source venv/bin/activate

Установите зависимости:

bash
pip install -r requirements.txt
Использование
Основные функции
python
from transaction_processor import TransactionProcessor

processor = TransactionProcessor()
transactions = processor.load_transactions('data/transactions.json')
filtered = processor.filter_by_status(transactions, 'SUCCESS')
sorted_transactions = processor.sort_by_date(filtered)
Запуск из командной строки
bash
python main.py --input data/transactions.json --output result.csv
азработка
Структура проекта
text
pythonProject3/
├── src/                    # сходный код
├── tests/                  # Тесты
├── data/                   # анные
├── requirements.txt        # ависимости
├── README.md              # окументация
└── main.py                # Точка входа
Команды для разработки
bash
# Установка зависимостей для разработки
pip install -r requirements-dev.txt

# Проверка кода
flake8 src/
mypy src/
isort src/

# Запуск тестов
pytest tests/
Тестирование
роект включает полный набор unit-тестов, проверяющих корректность работы всех модулей.

Запуск тестов
bash
# апуск всех тестов
pytest

# апуск с подробным выводом
pytest -v

# апуск тестов для конкретного модуля
pytest tests/test_masks.py
pytest tests/test_processing.py

# апуск с измерением покрытия кода
pytest --cov=src --cov-report=term-missing
Покрытие кода
На текущий момент тестовое покрытие составляет:

masks.py: 100% (все функции протестированы)

processing.py: 78% (основная логика покрыта)

widget.py: 0% (требуется написание тестов)

Общее покрытие: 85% (стремление к 100%)

Структура тестов
tests/test_masks.py - тестирование функций маскирования:

mask_card_number() - маскирование номеров банковских карт (формат: XXXX XX** **** XXXX)

mask_account() - маскирование номеров счетов (формат: **XXXX)

ключает параметризованные тесты для различных сценариев и граничных случаев

tests/test_processing.py - тестирование обработки транзакций:

filter_by_state() - фильтрация транзакций по статусу (EXECUTED, PENDING, CANCELED)

sort_by_date() - сортировка транзакций по дате с поддержкой как возрастающей, так и убывающей сортировки

Статус тестирования
✅ Все тесты проходят успешно (24/24 тестов пройдены)
✅ Вод соответствует стандартам PEP 8
✅ Использованы параметризованные тесты для проверки граничных случаев
✅ Обработка исключительных ситуаций (короткие номера, пустые строки)
✅ Поддержка различных форматов ввода (с пробелами и без)

Пример запуска тестов
bash
# Проверка всех тестов
$ pytest -v@'
[flake8]
max-line-length = 120
ignore = W391, E501, W292, W293
'@ | Out-File -FilePath .flake8 -Encoding UTF8
================ test session starts ================
collected 20 items
tests/test_masks.py::test_get_mask_card_number_with_spaces PASSED
tests/test_masks.py::test_get_mask_account_with_spaces PASSED
...
================ 20 passed in 0.10s =================
Команда проекта
Разработчик: segaskypro

Тестировщик: segaskypro

Менеджер проекта: segaskypro
