# Задаём функцию, которую будем интегрировать (лень делать распознование по вводу)
def f(x):
    y = 2 * x + 1
    return y
n = 0
dx = float(input("Введите величину dx (Точность вычисления): "))
a = float(input("Введите нижнюю границу интегрирования: "))
b = float(input("Введите верхнюю границу интегрирования: "))
S = 0
# Будем находить интеграл как сумму площадей прямоугольников со стороной dx (чем меньше, тем точнее) и значением функции в точке a+n*dx
while (a + n * dx) < b:
    S += dx * f(a + n * dx)
    n += 1
print(S)
