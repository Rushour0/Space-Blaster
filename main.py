import pygame

# PyGame initialized
pygame.init()

# Create screen
screen = pygame.display.set_mode((800,600))

# Set window name
pygame.display,set_caption("Space Blaster")

# Load logo image and set icon
icon = pygame.imgae.load("img/icon.png")
pygame.display.set_icon(icon)


running = True

def gameLoop():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			return False
	

while running:
	if (gameLoop() == False):return
