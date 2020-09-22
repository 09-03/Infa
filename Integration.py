def f(x):
    y = 2 * x + 1
    return y

n = 0
dx = float(input("Введите величину dx (Точность вычисления): "))
a = float(input("Введите нижнюю границу интегрирования: "))
b = float(input("Введите верхнюю границу интегрирования: "))
S = 0

while (a + n * dx) < b:
    S += dx * f(a + n * dx)
    n += 1

print(S)
