# TODO здесь писать код
import math
# Здесь создайте функцию get_sage_sqrt


def get_sage_sqrt(num):
    try:
        return f"{math.sqrt(num):.2f}"
    except (ValueError, TypeError) as exc:
        print(exc)


# Тестовые случаи
numbers = [16, 25, -9, 0, 4.5, "abc"]
for number in numbers:
    result = get_sage_sqrt(number)
    print(f"Квадратный корень numbers {number}: {result}")