from src.masks import mask_account, mask_card_number


# Тестируем функции
card_result = mask_card_number("7000792289606361")
account_result = mask_account("73654108430135874305")

print("Маскировка карты:")
print("Вход: 7000792289606361")
print(f"Выход: {card_result}")

print("\nМаскировка счета:")
print("Вход: 73654108430135874305")
print(f"Выход: {account_result}")

# Проверяем соответствие заданию
expected_card = "7000 79** **** 6361"
expected_account = "**4305"

print("\nПроверка:")
print(f"Карта: {'✓' if card_result == expected_card else '✗'} {card_result}")
print(f"Счет: {'✓' if account_result == expected_account else '✗'} "
      f"{account_result}")
