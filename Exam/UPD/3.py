"""
Написать программу, принимающую на вход от пользователя два числа, и
реализующую с ними все встроенные арифметические операции.
"""

def add(a,b):
    return print(f"Сумма {a} и {b}: {a+b}")
def subtract(a,b):
    return print(f"Разность {a} и {b}: {a-b}")
def multiply(a,b):
    return print(f"Произведение {a} и {b}: {a*b}")
def division(a,b):
    return print(f"Результат деления {a} на {b}: {a/b}")
def exp(a,b):
    return print(f"{a} в степени {b}: {a**b}")
def root(a,b):
    return print(f"Корень {b} степени из {a}: {a**(1/b)}")

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
add(a,b)
subtract(a,b)
multiply(a,b)
division(a,b)
exp(a,b)
root(a,b)
