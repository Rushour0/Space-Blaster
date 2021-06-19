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
		self.x_chg = 0
		self.y_chg = 1.5
		self.rotate_value = random.randrange(-7,7,3)
		self.rotate_counter = 0
		self.rotate_after = 110
	def load(self):
		return self.img,tuple([self.x-self.width/2,self.y-self.height/2])

	def changeXY(self,WINDOW_WIDTH = None,WINDOW_HEIGHT = None,WINDOW_DIMENSIONS = None):
	
		if not self.rotate_counter%self.rotate_after:
			self.img = pygame.transform.rotate(self.img,random.randrange(-1,1,2)*self.rotate_value+random.randint(-2,2))
		self.rotate_counter+=1

		if WINDOW_DIMENSIONS is not None:
			WINDOW_WIDTH,WINDOW_HEIGHT = WINDOW_DIMENSIONS
		if self.width/2<self.x+self.x_chg and self.x+self.x_chg+self.width<WINDOW_WIDTH+self.width*1.5:
			self.x+=self.x_chg
		if -self.height<self.y+self.y_chg and self.y+self.y_chg+self.height<WINDOW_HEIGHT+self.height*1.5:
			self.y+=self.y_chg
		else:
			return False
		return True
