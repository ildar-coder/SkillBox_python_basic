# TODO здесь писать код
def merge_sorted_lists(list1, list2):
    list1.extend(list2)
    list1.sort()
    for element in list1:
        if list1.count(element) > 1:
            count_el = list1.count(element)
            for _ in range(count_el - 1):
                list1.remove(element)
    return list1
# Пример использования:
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]
merged = merge_sorted_lists(list1, list2)
print(merged)
