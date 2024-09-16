# TODO здесь писать код
# Ответ в консоли: (-5, -1, 3, 4, 6, 8, 10)

def tpl_sort(tpl):
    tpl_lst = list(tpl)
    k = 0
    for i in range(len(tpl_lst) - 1):
        for j in range(len(tpl_lst) - 1 - k):
            if isinstance(tpl_lst[j], int):
                if tpl_lst[j] > tpl_lst[j+1]:
                    tpl_lst[j], tpl_lst[j+1] = tpl_lst[j+1], tpl_lst[j]
            else:
                return tpl
        k += 1

    return tuple(tpl_lst)


tpl = (6, 3, -1, 8, 4, 10, -5)
print(tpl_sort(tpl))
