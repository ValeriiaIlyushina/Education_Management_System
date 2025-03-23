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
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
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

def mean_all_stud(stud_list,name_course):
    stud_all=[gr_all for s in stud_list for gr_all in s.grades.get(name_course)]
    return sum(stud_all)/len(stud_all)
def mean_all_lect(lect_list,name_course):
    lect_all=[gr_all for s in lect_list for gr_all in s.grades.get(name_course)]
    return sum(lect_all)/len(lect_all)

student1 = Student('Василий','Золо','мужчина')
student1.courses_in_progress += ["Основы программирования","Git","ООП"]
student1.finished_courses += ["Java разработка"]

student2 = Student('Ирина','Пономарёва','женщина')
student2.courses_in_progress += ["Git","ООП","Внутренний баланс"]
student2.finished_courses += ["Основы программирования","Java разработка"]

lecturer1 = Lecturer('Том','Харди')
lecturer1.courses_attached += ["Git","ООП","Внутренний баланс"]
student1.rate_hw(lecturer1,"ООП",10)

lecturer2 = Lecturer('Рик','Санчез')
lecturer2.courses_attached += ["Git","ООП","Внутренний баланс","Современная философия"]
student2.rate_hw(lecturer2,"ООП",6)

reviewer1 = Reviewer('Катя','Масалова')
reviewer1.courses_attached += ["Git","ООП","Внутренний баланс","Основы программирования"]
reviewer1.rate_hw(student1,"Основы программирования",9)
reviewer1.rate_hw(student2,"Git",5)
reviewer1.rate_hw(student2,"ООП",7)

reviewer2 = Reviewer('Кристина','Балоян')
reviewer2.courses_attached += ["Git","ООП","Внутренний баланс","Основы программирования"]
reviewer2.rate_hw(student2,"Внутренний баланс",3)
reviewer2.rate_hw(student1,"ООП",5)

print(student1)
print(student1.mean_g())
print(student2)
print(student2.mean_g())
print(student1 == student2)
print(student1 < student2)
print(student1 > student2)

print(lecturer1)
print(lecturer1.mean_g())
print(lecturer2)
print(lecturer2.mean_g())
print(lecturer1 != lecturer2)
print(lecturer1 <= lecturer2)
print(lecturer1 >= lecturer2)

print(reviewer1)
print(reviewer2)

print(mean_all_stud([student1,student2],'ООП'))
print(mean_all_lect([lecturer1,lecturer2],'ООП'))