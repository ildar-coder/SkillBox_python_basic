# TODO здесь писать код
# Введите строку: aab
# Можно сделать палиндромом
# Введите строку: aabc
# Нельзя сделать палиндромом

text = input("Введите строку: ")
odd_symbols = set()
for sym in text:
    if sym in odd_symbols:
        odd_symbols.remove(sym)
    else:
        odd_symbols.add(sym)
if ((len(text) % 2 == 0 and len(odd_symbols)) == 0 or
        (len(text) % 2 != 0 and len(odd_symbols)) == 1):
    print("Можно сделать палиндромом")
else:
    print("Нельзя сделать палиндромом")
