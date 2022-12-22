import random

# game options/settings
WIDTH = 480
HEIGHT = 600
FPS = 60
FONT_NAME = 'arial'
HS_FILE = "highscore.txt"
SPRITESHEET = "spritesheet_jumper.png"

# PLayer properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.05
PLAYER_GRAV = 0.5
PLAYER_JUMP = 16


# Game properties
BOOST_POWER = 60
POW_SPAWN_PCT = 7

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 60),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4 - 25),
                 (40, 320),
                 (350, 220),
                 (300, 120)]
                 

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0 ,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
BGCOLOR = LIGHTBLUE
