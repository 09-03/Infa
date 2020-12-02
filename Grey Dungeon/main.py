from player import Player
from ray_casting import ray_casting_walls
from world import *
from network import Network


def Read_status(str):
    str = str.split(",")
    return int(str[0]), int(str[1]), int(str[2]), int(str[3]), int(str[4]), int(str[5]), int(str[6])


def Make_status(tup):
    return str(tup[0]) + "," + str(tup[1]) + "," + str(tup[2]) + "," + str(tup[3]) + "," + str(tup[4]) + "," + str(tup[5]) + "," + str(tup[6])


def sync(synced):
    if player2.dead_sprite == 1 and not synced:
        sprites.list_of_objects[1].is_dead = True
        synced = True


pygame.init()
sc = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()
pygame.display.set_caption("Grey Dungeon")
icon = pygame.image.load("img/icon.png")
pygame.display.set_icon(icon)
pygame.mouse.set_visible(True)

sprites = Sprites()
solo = False
try:
    net = Network()
    startstatus = Read_status(net.getstatus())
    player = Player(startstatus[0], startstatus[1], startstatus[2], startstatus[3], startstatus[4], startstatus[5], startstatus[6], sprites)

except:
    player = Player(250, 250, 100, 100, 0, 1200, 800, sprites)
    solo = True

player2 = Player(2150, 1350, 100, 100, 0, 1200, 800, sprites)
drawing = Drawing(sc, player, clock)
interaction = Interaction(player, player2, sprites, drawing)
interaction.play_menumusic()

synced = False
step = 800
tick = 0
ready = False
while not ready:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 480 and pygame.mouse.get_pos()[1] >= 500:
                if pygame.mouse.get_pos()[0] <= 700 and pygame.mouse.get_pos()[1] <= 570:
                    ready=True

    drawing.start_screen()
    pygame.display.flip()

pygame.mouse.set_visible(False)
interaction.play_music()
while True:
    if not solo:
        player2status = Read_status(net.send(Make_status((int(player.x), int(player.y), int(player.health), int(player.enemy_health), int(player.dead_sprite), int(player.enemy1_x), int(player.enemy1_y)))))
        player2.x = player2status[0]
        player2.y = player2status[1]
        player2.health = player2status[2]
        player2.enemy_health = player2status[3]
        player2.dead_sprite = player2status[4]
        player2.enemy1_x = player2status[5]
        player2.enemy1_y = player2status[6]

    drawing.background(player.angle)
    walls, wall_shot = ray_casting_walls(player, drawing.textures)
    drawing.world(walls + [obj.object_locate(player) for obj in sprites.list_of_objects])
    drawing.fps(clock)
    drawing.player_weapon([wall_shot, sprites.sprite_shot])

    player.movement()
    interaction.interaction_objects()
    sprites.list_of_objects[0].x = player2.x
    sprites.list_of_objects[0].y = player2.y
    interaction.npc_action(player, player2)

    sync(synced)
    drawing.health_bar(player, player2)
    if (player.health + player2.enemy_health) // 2 <= 0:
        win = False
        interaction.play_endmusic(win)
        if not solo:
            player2status = Read_status(net.send(Make_status((int(player.x), int(player.y), int(player.health), int(player.enemy_health), int(player.dead_sprite), int(player.enemy1_x), int(player.enemy1_y)))))
            player2.health = player2status[2]
            player2.enemy_health = player2status[3]

        drawing.health_bar(player, player2)
        pygame.mouse.set_visible(True)
        while True:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                exit()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >= 460 and pygame.mouse.get_pos()[1] >= 550:
                        if pygame.mouse.get_pos()[0] <= 880 and pygame.mouse.get_pos()[1] <= 730:
                            pygame.quit()

            drawing.end_screen(step, win)
            if step >= 400:
                step -= 10

            pygame.display.flip()
            clock.tick(90)

    if (player2.health + player.enemy_health) // 2 <= 0:
        tick+=1
        if tick == 100:
            win = True
            interaction.play_endmusic(win)
            if not solo:
                player2status = Read_status(net.send(Make_status((int(player.x), int(player.y), int(player.health), int(player.enemy_health), int(player.dead_sprite), int(player.enemy1_x), int(player.enemy1_y)))))
                player2.health = player2status[2]
                player2.enemy_health = player2status[3]

            drawing.health_bar(player, player2)
            pygame.mouse.set_visible(True)

            while True:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    exit()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pos()[0] >= 460 and pygame.mouse.get_pos()[1] >= 550:
                            if pygame.mouse.get_pos()[0] <= 880 and pygame.mouse.get_pos()[1] <= 730:
                                pygame.quit()

                drawing.end_screen(step, win)
                if step >= 400:
                    step -= 10

                pygame.display.flip()
                clock.tick(90)

    pygame.display.flip()
    clock.tick(90)
