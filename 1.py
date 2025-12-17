def caching_fibonacci():
    # Створюємо порожній словник для кешу
    cache = {}

    def fibonacci(n):
             
        # Базові випадки для послідовності Фібоначчі
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        
        # Рекурсивне обчислення з подальшим збереженням у кеш
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    # Повертаємо внутрішню функцію
    return fibonacci

# Приклад використання:
fib = caching_fibonacci()

# Перше обчислення (відбувається рекурсія)
print(fib(10))  
# Наступні виклики з тими самими аргументами братимуть значення з кешу
print(fib(15)) 
print(fib(16)) 
