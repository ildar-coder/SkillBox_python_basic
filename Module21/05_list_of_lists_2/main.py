nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

# TODO здесь писать код


def unpack_lst(lst):
    result = []
    for element in lst:
        if isinstance(element, int):
            result.append(element)

        elif isinstance(element, list):
            result.extend(unpack_lst(element))

    return result


result_1 = unpack_lst(nice_list)
print(result_1)
