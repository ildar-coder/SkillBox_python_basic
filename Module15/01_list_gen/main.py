# TODO здесь писать код
number = int(input("Введите число: "))
lst = []
for index in range(1, number + 1):
    if index % 2 != 0:
        lst.append(index)
print('Список из нечётных чисел от одного до N:', lst)
