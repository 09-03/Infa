import pygame
from settings import *
from player import Player
from sprite_objects import *
from ray_casting import ray_casting_walls
from drawing import Drawing
from network import Network


# Чтение координат в формате строки
def Read_Pos(str):
    str = str.split(",")
    return int(str[0]) ,int(str[1])


# Создание координат в формате строки из кортежа
def Make_Pos(tup):
    return str(tup[0]) + "," + str(tup[1])


# Фоновая музыка
def play_music():
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.init()
    pygame.mixer.music.load("sound/theme.mp3")
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1)

# Создание окна приложения
pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

# Создание классов со спрайтами и отрисовкой различных элементов
sprites = Sprites()
drawing = Drawing(sc)

# Создание сети и первичных координат игроков
net = Network()
startpos = Read_Pos(net.getPos())
player = Player(startpos[0], startpos[1], sprites)
player2 = Player(2150, 850, sprites)

play_music()

# Основной цикл приложения
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    clock.tick(FPS)

    # Получение координат второго игрока через сеть и обновление его координат
    player2pos = Read_Pos(net.send(Make_Pos((int(player.x), int(player.y)))))
    player2.x = player2pos[0]
    player2.y = player2pos[1]

    # Обновление координат спрайта второго игрока
    sprites.list_of_objects[0].x = player2.x
    sprites.list_of_objects[0].y = player2.y

    player.movement()

    # Отрисовка всех элементов
    sc.fill(BLACK)
    drawing.background(player.angle)
    walls = ray_casting_walls(player, drawing.textures)
    drawing.world(walls + [obj.object_locate(player) for obj in sprites.list_of_objects])
    drawing.fps(clock)

    pygame.display.update()
