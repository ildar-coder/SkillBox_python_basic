# TODO здесь писать код
word = input('Введите слово: ')
word_vice_versa =''
for symbol in word:
    word_vice_versa = symbol + word_vice_versa

if word == word_vice_versa:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')
