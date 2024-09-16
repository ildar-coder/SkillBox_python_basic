# TODO здесь писать код
class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Mud()
        elif isinstance(other, Ice):
            return Frost()
        return None


class Air:
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        return None


class Fire:
    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Earth):
            return Lava()
        return None


class Earth:
    def __add__(self, other):
        if isinstance(other, Water):
            return Mud()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        return None


class Storm:
    def __repr__(self):
        return "Шторм"


class Steam:
    def __repr__(self):
        return "Пар"


class Mud:
    def __repr__(self):
        return "Грязь"


class Lightning:
    def __repr__(self):
        return "Молния"


class Dust:
    def __repr__(self):
        return "Пыль"


class Lava:
    def __repr__(self):
        return "Лава"


water = Water()
air = Air()
fire = Fire()
earth = Earth()

print(water + air)
print(water + fire)
print(water + earth)
print(air + fire)
print(air + earth)
print(fire + earth)


class Ice:
    def __repr__(self):
        return "Лёд"


class Frost:
    def __repr__(self):
        return "Иней"


class Ice:
    def __add__(self, other):
        if isinstance(other, Water):
            return Frost()
        return None


ice = Ice()

print(water + ice)
print(ice + water)
