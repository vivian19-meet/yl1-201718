from turtle import *
import random
import math
class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
circle_1 = Ball(9,"blue",45)

circle_2 = Ball(12,"red",32)
circle_3 = Ball(20,"green",75)
circle_4 = Ball(39,"yellow",63)
def check_collision(circle_1,circle_2):
	h = math.sqrt(math.pow(circle_2.xcor()-circle_1.xcor(),2) + math.pow((circle_2.ycor()-circle_1.ycor()),2))
	y = circle_1.radius+circle_2.radius
	if h <= y:
		return True
	else: 
		return False
#check_collision(circle_1,circle_2)
vv = [circle_1,circle_2,circle_3,circle_4]
def check_list(list1):
	for i in range(len(vv)):
		for j in range(i+1,len(vv)):
			if check_collision(vv[i],vv[j]) == True :
				x = random.randint(-500, 500)
				y = random.randint(-500, 500)
				if vv[i].radius > vv[j].radius:
					vv[j].goto(x,y)
				else:
					vv[i].goto(x,y)

check_list(vv)


mainloop()
