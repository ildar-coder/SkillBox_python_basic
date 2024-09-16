# TODO здесь писать код
# Реализуйте модель с именем Student, содержащую поля: «ФИ», «Номер группы»,
# «Успеваемость» (список из пяти элементов). Затем создайте список из десяти студентов
# (данные о студентах можете придумать свои или запросить их у пользователя)
# и отсортируйте его по возрастанию среднего балла. Выведите результат на экран.
class Student:
    def __init__(self, surname, name, group_number, scores):
        self.surname = surname
        self.name = name
        self.group_number = group_number
        self.score = scores


def average(lst):
    return sum(lst) / len(lst)


students = [
    Student("Иванов", "Иван", "101", [5, 4, 3, 5, 4]),
    Student("Петров", "Петр", "102", [3, 4, 4, 3, 4]),
    Student("Сидоров", "Сидор", "103", [5, 5, 5, 4, 4]),
    Student("Кузнецова", "Анна", "101", [4, 3, 4, 5, 3]),
    Student("Смирнов", "Алексей", "102", [5, 5, 4, 5, 5]),
    Student("Васильева", "Мария", "103", [3, 3, 4, 3, 4]),
    Student("Николаев", "Николай", "101", [4, 4, 4, 4, 4]),
    Student("Михайлова", "Наталья", "102", [5, 5, 5, 5, 5]),
    Student("Федоров", "Федор", "103", [3, 4, 3, 4, 3]),
    Student("Козлова", "Ольга", "101", [4, 4, 5, 4, 5])
]
students_sorted_by_score = sorted(students, key=lambda stud: average(stud.score))
for student in students_sorted_by_score:
    print('{}, {}, {}, {}'.format(student.name,
                                  student.surname, student.group_number,
                                  average(student.score)))
