import random
from turtle import *
color("red")
shape("turtle")
speed(15)
pensize(6)
couleurs = ["blue","purple","cyan","black","yellow","green","orange","red","pink"]

def formev(taille):
    right(25)
    forward(taille)
    backward(taille)
    left(50)
    forward(taille)
    backward(taille)
    right(25)

def brancheFlocon(taille):
    for x in range(0,4):
        forward(taille)
        formev(taille)
    backward(taille*4)

def flocon(taille):
    for x in range(0,6):
        color(random.choice(couleurs))
        brancheFlocon(taille)
        right(60)
        right(20)
        left(32)
        forward(10)

for x in range(0,32):
    taille=random.randint(5,30)
    x= random.randint(-400, 400)
    y=random.randint(-400,400)
    penup()
    goto(x,y)
    pendown()
    flocon(taille)
    
    

hideturtle()
    
