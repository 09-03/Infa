"""
Написать программу, которая объединяет и выводит текст из двух внешних файлов,
предварительно проверив не совпадает ли он.
"""
import filecmp
if filecmp.cmp("1.1.txt","1.2.txt"):
    print("Контент совпадает")
else:
    print("Контент не совпадает")

f1 = open("1.1.txt", 'a+', encoding="utf-8")
f2 = open("1.2.txt", 'r', encoding="utf-8")
f1.write(f2.read())
f1.close()
f2.close()

f1 = open("1.1.txt", 'r', encoding="utf-8")
for line in f1:
    print(line, end = "")
f1.close()
