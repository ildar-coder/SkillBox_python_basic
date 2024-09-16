# TODO здесь писать код
s_list = list(input("Введите строку: "))
new_list = []
count = 1
for i_el in range(len(s_list)):
    if i_el == len(s_list) - 1:
        new_list.append(s_list[i_el])
        new_list.append(count)
    elif s_list[i_el] == s_list[i_el + 1]:
        count += 1
    else:
        new_list.append(s_list[i_el])
        new_list.append(count)
        count = 1
new_list = list(map(str, new_list))
compressed_data = ''.join(new_list)
print("Закодированная строка:", compressed_data)
