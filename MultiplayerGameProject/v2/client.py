import pygame
from network import Network
from player import Player

win_width = 800
win_height = 800
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Client")


def DrawWindow(win, player1, player2):
    win.fill((255, 255, 255))
    player1.DrawPlayer(win)
    player2.DrawPlayer(win)
    pygame.display.update()


def main():
    run = True
    net = Network()
    player1 = net.getPlayer()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        player2 = net.send(player1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        player1.PlayerMovement()
        DrawWindow(win, player1, player2)

main()
