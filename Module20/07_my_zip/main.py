# TODO здесь писать код
# Строка: abcd
# Кортеж чисел: (10, 20, 30, 40)

# Результат:
# <generator object <genexpr> at 0x00000204A4234048>
# ('a', 10)
# ('b', 20)
# ('c', 30)
# ('d', 40)

def my_zip(iterable_1, iterable_2):
    return ((iterable_1[i], iterable_2[i]) for i in range(len(iterable_1)))


iterable_1 = 'abcd'
iterable_2 = (10, 20, 30, 40)
print(my_zip(iterable_1, iterable_2))
for element in my_zip(iterable_1, iterable_2):
    print(element)

