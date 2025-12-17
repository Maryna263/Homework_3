import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    # Знаходимо всі окремі числа, оточені пробілами (або на початку/в кінці рядка)
    # Використовуємо регулярний вираз для пошуку дійсних чисел
    for word in text.split():
        try:
            yield float(word)
        except ValueError:
            # Якщо слово не є числом, просто ігноруємо його
            continue

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    # Обчислюємо суму, ітеруючись по генератору
    return sum(func(text))
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")