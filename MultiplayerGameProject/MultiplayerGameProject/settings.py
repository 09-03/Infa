import math

# win settings
win_width = 1200
win_height = 800
tile_size = 100
fps = 60

# server settings
server = "192.168.0.100"
port = 5555

# player settings
player_angle = 0
player_speed = 3
player_angle_speed = 0.03

# raycasting settings
FOV = math.pi / 3
half_FOV = FOV / 2
num_rays = 300
max_depth = 800
delta_angle = FOV / num_rays
dist = num_rays / (2 * math.tan(half_FOV))
projection_coef = 3 * dist * tile_size
scale = win_width // num_rays

# texture settings (1200 x 1200)
texture_width = 1200
texture_height = 1200
texture_scale = texture_width // tile_size

# sprite settings (1200 x 1200)
center_ray = num_rays // 2 - 1
fake_rays = 100
