import turtle
import random
from turtle import *
#turtle.addshape("cloud.gif")
#turtle.addshape("ccloud.gif")
#shapes=["cloud.gif","ccloud.gif"]
##s ="cloud.gif"
class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.dx=dx
		self.dy=dy
		self.r=r
		self.penup()
		self.goto(x,y)
		self.x=self.xcor()
		self.y=self.ycor()
		self.shape("circle")
		self.shapesize(r/10)
		self.color("white")
		
	def move(self,screen_width,screen_height):
		current_x=self.xcor() 
		new_x = current_x + self.dx
		current_y = self.ycor() 
		new_y = current_y +self.dy
		right__side__ball = new_x + self.r
		left__side__ball = new_x - self.r
		up__side__ball = new_y + self.r
		down__side__ball = new_y - self.r
		self.goto(new_x,new_y)
		if right__side__ball > screen_width :
			self.dx = -self.dx
			self.clear()
		if left__side__ball < -screen_width:
			self.dx = -self.dx
			self.clear()
		if up__side__ball > screen_height:
			self.dy = -self.dy
			self.clear()
		if down__side__ball < -screen_height:
			self.dy = -self.dy
			self.clear()