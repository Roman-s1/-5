# Простая программа на Python для демонстрации работы с репозиторием
# Практическая работа № 2

def factorial(n: int) -> int:
    """Вычисляет факториал числа n."""
    if n < 0:
        raise ValueError("Факториал определён только для неотрицательных чисел")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n: int) -> list:
    """Возвращает первые n чисел Фибоначчи."""
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq


if __name__ == "__main__":
    print("Факториал 5 =", factorial(5))
    print("Первые 10 чисел Фибоначчи:", fibonacci(10))
