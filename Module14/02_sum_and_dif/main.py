# TODO здесь писать код
def sum_num(num):
    summ = 0
    while num:
        last_num = num % 10
        summ += last_num
        num //= 10
    return summ


def num_count(num):
    count = 0
    while num:
        count += 1
        num //= 10
    return count


number = int(input("Введите число: "))
print(f"\nСумма чисел: {sum_num(number)}")
print(f"Количество цифр в числе: {num_count(number)}")
print(f"Разность суммы и количества цифр: {sum_num(number) - num_count(number)}")
