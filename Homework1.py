class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def mean_g(self):
        if len(self.grades) > 0:
            all_g=[n for i in self.grades.values() for n in i]
            mean = sum(all_g)/len(all_g)
            return mean
        else:
            return "оценок пока нет"

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in mentor.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.mean_g()}' \
               f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗаверщённые курсы: {", ".join(self.finished_courses)}'

    def __eq__(self, other):
        return self.mean_g() == other.mean_g()

    def __lt__(self, other):
        return self.mean_g() < other.mean_g()

    def __ne__(self, other):
        return self.mean_g() != other.mean_g()

    def __le__(self, other):
        return self.mean_g() <= other.mean_g()

    def __gt__(self, other):
        return self.mean_g() > other.mean_g()

    def __ge__(self, other):
        return self.mean_g() >= other.mean_g()

class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname,):
        super().__init__(name,surname)
        self.grades = {}

    def mean_g(self):
        if len(self.grades) > 0:
            all_g = [n for i in self.grades.values() for n in i]
            mean = sum(all_g) / len(all_g)
            return mean
        else:
            return "Оценок пока нет"

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{self.mean_g()}'

    def __eq__(self, other):
        return self.mean_g() == other.mean_g()

    def __lt__(self, other):
        return self.mean_g() < other.mean_g()

    def __ne__(self, other):
        return self.mean_g() != other.mean_g()

    def __le__(self, other):
        return self.mean_g() <= other.mean_g()

    def __gt__(self, other):
        return self.mean_g() > other.mean_g()

    def __ge__(self, other):
        return self.mean_g() >= other.mean_g()


class Reviewer(Mentor):

    def __init__(self, name, surname,):
        super().__init__(name,surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'