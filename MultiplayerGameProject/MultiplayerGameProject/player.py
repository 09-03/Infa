import pygame
import math
from settings import *


class Player():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.speed = player_speed
        self.angle = player_angle

    def DrawPlayer(self, win):
        pygame.draw.circle(win, self.color, (int(self.x), int(self.y)), 12)
        pygame.draw.line(win, self.color, (self.x, self.y),  (self.x + win_width * math.cos(self.angle),
                                                              self.y + win_width * math. sin(self.angle)), 2)

    def PlayerMovement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x += self.speed * cos_a
            self.y += self.speed * sin_a
        if keys[pygame.K_s]:
            self.x += -self.speed * cos_a
            self.y += -self.speed * sin_a
        if keys[pygame.K_a]:
            self.x += self.speed * sin_a
            self.y += -self.speed * cos_a
        if keys[pygame.K_d]:
            self.x += -self.speed * sin_a
            self.y += self.speed * cos_a
        if keys[pygame.K_LEFT]:
            self.angle -= player_angle_speed
        if keys[pygame.K_RIGHT]:
            self.angle += player_angle_speed

        self.angle %= math.pi * 2
