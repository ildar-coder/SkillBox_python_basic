# TODO здесь писать код
# Придумайте пароль: qwerty
# Пароль ненадёжный. Попробуйте ещё раз.
# Придумайте пароль: qwerty12
# Пароль ненадёжный. Попробуйте ещё раз.
# Придумайте пароль: qwerty123
# Пароль ненадёжный. Попробуйте ещё раз.
# Придумайте пароль: qWErty123
# Это надёжный пароль!

error_msg = 'Пароль ненадёжный. Попробуйте ещё раз.'
while True:
    password = input("Придумайте пароль: ")
    if len(password) < 8:
        print(error_msg, '\nпароль должен быть больше 8 символов' )
        continue
    sum_digit = 0
    sum_up_letters = 0
    for char in password:
        if char.isdigit():
            sum_digit += 1
        if char.isupper():
            sum_up_letters += 1
    if sum_digit >= 3 and sum_up_letters >= 1:
        print("Это надёжный пароль!")
        break
    else:
        print(error_msg)
