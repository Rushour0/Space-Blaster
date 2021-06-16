import pygame

class Laser:
	def __init__(self,img_name,x,y):
		img = pygame.image.load(img_name)
		self.img_path = img_name
		self.x = x
		self.y = y
		self.img = img
		self.width = img.get_width()
		self.height = img.get_height()
		self.default_x = 0
		self.default_y = 0.5
		self.x_chg = self.default_x
		self.y_chg = self.default_y
		# print(self.width,self.height)

	def load(self):
		return self.img,tuple([self.x-self.width/2,self.y-self.height/2])

	def changeXY(self,WINDOW_WIDTH = None,WINDOW_HEIGHT = None,WINDOW_DIMENSIONS = None):
		if WINDOW_DIMENSIONS is not None:
			WINDOW_WIDTH,WINDOW_HEIGHT = WINDOW_DIMENSIONS
		if self.width/2<self.x+self.x_chg and self.x+self.x_chg+self.width<WINDOW_WIDTH+self.width/2:
			self.x+=self.x_chg
		if self.width/2<self.y+self.y_chg and self.y+self.y_chg+self.height<WINDOW_HEIGHT+self.width/2:
			self.y-=self.y_chg
		else:
			return False
		return True