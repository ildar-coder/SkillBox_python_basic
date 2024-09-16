# TODO здесь писать код
import random


class House:
    def __init__(self):
        self.food = 50
        self.money = 0

    def __repr__(self):
        return f"Дом(Еда: {self.food}, Деньги: {self.money})"


class Person:
    def __init__(self, name, house):
        self.name = name
        self.satiety = 50
        self.house = house

    def eat(self):
        if self.house.food >= 10:
            self.satiety += 10
            self.house.food -= 10
            print(f"{self.name} поел. Сытость: {self.satiety}. Еда в доме: {self.house.food}")
        else:
            print(f"В доме недостаточно еды для {self.name}.")

    def work(self):
        self.satiety -= 10
        self.house.money += 50
        print(f"{self.name} поработал. Сытость: {self.satiety}. Деньги в доме: {self.house.money}")

    def play(self):
        self.satiety -= 10
        print(f"{self.name} поиграл. Сытость: {self.satiety}")

    def shop(self):
        if self.house.money >= 50:
            self.house.food += 50
            self.house.money -= 50
            print(f"{self.name} сходил в магазин. Еда в доме: {self.house.food}. Деньги в доме: {self.house.money}")
        else:
            print(f"Недостаточно денег у {self.name} для покупки еды.")

    def live_one_day(self):
        if self.satiety <= 0:
            print(f"{self.name} умер от голода...")
            return False

        dice = random.randint(1, 6)
        if self.satiety < 20:
            self.eat()
        elif self.house.food < 10:
            self.shop()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play()
        return True

    def __repr__(self):
        return f"Человек(Имя: {self.name}, Сытость: {self.satiety})"


def main():
    house = House()
    person1 = Person("Артём", house)
    person2 = Person("Олег", house)

    for day in range(1, 366):
        print(f"\nДень {day}:")
        if not person1.live_one_day() or not person2.live_one_day():
            break
        print(person1)
        print(person2)
        print(house)


main()
