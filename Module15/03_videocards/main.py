# TODO здесь писать код
lst_old = []
lst_new = []
maxx = 0
video_cart_number = int(input('Количество видеокарт: '))
for index in range(1, video_cart_number + 1):
    video_cart_model = int(input(f'{index} Видеокарта: '))
    if video_cart_model > maxx:
        maxx = video_cart_model
    lst_old.append(video_cart_model)

for video_cart in lst_old:
    if video_cart != maxx:
        lst_new.append(video_cart)

print(lst_old)
print(lst_new)
