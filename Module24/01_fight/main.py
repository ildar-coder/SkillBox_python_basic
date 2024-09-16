# TODO здесь писать код
## Задача 1. Драка
### Что нужно сделать
# Вы работаете в команде разработчиков мобильной игры, и
# вам досталась такая часть от ТЗ заказчика:
#
# Есть два юнита, каждый из них называется «Воин».
# Каждому устанавливается здоровье в 100 очков.
# Они бьют друг друга в случайном порядке. Тот, кто бьёт, здоровье не теряет.
# У того, кого бьют, оно уменьшается на 20 очков от одного удара.
# После каждого удара надо выводить сообщение, какой юнит атаковал и сколько у противника осталось здоровья.
# Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.
#
# Реализуйте такую программу.
import random


class Warrior:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def punced(self):
        self.health -= 20

    def is_dead(self):
        return self.health <= 0


def main(warrior_1 : Warrior, warrior_2: Warrior):
    while True:
        hit = random.randint(1,2)
        if hit == 1:
            warrior_2.punced()
            print(f'{warrior_1.name} наносит удар, '
                  f'у {warrior_2.name} осталось здоровья {warrior_2.health}')
            if warrior_2.is_dead():
                print("Битва окончена, победил {}".format(warrior_1.name))
                break
        if hit == 2:
            if hit == 2:
                warrior_1.punced()
                print(f'{warrior_2.name} наносит удар, '
                      f'у {warrior_1.name} осталось здоровья {warrior_1.health}')
                if warrior_1.is_dead():
                    print("Битва окончена, победил {}".format(warrior_2.name))
                    break


fighter_1 = Warrior('Max')
fighter_2 = Warrior('Farid')
main(fighter_1, fighter_2)



