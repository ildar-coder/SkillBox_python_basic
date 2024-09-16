films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

# TODO здесь писать код
films_number = int(input("Сколько фильмов хотите добавить? "))
favorite_films = []
count = 0
while count < films_number :
    films_name = input("Введите название фильма: ")
    if films_name in films:
        favorite_films.append(films_name)
        count += 1
    else:
        print(f"Ошибка: фильма {films_name} у нас нет :(")

print("Ваш список любимых фильмов: ", ', '.join(favorite_films))
