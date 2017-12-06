from turtle import *
import random
class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
circle_1 = Ball(9,"blue",45)

circle_2 = Ball(12,"blue",32)
def check_collision(cicle_1,circle_2):
	if math.sqrt(math.pow((circle_2.xcor()-circle_1.xcor(),2) + math.pow((circle_2.ycor()-circle_1.ycor(),2))<=circle_1.radius+circle_2.radius
		print("nice!")
