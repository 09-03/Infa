"""
Реализовать программу, получающую из файла текст и записывающую в тот же файл,
число гласных и согласных, а также общее число знаков в тексте.
"""
f = open('12.txt', 'r',encoding="UTF-8")
p = f.read()
consonants = sum(p.count(c) for c in "бвгджзклмнпрстфхцчшщqwrtpsdfghjklzxcvbnm")
vowels = sum(p.count(c) for c in "аеёиоуыэюяeyuioa")
f.close()

f = open('12.txt', 'a',encoding="UTF-8")
o1 = "Кол-во символов " + str(len(p)) + "\n"
o2 = "Гласных " + str(vowels) + "\n"
o3 = "Согласных " + str(consonants) + "\n"
f.write(o1)
f.write(o2)
f.write(o3)
f.close()
