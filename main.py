from globals import *

# PyGame initialized
pygame.init()

WINDOW_DIMENSIONS = (800,600)
WINDOW_WIDTH,WINDOW_HEIGHT = WINDOW_DIMENSIONS

# Set window name
pygame.display.set_caption("Space Blaster")

# Load logo image and set icon
icon = pygame.image.load(icon_img)
pygame.display.set_icon(icon)

# Create screen
screen = pygame.display.set_mode(WINDOW_DIMENSIONS)

# Background image
background = pygame.image.load(background_img)

# Blaster declaration
spaceship = Spaceship(spaceship_img,WINDOW_WIDTH/2,WINDOW_HEIGHT-WINDOW_HEIGHT/8)

# Bullets array
lasers = []

# Laser sound
lasersound = pygame.mixer.Sound(laser_sound)

def background_show():
	screen.blit(background,(0,0))

def spaceship_show():
	spaceship.changeXY(WINDOW_DIMENSIONS = WINDOW_DIMENSIONS)
	screen.blit(*spaceship.load())

def bullets_show():
	global lasers
	for num,laser in enumerate(lasers):
		if laser.changeXY(WINDOW_DIMENSIONS = WINDOW_DIMENSIONS):
			screen.blit(*laser.load())
		else:
			del lasers[num]

def gameLoop():

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			return False

		if event.type == pygame.KEYDOWN:
			if event.key in [pygame.K_LEFT,pygame.K_a]:
				spaceship.x_chg = -spaceship.default_x

			if event.key in [pygame.K_RIGHT,pygame.K_d]:
				spaceship.x_chg = spaceship.default_x

		if event.type == pygame.KEYUP:
			if event.key in [pygame.K_LEFT,pygame.K_a] and not (pygame.key.get_pressed()[79] or pygame.key.get_pressed()[7]):
				spaceship.x_chg = 0

			if event.key in [pygame.K_RIGHT,pygame.K_d] and not (pygame.key.get_pressed()[80] or pygame.key.get_pressed()[4]):
				spaceship.x_chg = 0

			if event.key == pygame.K_SPACE:
				if len(lasers)<3:
					lasers.append(Laser(laser_img,spaceship.x,spaceship.y))
					lasersound.play()

	background_show()
	bullets_show()
	spaceship_show()
	
	pygame.display.update()
	
	return True
while True:
	if (gameLoop() == False):break
