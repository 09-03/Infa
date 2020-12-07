import pygame
import math
from map import collision_walls


class Player:
    def __init__(self, x, y, health, enemy_health, dead_sprite, enemy1_x, enemy1_y, sprites):
        self.x, self.y = player_pos = x, y
        self.health = health
        self.enemy_health = enemy_health
        self.dead_sprite = dead_sprite
        self.enemy1_x = enemy1_x
        self.enemy1_y = enemy1_y
        self.sprites = sprites
        self.angle = 0
        self.sensitivity = 0.004
        self.side = 50
        self.rect = pygame.Rect(*player_pos, self.side, self.side)
        self.shot = False


    @property
    def pos(self):
        return (self.x, self.y)


    @property
    def collision_list(self):
        return collision_walls + [pygame.Rect(*obj.pos, obj.side, obj.side) for obj in
                                  self.sprites.list_of_objects if obj.blocked]


    def collision(self, dx, dy):
        next_rect = self.rect.copy()
        next_rect.move_ip(dx, dy)
        hit_indexes = next_rect.collidelistall(self.collision_list)
        if len(hit_indexes):
            delta_x, delta_y = 0, 0

            for hit_index in hit_indexes:
                hit_rect = self.collision_list[hit_index]
                if dx > 0:
                    delta_x += next_rect.right - hit_rect.left

                else:
                    delta_x += hit_rect.right - next_rect.left

                if dy > 0:
                    delta_y += next_rect.bottom - hit_rect.top

                else:
                    delta_y += hit_rect.bottom - next_rect.top

            if abs(delta_x - delta_y) < 10:
                dx, dy = 0, 0

            elif delta_x > delta_y:
                dy = 0

            elif delta_y > delta_x:
                dx = 0

        self.x += dx
        self.y += dy


    def movement(self):
        self.keys_control()
        self.mouse_control()
        self.rect.center = self.x, self.y
        self.angle %= 2*math.pi


    def keys_control(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            exit()

        if keys[pygame.K_RSHIFT]:
            self.shot = True

        if keys[pygame.K_w]:
            dx = 5 * cos_a
            dy = 5 * sin_a
            self.collision(dx, dy)

        if keys[pygame.K_s]:
            dx = -5 * cos_a
            dy = -5 * sin_a
            self.collision(dx, dy)

        if keys[pygame.K_a]:
            dx = 5 * sin_a
            dy = -5 * cos_a
            self.collision(dx, dy)

        if keys[pygame.K_d]:
            dx = -5 * sin_a
            dy = 5 * cos_a
            self.collision(dx, dy)

        if keys[pygame.K_LEFT]:
            self.angle -= 0.02

        if keys[pygame.K_RIGHT]:
            self.angle += 0.02

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not self.shot:
                    self.shot = True


    def mouse_control(self):
        if pygame.mouse.get_focused():
            difference = pygame.mouse.get_pos()[0] - 600
            pygame.mouse.set_pos((600, 400))
            self.angle += difference * self.sensitivity
