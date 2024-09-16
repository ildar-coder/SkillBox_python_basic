# TODO здесь писать код
# [1, 2, 1, 2, 2]
# [1, 2, 3, 4, 5]
# [1, 2, 1] — в этом случае ничего добавлять не нужно.
# [1, 2, 3, 4, 3] — в этом случае надо добавить минимум, то есть числа 2 и 1.
def is_palindrome(lst1):
    lst1_reverse = []
    for i_elem in range(len(lst1) - 1, -1, -1):
        lst1_reverse.append(lst[i_elem])
    if lst1 == lst1_reverse:
        return True
    else:
        return False


numbers = int(input('Кол-во чисел: '))
seq_in = []
for _ in range(numbers):
    print("Число:", end=" ")
    num = int(input())
    seq_in.append(num)
print()
print("Последовательность:", seq_in)

lst = []
lst_to_ad = []
for i_elem in range(0, len(seq_in)):
    for j_elem in range(i_elem, len(seq_in)):
        lst.append(seq_in[j_elem])
    if is_palindrome(lst):
        lst_to_ad = seq_in[: i_elem]
        lst_to_ad.reverse()
        break
    else:
        lst = []
else:
    lst_to_ad = seq_in[: len(seq_in) - 1]
    lst_to_ad.reverse()

print("Нужно приписать чисел:", len(lst_to_ad))
print("Сами числа:", *lst_to_ad)
