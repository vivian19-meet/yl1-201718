import turtle
import time
import random
from project import Ball
import math
import PIL
from PIL import Image
#from resizeimage import resizeimage
turtle.getscreen().bgpic("rain.gif")
turtle.tracer(0)
turtle.hideturtle()
running = True
SLEEP =0.05
SCREEN_WIDTH = int(turtle.getcanvas().winfo_width() /2)
SCREEN_HEIGHT= int(turtle.getcanvas().winfo_height()/2)
my_ball =Ball(0,0,0,0,20,"purple")
#????????random.choice(
turtle.addshape("thunder.gif")
turtle.shape("thunder.gif")
turtle.hideturtle()
#turtle.addshape("gry.gif")
#turtle.addshape("ccloud.gif")
#turtle.addshape("cloud.gif")
#mg = Image.open("gry.gif")
#global new_width
#wwidth=[]
#new_wwidth=40
#global new_height
#hhight=[]
#new_heigh=40
#img = img.resize((new_wwidth, new_heigh), Image.ANTIALIAS)
#img.save("gry.gif")
#my_ball.shape("gry.gif")

my_ball.color("grey")
#width, height = im.size
global new_width
new_width=40
width_list=[]
global new_height
height_list=[]
new_height=40
#new_height = new_width * (4 /4)
#global vv
#vv=0
	

#new_width  = new_height
#s =random.choice(shapes)
#????
NUMBER_OF_BALLS =7
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 45
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5
score =0
Balls =[]
ddx =random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
ddy =random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
im =Image.open("cloud.gif")
for i in range(NUMBER_OF_BALLS) :
	rr=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	bb = Ball(random.randint(-SCREEN_WIDTH +MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS),
		random.randint(-SCREEN_HEIGHT +MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT -MAXIMUM_BALL_RADIUS), 
		random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX),random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY),
		rr,"white")
	#(random.random(), random.random(),
		#random.random())
	#wid=rr*2
	#hei=rr*2
	#im = im.resize((wid, hei), Image.ANTIALIAS)
	#bb.shape("cloud.gif")
	Balls.append(bb)
def move_all_balls():
	for v in Balls:
		v.move(SCREEN_WIDTH,SCREEN_HEIGHT)
def collide(ball_a,ball_b):
	if ball_a==ball_b:
		return False
	if math.sqrt(math.pow((ball_a.xcor()-ball_b.xcor()),2) + math.pow((ball_a.ycor()-ball_b.ycor()),2))+10 <=ball_a.r +ball_b.r :
		return True
	else:
		return False
def check_all_balls_collision():
	for ball_a in Balls:
		for ball_b in Balls:
			if collide(ball_a,ball_b)==True:
				ar = ball_a.r
				br=ball_b.r
				X_coordinate = random.randint(-SCREEN_WIDTH +MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
				Y_coordinate = random.randint(-SCREEN_HEIGHT +MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT -MAXIMUM_BALL_RADIUS)
				ddx =random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				ddy =random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				while ddx == 0 :
					ddx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				while ddy == 0:
					ddy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				Radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
				r = random.random()
				b= random.random()
				g = random.random()
				color = "white"
				l =max(ball_a.r,ball_b.r) 
				if ball_b.r ==l :
					ball_a.goto(X_coordinate, Y_coordinate)
					ball_a.x = X_coordinate
					ball_a.y = Y_coordinate
					ball_a.dx =ddx
					ball_a.dy =ddy
					ball_a.r =Radius
					ball_a.color(color)
					ball_b.r =ball_b.r +1
					ball_a.shapesize(ball_a.r/10)
					ball_b.shapesize(ball_b.r/10)
				else :
					ball_b.goto(X_coordinate, Y_coordinate)
					ball_b.x = X_coordinate
					ball_b.y = Y_coordinate
					ball_b.dx =ddx
					ball_b.dy =ddy
					ball_b.r =Radius
					ball_b.color(color)
					ball_a.r =ball_a.r +1
					ball_b.shapesize(ball_b.r/10)
					ball_a.shapesize(ball_a.r/10)
global score 
score_list=[]
score =0

def check_myball_collision():
	img = Image.open("gry.gif")
	for ball_x in Balls :
		global score
		global new_width
		global new_height
		if collide(my_ball,ball_x)==True:
			x_radius=ball_x.r
			mine_radius =my_ball.r
			if x_radius > mine_radius :
				return False
			else:
				X_coordinate = random.randint(-SCREEN_WIDTH +MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
				Y_coordinate = random.randint(-SCREEN_HEIGHT +MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT -MAXIMUM_BALL_RADIUS)
				Radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
				ball_x.goto(X_coordinate, Y_coordinate)
				ball_x.x = X_coordinate
				ball_x.y = Y_coordinate
				ball_x.dx =ddx
				ball_x.dy =ddy
				Radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
				ball_x.r =Radius
				r = random.random()
				b= random.random()
				g = random.random()
				color = "white"
				ball_x.color(color)
				my_ball.r =my_ball.r +2
				my_ball.shapesize(my_ball.r/10)
				score=score+1
				#new_width =new_width+100
				#new_height=new_height+100
				#img = Image.open("gry.gif")
				#img = img.resize((new_width, new_height), Image.ANTIALIAS)
				
				#img.save("gry.gif")
				#my_ball.shape("gry.gif")
				#my_ball.shapesize(100)
				#turtle.clear()

				#l =score
				#score =l +1
				return True

	return True
	

def movearound(event):
	my_ball.goto(event.x - SCREEN_WIDTH ,SCREEN_HEIGHT - event.y)

turtle.getcanvas().bind("<Motion>",movearound)
turtle.getscreen().listen()

while running == True:
	if SCREEN_WIDTH != int(turtle.getcanvas().winfo_width() /2) or SCREEN_HEIGHT != int(turtle.getcanvas().winfo_height()/2):
		SCREEN_WIDTH = int(turtle.getcanvas().winfo_width() /2)
		SCREEN_HEIGHT = int(turtle.getcanvas().winfo_height()/2)
	move_all_balls()
	check_all_balls_collision()		
	if check_myball_collision() == False:
		turtle.showturtle()		
		turtle.write("Game over! :( \n you'r score is"+ " " +str(score) , move=False, align="left", font=("Arial", 30, "normal"))
		#print(new_width)
		running = False
	else:
		if my_ball.r > MAXIMUM_BALL_RADIUS:
			turtle.write("congrats! you won! \n now you are the \n biggest cloud\n you'r score is"+ " " +str(score),move=False, align="left", font=("Arial",20, "normal"))
			running = False
	time.sleep(SLEEP)
	turtle.getscreen().update()
turtle.mainloop()
		
























