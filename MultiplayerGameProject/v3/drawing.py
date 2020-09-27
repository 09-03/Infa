import pygame
from settings import *
from raycasting import ray_casting

class Drawing:
    def __init__(self, win):
        self.win = win
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.textures = {"1" : pygame.image.load("img/wall1.png").convert(),
                         "2" : pygame.image.load("img/wall2.png").convert(),
                         "Sky" : pygame.image.load("img/sky.png").convert(),
                         }

    def background(self, angle):
        sky_offset = -5 * math.degrees(angle) % win_width
        self.win.blit(self.textures['Sky'], (sky_offset, 0))
        self.win.blit(self.textures['Sky'], (sky_offset - win_width, 0))
        self.win.blit(self.textures['Sky'], (sky_offset + win_width, 0))
        pygame.draw.rect(self.win, (50, 50, 50), (0, win_height // 2, win_width, win_height // 2))

    def world(self, world_objects):
        for obj in sorted(world_objects, key=lambda n: n[0], reverse=True):
            if obj[0]:
                _, object, object_pos = obj
                self.win.blit(object, object_pos)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, (255, 0, 0))
        self.win.blit(render, (win_width - 65, 5))
