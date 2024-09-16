# TODO здесь писать код
def count_uppercase_lowercase(text: str):
    uppercase = 0
    lowercase = 0
    lst_text = text.split()
    for word in lst_text:
        for letter in word:
            if letter.isupper():
                uppercase += 1
            elif letter.islower():
                lowercase += 1

    return uppercase, lowercase

# Пример использования:
text = input("Введите строку для анализа: ")
uppercase, lowercase = count_uppercase_lowercase(text)
print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)
