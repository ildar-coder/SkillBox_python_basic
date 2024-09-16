# TODO здесь писать код
# При запуске запрашивается имя пользователя. После этого он выбирает одно из действий:
#
# 1. Посмотреть текущий текст чата.
# 2. Отправить сообщение (затем вводит сообщение).
# Действия запрашиваются бесконечно.
users = set()
chat = []
while True:
    user_name = input("Введите имя пользователя ")
    if user_name in users:
        entry_message = f'{user_name}, рады видеть Вас снова!'
    else:
        entry_message = f'{user_name}, добро пожаловать в чат!'
        users.add(user_name)

    chat.append(entry_message + '\n')

    try:
        user_choice = int(input("1. Посмотреть текущий текст чата.\n"
                                "2. Отправить сообщение\n"))

        if user_choice == 1:
            print(*chat)
        elif user_choice == 2:
            message = input("Введите сообщение ")
            chat_text = f'{user_name}: {message}\n'
            chat.append(chat_text)
        else:
            print("Неверно введено число!")
    except ValueError as exc:
        print(exc)
