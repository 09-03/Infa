"""
Написать программу, переводящую вводимое с клавиатуры число секунд в формат:
дни, часы:минуты:секунды.
"""

def convert(seconds):
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    day, hour = divmod(hour, 24)
    return "%d, %d:%02d:%02d" % (day, hour, min, sec)

n = int(input("Введите количество секунд: "))
print(convert(n))
