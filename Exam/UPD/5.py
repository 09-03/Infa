"""
Написать программу, проверяющую является ли введённая пользователем строка палиндромом.
"""

def pal(text):
    for char in range(len(text)//2):
        if text[char]!=text[len(text)-1-char]:
            return print("Не палиндром")
    return print("Палиндром")

text = input("Введите строку для анализа: ")
pal(text)
