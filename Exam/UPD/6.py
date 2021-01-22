"""
написать программу, получающую на вход набор цифр,
и упорядочивающую их, причем,
программа продолжается до тех пор,
пока пользователь не ввёдёт слово “stop”.
"""

def bubbleSort(list):
    for i in range(len(list)-1):
        for j in range(0, len(list)-i-1):
            if list[j] > list[j+1] :
                list[j], list[j+1] = list[j+1], list[j]
                print(f"После смены {list[j]} и {list[j+1]} получили {list}")
                cont = input("Для продолжения введите что-угодно, для остановки введите 'stop': ")
                if cont == "stop":
                    return print(f"Сортированный список: {list}")
    return print(f"Сортированный список: {list}")

list = [int(i) for i in input("Введите список цифр через пробел: ").split()]
bubbleSort(list)
