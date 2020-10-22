def f(x):
    global y
    return eval(y.replace("x", str(x)))


def solver(a, b, epsilon):
    if f(a) * f(b) < 0:
        c = 0
        while abs(b - a) >= epsilon:
            c = (a + b) / 2
            print({a, f(a), b, f(b), c, f(c)})
            if f(c) == 0:
                return print("Ответ: x=" + str(c))
            if f(a) * f(c) < 0:
                b = c
            if f(c) * f(b) < 0:
                a = c
        return print("Ответ: x=" + str((a+b) / 2))
    else:
        print("f(a) и f(b) должны быть разных знаков")


y = input("Введите функцию: ")
a = float(input("Введите нижнюю границу a: "))
b = float(input("Введите верхнюю границу b: "))
epsilon = float(input("Введите точность epsilon: "))
solver(a, b, epsilon)
