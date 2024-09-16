# TODO здесь писать код
def hist(string: str):
    hist_dict = {}
    for sym in string:
        if sym in hist_dict:
            hist_dict[sym] += 1
        else:
            hist_dict[sym] = 1

    return hist_dict


def hist_inv(dictionary: dict):
    hist_dict_inv = {}
#     {value: hist_dict_inv[value].append(key)
#     if value in hist_dict_inv
#     else value: list(key)
#     for key, value in dictionary
#      }
    for key, value in dictionary.items():
        if value in hist_dict_inv:
            hist_dict_inv[value].append(key)
        else:
            hist_dict_inv[value] = list(key)

    return hist_dict_inv


# здесь что-то написано
text = input("Введите текст: ").lower()
print("Оригинальный словарь частот:")
orig_dic = hist(text)
for i_sym in sorted(orig_dic.keys()):
    print("{0} : {1}".format(i_sym, orig_dic[i_sym]))

print("Инвертированный словарь частот:")
inv_dic = hist_inv(orig_dic)
for i_sym in inv_dic:
    print("{0} : {1}".format(i_sym, inv_dic[i_sym]))
