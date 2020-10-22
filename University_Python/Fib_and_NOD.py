def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


def fib_series(n):
    for num in range(n):
        if num == n-1:
            print(fib(num))
        else:
            print(fib(num), end = " ")

def NOD(a,b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a+b

print(fib(6))
fib_series(10)
print(NOD(12,42))
