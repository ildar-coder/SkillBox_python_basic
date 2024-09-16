import copy
struct = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

# TODO здесь писать код
import copy


def deep_update(data, old_value, new_value):
    if isinstance(data, dict):
        return {k: deep_update(v, old_value, new_value) for k, v in data.items()}
    elif isinstance(data, list):
        return [deep_update(i, old_value, new_value) for i in data]
    elif isinstance(data, str) and old_value in data:
        return data.replace(old_value, new_value)
    return data


def create_sites():

    num_sites = int(input("Сколько сайтов: "))

    sites = []

    for _ in range(num_sites):
        product_name = input("Введите название продукта для нового сайта: ")

        new_site = copy.deepcopy(struct)

        new_site = deep_update(new_site, 'телефон', product_name)
        new_site = deep_update(new_site, 'iphone', product_name)

        sites.append(new_site)

        print(f"Сайт для {product_name}:")
        print(f"site = {new_site}")
        print()


create_sites()
