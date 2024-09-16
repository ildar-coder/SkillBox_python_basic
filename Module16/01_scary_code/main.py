# a = [1, 5, 3]
# b = [1, 5, 1, 5]
# c = [1, 3, 1, 5, 3, 3]
# for i in b:
#     a.append(i)
# print(a)
# t = 0
# for i in a:
#     if i == 5:
#         t += 1
# print(t)
# d = []
# for i in a:
#     if i != 5:
#         d.append(i)
# print(d)
# for i in c:
#     d.append(i)
# t = 0
# for i in d:
#     if i == 3:
#         t += 1
# print(t)
# print(d)

# TODO переписать программу
lst_main = [1, 5, 3]
lst_secondary_1 = [1, 5, 1, 5]
lst_secondary_2 = [1, 3, 1, 5, 3, 3]

print('Результат работы программы:')
lst_main.extend(lst_secondary_1)
count_1 = lst_main.count(5)
print('Кол-во цифр 5 при первом объединении:', count_1)
for _ in range(count_1):
    lst_main.remove(5)
lst_main.extend(lst_secondary_2)
count_2 = lst_main.count(3)
print('Кол-во цифр 3 при втором объединении:', count_2)
print('Итоговый список', lst_main)
