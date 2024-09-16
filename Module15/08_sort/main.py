# TODO здесь писать код
lst_in = list(map(int, input('Введи числа - элементы списка через пробел: ').split()))
print('Изначальный список:', lst_in)
k = 0
for i in range(0, len(lst_in) - 1):
    for j in range(0, len(lst_in) - 1 - k):
        if lst_in[j] > lst_in[j + 1]:
            lst_in[j], lst_in[j + 1] = lst_in[j + 1], lst_in[j]
    k += 1
print('Отсортированный список:', lst_in)
