# TODO здесь писать код
# числа = [4, 9, 2, 7, 5]
# вспомогательная_функция(числа) → [4, 2], [5], [9, 7]

def partition(lst, pivot):
    less = []
    equal = []
    greater = []

    for x in lst:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)

    return less, equal, greater


def quick_sort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[-1]
    less, equal, greater = partition(lst, pivot)

    return quick_sort(less) + equal + quick_sort(greater)


nice_list = [4, 9, 2, 7, 5, 8, 3, 6, 1]
sorted_list = quick_sort(nice_list)
print(sorted_list)
