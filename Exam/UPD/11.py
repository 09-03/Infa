"""
Написать программу, вычисляющую наибольший общий делитель двух чисел,
введённых с клавиатуры.
"""

def NOD(a,b):
    a_start = a
    b_start = b
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return print(f"НОД {a_start} и {b_start}: {a+b}")

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
NOD(a,b)
