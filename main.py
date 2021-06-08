import pygame

# PyGame initialized
pygame.init()

# Create screen
screen = pygame.display.set_mode((800,600))

running = True

def gameLoop():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			return False

while running:
	if (gameLoop() == False):return