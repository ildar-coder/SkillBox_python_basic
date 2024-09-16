# TODO здесь писать код
text_lst = input("Введите строку: ").split()
lst_lenghts = [len(i_word) for i_word in text_lst]
mx = max(lst_lenghts)
word_mx_lenght = text_lst[lst_lenghts.index(mx)]
print('Самое длинное слово:', word_mx_lenght)
print('Длина этого слова:', mx)
