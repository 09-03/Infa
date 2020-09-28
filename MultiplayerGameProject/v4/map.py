from settings import *
import pygame
from numba.core import types
from numba.typed import Dict
from numba import int32


_ = False
matrix_map = [
    [7, 6 , 7 , 6 , 7, 6 , 7 , 6, 7, 6, 7, 6, 7, 6 , 7 , 6, 7, 6 , 7 , 6, 7 , 6 , 7 , 6],
    [7, _ , _ , _ , _, _ , _ , _, _, _, _, _, _, _ , _ , _, _, _ , _ , _, _ , _ , _ , 7],
    [6, _ , _ , _ , _, _ , _ , _, _, _, _, _, _, _ , _ , _, _, _ , _ , _, _ , _ , _ , 6],
    [7, _ , _ , _ , _, _ , 2 , 3, _, _, _, _, _, _ , _ , _, _, 10, 11, _, _ , _ , _ , 7],
    [6, _ , _ , _ , _, _ , 4 , 5, _, _, _, _, _, 1 , 1 , _, _, _ , _ , _, _ , _ , _ , 6],
    [7, _ , _ , _ , _, _ , _ , _, _, _, _, _, _, _ , 1 , _, _, _ , _ , _, _ , _ , _ , 7],
    [6, _ , 14, 15, _, _ , _ , _, _, _, _, _, _, _ , 1 , 1, 1, 1 , _ , _, 12, 13, _ , 6],
    [7, 7 , _ , _ , _, _ , _ , _, _, _, _, _, _, _ , 1 , _, _, _ , _ , _, _ , _ , 6 , 7],
    [6, 16, _ , _ , _, _ , _ , _, _, 1, _, _, _, _ , 1 , _, _, _ , _ , _, _ , _ , 16, 6],
    [7, 6 , _ , _ , _, _ , _ , _, _, 1, _, _, _, _ , _ , _, _, _ , _ , _, _ , _ , 7 , 7],
    [6, _ , 14, 15, _, _ , 1 , 1, 1, 1, _, _, _, _ , _ , _, _, _ , _ , _, 12, 13, _ , 6],
    [7, _ , _ , _ , _, _ , _ , _, _, 1, _, _, _, 8 , 9 , _, _, 2 , 3 , _, _ , _ , _ , 7],
    [6, _ , _ , _ , _, _ , _ , _, _, 1, 1, _, _, 12, 11, _, _, 4 , 5 , _, _ , _ , _ , 6],
    [7, _ , _ , _ , _, 10, 11, _, _, _, _, _, _, _ , 8 , 9, _, _ , _ , _, _ , _ , _ , 7],
    [6, _ , _ , _ , _, _ , _ , _, _, _, _, _, _, _ , _ , _, _, _ , _ , _, _ , _ , _ , 6],
    [7, 6 , 7 , 6 , 7, 6 , 7 , 6, 7, 6, 7, 6, 7, 6 , 7 , 6, 7, 6 , 7 , 6, 7 , 6 , 7 , 6]
]


WORLD_WIDTH = len(matrix_map[0]) * TILE
WORLD_HEIGHT = len(matrix_map) * TILE
world_map = Dict.empty(key_type=types.UniTuple(int32, 2), value_type=int32)
collision_walls = []
for j, row in enumerate(matrix_map):
    for i, char in enumerate(row):
        if char:
            collision_walls.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
            if char == 1:
                world_map[(i * TILE, j * TILE)] = 1
            elif char == 2:
                world_map[(i * TILE, j * TILE)] = 2
            elif char == 3:
                world_map[(i * TILE, j * TILE)] = 3
            elif char == 4:
                world_map[(i * TILE, j * TILE)] = 4
            elif char == 5:
                world_map[(i * TILE, j * TILE)] = 5
            elif char == 6:
                world_map[(i * TILE, j * TILE)] = 6
            elif char == 7:
                world_map[(i * TILE, j * TILE)] = 7
            elif char == 8:
                world_map[(i * TILE, j * TILE)] = 8
            elif char == 9:
                world_map[(i * TILE, j * TILE)] = 9
            elif char == 10:
                world_map[(i * TILE, j * TILE)] = 10
            elif char == 11:
                world_map[(i * TILE, j * TILE)] = 11
            elif char == 12:
                world_map[(i * TILE, j * TILE)] = 12
            elif char == 13:
                world_map[(i * TILE, j * TILE)] = 13
            elif char == 14:
                world_map[(i * TILE, j * TILE)] = 14
            elif char == 15:
                world_map[(i * TILE, j * TILE)] = 15
            elif char == 16:
                world_map[(i * TILE, j * TILE)] = 16
            elif char == 17:
                world_map[(i * TILE, j * TILE)] = 17
