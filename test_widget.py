from src.widget import mask_account_card, get_date

print("=== Тестируем mask_account_card ===")
test_cases = [
    "Maestro 1596837868705199",
    "Счет 64686473678894779589",
    "MasterCard 7158300734726758",
    "Счет 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum 8990922113665229",
    "Visa Gold 5999414228426353",
    "Счет 73654108430135874305"
]

for case in test_cases:
    result = mask_account_card(case)
    print(f"Вход: {case}")
    print(f"Выход: {result}")
    print()

print("=== Тестируем get_date ===")
date_test = "2024-03-11T02:26:18.671407"
print(f"Вход: {date_test}")
print(f"Выход: {get_date(date_test)}")