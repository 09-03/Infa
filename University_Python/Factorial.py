# Функция Факториала
def P(n):
    if n == 0:
        return 1
    elif n < 0:
        return "Введено отрицательное число"
    return P(n-1) * n
# Функция Размещений
def A(n, k):
    if n >= k:
        return P(n) / P(n - k)
    return "Error: n должно быть больше k"
# Функция Сочетаний
def C(n,k):
    if n >= k:
        return A(n, k) / P(k)
    return "Error: n должно быть больше k"
