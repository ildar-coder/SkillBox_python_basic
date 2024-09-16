# TODO здесь писать код


def is_prime(num):
    if num <= 1:
        return False
    for i_num in range(2, int(num ** 0.5) + 1):
        if num % i_num == 0:
            return False
    else:
        return True


def get_elements(seq):
    return [el for i_el, el in enumerate(seq) if is_prime(i_el)]


print(get_elements('О Дивный Новый мир!'))
