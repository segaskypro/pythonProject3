# Простейший тест
print("=" * 50)
print("ТЕСТ ПРОГРАММЫ")
print("=" * 50)

# Пробуем импортировать модули
try:
    print("1. Пробуем импортировать masks...")
    import src.masks

    print("   ✅ Успешно!")

    from src.masks import mask_account, mask_card_number

    print("   ✅ Функции импортированы!")

    # Тест
    card = "7000792289606361"
    account = "73654108430135874305"

    print(f"\n2. Тест маскировки:")
    print(f"   Карта: {card} -> {mask_card_number(card)}")
    print(f"   Счет: {account} -> {mask_account(account)}")

except ImportError as e:
    print(f"   ❌ Ошибка импорта: {e}")
except SyntaxError as e:
    print(f"   ❌ Синтаксическая ошибка: {e}")
except Exception as e:
    print(f"   ❌ Неизвестная ошибка: {type(e).__name__}: {e}")

print("\n" + "=" * 50)
print("ТЕСТ ЗАВЕРШЕН")
print("=" * 50)
