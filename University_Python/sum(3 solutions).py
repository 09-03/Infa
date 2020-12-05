"""
Разработка алгоритма, обнаруживающего в массиве все пары целых чисел,
сумма которых равна заданному значению.
Эту задачу можно решить двумя способами.
Выбор определяется компромиссом между эффективностью использования времени, памяти или сложностью кода.
Решить двумя способами
"""
from random import randint


massive = [randint(0,10) for i in range(20)]
c = int(input("Заданное число C: "))

def d_code(massive, c): # Итого O(n) + O(n) + O(n) = O(n)
    massive = list(set(massive)) # O(n)
    num_dict = {}
    for num in massive: # O(n)
        if num not in num_dict:
            num_dict[num] = num

    for num in massive: # O(n)
        if c-num in num_dict:
            print(f"{num} + {num_dict[c-num]} = {c}")
            del num_dict[num]


def s_code(massive, c): # Итого O(n) + O(n) + O(n^2) = O(n^2)
    if c % 2 == 0 and massive.count(c/2) > 1: # O(n)
        print(f"{int(c/2)} + {int(c/2)} = {c}")

    massive = list(set(massive)) # O(n)
    for i in range(len(massive)):  # O(n^2) (Если быть точным, то O(0.5n^2 - n/2))
        for j in range(1, len(massive)-i):
            if massive[i] + massive[j+i] == c:
                print(f"{massive[i]} + {massive[j+i]} = {c}")


def e_code(massive, c): # Итого O(n) + O(n) + O(nlogn) + O(n) = O(nlogn)
    if c % 2 == 0 and massive.count(c/2) > 1: # O(n)
        print(f"{int(c/2)} + {int(c/2)} = {c}")

    massive = list(set(massive)) # O(n)
    massive.sort() # O(nlogn)
    i = 0
    j = len(massive) - 1
    while i < j: # O(n) (Если быть точным, то O(3(n-1)))
        sum = massive[i] + massive[j]
        if sum == c:
            print(f"{massive[i]} + {massive[j]} = {c}")
            i+=1
            j-=1
        elif sum < c:
            i+=1
        else:
            j-=1

print(massive)
s_code(massive, c)
print("---------------")
print(massive)
e_code(massive, c)
print("---------------")
print(massive)
d_code(massive, c)
