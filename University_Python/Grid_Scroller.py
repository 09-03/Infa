from tkinter import *
import random


def click(x):
    global element, length
    entry = entry_box.get().lower().replace(" ", "")
    text_func = entry.replace("x", str(x))

    if text_func == "":
        return print("Не введена функция\n--------------------")

    for item in text_func:
        if item not in symbols:
            return print("Использованы неверные символы\n--------------------")

    try:
        solution = eval(text_func)
    except:
        return print("Неправильный формат ввода\n--------------------")

    print(f"f(x)={entry}")
    if solution > 0:
        if element == length - 1:
            print(f"f({x})={solution}\nСтарый индекс {element} Новый индекс 0\n--------------------")
            element = 0
        else:
            print(f"f({x})={solution}\nСтарый индекс {element} Новый индекс {element+1}\n--------------------")
            element += 1

    elif solution < 0:
        if element == 0:
            print(f"f({x})={solution}\nСтарый индекс {element} Новый индекс {length - 1}\n--------------------")
            element = length - 1
        else:
            print(f"f({x})={solution}\nСтарый индекс {element} Новый индекс {element-1}\n--------------------")
            element -= 1

    else:
        print("Достигнут ноль\n--------------------")

    color_update(element, length)


def clear():
    entry_box.delete(0, END)


def color_update(element, length):
    for i in range(length):
        if i == element:
            cell_label_list[i].config(fg="green")
        else:
            cell_label_list[i].config(fg="blue")

    root.update()


symbols = {"%", "*", "(", ")", "-", "+", ".", "/", "x",
           "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

cell_label_list=[]
element = 0
valid_length, valid_a, valid_b = False, False, False

while not valid_length:
    valid_length = True
    try:
        length = int(input("Введите количество элементов: "))
        if length <= 0:
            print("--------------------\nВведено неположительное значение\n--------------------")
            valid_length = False

    except:
        print("--------------------\nВведено неправильное значение\n--------------------")
        valid_length = False

while not valid_a:
    valid_a = True
    try:
        a = int(input("--------------------\nВведите минимально возможный элемент: "))
    except:
        print("--------------------\nВведено неправильное значение")
        valid_a = False

while not valid_b:
    valid_b = True
    try:
        b = int(input("--------------------\nВведите максимально возможный элемент: "))
        if b < a:
            print(f"--------------------\nВведено число b ({b}), меньшее числа a ({a})")
            valid_b = False

    except:
        print("--------------------\nВведено неправильное значение")
        valid_b = False

print("--------------------")

root = Tk()
root.title("Grid Scroller")
entry_box = Entry()
button_func = Button(text="Ввод",command = lambda: click(cell_label_list[element].cget("text")))
button_clear = Button(text="Очистить", command = clear)

for i in range(length//10 + 1):
    if i == length//10:
        for j in range(length % 10):
            if i == 0 and j == 0:
                cell = Label(text=random.randint(a,b), fg = "green")
            else:
                cell = Label(text=random.randint(a,b), fg = "blue")

            cell_label_list.append(cell)
            cell_label_list[i*10+j].grid(row=i, column=j,padx = 30, pady = 30)

    else:
        for j in range(10):
            if i == 0 and j == 0:
                cell = Label(text=random.randint(a,b), fg = "green")
            else:
                cell = Label(text=random.randint(a,b), fg = "blue")

            cell_label_list.append(cell)
            cell_label_list[i*10+j].grid(row=i, column=j,padx = 30, pady = 30)

if length < 10:
    if length % 2 == 0:
        entry_box.grid(row = 1, column = int(length/2-1), columnspan = 2)
        button_func.grid(row = 2, column = int(length/2-1), columnspan = 2)
        button_clear.grid(row = 3, column = int(length/2-1), columnspan = 2)
    else:
        entry_box.grid(row = 1, column = int(length/2))
        button_func.grid(row = 2, column = int(length/2))
        button_clear.grid(row = 3, column = int(length/2))

else:
    entry_box.grid(row=length//10 + 1, column = 4, columnspan = 2)
    button_func.grid(row=length//10 + 2, column = 4, columnspan = 2)
    button_clear.grid(row=length//10 + 3, column = 4, columnspan = 2)

root.mainloop()
