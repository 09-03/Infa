"""
Написать программу, получающую на вход от пользователя данные о его имени,
возрасте, росте, весе, и выводящую метрику на пользователя в виде:
ФИО:
Возраст:
Пол:
Рост:
Вес:
BMI:
"""

def metric(user_data):
    print(f"ФИО: {user_data[0]} {user_data[1]} {user_data[2]}")
    print(f"Возраст: {user_data[3]}")
    print(f"Пол: {user_data[4]}")
    print(f"Рост: {user_data[5]} см")
    print(f"Вес: {user_data[6]} кг")
    print(f"BMI: " + str(int(user_data[6])/((int(user_data[5])/100) **2 )))

user_data = input("Введите своё ФИО, Возраст, Пол (M/F), Рост (см), Вес (кг) через пробел:  ").split()
print(user_data)
metric(user_data)
