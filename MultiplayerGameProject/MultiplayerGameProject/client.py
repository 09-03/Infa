import pygame
from network import Network
from player import *
from drawing import *
from sprite_objects import *
from raycasting import *
from settings import *

pygame.init()
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Client")
sprites = Sprites()
drawing = Drawing(win)

def change(x, y):
    sprites.list_of_objects[0] = SpriteObject(sprites.sprite_types['player'], False, (x / tile_size, y / tile_size), 0.2, 0.7)

def main():
    run = True
    net = Network()
    player1 = net.getPlayer()
    clock = pygame.time.Clock()

    while run:
        clock.tick(fps)
        player2 = net.send(player1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        player1.PlayerMovement()
        drawing.background(player1.angle)
        walls = ray_casting(player1, drawing.textures)
        try:
            drawing.world(walls + [obj.object_locate(player1, walls) for obj in sprites.list_of_objects])
            change(player2.x, player2.y)
        except:
            pass
        drawing.fps(clock)
        pygame.display.update()


main()
