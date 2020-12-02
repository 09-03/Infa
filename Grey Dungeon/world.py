import pygame
from ray_casting import *
from collections import deque
import random
import sys
from map import world_map
import math
from numba import njit
from numba.core import types
from numba.typed import Dict
from numba import int32


class Drawing:
    def __init__(self, sc, player, clock):
        self.sc = sc
        self.player = player
        self.clock = clock
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.textures = {1: pygame.image.load('img/1.png').convert(),
                         2: pygame.image.load('img/2.png').convert(),
                         3: pygame.image.load('img/3.png').convert(),
                         4: pygame.image.load('img/4.png').convert(),
                         'S': pygame.image.load('img/sky.png').convert(),
                         'hp_bar': pygame.image.load('img/hp_bar.png').convert_alpha(),
                         "start": pygame.image.load('img/start.png').convert(),
                         "end_top": pygame.image.load('img/end_top.png').convert(),
                         "end_bottom": pygame.image.load('img/end_bottom.png').convert()
                         }

        self.weapon_base_sprite = pygame.image.load('sprites/weapons/shotgun/base/0.png').convert_alpha()
        self.weapon_shot_animation = deque([pygame.image.load(f'sprites/weapons/shotgun/shot/{i}.png').convert_alpha() for i in range(20)])
        self.weapon_rect = self.weapon_base_sprite.get_rect()
        self.weapon_pos = (600 - self.weapon_rect.width // 2, 800 - self.weapon_rect.height)
        self.shot_length = len(self.weapon_shot_animation)
        self.shot_length_count = 0
        self.shot_animation_speed = 3
        self.shot_animation_count = 0
        self.shot_animation_trigger = True
        self.shot_sound = pygame.mixer.Sound('sound/shotgun.wav')
        self.sfx = deque([pygame.image.load(f'sprites/weapons/sfx/{i}.png').convert_alpha() for i in range(9)])
        self.sfx_length_count = 0
        self.sfx_length = len(self.sfx)


    def background(self, angle):
        sky_offset = -10 * math.degrees(angle) % 1200
        self.sc.blit(self.textures['S'], (sky_offset, 0))
        self.sc.blit(self.textures['S'], (sky_offset - 1200, 0))
        self.sc.blit(self.textures['S'], (sky_offset + 1200, 0))
        pygame.draw.rect(self.sc,(40, 40, 40), (0, 400, 1200, 400))


    def world(self, world_objects):
        for obj in sorted(world_objects, key=lambda n: n[0], reverse=True):
            if obj[0]:
                _, object, object_pos = obj
                self.sc.blit(object, object_pos)


    def end_screen(self, step, win):
        x = random.randrange(150,255)
        if win:
            render = pygame.font.SysFont("Arial", 40, bold = True).render("YOU WIN!!!", 1, (x, x, x))

        else:
            render = pygame.font.SysFont("Arial", 40, bold = True).render("YOU LOSE!!!", 1, (x, x, x))

        self.sc.blit(self.textures["end_top"], (0,390-step))
        self.sc.blit(self.textures["end_bottom"], (0,step))
        self.sc.blit(render, (600 - 40, 650-step))


    def start_screen(self):
        self.sc.blit(self.textures["start"], (0,0))


    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, (255, 255, 255))
        self.sc.blit(render, (1135, 5))


    def health_bar(self,player, player2):
        if (player.health +player2.enemy_health)//2 == 100:
            pygame.draw.rect(self.sc, (180,180,180), (0,0,int((player.health +player2.enemy_health)//2 * 2),50))

        elif 50 <= (player.health +player2.enemy_health)//2 < 100:
            pygame.draw.rect(self.sc, (180,180,180), (0,0,int((player.health +player2.enemy_health)//2 * 2),50))

        elif 0 < (player.health +player2.enemy_health)//2 < 50:
            pygame.draw.rect(self.sc, (180,180,180), (0,0,int((player.health +player2.enemy_health)//2 * 2),50))

        else:
            pygame.draw.rect(self.sc, (180,180,180), (0,0,200,50))

        display_health = str(int((player.health + player2.enemy_health)//2))
        render = self.font.render(display_health, 0, (255, 255, 255))
        self.sc.blit(render, (10,5))
        self.sc.blit(self.textures["hp_bar"], (0,0))


    def player_weapon(self, shots):
        if self.player.shot:
            if not self.shot_length_count:
                self.shot_sound.set_volume(0.05)
                self.shot_sound.play()

            self.shot_projection = min(shots)[1] // 2
            self.bullet_sfx()
            shot_sprite = self.weapon_shot_animation[0]
            self.sc.blit(shot_sprite, self.weapon_pos)
            self.shot_animation_count += 1
            if self.shot_animation_count == self.shot_animation_speed:
                self.weapon_shot_animation.rotate(-1)
                self.shot_animation_count = 0
                self.shot_length_count += 1
                self.shot_animation_trigger = False

            if self.shot_length_count == self.shot_length:
                self.player.shot = False
                self.shot_length_count = 0
                self.sfx_length_count = 0
                self.shot_animation_trigger = True

        else:
            self.sc.blit(self.weapon_base_sprite, self.weapon_pos)


    def bullet_sfx(self):
        if self.sfx_length_count < self.sfx_length:
            sfx = pygame.transform.scale(self.sfx[0], (self.shot_projection, self.shot_projection))
            sfx_rect = sfx.get_rect()
            self.sc.blit(sfx, (600 - sfx_rect.w // 2, 400 - sfx_rect.h // 2))
            self.sfx_length_count += 1
            self.sfx.rotate(-1)


class Sprites:
    def __init__(self):
        self.sprite_parameters = {
            "sprite_player": {
                "sprite": pygame.image.load("sprites/player/base/0.png").convert_alpha(),
                "shift": 0.4,
                "scale": (0.7, 0.7),
                "side": 30,
                "animation": deque(
                    [pygame.image.load(f"sprites/player/anim/{i}.png").convert_alpha() for i in range(4)]),
                "death_animation": deque(
                    [pygame.image.load(f"sprites/player/death/{i}.png").convert_alpha() for i in range(8)]),
                "is_dead": None,
                "dead_shift": 0.7,
                "animation_dist": 1800,
                "animation_speed": 10,
                "blocked": True,
                "flag": "player",
                "obj_action": []},

            "sprite_barrel": {
                "sprite": pygame.image.load("sprites/barrel/base/0.png").convert_alpha(),
                "shift": 0.9,
                "scale": (0.4, 0.6),
                "side": 30,
                "animation": deque(
                    [pygame.image.load(f"sprites/barrel/anim/{i}.png").convert_alpha() for i in range(6)]),
                "death_animation": deque(
                    [pygame.image.load(f"sprites/barrel/death/{i}.png").convert_alpha() for i in range(4)]),
                "is_dead": None,
                "dead_shift": 1.4,
                "animation_dist": 800,
                "animation_speed": 10,
                "blocked": True,
                "flag": "decor",
                "obj_action": []},

            "sprite_flame": {
                "sprite": pygame.image.load("sprites/flame/base/0.png").convert_alpha(),
                "shift": 0.7,
                "scale": (0.6, 0.6),
                "side": 30,
                "animation": deque(
                    [pygame.image.load(f"sprites/flame/anim/{i}.png").convert_alpha() for i in range(16)]),
                "death_animation": [],
                "is_dead": "immortal",
                "dead_shift": 1.8,
                "animation_dist": 1800,
                "animation_speed": 5,
                "blocked": None,
                "flag": "decor",
                "obj_action": []},

            "sprite_npc": {
                "sprite": pygame.image.load("sprites/npc/base/0.png").convert_alpha(),
                "shift": 0.3,
                "scale": (0.4, 0.7),
                "side": 50,
                "animation": [],
                "death_animation": deque(
                    [pygame.image.load(f"sprites/npc/death/{i}.png").convert_alpha() for i in range(6)]),
                "is_dead": None,
                "dead_shift": 0.9,
                "animation_dist": None,
                "animation_speed": 10,
                "blocked": True,
                "flag": "npc",
                "obj_action": deque(
                    [pygame.image.load(f"sprites/npc/anim/{i}.png").convert_alpha() for i in range(4)]),}
                }

        self.list_of_objects = [
            SpriteObject(self.sprite_parameters["sprite_player"], (2, 10)),
            SpriteObject(self.sprite_parameters["sprite_npc"], (12, 8)),
            SpriteObject(self.sprite_parameters["sprite_flame"], (1.8, 11.8)),
            SpriteObject(self.sprite_parameters["sprite_flame"], (4.2, 11.8)),
            SpriteObject(self.sprite_parameters["sprite_flame"], (1.8, 14.2)),
            SpriteObject(self.sprite_parameters["sprite_flame"], (4.2, 14.2)),
            SpriteObject(self.sprite_parameters["sprite_flame"], (19.8, 1.8)),
            SpriteObject(self.sprite_parameters["sprite_flame"], (22.2, 1.8)),
            SpriteObject(self.sprite_parameters["sprite_flame"], (19.8, 4.2)),
            SpriteObject(self.sprite_parameters["sprite_flame"], (22.2, 4.2)),
            SpriteObject(self.sprite_parameters["sprite_barrel"], (10.2, 13.2)),
            SpriteObject(self.sprite_parameters["sprite_barrel"], (10.2, 14.8)),
            SpriteObject(self.sprite_parameters["sprite_barrel"], (13.8, 14.2)),
            SpriteObject(self.sprite_parameters["sprite_barrel"], (13.8, 1.2)),
            SpriteObject(self.sprite_parameters["sprite_barrel"], (13.8, 2.8)),
            SpriteObject(self.sprite_parameters["sprite_barrel"], (10.2, 1.8))
            ]


    @property
    def sprite_shot(self):
        return min([obj.is_on_fire for obj in self.list_of_objects], default=(float("inf"), 0))


class SpriteObject:
    def __init__(self, parameters, pos):
        self.object = parameters["sprite"].copy()
        self.shift = parameters["shift"]
        self.scale = parameters["scale"]
        self.animation = parameters["animation"].copy()
        self.death_animation = parameters["death_animation"].copy()
        self.is_dead = parameters["is_dead"]
        self.dead_shift = parameters["dead_shift"]
        self.animation_dist = parameters["animation_dist"]
        self.animation_speed = parameters["animation_speed"]
        self.blocked = parameters["blocked"]
        self.flag = parameters["flag"]
        self.obj_action = parameters["obj_action"].copy()
        self.x, self.y = pos[0] * 100, pos[1] * 100
        self.side = parameters["side"]
        self.dead_animation_count = 0
        self.animation_count = 0
        self.npc_action_trigger = False


    @property
    def is_on_fire(self):
        if 149 - self.side // 2 < self.current_ray < 149 + self.side // 2 and self.blocked:
            return self.distance_to_sprite, self.proj_height
        return float("inf"), None


    @property
    def pos(self):
        return self.x - self.side // 2, self.y - self.side // 2


    def object_locate(self, player):
        dx, dy = self.x - player.x, self.y - player.y
        self.distance_to_sprite = math.sqrt(dx ** 2 + dy ** 2)
        self.theta = math.atan2(dy, dx)
        gamma = self.theta - player.angle
        if dx > 0 and 180 <= math.degrees(player.angle) <= 360 or dx < 0 and dy < 0:
            gamma += 2 * math.pi

        self.theta -= 1.4 * gamma
        delta_rays = int(gamma / (math.pi/900))
        self.current_ray = 149 + delta_rays
        self.distance_to_sprite *= math.cos(math.pi/6 - self.current_ray * (math.pi/900))
        fake_ray = self.current_ray + 100
        if 0 <= fake_ray <= 499 and self.distance_to_sprite > 30:
            self.proj_height = min(int(90000/(2*math.tan(math.pi/6)) / self.distance_to_sprite), 1600)
            sprite_width = int(self.proj_height * self.scale[0])
            sprite_height = int(self.proj_height * self.scale[1])
            half_sprite_width = sprite_width // 2
            half_sprite_height = sprite_height // 2
            shift = half_sprite_height * self.shift
            if self.is_dead and self.is_dead != "immortal":
                sprite_object = self.dead_animation()
                shift = half_sprite_height * self.dead_shift
                sprite_height = int(sprite_height / 1.3)

            elif self.npc_action_trigger:
                sprite_object = self.npc_in_action()

            else:
                sprite_object = self.sprite_animation()

            sprite_pos = (self.current_ray * 4 - half_sprite_width, 400 - half_sprite_height + shift)
            sprite = pygame.transform.scale(sprite_object, (sprite_width, sprite_height))
            return (self.distance_to_sprite, sprite, sprite_pos)
        else:
            return (False,)


    def sprite_animation(self):
        if self.animation and self.distance_to_sprite < self.animation_dist:
            sprite_object = self.animation[0]

            if self.animation_count < self.animation_speed:
                self.animation_count += 1

            else:
                self.animation.rotate()
                self.animation_count = 0

            return sprite_object
        return self.object


    def dead_animation(self):
        if len(self.death_animation):
            if self.dead_animation_count < self.animation_speed:
                self.dead_sprite = self.death_animation[0]
                self.dead_animation_count += 1

            else:
                self.dead_sprite = self.death_animation.popleft()
                self.dead_animation_count = 0

        return self.dead_sprite


    def npc_in_action(self):
        sprite_object = self.obj_action[0]
        if self.animation_count < self.animation_speed:
            self.animation_count += 1

        else:
            self.obj_action.rotate()
            self.animation_count = 0

        return sprite_object


class Interaction:
    def __init__(self, player, player2, sprites, drawing):
        self.player = player
        self.player2 = player2
        self.sprites = sprites
        self.drawing = drawing
        self.pain_sound = pygame.mixer.Sound('sound/pain.wav')
        self.shot_sound = pygame.mixer.Sound('sound/shotgun.wav')


    def interaction_objects(self):
        if self.player.shot and self.drawing.shot_animation_trigger:
            for obj in sorted(self.sprites.list_of_objects, key=lambda obj: obj.distance_to_sprite):
                if obj.is_on_fire[1]:
                    if obj.is_dead != 'immortal' and not obj.is_dead:
                        if ray_casting_npc_player(obj.x, obj.y, world_map, self.player.pos):
                            if obj.flag == 'npc':
                                self.pain_sound.set_volume(0.05)
                                self.pain_sound.play()
                                obj.is_dead = True
                                obj.blocked = None
                                self.player.dead_sprite = 1

                            elif obj.flag == 'player':
                                self.pain_sound.set_volume(0.05)
                                self.pain_sound.play()
                                self.player.enemy_health -= 40
                                if (self.player2.health + self.player.enemy_health)//2 <= 0:
                                    obj.is_dead = True
                                    obj.blocked = None

                            else:
                                obj.is_dead = True
                                obj.blocked = None

                            self.drawing.shot_animation_trigger = False
                    break


    def npc_action(self, player, player2):
        for obj in self.sprites.list_of_objects:
            if obj.flag == 'npc' and not obj.is_dead:
                dist_to_p1 = math.sqrt((obj.x-player.x) ** 2 + (obj.y-player.y) ** 2)
                dist_to_p2 = math.sqrt((obj.x-player2.x) ** 2 + (obj.y-player2.y) ** 2)
                if dist_to_p1 <= dist_to_p2:
                    if ray_casting_npc_player(obj.x, obj.y, world_map, self.player.pos):
                        obj.npc_action_trigger = True
                        self.npc_move(obj, player)
                        if obj.animation_count == 4:
                            chance = random.randint(0, 100)
                            if chance <= 30:
                                self.player.health -= random.randint(1, 5)
                    else:
                        obj.npc_action_trigger = False
                else:
                    obj.npc_action_trigger = False
                    obj.x = player2.enemy1_x
                    obj.y = player2.enemy1_y


    def npc_move(self, obj, player):
        if obj.distance_to_sprite > 100:
            dx = obj.x - player.pos[0]
            dy = obj.y - player.pos[1]
            if obj.flag == 'npc':
                player.enemy1_x = obj.x = obj.x + 1 if dx < 0 else obj.x - 1
                player.enemy1_y = obj.y = obj.y + 1 if dy < 0 else obj.y - 1


    def play_music(self):
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()
        pygame.mixer.music.load('sound/theme.mp3')
        pygame.mixer.music.set_volume(0.06)
        pygame.mixer.music.play(-1)


    def play_menumusic(self):
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()
        pygame.mixer.music.load('sound/menu.mp3')
        pygame.mixer.music.set_volume(0.06)
        pygame.mixer.music.play(-1)


    def play_endmusic(self,win):
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()
        if win:
            pygame.mixer.music.load('sound/win.mp3')

        else:
            pygame.mixer.music.load('sound/lose.mp3')

        pygame.mixer.music.set_volume(0.06)
        pygame.mixer.music.play(-1)
