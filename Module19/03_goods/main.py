goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
goods_inv = {value: key for key, value in goods.items()}
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# TODO здесь писать код
for key_prod, value_prod in store.items():
    quantity_sum = 0
    price_total = 0
    price_sum = 0
    for i_dict in value_prod:
        quantity_sum += i_dict['quantity']
        price_total = i_dict['quantity'] * i_dict['price']
        price_sum += price_total
    print("{0} - {1} штук, стоимость {2} рублей".format(goods_inv[key_prod], quantity_sum, price_sum))
