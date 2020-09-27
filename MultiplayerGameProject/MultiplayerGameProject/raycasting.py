import pygame
from settings import *
from map import world_map


def mapping(a, b):
    return (a // tile_size) * tile_size, (b // tile_size) * tile_size


def ray_casting(player, textures):
    walls = []
    x0 = player.x
    y0 = player.y
    xm, ym = mapping(x0, y0)
    cur_angle = player.angle - half_FOV
    for ray in range(num_rays):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        sin_a = sin_a if sin_a else 0.000001
        cos_a = cos_a if cos_a else 0.000001

        # verticals
        x, dx = (xm + tile_size, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, win_width, tile_size):
            depth_v = (x - x0) / cos_a
            yv = y0 + depth_v * sin_a
            tile_v = mapping(x + dx, yv)
            if tile_v in world_map:
                texture_v = world_map[tile_v]
                break
            x += dx * tile_size

        # horizontals
        y, dy = (ym + tile_size, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, win_height, tile_size):
            depth_h = (y - y0) / sin_a
            xh = x0 + depth_h * cos_a
            tile_h = mapping(xh, y + dy)
            if tile_h in world_map:
                texture_h = world_map[tile_h]
                break
            y += dy * tile_size

        # projection
        depth, offset, texture = (depth_v, yv, texture_v) if depth_v < depth_h else (depth_h, xh, texture_h)
        offset = int(offset) % tile_size
        depth *= math.cos(player.angle - cur_angle)
        depth = max(depth, 0.00001)
        proj_height = min(int(projection_coef / depth), 2 * win_height)

        wall_column = textures[texture].subsurface(offset * texture_scale, 0, texture_scale, texture_height)
        wall_column = pygame.transform.scale(wall_column, (scale, proj_height))
        wall_pos = (ray * scale, win_height // 2 - proj_height // 2)

        walls.append((depth, wall_column, wall_pos))
        cur_angle += delta_angle
    return walls
