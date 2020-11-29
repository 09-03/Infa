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

            return abs(convex_hull_area)

        else:
            convex_hull_area += int((points_set[n][0]*points_set[n+1][1]-
                                 points_set[n][1]*points_set[n+1][0])/2)


def stick_placing(N):
    stick_list = []
    for i in range(N+1):
        for j in range(N+1):
            if random.randint(1,N+1) == 1:
                x = 15+j*100
                y =15+i*100
                stick_list.append([x, y])
    return stick_list




def E(N, num_tests):
    E = 0
    area_counter = {}
    area_list=[]
    for i in range(num_tests):
        sticks = stick_placing(N)
        area_list.append(convex_hull(sticks))
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
