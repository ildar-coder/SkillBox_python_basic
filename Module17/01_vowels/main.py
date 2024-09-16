# TODO здесь писать код
vowels = 'аэоуыиеёюя'
text = input("Введите текст: ")
vowels_out = []
[vowels_out.append(symbol) for symbol in text if symbol in vowels]
print("Список гласных букв:", vowels_out)
print("Длина списка:", len(vowels_out))
