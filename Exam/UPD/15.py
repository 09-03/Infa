"""
Реализовать программу, Получающую на вход список студентов,
и сохраняющую оценку студента после экзамена:
Вход: студент1, студент2, студент3….
Поставьте оценку студенту: студент1 – 5 ….(пользователь выставляет оценку)
Вывод:
Студент1 – 5
Студент2 – 4
Студент3 – 5
….
"""
students = input("Введите студентов в формате 'Иванов.A.A' через пробел: ").split()
gradesstr =[]
gradeslist=[]
print("Поставьте оценку студенту: ")
for student in students:
    grade = input(f"{student} - ")
    gradesstr.append(f"{student} - {grade}")
    gradeslist.append([student,grade])

print("--------")
print(gradesstr)
print(gradeslist)
