# TODO здесь писать код
first_file = open('first_tour.txt', 'w')
text = ('80\n'
        'Ivanov Serg 80\n'
        'Sergeev Petr 92\n'
        'Petrov Vasiliy 98\n'
        'Vasiliev Maxim 78'
        )
first_file.write(text)
first_file.close()


def get_score(data):
    return int(data[2])


first_file = open('first_tour.txt', 'r')
lines = first_file.readlines()
passing_score = int(lines[0].strip())
passed_people = []
for line in lines[1:]:
    score = int(line.split()[2])
    if score > passing_score:
        passed_people.append(tuple(line.split()))
sorted_passed_people = sorted(passed_people, key=get_score, reverse=True)
first_file.close()
second_file = open('second_tour.txt', 'w')
second_file.write(f'{len(sorted_passed_people)}\n')
for i, (surname, name, score) in enumerate(sorted_passed_people, start=1):
    second_file.write(f'{i}) {name[0]}. {surname} {score}\n')

second_file.close()
