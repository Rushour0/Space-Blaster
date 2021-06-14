import sys
import pygame

sys.path.append("src")
sys.path.append("img")
from Blaster import *
from paths import *
# PyGame initialized
pygame.init()

WINDOW_DIMENSIONS = (800,600)
WINDOW_WIDTH,WINDOW_HEIGHT = WINDOW_DIMENSIONS
# Create screen
screen = pygame.display.set_mode(WINDOW_DIMENSIONS)

# Set window name
pygame.display.set_caption("Space Blaster")

# Load logo image and set icon
icon = pygame.image.load(icon_img)
pygame.display.set_icon(icon)

# Blaster declaration
spaceship = Blaster(spaceship_img,WINDOW_WIDTH/2,WINDOW_HEIGHT-WINDOW_HEIGHT/8)

def show_me():
	spaceship.changeXY(WINDOW_DIMENSIONS = WINDOW_DIMENSIONS)
	screen.blit(*list(spaceship.load()))
running = True

def gameLoop():


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			return False

		if event.type == pygame.KEYDOWN:
			print(pygame.key.get_pressed().index(1))
			if event.key in [pygame.K_LEFT,pygame.K_a]:
				spaceship.x_chg = -spaceship.default_x

			if event.key in [pygame.K_RIGHT,pygame.K_d]:
				spaceship.x_chg = spaceship.default_x

		if event.type == pygame.KEYUP:
			if event.key in [pygame.K_LEFT,pygame.K_a] and not (pygame.key.get_pressed()[79] or pygame.key.get_pressed()[7]):
				spaceship.x_chg = 0

			if event.key in [pygame.K_RIGHT,pygame.K_d] and not (pygame.key.get_pressed()[80] or pygame.key.get_pressed()[4]):
				spaceship.x_chg = 0


			
	show_me()
	pygame.display.update()
	
	return True
while running:
	if (gameLoop() == False):break
