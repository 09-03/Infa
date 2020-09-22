# Создание функции готового массива ввиде пирамиды
def vivod():
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print()

# Основная функция создания числовой пирамиды
def triangle(y):
    z = 0
    p = 0
    q = 0
    for x in range(y):
        # Заполнение левой грани треугольника
        for i in range(0 + z, n - 1 - z):
            a[i + 1][n - i + z - 2] = a[i][n - i + z - 1] + 1
        z += 1
        # Заполнение нижней грани 
        for i in range(0 + p, 2 * n - 2 - 3 * p):
            a[n - 1 - p][i + 1 + p] = a[n - 1 - p][i + p] + 1
        p += 1
        # Заполнение правой грани 
        for i in range(0 + q, n - 2 - q):
            a[n - 2 - i][2 * n - 3 - i - q] = a[n - 1 - i][2 * n - 2 - i - q] + 1
        q += 1
        # Заполнение последнего (на конечном этапе центрального) числа в треугольнике
        if (n != 1) and (n != 2):
            a[n - 2 - i][n - 1] = a[n - 2 - i][n] + 1

# Замена всех нулей в массиве на пробелы для корректного изображения пирамиды
def zamena():
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 0:
                a[i][j] = " "


start = input("Запустить программу? Чтобы продолжить введите 'y'; для выхода - любую клавишу: ")
while start == "y":
    n = int(input("Кол-во строк: "))
    if n > 0:
        a = [[0] * (2 * n - 1) for i in range(n)]
        a[0][n - 1] = 1
        triangle(n // 2)
        zamena()
        vivod()
        start = input("Запустить программу еще раз? Чтобы продолжить введите 'y'; для выхода - любую клавишу: ")
    else:
        print("ERROR: Количество строк введено неправильно")
        start = input("Запустить программу еще раз? Чтобы продолжить введите 'y'; для выхода - любую клавишу: ")
