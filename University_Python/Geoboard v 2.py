import random

"""
Если придумаете как реализовать триангуляцию точек на плоскости
без этих библеотек, тогда отпишите мне
"""

from scipy.spatial import Delaunay
import numpy as np
 

def stick_placing(N):
    stick_list = []
    for i in range(N+1):
        for j in range(N+1):
            if random.randint(1,N+1) == 1:
                x = 15+j*100
                y =15+i*100
                stick_list.append([x, y])
    return stick_list

            
def polygons(stick_list):
    S = 0
    polygon_area = 0
    if len(stick_list)<3:
        return S
    points = np.array(stick_list)
    try:
        triangles = Delaunay(points)
    except:
        return S
    for polygon in points[triangles.simplices]:
        for n in range(len(polygon)):
            if n == len(polygon)-1:
                polygon_area += (polygon[n][0]*polygon[0][1]- polygon[n][1]*polygon[0][0])/2
                S+=abs(polygon_area)
                polygon_area = 0
            else:
                polygon_area += (polygon[n][0]*polygon[n+1][1] - polygon[n][1]*polygon[n+1][0])/2
    return int(S)


def E(N, num_tests):
    E = 0
    area_counter = {}
    area_list=[]
    for i in range(num_tests):
        sticks = stick_placing(N)
        area_list.append(polygons(sticks))
        if area_list[i] in area_counter:
            area_counter[area_list[i]] += 1
        else:
            area_counter[area_list[i]] = 1
        print(f"Геодосок сделано: {i+1}/{num_tests}")

    for key, value in area_counter.items():
        E+=key*value
    E /= (num_tests * 10000)
    print(round(E, 5))


valid_N = False
valid_num_tests = False
while not valid_N:
    valid_N = True
    try:
        N = int(input("Введите N: "))
        if N <= 0:
            print("--------------------\nВведено неположительное значение", end = "\n--------------------\n")
            valid_N = False

    except:
        print("--------------------\nВведено неправильное значение", end = "\n--------------------\n")
        valid_N = False

while not valid_num_tests:
    valid_num_tests = True
    try:
        num_tests = int(input("--------------------\nВведите количество Геодосок: "))
        if num_tests <= 0:
            print("--------------------\nВведено неположительное значение", end = "\n--------------------\n")
            valid_num_tests = False

    except:
        print("--------------------\nВведено неправильное значение", end = "\n--------------------\n")
        valid_num_tests = False

E(N, num_tests)
