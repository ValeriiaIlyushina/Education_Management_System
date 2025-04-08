# Программа: "Education Management System"
Назначение:
+ Система для управления учебным процессом с функциями:

+ Наследование преподавателей (лекторы/проверяющие)

+ Выставление оценок студентам и лекторам

+ Расчёт средних оценок

+ Сравнение успеваемости через перегруженные операторы

1. Архитектура классов
Базовый класс Mentor

Дочерние классы
+ Lecturer (лектор):

+ Reviewer (проверяющий):

класс Student

2. Полиморфизм и магические методы
Перегрузка __str__ и __lt__, __gt__ для сравнения

3. Функции для статистики

4. Технологии и требования  
Язык: Python 3.7+  
Дополнительно: pytest (для тестов)

Диаграмма классов
>
    Mentor <|-- Lecturer  
    Mentor <|-- Reviewer  
    Student --> Lecturer : Оценивает лекции  
    Reviewer --> Student : Проверяет ДЗ  
>
