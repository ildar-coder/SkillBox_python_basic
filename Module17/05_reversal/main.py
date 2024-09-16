# TODO здесь писать код
def reverse_h(text: str):
    start = text.find('h')
    stop = text.rfind('h')
    return text[stop - 1: start: -1]


line = input("Введите строку: ")
print(reverse_h(line))
