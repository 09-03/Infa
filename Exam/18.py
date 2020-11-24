"""
Написать программу, которая выводит два четверостишия, сохраняя традиционное
форматирование, используемое в поэзии.
"""

file = open("18.txt")
i = 0
for line in file:
    print(line, end = "")
    i+=1
    if i == 4:
        print("\n")
    if i == 8:
        file.close()
        break
