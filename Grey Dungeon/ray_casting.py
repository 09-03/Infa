import pygame
from map import world_map, WORLD_WIDTH, WORLD_HEIGHT
from numba import njit
import math


@njit(fastmath=True, cache=True)
def mapping(a, b):
    return int(a // 100) * 100, int(b // 100) * 100


@njit(fastmath=True, cache=True)
def ray_casting(player_pos, player_angle, world_map):
    casted_walls = []
    ox, oy = player_pos
    texture_v, texture_h = 1, 1
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - math.pi / 6
    for ray in range(300):
        sin_a = math.sin(cur_angle)
        sin_a = sin_a if sin_a else 0.000001
        cos_a = math.cos(cur_angle)
        cos_a = cos_a if cos_a else 0.000001

        x, dx = (xm + 100, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, WORLD_WIDTH, 100):
            depth_v = (x - ox) / cos_a
            yv = oy + depth_v * sin_a
            tile_v = mapping(x + dx, yv)
            if tile_v in world_map:
                texture_v = world_map[tile_v]
                break
            x += dx * 100

        y, dy = (ym + 100, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, WORLD_HEIGHT, 100):
            depth_h = (y - oy) / sin_a
            xh = ox + depth_h * cos_a
            tile_h = mapping(xh, y + dy)
            if tile_h in world_map:
                texture_h = world_map[tile_h]
                break
            y += dy * 100

        depth, offset, texture = (depth_v, yv, texture_v) if depth_v < depth_h else (depth_h, xh, texture_h)
        offset = int(offset) % 100
        depth *= math.cos(player_angle - cur_angle)
        depth = max(depth, 0.00001)
        proj_height = int((90000 / (2 * math.tan(math.pi/6))) / depth)
        casted_walls.append((depth, offset, proj_height, texture))
        cur_angle += math.pi / 900
    return casted_walls


@njit(fastmath=True, cache=True)
def ray_casting_npc_player(npc_x, npc_y, world_map, player_pos):
    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    delta_x, delta_y = ox - npc_x, oy - npc_y
    cur_angle = math.atan2(delta_y, delta_x)
    cur_angle += math.pi
    sin_a = math.sin(cur_angle)
    sin_a = sin_a if sin_a else 0.000001
    cos_a = math.cos(cur_angle)
    cos_a = cos_a if cos_a else 0.000001
    
    x, dx = (xm + 100, 1) if cos_a >= 0 else (xm, -1)
    for i in range(0, int(abs(delta_x)) // 100):
        depth_v = (x - ox) / cos_a
        yv = oy + depth_v * sin_a
        tile_v = mapping(x + dx, yv)
        if tile_v in world_map:
            return False
        x += dx * 100

    y, dy = (ym + 100, 1) if sin_a >= 0 else (ym, -1)
    for i in range(0, int(abs(delta_y)) // 100):
        depth_h = (y - oy) / sin_a
        xh = ox + depth_h * cos_a
        tile_h = mapping(xh, y + dy)
        if tile_h in world_map:
            return False
        y += dy * 100
    return True


def ray_casting_walls(player, textures):
    casted_walls = ray_casting(player.pos, player.angle, world_map)
    wall_shot = casted_walls[149][0], casted_walls[149][2]
    walls = []
    for ray, casted_values in enumerate(casted_walls):
        depth, offset, proj_height, texture = casted_values
        if proj_height > 800:
            coeff = proj_height / 800
            texture_height = 1200 / coeff
            wall_column = textures[texture].subsurface(offset * 12,
                                                       600 - texture_height // 2,
                                                       12, texture_height)
            wall_column = pygame.transform.scale(wall_column, (4, 800))
            wall_pos = (ray * 4, 0)
        else:
            wall_column = textures[texture].subsurface(offset * 12, 0, 12, 1200)
            wall_column = pygame.transform.scale(wall_column, (4, proj_height))
            wall_pos = (ray * 4, 400 - proj_height // 2)

        walls.append((depth, wall_column, wall_pos))
    return walls, wall_shot
