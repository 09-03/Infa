"""
Написать программу, упорядочивающую список по возрастанию или по убыванию, без
использования встроенных функций.
"""

def bubbleSort(list):
    for i in range(len(list)-1):
        for j in range(0, len(list)-i-1):
            if list[j] > list[j+1] :
                list[j], list[j+1] = list[j+1], list[j]
    return print(f"Сортированный список: {list}")

def inversebubbleSort(list):
    for i in range(len(list)-1):
        for j in range(0, len(list)-i-1):
            if list[j] < list[j+1] :
                list[j], list[j+1] = list[j+1], list[j]
    return print(f"Сортированный список: {list}")

list = [int(i) for i in input("Введите список чисел через пробел: ").split()]
order = input("В каком порядке сортировать (по возрастанию - a, по убыванию - d)? ")
if order == "a":
    bubbleSort(list)
elif order == "d":
    inversebubbleSort(list)
else:
    print("Ошибка")
