from globals import *
from pygame.locals import *

# PyGame initialized
pygame.init()

# For performance
pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])

# Set window name
pygame.display.set_caption("Space Blaster")

# Load logo image and set icon
icon = pygame.image.load(icon_img)
pygame.display.set_icon(icon)

# Create screen
flags = DOUBLEBUF
screen = pygame.display.set_mode(WINDOW_DIMENSIONS, flags, 16)

# Background image
background = pygame.image.load(background_img)

# Blaster declaration
spaceship = Spaceship(spaceship_img,WINDOW_WIDTH/2,WINDOW_HEIGHT-WINDOW_HEIGHT/8)

# Bullets array
lasers = []

# Laser sound
lasersound = pygame.mixer.Sound(laser_sound)

# Display available bullets
available_bullets = [DisplayBullet(available_bullet_img,WINDOW_WIDTH-32-32*i,96) for i in range(bullet_limit,0,-1)]

# Universal asteroid available spawns
asteroid_spawn_x = uni_asteroid_spawn_x[random.randint(0,len(uni_asteroid_spawn_x)-1)].copy()

# Asteroids list
asteroids = []

# last time when an asteroid was generated
last_time = time.time()

# Asteroid Generator with time parameter
def asteroid_generator(time_elapse):
	if len(asteroids)>5:
		return 
	global last_time,asteroid_spawn_x
	current_time = time.time()
	if current_time-last_time>time_elapse:
		x = random.choice(asteroid_spawn_x)
		del asteroid_spawn_x[asteroid_spawn_x.index(x)]

		# Change to new x-spawn sequence
		if len(asteroid_spawn_x) == 0:
			asteroid_spawn_x = uni_asteroid_spawn_x[random.randint(0,len(uni_asteroid_spawn_x)-1)].copy()

		y = uni_asteroid_spawn_y
		asteroids.append(Asteroid(asteroid_imgs[random.randint(0,3)],x,y))
		last_time = current_time

# Draw background
def background_show():
	screen.blit(background,(0,0))

# Draw spaceship
def spaceship_show():
	spaceship.changeXY(WINDOW_DIMENSIONS = WINDOW_DIMENSIONS)
	screen.blit(*spaceship.load())

# Draw bullets/lasers
def bullets_show():
	global lasers
	for num,laser in enumerate(lasers):
		if laser.changeXY(WINDOW_DIMENSIONS = WINDOW_DIMENSIONS):
			screen.blit(*laser.load())
		else:
			del lasers[num]

	for bullet in available_bullets[:bullet_limit-len(lasers)]:
		screen.blit(*bullet.load())

# Draw asteroids
def asteroid_show():
	global asteroids
	for num,asteroid in enumerate(asteroids):
		if asteroid.changeXY(WINDOW_DIMENSIONS = WINDOW_DIMENSIONS):
			screen.blit(*asteroid.load())
		else:
			del asteroids[num]


# Eternally running game loop
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit(0) 

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
				if len(lasers)<bullet_limit:
					lasers.append(Laser(laser_img,spaceship.x,spaceship.y))
					lasersound.play()

	
	screen.fill((0,0,0))
	background_show()
	asteroid_generator(time_elapse)
	asteroid_show()
	bullets_show()
	spaceship_show()
		
	pygame.display.update()

