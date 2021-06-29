import tkinter as tk
from tkinter import filedialog
import imghdr
from PIL import Image, ImageTk


def open_action():
    global raw_image, raw_img_widget, file
    filename = filedialog.askopenfilename(initialdir = "/", title = "Выберите файл")
    file.destroy()
    file = tk.Label(frame, text = f"Выбранный Файл: {filename}", fg = "#FFFFFF", bg= "#263D42")
    file.grid(row = 2, column = 0, columnspan = 3)
    raw_image = Image.open(filename)
    image = raw_image.copy().resize((300,300))
    photo = ImageTk.PhotoImage(image)
    raw_img_widget.destroy()
    raw_img_widget = tk.Label(frame, image = photo)
    raw_img_widget.image = photo
    raw_img_widget.grid(row = 0, column = 0)



def run_action():
    global grey_img_widget, bin_img_widget, grey_image, bin_image, stats
    threshold = slider.get()
    grey_image = raw_image.convert("L")
    bin_image = grey_image.copy()

    image = grey_image.copy().resize((300,300))
    photo = ImageTk.PhotoImage(image)
    grey_img_widget.destroy()
    grey_img_widget = tk.Label(frame, image = photo)
    grey_img_widget.image = photo
    grey_img_widget.grid(row = 0, column = 1)

    pixel = bin_image.load()
    white = 0
    black = 0
    for row in range(bin_image.size[0]):
      for column in range(bin_image.size[1]):
        if pixel[row, column] < threshold:
          pixel[row, column] = 0
          black += 1
        else:
          pixel[row, column] = 255
          white += 1

    image = bin_image.copy().resize((300,300))
    photo = ImageTk.PhotoImage(image)
    bin_img_widget.destroy()
    bin_img_widget = tk.Label(frame, image = photo)
    bin_img_widget.image = photo
    bin_img_widget.grid(row = 0, column = 2)

    stats.destroy()
    stats = tk.Label(frame, text = f"Размер изображения {raw_image.size[0]} на {raw_image.size[1]} пикселей\nУровень отсечки - {slider.get()}\nБелые пиксели - {white}\nЧерные пиксели - {black}\nПроцент затененности - {round(black * 100 / (white + black), 4)}%", fg = "#FFFFFF", bg= "#263D42")
    stats.grid(row = 3, column = 0, columnspan = 3)


def save_action():
    savefile = filedialog.askdirectory(initialdir = "/", title = "Выберите папку для сохранения")
    orig_path = file.cget("text").replace("Выбранный Файл: ", "")
    format = imghdr.what(orig_path)
    grey_image.save(f"{savefile}/grey_img.{format}")
    bin_image.save(f"{savefile}/bin_img.{format}")


root = tk.Tk()
root.title("Расчет Затененности")
root.configure(background='#263D42')
canvas = tk.Canvas(root)
canvas.pack()
frame = tk.Frame(canvas, bg = "#263D42")
frame.pack()

raw_img_widget = tk.Label(frame, bg = "#777777", width = 50, height = 20)

grey_img_widget = tk.Label(frame, bg = "#777777", width = 50, height = 20)

bin_img_widget = tk.Label(frame, bg = "#777777", width = 50, height = 20)

file = tk.Label(frame, text = "Файл не выбран", fg = "#FFFFFF", bg= "#263D42")

stats = tk.Label(frame, text = "Ожидание обработки", fg = "#FFFFFF", bg= "#263D42")

open_button = tk.Button(frame, text = "Открыть файл", fg = "#FFFFFF", bg= "#263D42",
                        width = 50, height = 2,
                        command = open_action)

run_button = tk.Button(frame, text = "Обработать", fg = "#FFFFFF", bg= "#263D42",
                        width = 50, height = 2,
                        command = run_action)

save_button = tk.Button(frame, text = "Сохранить", fg = "#FFFFFF", bg= "#263D42",
                        width = 50, height = 2,
                        command = save_action)

slider = tk.Scale(frame, from_= 0, to = 255, troughcolor = "#263D42", bg = "#FFFFFF", orient = "horizontal", length=1000, tickinterval=8, resolution=1)

raw_img_widget.grid(row = 0, column = 0)
grey_img_widget.grid(row = 0, column = 1)
bin_img_widget.grid(row = 0, column = 2)
open_button.grid(row = 1, column = 0)
run_button.grid(row = 1, column = 1)
save_button.grid(row = 1, column = 2)
file.grid(row = 2, column = 0, columnspan = 3)
stats.grid(row = 3, column = 0, columnspan = 3)
slider.grid(row = 4, column = 0, columnspan = 3)

root.mainloop()
