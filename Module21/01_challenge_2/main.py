# TODO здесь писать код
def display_nums(num):
    if num == 1:
        print(1)
    else:
        display_nums(num - 1)
        print(num)


num = int(input("Введите num: "))
display_nums(num)
