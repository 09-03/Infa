import pygame
from settings import *
from ray_casting import ray_casting


class Drawing:
    def __init__(self, sc):
        self.sc = sc
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.textures = {1: pygame.image.load('img/1.png').convert(),
                         2: pygame.image.load('img/2.png').convert(),
                         3: pygame.image.load('img/3.png').convert(),
                         4: pygame.image.load('img/4.png').convert(),
                         5: pygame.image.load('img/5.png').convert(),
                         6: pygame.image.load('img/6.png').convert(),
                         7: pygame.image.load('img/7.png').convert(),
                         8: pygame.image.load('img/8.png').convert(),
                         9: pygame.image.load('img/9.png').convert(),
                         10: pygame.image.load('img/10.png').convert(),
                         11: pygame.image.load('img/11.png').convert(),
                         12: pygame.image.load('img/12.png').convert(),
                         13: pygame.image.load('img/13.png').convert(),
                         14: pygame.image.load('img/14.png').convert(),
                         15: pygame.image.load('img/15.png').convert(),
                         16: pygame.image.load('img/16.png').convert(),
                         17: pygame.image.load('img/17.png').convert(),
                         'S': pygame.image.load('img/sky.png').convert()
                         }


    def background(self, angle):
        sky_offset = -10 * math.degrees(angle) % WIDTH
        self.sc.blit(self.textures['S'], (sky_offset, 0))
        self.sc.blit(self.textures['S'], (sky_offset - WIDTH, 0))
        self.sc.blit(self.textures['S'], (sky_offset + WIDTH, 0))
        pygame.draw.rect(self.sc, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))


    def world(self, world_objects):
        for obj in sorted(world_objects, key=lambda n: n[0], reverse=True):
            if obj[0]:
                _, object, object_pos = obj
                self.sc.blit(object, object_pos)


    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, DARKORANGE)
        self.sc.blit(render, FPS_POS)
