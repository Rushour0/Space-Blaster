import pygame

class Asteroid:
	def __init__(self,img_name,x,y):
		img = pygame.image.load(img_name)
		self.img_path = img_name
		self.x = x
		self.y = y
		self.img = img
		self.isCollision = False
		self.width = img.get_width()
		self.height = img.get_height()