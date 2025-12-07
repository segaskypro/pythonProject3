# Проект по обработке банковских транзакций

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Status](https://img.shields.io/badge/status-в%20разработке-yellow)
![Build](https://img.shields.io/badge/build-проходит-green)
![Tests](https://img.shields.io/badge/tests-ожидаются-orange)

Проект для обработки и анализа банковских транзакций клиента. Решает задачи фильтрации операций по статусу и сортировки по дате для удобного отображения в виджете банковских операций.

## Содержание
- [Технологии](#технологии)
- [Начало работы](#начало-работы)
- [Использование](#использование)
- [Разработка](#разработка)
- [To do](#to-do)
- [Команда проекта](#команда-проекта)

## Технологии
- **Python 3.8+** - основной язык разработки
- **flake8** - линтер для проверки стиля кода
- **mypy** - проверка статических типов
- **isort** - сортировка импортов
- **Git** - система контроля версий
- **GitHub** - хостинг репозитория

## Начало работы

### Требования
- Python 3.8 или выше
- Установленный pip (менеджер пакетов Python)

### Установка зависимостей
```bash
pip install -r requirements.txt

from src.processing import filter_by_state, sort_by_date
** ИСПОЛЬЗОВАНИЕ ** 
# Пример данных
transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Фильтрация по статусу
executed_transactions = filter_by_state(transactions)  # Только EXECUTED
canceled_transactions = filter_by_state(transactions, 'CANCELED')  # Только CANCELED

# Сортировка по дате
newest_first = sort_by_date(transactions)  # По убыванию (новые сверху)
oldest_first = sort_by_date(transactions, reverse=False)  # По возрастанию
** РАЗРАБОТКА **
pip install flake8 mypy isort
** ПРОВЕРКА **
# Проверка стиля
flake8 src/

# Проверка типов
mypy src/

# Сортировка импортов
isort src/
** СТРУКТУРА ПРОЕКТА **
project/
├── src/
│   ├── processing.py    # Основной модуль обработки
│   └── masks.py         # Дополнительные функции
├── README.md           # Документация
├── requirements.txt    # Зависимости
└── .gitignore         # Игнорируемые файлы
