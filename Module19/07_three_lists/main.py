# TODO здесь писать код
# Найти элементы, которые есть в каждом списке;
# Найти элементы из первого списка, которых нет во втором и третьем списках.

array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

print("1. Решение без использования множеств:")
array_4 = []
total_array = []
for i_1 in range(len(array_1)):
    if array_1[i_1] in array_2:
        array_4.append(array_1[i_1])
for i_4 in range(len(array_4)):
    if array_4[i_4] in array_3:
        total_array.append(array_4[i_4])
print(*total_array)

print("1. Решение c использованием множеств.")
s1 = set(array_1)
s2 = set(array_2)
s3 = set(array_3)
print(*s1.intersection(s2).intersection(s3))

print("2. Решение без использования множеств:")
array_5 = []
array_difference = []
for i_1 in range(len(array_1)):
    if array_1[i_1] not in array_2:
        array_5.append(array_1[i_1])
for i_5 in range(len(array_5)):
    if array_5[i_5] not in array_3:
        array_difference.append(array_5[i_5])
print(*array_difference)

print("2. Решение c использованием множеств.")
print(*s1.difference(s2).difference(s3))
