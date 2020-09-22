# В данном варианте испольуется библиотека tkinter для отображение окна приложения
from tkinter import *
# Функция для определения отступа для новой пирамиды (участка ёлки)
def l(x):
    return int(0.5 * x ** 2 + 2.5 * x + 2)
# Функция для составления пирамид из прошлой программы (Pyramid)
# Вообще можно было сослаться на этот файл если он у вас находиться в одной папке (from Pyramid import triangle), и тогда данный кусок не нужен
def triangle(y):
    z = 0
    p = 0
    q = 0
    for x in range(y):
        for i in range(0 + z, n - 1 - z):
            a[i + 1][n - i + z - 2] = a[i][n - i + z - 1] + 1
        z += 1
        for i in range(0 + p, 2 * n - 2 - 3 * p):
            a[n - 1 - p][i + 1 + p] = a[n - 1 - p][i + p] + 1
        p += 1
        for i in range(0 + q, n - 2 - q):
            a[n - 2 - i][2 * n - 3 - i - q] = a[n - 1 - i][2 * n - 2 - i - q] + 1
        q += 1
        if (n != 1) and (n != 2):
            a[n - 2 - i][n - 1] = a[n - 2 - i][n] + 1

start = input("Запустить программу? Чтобы продолжить введите 'y'; для выхода - любую клавишу: ")
while start == "y":
    s = int(input("Кол-во Слоёв Ёлки: "))
    if s <= 0:
        print("Error: Введено неправильное число слоёв")
    root = Tk()
    root.title("Ёлочка")
    n = 2
    for k in range(s):
        a = []
        a = [[0] * (2 * n - 1) for i in range(n)]
        a[0][n - 1] = 1
        triangle(n // 2)
        for i in range(n):
            for j in range(len(a[i])):
                if a[i][j] != 0:
                    cell = Label(root, text=a[i][j]).grid(row=i+l(k), column=j+s-k)
        n += 1
    start = input("Запустить программу еще раз? Чтобы продолжить введите 'y'; для выхода - любую клавишу: ")
    root.destroy()
