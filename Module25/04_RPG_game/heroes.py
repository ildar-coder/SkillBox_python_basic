class Hero:
    max_hp = 150
    start_power = 10

    def __init__(self, name):
        self.name = name
        self.__hp = self.max_hp
        self.__power = self.start_power
        self.__is_alive = True

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_value):
        self.__hp = max(new_value, 0)
        if self.__hp == 0:
            self.__is_alive = False

    def get_power(self):
        return self.__power

    def set_power(self, new_power):
        self.__power = new_power

    def is_alive(self):
        return self.__is_alive

    def attack(self, target):
        raise NotImplementedError("Вы забыли переопределить метод Attack!")

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - damage)
        print(f"\t{self.name} получил удар с силой {round(damage)}. Осталось здоровья: {round(self.get_hp())}")

    def make_a_move(self, friends, enemies):
        self.set_power(self.get_power() + 0.1)

    def __str__(self):
        return f"Name: {self.name} | HP: {self.get_hp()}"


class Healer(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.magic_power = self.get_power() * 3

    def attack(self, target):
        target.take_damage(self.get_power() / 2)

    def take_damage(self, damage):
        super().take_damage(damage * 1.2)

    def heal(self, target):
        target.set_hp(target.get_hp() + self.magic_power)

    def make_a_move(self, friends, enemies):
        super().make_a_move(friends, enemies)
        target_of_potion = min(friends, key=lambda friend: friend.get_hp())
        if target_of_potion.get_hp() <= 80:
            print(f"{self.name} исцеляет {target_of_potion.name}")
            self.heal(target_of_potion)
        else:
            if enemies:
                print(f"{self.name} атакует ближнего - {enemies[0].name}")
                self.attack(enemies[0])

    def __str__(self):
        return super().__str__() + f" | Magic Power: {self.magic_power}"


class Tank(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.defense = 1
        self.shield = False

    def attack(self, target):
        target.take_damage(self.get_power() / 2)

    def take_damage(self, damage):
        super().take_damage(damage / self.defense)

    def set_shield_state(self):
        if self.shield:
            self.shield = False
            self.defense /= 2
            self.set_power(self.get_power() * 2)
        else:
            self.shield = True
            self.defense *= 2
            self.set_power(self.get_power() / 2)

    def make_a_move(self, friends, enemies):
        super().make_a_move(friends, enemies)
        if self.get_hp() < 80 and not self.shield:
            print(f"{self.name} поднимает щит")
            self.set_shield_state()
        elif self.get_hp() > 80 and self.shield:
            print(f"{self.name} опускает щит")
            self.set_shield_state()
        else:
            if enemies:
                target = min(enemies, key=lambda enemy: enemy.get_hp())
                print(f"{self.name} атакует ближнего - {target.name}")
                self.attack(target)

    def __str__(self):
        return super().__str__() + f" | Shield: {self.shield}"


class Attacker(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.power_multiply = 1

    def attack(self, target):
        target.take_damage(self.get_power() * self.power_multiply)
        self.power_down()

    def power_down(self):
        self.power_multiply /= 2

    def power_up(self):
        self.power_multiply *= 2

    def take_damage(self, damage):
        super().take_damage(damage * (self.power_multiply / 2))

    def make_a_move(self, friends, enemies):
        super().make_a_move(friends, enemies)
        if enemies:
            target = min(enemies, key=lambda enemy: enemy.get_hp())
            print(f"{self.name} атакует ближнего - {target.name}")
            self.attack(target)
            self.power_up()

    def __str__(self):
        return super().__str__() + f" | Power Multiply: {self.power_multiply}"
