# TODO здесь писать код
import random

total_sum = 0
while True:
    num = int(input("Введите число: "))
    try:
        if random.randint(1, 13) == 5:
            raise BaseException('Вас постигла неудача!')
    except BaseException:
        print('Вас постигла неудача!')
        break
    with open('out_file.txt', 'a') as out_file:
        out_file.write(f'{str(num)}\n')
    total_sum += num
    if total_sum >= 777:
        print("Вы успешно выполнили условие для выхода из порочного цикла!")
        break
