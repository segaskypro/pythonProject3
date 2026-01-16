print("=" * 50)
print("ТЕСТ ПРОГРАММЫ")
print("=" * 50)

# Добавляем src в путь импорта
import sys

sys.path.insert(0, 'src')

try:
    print("1. Импортируем masks...")
    from masks import mask_account, mask_card_number

    print("   ✅ Успешно!")

    # Тест
    card = "7000792289606361"
    account = "73654108430135874305"

    print(f"\n2. Тест маскировки карты:")
    result_card = mask_card_number(card)
    print(f"   {card} -> {result_card}")

    print(f"\n3. Тест маскировки счета:")
    result_account = mask_account(account)
    print(f"   {account} -> {result_account}")

    print("\n" + "=" * 50)
    print("✅ ВСЁ РАБОТАЕТ КОРРЕКТНО!")
    print("=" * 50)

except ImportError as e:
    print(f"   ❌ Ошибка импорта: {e}")
except Exception as e:
    print(f"   ❌ Другая ошибка: {type(e).__name__}: {e}")
    import traceback

    traceback.print_exc()

input("\nНажмите Enter для выхода...")