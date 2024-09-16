# TODO здесь писать код
N = int(input("Введите длину списка: "))
result = [1 if index % 2 == 0 else index % 5 for index in range(N)]
print("Результат:", result)
