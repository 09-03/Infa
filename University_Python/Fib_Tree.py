from tkinter import *


class Tree():
    def __init__(self, level, height, x, y, level_factor):
        self.level = level
        self.height = height
        self.x = x
        self.y = y
        self.level_factor = level_factor
        self.factor = self.height * self.level_factor * self.level
        self.ancestor()


    def ancestor(self):
        if self.level == 1:
            self.draw_node(self.x, self.y)

        elif self.level == 2:
            canvas.create_line(self.x, self.y,
                               self.x-self.factor, self.y+self.height,
                               width = 2, fill = "black")

            self.draw_node(self.x, self.y)
            self.draw_node(self.x-self.factor, self.y+self.height)

        elif self.level > 2:
            L_tree = Tree(self.level-1, self.height, self.x-self.factor, self.y + self.height, self.level_factor)
            canvas.create_line(self.x, self.y,
                               self.x-self.factor, self.y+self.height,
                               width = 2, fill = "black")

            L_tree.draw_node(L_tree.x, L_tree.y)

            R_tree = Tree(self.level-2, self.height, self.x+self.factor, self.y + self.height, self.level_factor)
            canvas.create_line(self.x, self.y,
                               self.x+self.factor, self.y+self.height,
                               width = 2, fill = "black")

            R_tree.draw_node(R_tree.x, R_tree.y)
        else:
            print("Невозможно построить далее")


    def draw_node(self,x,y):
        canvas.create_oval(-10 + x, -10 + y,
                            10 + x, 10 + y,
                            width = 2,
                            fill = "red")


root = Tk()
w = 1200
h = 800
canvas = Canvas(root, width = w , height = h, bg = "white")
canvas.pack()
tree = Tree(7,75, 3*w/5, 20, 0.3)
tree.draw_node(tree.x, tree.y)
root.mainloop()
