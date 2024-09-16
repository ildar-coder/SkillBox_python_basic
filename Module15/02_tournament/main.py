# TODO здесь писать код
lst = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
lst_for_first_day = []
for i in range(len(lst)):
    if i % 2 == 0:
        lst_for_first_day.append(lst[i])
print('Первый день:', lst_for_first_day)
