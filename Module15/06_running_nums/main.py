# TODO здесь писать код
shift = int(input('Сдвиг: '))
lst_in = list(map(int, input('Введи числа - элементы списка через пробел: ').split()))
print('Изначальный список:', lst_in)
shift = shift % len(lst_in)
lst_in = lst_in[-shift:] + lst_in[:-shift]
print('Сдвинутый список:', lst_in)
