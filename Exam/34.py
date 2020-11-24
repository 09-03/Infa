"""
Написать программу, получающую на вход сумму, срок и ставку кредита и выдающую
на выходе размер аннуитетного платежа
"""

def annuity_payment(credit_sum, duration, percent):
    annuity_coef = ((percent/1200)*((1+percent/1200)**duration))/(((1+percent/1200)**duration)-1)
    payment = credit_sum * annuity_coef
    return print(f"Аннуитетный платеж: {payment}")

cs = int(input("Введите сумму кредита: "))
d = int(input("Введите срок кредита (в месяцах): "))
p = int(input("Введите ставку кредита (N%-годовых): "))
annuity_payment(cs, d, p)
