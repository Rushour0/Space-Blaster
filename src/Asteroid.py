import pygame
import random

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
		self.x_chg = random.randrange(-0.75,0.75,0.05)
		self.y_chg = random.randrange(0.35,0.75,0.05)

	def load(self):
		return self.img,tuple([self.x-self.width/2,self.y-self.height/2])