import pygame

class Bullet:
	def __init__(self,img_name,x,y):
		img = pygame.image.load(img_name)
		self.img_path = img_name
		self.x = x
		self.y = y
		self.img = img
		self.width = img.get_width()
		self.height = img.get_height()
		self.default_x = 0
		self.default_y = 1
		self.x_chg = self.default_x
		self.y_chg = self.default_y
		print(self.width,self.height)

	def load(self):
		return self.img,(self.x,self.y)

	def changeXY()