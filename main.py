"""
Главный модуль программы для работы с банковскими транзакциями.

Пользовательская версия программы.
Модуль реализует консольный интерфейс для работы с транзакциями.
"""

import sys
from typing import List, Dict

# Добавляем src в путь импорта
sys.path.insert(0, 'src')

try:
    from processing import (
        filter_by_state,
        sort_by_date,
        process_bank_search
    )

    print("✅ Все модули успешно импортированы")
except ImportError as e:
    print(f"❌ Ошибка импорта: {e}")
    print("Проверьте наличие файлов в папке src/")
    sys.exit(1)


def get_user_choice(prompt: str, valid_choices: List[str]) -> str:
    """
    Получает и проверяет выбор пользователя.

    Args:
        prompt: Текст приглашения для ввода
        valid_choices: Список допустимых вариантов

    Returns:
        str: Выбор пользователя
    """
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_choices:
            return choice
        msg = f"❌ Неверный выбор. Допустимые варианты: {', '.join(valid_choices)}"
        print(msg)


def get_valid_status() -> str:
    """
    Запрашивает и возвращает валидный статус транзакции.

    Returns:
        str: Выбранный статус или 'EXIT' для возврата
    """
    while True:
        print("\nВыберите статус транзакции:")
        print("1. EXECUTED - выполнена")
        print("2. CANCELED - отменена")
        print("3. PENDING - в обработке")
        print("4. Вернуться в меню")

        choice = input("Ваш выбор (1-4): ").strip()

        if choice == "1":
            return "EXECUTED"
        elif choice == "2":
            return "CANCELED"
        elif choice == "3":
            return "PENDING"
        elif choice == "4":
            return "EXIT"
        else:
            print("❌ Неверный выбор. Пожалуйста, введите число от 1 до 4")


def get_test_transactions() -> List[Dict]:
    """
    Возвращает тестовые транзакции для демонстрации.

    Returns:
        List[Dict]: Список тестовых транзакций
    """
    return [
        {
            "id": 1,
            "date": "2024-01-15",
            "description": "Перевод организации",
            "from": "Visa Platinum 7000 7922 8960 6361",
            "to": "Счет **4305",
            "amount": 100.50,
            "currency": "RUB",
            "state": "EXECUTED"
        },
        {
            "id": 2,
            "date": "2024-01-14",
            "description": "Открытие вклада",
            "to": "Счет **4321",
            "amount": 40542.00,
            "currency": "RUB",
            "state": "EXECUTED"
        },
        {
            "id": 3,
            "date": "2024-01-13",
            "description": "Перевод с карты на карту",
            "from": "MasterCard 7771 2727 **** 3727",
            "to": "Visa Platinum 1293 3829 **** 9203",
            "amount": 130.00,
            "currency": "USD",
            "state": "CANCELED"
        },
        {
            "id": 4,
            "date": "2024-01-12",
            "description": "Оплата услуг",
            "from": "Счет **2935",
            "to": "Счет **4321",
            "amount": 8200.00,
            "currency": "EUR",
            "state": "PENDING"
        },
        {
            "id": 5,
            "date": "2024-01-11",
            "description": "Перевод организации",
            "from": "Счет **7202",
            "to": "Счет **0034",
            "amount": 8390.00,
            "currency": "RUB",
            "state": "EXECUTED"
        }
    ]


def display_transaction(transaction: Dict) -> None:
    """
    Отображает одну транзакцию в читаемом формате.

    Args:
        transaction: Словарь с данными транзакции
    """
    print(f"\nДата: {transaction.get('date', 'Дата неизвестна')}")
    print(f"Описание: {transaction.get('description', '')}")

    status = transaction.get('state', '')
    status_symbol = {
        'EXECUTED': '✅',
        'CANCELED': '❌',
        'PENDING': '⏳'
    }.get(status, '')
    print(f"Статус: {status} {status_symbol}")

    if 'from' in transaction:
        print(f"Со счета: {transaction['from']}")
    if 'to' in transaction:
        print(f"На счет: {transaction['to']}")

    amount = transaction.get('amount', 0)
    currency = transaction.get('currency', '')
    print(f"Сумма: {amount} {currency}")
    print("-" * 40)


def run_full_transaction_cycle() -> None:
    """Запускает полный цикл работы с транзакциями."""
    print("\n" + "=" * 40)
    print("ШАГ 1: Получение транзакций")
    print("=" * 40)

    print("\nВыберите тип файла:")
    print("1. JSON-файл")
    print("2. CSV-файл")
    print("3. XLSX-файл")
    print("4. Вернуться в главное меню")

    file_choice = get_user_choice("Ваш выбор: ", ["1", "2", "3", "4"])

    if file_choice == "4":
        return

    file_type = {"1": "JSON", "2": "CSV", "3": "XLSX"}[file_choice]
    print(f"\n✅ Для обработки выбран {file_type}-файл.")

    # Используем тестовые данные
    transactions = get_test_transactions()
    print(f"✅ Всего прочитано транзакций: {len(transactions)}")

    # Фильтрация по статусу
    print("\n" + "=" * 40)
    print("ШАГ 2: Фильтрация по статусу")
    print("=" * 40)

    while True:
        status = get_valid_status()
        if status == "EXIT":
            return
        break

    filtered = filter_by_state(transactions, status)
    print(f"✅ Операции отфильтрованы по статусу '{status}'")
    print(f"📊 Осталось транзакций: {len(filtered)}")

    if not filtered:
        print("❌ Не найдено ни одной транзакции с выбранным статусом.")
        return

    # Сортировка по дате
    print("\n" + "=" * 40)
    print("ШАГ 3: Сортировка по дате")
    print("=" * 40)
    sort_choice = get_user_choice(
        "Отсортировать операции по дате? (да/нет): ", ["да", "нет"]
    )

    if sort_choice == "да":
        order_choice = get_user_choice(
            "Отсортировать по возрастанию или по убыванию? "
            "(возрастание/убывание): ",
            ["возрастание", "убывание"]
        )
        reverse = (order_choice == "убывание")
        filtered = sort_by_date(filtered, reverse)
        order_text = "по убыванию" if reverse else "по возрастанию"
        print(f"✅ Транзакции отсортированы {order_text}")
    else:
        print("ℹ️  Сортировка пропущена.")

    # Фильтрация рублевых транзакций
    print("\n" + "=" * 40)
    print("ШАГ 4: Фильтрация по валюте")
    print("=" * 40)
    ruble_choice = get_user_choice(
        "Выводить только рублевые транзакции? (да/нет): ", ["да", "нет"]
    )

    if ruble_choice == "да":
        ruble_transactions = [t for t in filtered if t.get('currency') == 'RUB']
        print(f"💰 Рублевых транзакций: {len(ruble_transactions)}")
        filtered = ruble_transactions
    else:
        print("ℹ️  Фильтрация по валюте пропущена.")

    # Поиск по описанию
    print("\n" + "=" * 40)
    print("ШАГ 5: Поиск по описанию")
    print("=" * 40)
    search_choice = get_user_choice(
        "Отфильтровать список транзакций по определенному "
        "слову в описании? (да/нет): ",
        ["да", "нет"]
    )

    if search_choice == "да":
        search_word = input("Введите слово для поиска в описании: ").strip()
        if search_word:
            filtered = process_bank_search(filtered, search_word)
            print(f"🔍 Найдено транзакций с '{search_word}': {len(filtered)}")
        else:
            print("ℹ️  Поисковый запрос пуст.")
    else:
        print("ℹ️  Поиск по описанию пропущен.")

    # Вывод результатов
    print("\n" + "=" * 60)
    print("📋 ИТОГОВЫЙ РЕЗУЛЬТАТ")
    print("=" * 60)
    print(f"Всего банковских операций в выборке: {len(filtered)}")
    print("=" * 60)

    if filtered:
        for i, transaction in enumerate(filtered, 1):
            print(f"\nТранзакция #{i}:")
            display_transaction(transaction)
    else:
        print(
            "\n❌ Не найдено ни одной транзакции, "
            "подходящей под ваши условия фильтрации"
        )


def main() -> None:
    """
    Основная функция программы.

    Реализует логику из домашнего задания.
    """
    print("=" * 60)
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("=" * 60)

    while True:
        print("\nГлавное меню:")
        print("1. Работа с транзакциями (полный цикл)")
        print("2. Выход")

        choice = get_user_choice("Ваш выбор: ", ["1", "2"])

        if choice == "2":
            print("\n👋 До свидания! Спасибо за использование программы.")
            break

        elif choice == "1":
            run_full_transaction_cycle()


if __name__ == "__main__":
    main()
