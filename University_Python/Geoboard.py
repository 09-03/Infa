from tkinter import *
import random
import math

"""
Если сможете написать триангуляцию точек, 
неиспользую этих библиотек, то отпишите мне
"""
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
import numpy as np
 
N = 10
stick_list = []
S = 0
polygon_area = 0
num_test = 100

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
            stick_list.append([x, y])
            
def polygons(stick_list):
    S = 0
    polygon_area = 0
    if len(stick_list)<3:
        return S , 0, 0
    points = np.array(stick_list)
    try:
        triangles = Delaunay(points)
    except:
        return S, 0, 0
    for polygon in points[triangles.simplices]:
        for n in range(len(polygon)):
            if n == len(polygon)-1:
                polygon_area += (polygon[n][0]*polygon[0][1]- polygon[n][1]*polygon[0][0])/2
                S+=abs(polygon_area)
                polygon_area = 0
            else:
                polygon_area += (polygon[n][0]*polygon[n+1][1] - polygon[n][1]*polygon[n+1][0])/2

    return S / 100**2 , points, triangles


print(polygons(stick_list)[0])
try:
    plt.triplot(polygons(stick_list)[1][:,0], polygons(stick_list)[1][:,1], polygons(stick_list)[2].simplices)
    plt.gca().invert_yaxis()
    plt.show()
except:
    pass

root.mainloop()




