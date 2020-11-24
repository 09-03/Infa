"""
Написать программу, упорядочивающую список по возрастанию(убыванию), и
переворачивающую в обратном порядке.
"""

def sorting(list, order):
    list.sort(reverse = order)
    print(f"Сортированный список: {list}")
    if order:
        order = False
    else:
        order = True
    list.sort(reverse = order)
    print(f"Перевернутый список список: {list}")

list = [int(i) for i in input("Введите список чисел через пробел: ").split()]
order = input("В каком порядке сортировать (по возрастанию - a, по убыванию - d)? ")
if order == "a":
    sorting(list, False)
elif order == "d":
    sorting(list, True)
else:
    print("Ошибка")
