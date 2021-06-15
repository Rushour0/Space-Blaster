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
spaceship = Blaster(spaceship_img,WINDOW_WIDTH/2,WINDOW_HEIGHT-WINDOW_HEIGHT/8)

# Bullets array
bullets = []

def background_show():
	screen.blit(background,(0,0))

def spaceship_show():
	spaceship.changeXY(WINDOW_DIMENSIONS = WINDOW_DIMENSIONS)
	screen.blit(*spaceship.load())

def bullets_show(bullets = bullets):
	for num,bullet in enumerate(bullets):
		if bullet.changeXY(WINDOW_DIMENSIONS = WINDOW_DIMENSIONS):
			screen.blit(*bullet.load())
			print("dikha?")
		else:
			bullets = bullets[1:]

def gameLoop():

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			return False

		if pygame.key.get_pressed()[32]:
			if len(bullets)<=3:
				print("ini")
				bullets.append(Bullet(bullet_img,spaceship.x,spaceship.y))

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

	background_show()	
	spaceship_show()
	bullets_show()
	pygame.display.update()
	
	return True
while True:
	if (gameLoop() == False):break
