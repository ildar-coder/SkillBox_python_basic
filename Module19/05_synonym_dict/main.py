# TODO здесь писать код
count_of_pairs = int(input("Введите количество пар слов: "))
pairs_dict = dict()
for idx in range(count_of_pairs):
    print("пара № {}".format(idx + 1), end=" ")
    pair = input().lower().split()
    pairs_dict[pair[0]] = pair[1]

while True:
    word = input("Введите слово: ").lower()
    word_exist = False
    for key, value in pairs_dict.items():
        if word == key:
            print("Синоним: ", value.title())
            word_exist = True
            break
        elif word == value:
            print("Синоним: ", key.title())
            word_exist = True
            break
    if word_exist:
        break
    else:
        print("Такого слова в словаре нет.")


