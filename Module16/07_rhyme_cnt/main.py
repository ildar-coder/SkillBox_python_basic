# TODO здесь писать код
def find_last_person(N, K):
    circle = list(range(1, N + 1))

    index = 0
    next_round_start = 1
    while len(circle) > 1:
        print(f"\nТекущий круг людей: {circle}")
        index = (index + K - 1) % len(circle)
        print(f"Начало счёта с номера {next_round_start}")
        print(f"Выбывает человек под номером {circle[index]}")
        next_round_start = circle[(index + 1) % len(circle)]
        circle.pop(index)


    return circle[0]


N = int(input("Кол-во человек: "))
K = int(input("Какое число в считалке? "))
print(f"Значит, выбывает каждый {K}-й человек")
print(f"Остался человек под номером {find_last_person(N, K)}")