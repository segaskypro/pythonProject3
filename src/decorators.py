"""одуль с декораторами для логирования."""

import functools
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    екоратор для логирования работы функций.

    Args:
        filename (str, optional): мя файла для записи логов.
            сли None, логи выводятся в консоль.

    Returns:
        Callable: екорированная функция.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok\n"

                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(message)
                else:
                    print(message, end='')

                return result

            except Exception as e:
                message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"

                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(message)
                else:
                    print(message, end='')

                raise

        return wrapper

    return decorator
