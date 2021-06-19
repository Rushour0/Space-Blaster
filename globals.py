import sys
import random

sys.path.append("src")
sys.path.append("img")
sys.path.append("music")

bullet_limit = 10

from Blaster import *
from Bullet import *
from Asteroid import *
from paths import *

asteroid_spawn_x = [[i for i in range(j,32,800)] for i in range(16)]