import turtle

class Square(Turtle):
	def __init__(self,size,):
		Turtle.__init__(self)
		self.shapesize(size)
		self.shape('square')

class Rectangle(object):
	def __init__(self,width,hight):
		self.width(width)
		self.hight(hight)
