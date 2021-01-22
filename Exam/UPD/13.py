"""
Написать программу, переводящую любое число из десятичной системы
в систему с произвольным основанием.
"""
def convert(n):
    base = int(input("Выберете основание от 2 до 9: "))
    if not(2 <= base <= 9):
        return print("Неправильно основание")
    converted = ''

    while n > 0:
        converted = str(n % base) + converted
        n //= base

    return print(converted)
n = int(input("Введите число для перевода:" ))
convert(n)
