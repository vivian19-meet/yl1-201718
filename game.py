import random
import turtle
import math
import time
score=0
run=True
turtle.setup (width=800, height=500, startx=0, starty=0)
SCREEN_WIDTH= int(turtle.getcanvas().winfo_width()/2)
SCREEN_HEIGHT= int(turtle.getcanvas().winfo_width()/2)
turtle.hideturtle()
play1=turtle.clone()
how=turtle.clone()
scorew=turtle.clone()
scorew.penup()
scorew.goto(250,-200)

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
    turtle.write("press easy, medium, or hard", font = ("Ariel", 18), align = "center")
    turtle.goto(0,-50)
    turtle.write("the harder the riddle, the more money you get", font = ("Ariel", 20), align = "center")
    turtle.goto(200,-200)
    turtle.write("back", font = ("Ariel", 12), align = "center")
    

    
def levels(x,y):
    dgreen=math.sqrt(math.pow(-250-x, 2) + math.pow(0-y,2))
    if(dgreen<30):
        chooseeasy()
    dyellow=math.sqrt(math.pow(0-x, 2) + math.pow(0-y,2))
    if(dyellow<30):
        choosemedium()
    dred=math.sqrt(math.pow(250-x, 2) + math.pow(0-y,2))
    if(dred<30):
        choosehard()
def click(x,y):
        Dplay = math.sqrt(math.pow(0-x, 2) + math.pow(0-y,2))
        if(Dplay<20):
                play1.clear()
                how.clear()
                turtle.clear()
                turtle.bgpic("back.png")
                turtle.goto(-250,0)
                turtle.color("white")
                turtle.write("easy", font = ("Ariel", 30), align = "center")
                turtle.goto(0,0)
                turtle.write("medium", font = ("Ariel", 30), align = "center")
                turtle.goto(250,0)
                turtle.write("hard", font = ("Ariel", 30), align = "center")
                turtle.onscreenclick(levels)
                return True
        Dhowto = math.sqrt(math.pow(0-x, 2) + math.pow(-50-y,2))
        if(Dhowto<30):
                howto()
                return True
        Dback = math.sqrt(math.pow(200-x, 2) + math.pow(-200-y,2))
        if(Dback<20):
                turtle.clear()
                interface()
                return True
turtle.onscreenclick(click)


interface()
turtle.listen()
##***************************************************************************************************************
class Riddle(object):
        def __init__(self,riddle_Text,answer1,answer2,answer3,correct_answer):
                self.riddle_Text=riddle_Text
                self.answer1=answer1
                self.answer2=answer2
                self.answer3=answer3
                self.correct_answer=correct_answer

easy=[]
medium=[]
hard=[]
#make_easy_riddles
five_e=Riddle("If you are running in a race and pass the second place person, what place are you in?","a)third place","b)second place","c)first place","b")
second_e=Riddle("which part of the body closes when we sneeze?","a)ears","b)nose","c)eyes","c")
third_e=Riddle("l=i c=z r=a n=p which code means pizza? :p","a)frlc","b)nlccn","c)nlccr","c")
easy.append(five_e)
easy.append(second_e)
easy.append(third_e)
##
##
sixth_m=Riddle("Tamer is 6 years old Inon is tow times younger than Tamer. a few years pass..now Tamer is 70 years old.how old is Inon?","a)35","b)73","c)67","c")
four_m=Riddle("there are 10 fishes in the aqurium, 7 died how many fishes are in the aquarium now? ","a)10","b)3","c)54","a")
first_m=Riddle("find the code! meet-meetmeetmeetmeetmeet-meetmeetmeet-meetmeet","a)1431","b)1532","c)banana","b")
medium.append(sixth_m)
medium.append(four_m)
medium.append(first_m)
##
##
nn_h=Riddle("a BMW car was going to the hub, in the way it MEETs 3 cars. how many cars R going to the hub?","a)1","b)3","c)4","a")
seventh_h=Riddle("when did meet start?","a)1989","b)2004","c)2003","b")
e_h=Riddle("why does Nizar own a lot of ducks?","a)it's a gift from his girlfriend","b)because a duck saved him when he was little","c)because it's cheep and good for debuging","c")
hard.append(seventh_h)
hard.append(e_h)
hard.append(nn_h)

def playagain():
        time.sleep(2)
        turtle.clear()
        turtle.bgpic("back.png")
        turtle.goto(-250,0)
        turtle.color("white")
        turtle.write("easy", font = ("Ariel", 30), align = "center")
        turtle.goto(0,0)
        turtle.write("medium", font = ("Ariel", 30), align = "center")
        turtle.goto(250,0)
        turtle.write("hard", font = ("Ariel", 30), align = "center")
        turtle.onscreenclick(levels)

def chooseeasy():
        x=random.randint(1,random.randint(2,3))
        if(x==1):
                f=five_e.correct_answer
                turtle.clear()
                turtle.goto(0,200)
                turtle.color("black")
                turtle.write(five_e.riddle_Text, font = ("Ariel", 13), align = "center")
                turtle.goto(-250,100)
                turtle.write(five_e.answer1, font = ("Ariel", 30), align = "left")
                turtle.goto(-250,0)
                turtle.write(five_e.answer2, font = ("Ariel", 30), align = "left")
                turtle.goto(-250,-100)
                turtle.write(five_e.answer3, font = ("Ariel", 30), align = "left")
                def check(x,y):
                        da=math.sqrt(math.pow(-250-x, 2) + math.pow(100-y,2))
                        if(da<30):
                                turtle.clear()
                                turtle.goto(0,0)
                                turtle.color("white")
                                turtle.write("wrong!!", font = ("Ariel", 60), align = "center")
                                playagain()
                        db=math.sqrt(math.pow(-250-x, 2) + math.pow(0-y,2))
                        if(db<30):
                                global score
                                turtle.clear()
                                turtle.goto(0,0)
                                turtle.color("white")
                                turtle.write("congratiulations!!", font = ("Ariel", 60), align = "center")
                                score=score+100
                                playagain()
                        dc=math.sqrt(math.pow(-250-x, 2) + math.pow(-100-y,2))
                        if(dc<30):
                                turtle.clear()
                                turtle.goto(0,0)
                                turtle.color("white")
                                turtle.write("wrong!!", font = ("Ariel", 60), align = "center")
                                playagain()
                turtle.onscreenclick(check)
        if(x==2):
                f=second_e.correct_answer
                turtle.clear()
                turtle.goto(0,200)
                turtle.color("black")
                turtle.write(second_e.riddle_Text, font = ("Ariel", 13), align = "center")
                turtle.goto(-250,100)
                turtle.write(second_e.answer1, font = ("Ariel", 30), align = "left")
                turtle.goto(-250,0)
                turtle.write(second_e.answer2, font = ("Ariel", 30), align = "left")
                turtle.goto(-250,-100)
                turtle.write(second_e.answer3, font = ("Ariel", 30), align = "left")
                def check(x,y):
                        da=math.sqrt(math.pow(-250-x, 2) + math.pow(100-y,2))
                        if(da<30):
                                turtle.clear()
                                turtle.goto(0,0)
                                turtle.color("white")
                                turtle.write("wrong!!", font = ("Ariel", 60), align = "center")
                                playagain()
                        db=math.sqrt(math.pow(-250-x, 2) + math.pow(0-y,2))
                        if(db<30):
                                turtle.clear()
                                turtle.goto(0,0)
                                turtle.color("white")
                                turtle.write("wrong!!", font = ("Ariel", 60), align = "center")
                                playagain()
                        dc=math.sqrt(math.pow(-250-x, 2) + math.pow(-100-y,2))
                        if(dc<30):
                                global score
                                turtle.clear()
                                turtle.goto(0,0)
                                turtle.color("white")
                                turtle.write("congratiulations!!", font = ("Ariel", 60), align = "center")
                                score=score+100
                                playagain()
                turtle.onscreenclick(check)

        if(x==3):
                f=third_e.correct_answer
                turtle.clear()
                turtle.goto(0,200)
                turtle.color("black")
                turtle.write(third_e.riddle_Text, font = ("Ariel", 13), align = "center")
                turtle.goto(-250,100)
                turtle.write(third_e.answer1, font = ("Ariel", 30), align = "left")
                turtle.goto(-250,0)
                turtle.write(third_e.answer2, font = ("Ariel", 30), align = "left")
                turtle.goto(-250,-100)
                turtle.write(third_e.answer3, font = ("Ariel", 30), align = "left")
                def check(x,y):
                        da=math.sqrt(math.pow(-250-x, 2) + math.pow(100-y,2))
                        if(da<30):
                                turtle.clear()
                                turtle.goto(0,0)
                                turtle.color("white")
                                turtle.write("wrong!!", font = ("Ariel", 60), align = "center")
                                playagain()
                        db=math.sqrt(math.pow(-250-x, 2) + math.pow(0-y,2))
                        if(db<30):
                                turtle.clear()
                                turtle.goto(0,0)
                                turtle.color("white")
                                turtle.write("wrong!!", font = ("Ariel", 60), align = "center")
                                playagain()
                        dc=math.sqrt(math.pow(-250-x, 2) + math.pow(-100-y,2))
                        if(dc<30):
                                global score
                                turtle.clear()
                                turtle.goto(0,0)
                                turtle.color("white")
                                turtle.write("congratiulations!!", font = ("Ariel", 60), align = "center")
                                score=score+100
                                playagain()

                turtle.onscreenclick(check)
def choosemedium():
        x=random.randint(1,random.randint(2,3))
        if(x==1):
                f=sixth_m.correct_answer
                turtle.clear()
                turtle.goto(0,200)
                turtle.color("black")
                turtle.write(sixth_m.riddle_Text, font = ("Ariel", 13), align = "center")
                turtle.goto(-250,100)
                turtle.write(sixth_m.answer1, font = ("Ariel", 30), align = "left")
                turtle.goto(-250,0)
                turtle.write(sixth_m.answer2, font = ("Ariel", 30), align = "left")
                turtle.goto(-250,-100)
                turtle.write(sixth_m.answer3, font = ("Ariel", 30), align = "left")
                def check(x,y):
                        da=math.sqrt(math.pow(-250-x, 2) + math.pow(100-y,2))
                        if(da<30):
                                turtle.clear()
                                turtle.goto(0,0)
                                turtle.color("white")
                                turtle.write("wrong!!", font = ("Ariel", 60), align = "center")
                                playagain()
                        db=math.sqrt(math.pow(-250-x, 2) + math.pow(0-y,2))
                        if(db<30):
                                turtle.clear()
                                turtle.goto(0,0)
                                turtle.color("white")
                                turtle.write("wrong!!", font = ("Ariel", 60), align = "center")
                                playagain()
                        dc=math.sqrt(math.pow(-250-x, 2) + math.pow(-100-y,2))
                        if(dc<30):
                                global score
                                turtle.clear()
                                turtle.goto(0,0)
                                turtle.color("white")
                                turtle.write("congratiulations!!", font = ("Ariel", 60), align = "center")
                                score=score+200
                                playagain()
                turtle.onscreenclick(check)
        if(x==2):
                f=four_m.correct_answer
                turtle.clear()
                turtle.goto(0,200)
                turtle.color("black")
                turtle.write(four_m.riddle_Text, font = ("Ariel", 13), align = "center")
                turtle.goto(-250,100)
                turtle.write(four_m.answer1, font = ("Ariel", 30), align = "left")
                turtle.goto(-250,0)
                turtle.write(four_m.answer2, font = ("Ariel", 30), align = "left")
                turtle.goto(-250,-100)
                turtle.write(four_m.answer3, font = ("Ariel", 30), align = "left")
                def check(x,y):
                        da=math.sqrt(math.pow(-250-x, 2) + math.pow(100-y,2))
                        if(da<30):
                                global score
                                turtle.clear()
                                turtle.goto(0,0)
                                turtle.color("white")
                                turtle.write("congratiulations!!", font = ("Ariel", 60), align = "center")
                                score=score+200
                                playagain()
                        db=math.sqrt(math.pow(-250-x, 2) + math.pow(0-y,2))
                        if(db<30):
                                turtle.clear()
                                turtle.goto(0,0)
                                turtle.color("white")
                                turtle.write("wrong!!", font = ("Ariel", 60), align = "center")
                                playagain()
                        dc=math.sqrt(math.pow(-250-x, 2) + math.pow(-100-y,2))
                        if(dc<30):
                                turtle.clear()
                                turtle.goto(0,0)
                                turtle.color("white")
                                turtle.write("wrong!!", font = ("Ariel", 60), align = "center")
                                playagain()
                turtle.onscreenclick(check)
        if(x==3):
                f=first_m.correct_answer
                turtle.clear()
                turtle.goto(0,200)
                turtle.color("black")
                turtle.write(first_m.riddle_Text, font = ("Ariel", 13), align = "center")
                turtle.goto(-250,100)
                turtle.write(first_m.answer1, font = ("Ariel", 30), align = "left")
                turtle.goto(-250,0)
                turtle.write(first_m.answer2, font = ("Ariel", 30), align = "left")
                turtle.goto(-250,-100)
                turtle.write(first_m.answer3, font = ("Ariel", 30), align = "left")
                def check(x,y):
                        da=math.sqrt(math.pow(-250-x, 2) + math.pow(100-y,2))
                        if(da<30):
                                turtle.clear()
                                turtle.goto(0,0)
                                turtle.color("white")
                                turtle.write("wrong!!", font = ("Ariel", 60), align = "center")
                                playagain()
                        db=math.sqrt(math.pow(-250-x, 2) + math.pow(0-y,2))
                        if(db<30):
                                global score
                                turtle.clear()
                                turtle.goto(0,0)
                                turtle.color("white")
                                turtle.write("congratiulations!!", font = ("Ariel", 60), align = "center")
                                score=score+200
                                playagain()
                        dc=math.sqrt(math.pow(-250-x, 2) + math.pow(-100-y,2))
                        if(dc<30):
                                turtle.clear()
                                turtle.goto(0,0)
                                turtle.color("white")
                                turtle.write("wrong!!", font = ("Ariel", 60), align = "center")
                                playagain()
                turtle.onscreenclick(check)

def choosehard():
        x=random.randint(1,random.randint(2,3))
        if(x==1):
                f=seventh_h.correct_answer
                turtle.clear()
                turtle.goto(0,200)
                turtle.color("black")
                turtle.write(seventh_h.riddle_Text, font = ("Ariel", 13), align = "center")
                turtle.goto(-250,100)
                turtle.write(seventh_h.answer1, font = ("Ariel", 30), align = "left")
                turtle.goto(-250,0)
                turtle.write(seventh_h.answer2, font = ("Ariel", 30), align = "left")
                turtle.goto(-250,-100)
                turtle.write(seventh_h.answer3, font = ("Ariel", 30), align = "left")
                def check(x,y):
                        da=math.sqrt(math.pow(-250-x, 2) + math.pow(100-y,2))
                        if(da<30):
                                turtle.clear()
                                turtle.goto(0,0)
                                turtle.color("white")
                                turtle.write("wrong!!", font = ("Ariel", 60), align = "center")
                                playagain()
                        db=math.sqrt(math.pow(-250-x, 2) + math.pow(0-y,2))
                        if(db<30):
                                global score
                                turtle.clear()
                                turtle.goto(0,0)
                                turtle.color("white")
                                turtle.write("congratiulations!!", font = ("Ariel", 60), align = "center")
                                score=score+300
                                playagain()
                        dc=math.sqrt(math.pow(-250-x, 2) + math.pow(-100-y,2))
                        if(dc<30):
                                turtle.clear()
                                turtle.goto(0,0)
                                turtle.color("white")
                                turtle.write("wrong!!", font = ("Ariel", 60), align = "center")
                                playagain()
                turtle.onscreenclick(check)
        if(x==2):
                f=e_h.correct_answer
                turtle.clear()
                turtle.goto(0,200)
                turtle.color("black")
                turtle.write(e_h.riddle_Text, font = ("Ariel", 13), align = "center")
                turtle.goto(-320,100)
                turtle.write(e_h.answer1, font = ("Ariel", 25), align = "left")
                turtle.goto(-320,0)
                turtle.write(e_h.answer2, font = ("Ariel", 25), align = "left")
                turtle.goto(-320,-100)
                turtle.write(e_h.answer3, font = ("Ariel", 25), align = "left")
                def check(x,y):
                        da=math.sqrt(math.pow(-320-x, 2) + math.pow(100-y,2))
                        if(da<30):
                                turtle.clear()
                                turtle.goto(0,0)
                                turtle.color("white")
                                turtle.write("wrong!!", font = ("Ariel", 60), align = "center")
                                playagain()
                        db=math.sqrt(math.pow(-320-x, 2) + math.pow(0-y,2))
                        if(db<30):
                                turtle.clear()
                                turtle.goto(0,0)
                                turtle.color("white")
                                turtle.write("wrong!!", font = ("Ariel", 60), align = "center")
                                playagain()
                        dc=math.sqrt(math.pow(-320-x, 2) + math.pow(-100-y,2))
                        if(dc<30):
                                global score
                                turtle.clear()
                                turtle.goto(0,0)
                                turtle.color("white")
                                turtle.write("congratiulations!!", font = ("Ariel", 60), align = "center")
                                score=score+300
                                playagain()
                turtle.onscreenclick(check)
        if(x==3):
                f=nn_h.correct_answer
                turtle.clear()
                turtle.goto(0,200)
                turtle.color("black")
                turtle.write(nn_h.riddle_Text, font = ("Ariel", 13), align = "center")
                turtle.goto(-250,100)
                turtle.write(nn_h.answer1, font = ("Ariel", 30), align = "left")
                turtle.goto(-250,0)
                turtle.write(nn_h.answer2, font = ("Ariel", 30), align = "left")
                turtle.goto(-250,-100)
                turtle.write(nn_h.answer3, font = ("Ariel", 30), align = "left")
                def check(x,y):
                        da=math.sqrt(math.pow(-250-x, 2) + math.pow(100-y,2))
                        if(da<30):
                                global score
                                turtle.clear()
                                turtle.goto(0,0)
                                turtle.color("white")
                                turtle.write("congratiulations!!", font = ("Ariel", 60), align = "center")
                                score=score+300
                                playagain()
                        db=math.sqrt(math.pow(-250-x, 2) + math.pow(0-y,2))
                        if(db<30):
                                turtle.clear()
                                turtle.goto(0,0)
                                turtle.color("white")
                                turtle.write("wrong!!", font = ("Ariel", 60), align = "center")
                                playagain()
                        dc=math.sqrt(math.pow(-250-x, 2) + math.pow(-100-y,2))
                        if(dc<30):
                                turtle.clear()
                                turtle.goto(0,0)
                                turtle.color("white")
                                turtle.write("wrong!!", font = ("Ariel", 60), align = "center")
                                playagain()
                turtle.onscreenclick(check)
while run:
        scorew.clear()
        scorew.write(str(score), font = ("Ariel", 30), align = "center")

