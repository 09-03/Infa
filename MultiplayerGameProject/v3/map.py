from settings import *

bin_map = [[1,1,1,1,1,1,1,1,1,1,1,1],
           [1,0,0,0,0,0,2,0,0,0,0,1],
           [1,0,2,2,0,0,0,0,0,2,0,1],
           [1,0,0,0,0,0,0,0,0,0,0,1],
           [1,0,2,2,0,0,0,0,0,0,0,1],
           [1,0,2,0,0,0,0,0,0,2,0,1],
           [1,0,0,0,0,0,2,0,0,0,0,1],
           [1,1,1,1,1,1,1,1,1,1,1,1]
]

world_map = {}
for j, row in enumerate(bin_map):
    for i, key in enumerate(row):
        if key == 1:
            world_map[(i * tile_size, j * tile_size)] = "1"
        elif key == 2:
            world_map[(i * tile_size, j * tile_size)] = "2"
