"""
Реализовать программу, реализующую действия со списками: добавление и удаление
элементов, упорядочивание, определение длины списка, вставку элемента, определение
индекса и др.
"""

def add(list,element):
    list.append(element)
    return print(f"Список после добавления элемента {element}: {list}")

def delete(list,element):
    list.remove(element)
    return print(f"Список после удаления элемента {element}: {list}")

def bubbleSort(list):
    for i in range(len(list)-1):
        for j in range(0, len(list)-i-1):
            if list[j] > list[j+1] :
                list[j], list[j+1] = list[j+1], list[j]
    return print(f"Сортированный список: {list}")

def lenth(list):
    return print(f"Длина списка: {len(list)}")

def insert(list, element):
    index = int(input("Введите индекс вставки: "))
    list.insert(index, element)
    return print(f"Список после вставки элемента: {list}")

def find_index(list, element):
    return print(f"Элемент {element} имеет индекс: {list.index(element)}")


massive = [25 ,-6, 6, 6, 0, 11, 20, 1]

add(massive.copy(), "a")
delete(massive.copy(), 0)
bubbleSort(massive.copy())
lenth(massive.copy())
insert(massive.copy(), "b")
find_index(massive.copy(), -6)
