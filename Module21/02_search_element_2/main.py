# TODO здесь писать код
site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def key_search(struct: dict, new_key, depth=None):
    if depth is None:
        depth = float('inf')
    if depth == 0:
        return None

    if new_key in struct:
        return struct[new_key]
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = key_search(sub_struct, new_key, depth - 1)
            if result:
                break
    else:
        result = None

    return result


key_to_find = input("Введите искомый ключ: ")
choice_depth = input("Хотите ввести максимальную глубину? Y/N: ").lower()
if choice_depth == "y":
    maximum_depth = int(input("Введите максимальную глубину: "))
    answer = key_search(site, key_to_find, depth=maximum_depth)
    print(answer)
elif choice_depth == "n":
    answer = key_search(site, key_to_find)
    print(answer)
else:
    print("Неправильный ввод")


