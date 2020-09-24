import pygame
from network import Network


win_width = 800
win_height = 800
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Client")

client_num = 0

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.speed = 3

    def DrawPlayer(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def PlayerMovement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.y -= self.speed

        if keys[pygame.K_a]:
            self.x -= self.speed

        if keys[pygame.K_s]:
            self.y += self.speed

        if keys[pygame.K_d]:
            self.x += self.speed

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)


def Read_Pos(str):
    str = str.split(",")
    return int(str[0]) ,int(str[1])


def Make_Pos(tup):
    return str(tup[0]) + "," + str(tup[1])


def DrawWindow(win, player, player2):
    win.fill((255, 255, 255))
    player.DrawPlayer(win)
    player2.DrawPlayer(win)
    pygame.display.update()


def main():
    run = True
    net = Network()
    startpos = Read_Pos(net.getPos())
    player = Player(startpos[0], startpos[1], 100, 100, (0, 255,0 ))
    player2 = Player(0, 0, 100, 100, (255, 0,0 ))
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        player2pos = Read_Pos(net.send(Make_Pos((player.x, player.y))))
        player2.x = player2pos[0]
        player2.y = player2pos[1]
        player2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        player.PlayerMovement()
        DrawWindow(win, player, player2)

main()
