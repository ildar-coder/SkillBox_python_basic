# TODO здесь писать код
# Введите номер действия:
#  1. Добавить контакт
#  2. Найти человека
# 2
# Введите фамилию для поиска: Сидоров
# Иван Сидоров 888

contacts_dict = {}
def find_person():
    surname_to_find = input("Введите фамилию для поиска: ")
    for name, last_name in contacts_dict:
        if last_name.lower() == surname_to_find.lower():
            return (f"{name} {last_name} {contacts_dict[(name, last_name)]}")
    else:
        return "Такого человека нет в контактах"



def add_contact():
    name, surname = input("Введите имя и фамилию нового контакта"
                          " (через пробел): ").split()
    if (name, surname) not in contacts_dict:
        phone_num = int(input("Введите номер телефона: "))
        contacts_dict[(name, surname)] = phone_num
    else:
        return ("Такой человек уже есть в контактах.")

    return f"Текущий словарь контактов: {contacts_dict}"

while True:
    choice_action = int(input(
        "Введите номер действия:\n"
        " 1. Добавить контакт\n"
        " 2. Найти человека\n"
    ))
    if choice_action == 1:
        print(add_contact())
    elif choice_action == 2:
        print(find_person())
    else:
        print("Ошибка ввода, такого номера команды нет")