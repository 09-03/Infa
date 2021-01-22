"""
Написать программу, получающую на вход список,
и разбивающую его на три: четные числа, нечетные числа, символы.
"""
list = input("Введите символы: ").split()
for i in range(len(list)):
    try:
        list[i] = int(list[i])
    except:
        pass
new_list=[[],[],[]]
for item in list:
    if isinstance(item, str):
        new_list[2].append(item)
    elif item % 2 == 0:
        new_list[0].append(item)
    else:
        new_list[1].append(item)
print(new_list)
