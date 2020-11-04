from tkinter import *
import random
import math


def GrahamScan(stick_list):
    stick_list.sort()
    L_upper = [stick_list[0], stick_list[1]]
    for i in range(2,len(stick_list)):
        L_upper.append(stick_list[i])
        while len(L_upper) > 2 and not RightTurn(L_upper[-1],L_upper[-2],L_upper[-3]):
            del L_upper[-2]
    L_lower = [stick_list[-1], stick_list[-2]]
    for i in range(len(stick_list)-3,-1,-1):
        L_lower.append(stick_list[i])
        while len(L_lower) > 2 and not RightTurn(L_lower[-1],L_lower[-2],L_lower[-3]):
            del L_lower[-2] 
    del L_lower[0]
    del L_lower[-1]
    L = L_upper + L_lower
    return L


def RightTurn(p1, p2, p3):
    if (p3[1]-p1[1])*(p2[0]-p1[0]) >= (p2[1]-p1[1])*(p3[0]-p1[0]):
        return False
    return True


def convex_hull(stick_list):
    convex_hull_area = 0
    if len(stick_list) < 3:
        return convex_hull_area
    points_set = GrahamScan(stick_list)
    for n in range(len(points_set)):
        if n == len(points_set)-1:
            convex_hull_area += int((points_set[n][0]*points_set[0][1]-
                                 points_set[n][1]*points_set[0][0])/2)
            
            canvas.create_line(points_set[n][0], points_set[n][1],
                               points_set[0][0], points_set[0][1], width = 2, fill = "blue")
            
            return abs(convex_hull_area)
        else:
            convex_hull_area += int((points_set[n][0]*points_set[n+1][1]-
                                 points_set[n][1]*points_set[n+1][0])/2)
            
            canvas.create_line(points_set[n][0], points_set[n][1],
                               points_set[n+1][0], points_set[n+1][1], width = 2, fill = "blue")

N = 5
stick_list = []
root = Tk()
canvas = Canvas(root, width = N*100+30 , height = N*100+30, bg = "grey")
canvas.pack()

for i in range(N+1):
    for j in range(N+1):
        oval = canvas.create_oval(10+j*100,10+i*100,
                                  20+j*100,20+i*100,
                                  width=2,fill="white")
        if random.randint(1,N+1) == 1:
            canvas.itemconfig(oval, fill="green")
            x = 15+j*100
            y =15+i*100
            stick_list.append((x, y))
print(convex_hull(stick_list)/10000)
root.mainloop()
