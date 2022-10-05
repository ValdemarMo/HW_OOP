class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def grade_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка добавления'

    def mid_grade(self):
        r1 = sum(self.grades.values(),[])
        r2 = (sum(r1) / len(r1))
        return r2

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.mid_grade() < other.mid_grade()
        else:
            return 'Сравнение невозможно'

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname} \n' \
               f'Средняя оценка за домашние задания: {round(self.mid_grade(),2)}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def mid_grade(self):
        r1 = sum(self.grades.values(),[])
        r2 = (sum(r1) / len(r1))
        return r2

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.mid_grade() < other.mid_grade()
        else:
            return 'Сравнение невозможно'

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname} \n' \
               f'Средняя оценка за лекции: {round(self.mid_grade(),2)}'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def grade_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка добавления'

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}'

################################################################
#Полевые испытания
student_1 = Student('Archie', 'Fisher', 'your_gender')
student_1.finished_courses += ['Git']
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Введение в программирование']
student_1.grades['Git'] = [10, 10, 10, 7, 10]
student_1.grades['Python'] = [10, 10]
student_1.grades['Введение в программирование'] = [1, 10]

student_2 = Student('Bert', 'Jansch', 'your_gender')
student_2.finished_courses += ['Git']
student_2.courses_in_progress += ['Python']
student_2.grades['Git'] = [8, 7, 9, 5, 10]
student_2.grades['Python'] = [7, 8]

lecturer_1 = Lecturer('Patti', 'Smith')
lecturer_1.courses_attached = ['Python']
lecturer_1.grades['Python'] = [10, 8, 1, 3]

lecturer_2 = Lecturer('Siouxsie', 'Sioux')
lecturer_2.courses_attached = ['Git']
lecturer_2.grades['Git'] = [10, 10, 9]

lecturer_3 = Lecturer('Lee', 'Wiley')
lecturer_3.courses_attached = ['Git']
lecturer_3.grades['Git'] = [8, 9, 1, 3, 2, 4]

reviewer_1 = Reviewer('John', 'Cale')
reviewer_1.courses_attached = ['Git']

reviewer_2 = Reviewer('Daisy', 'Chainsaw')
reviewer_2.courses_attached = ['Python']

#тестирование перезагрузки магических методов
print(f'\nтестирование стандартного вывода (Задание № 3.1)\n')
print(f'Cтудент: \n\n{student_1}\n')
print(f'Лектор: \n\n{lecturer_1}\n')
print(f'Проверяющий: \n\n{reviewer_2}\n')
print(f'{"_" * 12}')

#тестирование операторов сравнения
print(f'\nтестирование операторов сравнения (Задание № 3.2)\n')
print(f'{student_1 < student_2} - ({round(student_1.mid_grade(),2)} <  {round(student_2.mid_grade(),2)} )')
print(f'{lecturer_1 < lecturer_2} - ({round(lecturer_1.mid_grade(),2)} <  {round(lecturer_2.mid_grade(),2)} )')
print(f'{lecturer_1 < reviewer_1} - (лектор и проверяющий) ')
print(f'{student_1 < reviewer_1} - (студент и проверяющий)')
print(f'{"_" * 12}')

#тестирование реализации методов выставления оценок
print(f'\nтестирование реализации методов добавления оценок (Задание № 2)\n')
print(f"{reviewer_2.grade_hw(student_1, 'Python', 3)} - (ошибки нет, оценка добавлена)") #условия добавления оценки должны выполняться
print(reviewer_2.grade_hw(student_1, 'Git', 3)) #ошибка
print(student_1.grade_lect(reviewer_2, 'Git', 3)) #ошибка
print(f"{student_1.grade_lect(lecturer_1, 'Python', 3)} - (ошибки нет, оценка добавлена)") #условия добавления оценки должны выполняться
print(student_1.grade_lect(lecturer_1, 'Git', 3)) #ошибка
print(student_1.grade_lect(lecturer_1, 'Введение в программирование', '1')) #ошибка

#тестирование надлежащего добавления новых оценок (изменение средних)
print(f'\nв результате средние оценки изменились:\n')
print(f'Cтудент: \n\n{student_1}\n')
print(f'Лектор: \n\n{lecturer_1}\n')
print(f'{"_" * 12}')

#Заданиt № 4 (средние оценки для каждого курса для студенов и лекторов)

def mid_grade_course(list, course):
    mid_grade = 0
    r = []
    for x in list:
        if eval(x).grades.get(course):
            r += eval(x).grades.get(course)
    if len(r) != 0:
        mid_grade = sum(r) / len(r)
    return mid_grade

print(f'\nЗадание № 4.1:\n')
student_list = ['student_1', 'student_2']

print(f'средние оценки по ДЗ для всех студенов\n')
print(f"курса Git - {round(mid_grade_course(student_list, 'Git'),2)}")
print(f"курса Python - {round(mid_grade_course(student_list, 'Python'),2)}")
print(f"курса Введение в программирование - {round(mid_grade_course(student_list, 'Введение в программирование'),2)}")

print(f'\nЗадание № 4.2:\n')
lecturers_list = ['lecturer_1', 'lecturer_2', 'lecturer_3']

print(f'средние оценки по лекциям для всех лекторов\n')
print(f"курса Git - {round(mid_grade_course(lecturers_list, 'Git'),2)}")
print(f"курса Python - {round(mid_grade_course(lecturers_list, 'Python'),2)}")
print(f"курса Введение в программирование - {round(mid_grade_course(lecturers_list, 'Введение в программирование'),2)}")

# course_list = ['Git', 'Python', 'Введение в программирование']


