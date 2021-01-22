"""
Написать программу вычисляющую наименьшее общее кратное двух чисел,
введённых с клавиатуры.
"""

def NOD(a,b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a+b

def NOK(a,b):
    return print(f"НОК {a} и {b}: {int(a*b/NOD(a,b))}")
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
NOK(a,b)
