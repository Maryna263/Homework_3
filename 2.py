import re
from typing import Callable, Generator

import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    # Розбиваємо рядок на окремі елементи (слова)
    parts = text.split()
    
    # Якщо елементів менше 3, число не може бути "всередині" з пробілами з обох боків
    if len(parts) < 3:
        return

    # Ітеруємося з другого елемента до передостаннього
    for i in range(1, len(parts) - 1):
        try:
            # Спробуємо перетворити елемент на дійсне число
            yield float(parts[i])
        except ValueError:
            # Якщо це не число, просто пропускаємо
            continue

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    # Обчислюємо суму, ітеруючись по генератору
    return sum(func(text))
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")