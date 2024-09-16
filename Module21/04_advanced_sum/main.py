# TODO здесь писать код
def summa(*args):
    total = 0
    for data in args:
        if isinstance(data, list):
            total += summa(*data)
        elif isinstance(data, int):
            total += data
    return total


result_1 = summa(1, 2, 3, 4, 5)
print(result_1)

result_2 = summa(([[1, 2, [3]], [1], 3]))
print(result_2)
