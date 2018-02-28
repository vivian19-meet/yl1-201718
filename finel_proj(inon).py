import turtle
money = 0
MODE = 0

def easyMode():
    print("easy")
    MODE = 1
def mediumMode():
    print("medium")
    MODE = 2
def hardMode ():
    print("hard")
    MODE = 3
turtle.onkeypress(easyMode, "e")
turtle.onkeypress(mediumMode, "m")
turtle.onkeypress(hardMode, "h")
turtle.listen()


if MODE == 1:
    if mode == True:
        money = money+2000
    else:
        turtle.sleep(1)


if MODE == 2:
    if mode == True:
        money = money+7500
    else:
        turtle.sleep(1)

if MODE == 3:
    if mode == True:
        money = money+15000
    else:
        turtle.sleep(1)
    
       
