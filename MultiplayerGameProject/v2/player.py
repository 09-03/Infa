import pygame

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
