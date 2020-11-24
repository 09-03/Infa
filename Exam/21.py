"""
Написать программу, реализующую алгоритм с двумя вложенными условиями.
"""

def greeting(time):
    if time < 0 or time > 24:
        return print("Ошибка")
    if time >= 6:
        if time <= 10:
            return print("Доброе утро")
        if time <= 17:
            return print("Добрый день")
        return print("Добрый вечер")
    else:
        print("Доброй Ночи")
time = int(input("Введите час: "))
greeting(time)
