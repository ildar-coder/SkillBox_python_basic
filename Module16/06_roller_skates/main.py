# TODO здесь писать код
def max_people_with_skates(skate_sizes, person_sizes):
    people_count = 0
    for skate_size in skate_sizes:
        for person_size in person_sizes:
            if skate_size == person_size:
                people_count += 1
                person_sizes.remove(person_size)
                break
    return people_count


skate_number = int(input("Кол-во коньков: "))
skate_sizes = []
person_sizes = []

for i_skate in range(skate_number):
    print(f'размер {i_skate + 1}-й пары:', end=' ')
    skate_size = int(input())
    skate_sizes.append(skate_size)

person_number = int(input("Кол-во людей: "))
for i_person in range(person_number):
    print(f'Размер ноги {i_person + 1}-го человека:', end=' ')
    person_size = int(input())
    person_sizes.append(person_size)

print('Наибольшее кол-во людей, которые могут взять ролики:',
      max_people_with_skates(skate_sizes, person_sizes)
      )

