import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))
class Sprites:
    def __init__(self):
        self.sprite_types = {
            'barrel': pygame.image.load('sprites/barrel/0.png').convert_alpha(),
            'pedestal': pygame.image.load('sprites/pedestal/0.png').convert_alpha(),
            'devil': [pygame.image.load(f'sprites/devil/{i}.png').convert_alpha() for i in range(8)],
            'player': pygame.image.load(f'sprites/player/{j}.png').convert_alpha() for j in range(8)]
        }
        self.list_of_objects = [
            SpriteObject(self.sprite_types['barrel'], True, (7.1, 2.1), 1.8, 0.4),
            SpriteObject(self.sprite_types['barrel'], True, (5.9, 2.1), 1.8, 0.4),
            SpriteObject(self.sprite_types['pedestal'], True, (8.8, 2.5), 1.6, 0.5),
            SpriteObject(self.sprite_types['pedestal'], True, (8.8, 5.6), 1.6, 0.5),
            SpriteObject(self.sprite_types['devil'], False, (7, 4), -0.2, 0.7),
        ]

class SpriteObject:
    def __init__(self, object, static, pos, shift, scale):
        self.object = object
        self.static = static
        self.pos = self.x, self.y = pos[0] * 2, pos[1] * 2
        self.shift = shift
        self.scale = scale
sp = Sprites()
def change(x, y):
    sp.list_of_objects[2] = SpriteObject(sp.sprite_types['devil'], False, (x, y), -0.2, 0.7)
change(2,3)
