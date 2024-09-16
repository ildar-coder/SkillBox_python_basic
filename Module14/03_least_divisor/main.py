# TODO здесь писать код
def least_divider(num):
    divider = 1
    for idx in range(2, int(number ** 0.5) + 1):
        if num % idx == 0:
            divider = idx
            break
    else:
        divider = num

    return divider


number = int(input("Введите число: "))
print(f'Наименьший делитель, отличный от единицы: {least_divider(number)}')
