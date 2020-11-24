"""
Реализовать программу, реализующую алгоритм чтения из файла и записи в файл
"""
def read(file_path, symbols):
    file = open(file_path, "r")
    print(file.read(symbols))
    file.close()

def write(file_path):
    file = open(file_path, "w")
    text = input("Введите текст на запись:")
    file.write(text)
    file.close()

read("29read.txt", None)
write("29write.txt")
