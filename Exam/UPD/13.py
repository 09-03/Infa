"""
Написать программу, переводящую любое число из десятичной системы
в систему с произвольным основанием.
"""
def convert(n):
    base = int(input("Выберете основание: "))
    if base>10:
        return decToHigh(n,base)
    converted = ''

    while n > 0:
        converted = str(n % base) + converted
        n //= base

    return print(converted)

def decToHigh(dec_value,base):
    ret_val = str()
    while dec_value > 0:
        hex_value=dec_value%base
        dec_value=dec_value//base
        ret_val = getHighChar(hex_value) + ret_val
    return print(ret_val)

def getHighChar(dec_digit):
    if dec_digit < 10:
        return str(dec_digit)
    if dec_digit == 10:
        return "A"
    if dec_digit == 11:
        return "B"
    if dec_digit == 12:
        return "C"
    if dec_digit == 13:
        return "D"
    if dec_digit == 14:
        return "E"
    if dec_digit == 15:
        return "F"

n = int(input("Введите число для перевода:" ))
convert(n)
