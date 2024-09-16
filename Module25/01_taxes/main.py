# TODO здесь писать код
class Property:
    def __init__(self, worth):
        self.worth = worth

    def calc_tax(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} налогооблагаемая база {self.worth}\n"


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calc_tax(self):
        return self.worth / 1000


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calc_tax(self):
        return self.worth / 200


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calc_tax(self):
        return self.worth / 500


money = int(input("Введите количество денег: "))
apart_worth = int(input("Введите стоимость квартиры: "))
apart = Apartment(apart_worth)
print('Налог на квартиру будет составлять {}'.format(apart.calc_tax()))
car_worth = int(input("Введите стоимость машины: "))
car = Apartment(car_worth)
print('Налог на машину будет составлять {}'.format(car.calc_tax()))
count_house_worth = int(input("Введите стоимость дачи: "))
count_house = Apartment(count_house_worth)
print('Налог на дачу будет составлять {}'.format(count_house.calc_tax()))
money_rest = money - apart.calc_tax() - car.calc_tax() - count_house.calc_tax()
if money_rest >= 0:
    print("На выплату налогов денег хватает!")
else:
    print("Не хватает {}".format(abs(money_rest)))



