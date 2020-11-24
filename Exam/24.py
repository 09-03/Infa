"""
Реализовать программу, способную находить наибольший и наименьший элемент в
списке и менять их местами. Список задается с клавиатуры
"""

list = [int(i) for i in input("Введите список чисел через пробел: ").split()]
max_value = max(list)
min_value = min(list)
for n in range(len(list)):
    if list[n] == min_value:
        list[n] = max_value
    elif list[n] == max_value:
        list[n] = min_value
print(f"Новый список: {list}")
