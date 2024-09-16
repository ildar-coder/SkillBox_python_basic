guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

# TODO здесь писать код
while True:
    print(f'Сейчас на вечеринке {len(guests)} человек: {guests}')
    guest_action = input('Гость пришёл или ушёл? ').lower()
    if guest_action == 'пришел':
        guest_name = input('Имя гостя: ')
        if len(guests) < 6:
            print(f'Привет, {guest_name}!')
            guests.append(guest_name)
        else:
            print(f'Прости, {guest_name}, но мест нет.')
    elif guest_action == 'ушёл' or guest_action == 'ушел':
        guest_name = input('Имя гостя: ')
        if guest_name in guests:
            print(f'Пока, {guest_name}!')
            guests.remove(guest_name)
        else:
            print('Такого гостя у нас нет!')
    elif guest_action == 'пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
    else:
        print('Неправильный ввод')
