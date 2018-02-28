import turtle
import math


SCREEN_WIDTH= int(turtle.getcanvas().winfo_width()/2)
SCREEN_HEIGHT= int(turtle.getcanvas().winfo_width()/2)
turtle.hideturtle()
play1=turtle.clone()
how=turtle.clone()
def interface():
	turtle.tracer(0)
	turtle.hideturtle()
	turtle.penup()
	play1.color("purple")
	play1.penup()
	play1.write ("Play", font = ("Ariel", 20), align = "center")
	how.color("purple")
	how.penup()
	how.goto(0, -50)
	how.write("How to play", font = ("Ariel", 20), align = "center")
	turtle.goto(0, 75)
	turtle.color("blue")
	turtle.write("Riddle-Grounds", font = ("Ariel", 45), align = "center")

def howto():
    play1.clear()
    how.clear()
    turtle.clear()
    turtle.goto(0,100)
    turtle.write("instructions:", font = ("Ariel", 20), align = "center")
    turtle.goto(0,0)
    turtle.write("press on the land, whether it's easy, medium, or hard", font = ("Ariel", 18), align = "center")
    turtle.goto(0,-50)
    turtle.write("the harder the riddle, the more money you get", font = ("Ariel", 20), align = "center")
    turtle.goto(200,-200)
    turtle.write("back", font = ("Ariel", 12), align = "center")
    
def play():
    play1.clear()
    how.clear()
    turtle.clear()
    turtle.write("playing", font = ("Ariel", 20), align = "center")


def click(x,y):
        Dplay = math.sqrt(math.pow(0-x, 2) + math.pow(0-y,2))
        print(Dplay)
        if(Dplay<20):
                print("playing")
                play()
                return True
        Dhowto = math.sqrt(math.pow(0-x, 2) + math.pow(-50-y,2))
        print(Dhowto)
        if(Dhowto<30):
                howto()
                return True
        Dback = math.sqrt(math.pow(200-x, 2) + math.pow(-200-y,2))
        print(Dback)
        if(Dback<20):
                turtle.clear()
                interface()
                return True
turtle.onscreenclick(click)



##def play():


##score = turtle.Turtle()
#score.hideturtle()
#score.pu()
#score.goto(-650,300)
#	turtle.penup()
#	turtle.goto()
#	turtle.pendown()
#	turtle.width(10)
#	turtle.goto()
interface()
turtle.listen()






