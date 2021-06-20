import sys
import random
import time
import copy

sys.path.append("src")
sys.path.append("img")
sys.path.append("music")

# importing all classes and extra methods
from Blaster import *
from Bullet import *
from Asteroid import *
from Blast import *
from colors import *
from paths import *

# laser bullets limit
bullet_limit = 3
bullet_restore_time = 5

# Time for generation of new asteroid
time_interval = 0.2

# Window Dimensions
WINDOW_DIMENSIONS = (800,600)
WINDOW_WIDTH,WINDOW_HEIGHT = WINDOW_DIMENSIONS

# Universal spawning coordinates for the asteroids
uni_asteroid_spawn_x = [list([i for i in range(j,800,36)])[1:-1] for j in range(2,14)]
uni_asteroid_spawn_y = 0

score = 0