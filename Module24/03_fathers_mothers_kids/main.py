# TODO здесь писать код



def calm_dawn():
    if Child.calmness == False:
        return True


class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.my_children = []

    def print_info(self):
        print("Меня зовут {}, мне {}".format(self.name, self.age))
        print(f"Дети:\n{'*':_^20}")
        for i_child in self.my_children:
            print("Имя ребенка: {}\n "
                  "Возраст ребенка: {}".format(i_child.child_name,
                                               i_child.age))
        print(f"{'*':_^20}")

    def add_child(self, child):
        if self.age - child.age > 16:
            self.my_children.append(child)
            print("Ребенок добавлен")
        else:
            print("Ребенок не подходит")

    def feed(self):
        if Child.hunger == False:
            return True


class Child:
    def __init__(self, child_name, age):
        self.child_name = child_name
        self.age = age
        self.calmness = True
        self.hunger = False


child_1 = Child('Лиза', 25)
child_2 = Child('Марта', 2)
parent_1 = Parent('Тамара', 42)
parent_1.add_child(child_1)
parent_1.add_child(child_2)
parent_1.print_info()
