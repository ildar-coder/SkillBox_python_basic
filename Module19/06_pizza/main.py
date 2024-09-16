# TODO здесь писать код
def pizza_orders():
    num_orders = int(input("Введите количество заказов: "))
    orders = {}

    for i in range(num_orders):
        order = input(f"Заказ {i+1}: ").split()
        customer = order[0]
        pizza = order[1]
        quantity = int(order[2])

        if customer not in orders:
            orders[customer] = {}
        if pizza not in orders[customer]:
            orders[customer][pizza] = 0
        orders[customer][pizza] += quantity

    return orders


def print_orders(orders):
    for customer in sorted(orders):
        print(f"{customer}:")
        for pizza, quantity in sorted(orders[customer].items()):
            print(f"     {pizza}: {quantity}")


orders_dict = pizza_orders()
print_orders(orders_dict)