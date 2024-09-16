# TODO здесь писать код
container_number = int(input("Количество контейнеров: "))
container_lst = []
for index in range(1, container_number + 1):
    container_weight = int(input("Введите вес контейнера: "))
    container_lst.append(container_weight)

new_container_weight = int(input("Введите вес нового контейнера: "))

for i, container in enumerate(container_lst):
    if new_container_weight > container:
        print(f'Номер, который получит новый контейнер: {i + 1}')
        break
    elif new_container_weight == container:
        print(f'Номер, который получит новый контейнер: {i + 2}')
        break
else:
    print(f'\n\nНомер, который получит новый контейнер: {len(container_lst) + 1}')
