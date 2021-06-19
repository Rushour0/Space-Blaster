import pygame
import random

def CollisionDetect(toCheck,objectList):
	for obj in objectList[::-1]:
		x_range = [-obj.width/2,obj.width/2+obj.x]
		y_range = [-obj.height/2+obj.y,obj.height/2+obj.y]
		if x_range[0]<=toCheck.x<=x_range[1] and y_range[0]<=toCheck.y<=y_range[1]:
			return True
	return False

class Asteroid:
	def __init__(self,img_name,x,y):
		img = pygame.image.load(img_name)
		self.img_path = img_name
		self.x = x
		self.y = y
		self.img = img
		self.isShot = False
		self.width = img.get_width()
		self.height = img.get_height()
		self.x_chg = random.randrange(-0.75,0.75,0.05)
		self.y_chg = 0.6

	def load(self):
		return self.img,tuple([self.x-self.width/2,self.y-self.height/2])

