students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def f(dict):
    lst = []
    string = ''
    for i in dict:
        lst += (dict[i]['interests'])
        string += dict[i]['surname']
    cnt = 0
    for s in string:
        cnt += 1
    return lst, cnt


pairs = []
for i in students:
    pairs += (i, students[i]['age'])


my_lst = f(students)[0]
l = f(students)[1]
print(my_lst, l)

# TODO исправить код


def interests_surname_len(students):
    interests = set()
    total_surname_lenght = 0
    for i_stud in students:
        total_surname_lenght += len(students[i_stud]['surname'])
        for interest in students[i_stud]['interests']:
            interests.add(interest)

    return interests, total_surname_lenght


pairs_id_age = [
    (i_stud, student_dict['age'])
    for i_stud, student_dict
    in students.items()
]
print('Список пар "ID студента — возраст":', pairs_id_age)
total_interests, total_lenght = interests_surname_len(students)
print('Полный список интересов всех студентов:', total_interests)
print('Общая длина всех фамилий студентов:', total_lenght)
