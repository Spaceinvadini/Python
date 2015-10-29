from graphics import *
import random
from random import randint

window = GraphWin("Visualisation", 1000, 750)

with open("data.txt","r") as f:
    content = f.read().splitlines()
    content.sort()
    print(content)

counter1 = 0
counter2 = 0
counter3 = 0
xspeed = randint(1, 7)
yspeed = randint(1, 7)
xspeed2 = randint(1, 7)
yspeed2 = randint(1, 7)
xspeed3 = randint(1, 7)
yspeed3 = randint(1, 7)
for i in content:
    xpos = float(i)
    i = float(i)
    if((i >= 30) and (i <= 40)):
        ranxpos = randint(400, 550) 
        ranypos = randint(30, 730)
        counter1 += 20
        coloradd = float(i) + counter1
        ball3 = Circle(Point(ranxpos, ranypos), xpos)
        ball3.setFill(color_rgb(0,coloradd,0))
        ball3.draw(window)
    elif((i >= 41) and (i <= 61)):
        xranpos = randint(30,300)
        yranpos = randint(30, 720)
        counter2 += 15
        colorredadd = float(i) + counter2
        ball2 = Circle(Point(xranpos, yranpos), xpos)
        ball2.setFill(color_rgb(colorredadd,0,0))
        ball2.draw(window)
    elif (i >= 62):
        ranposx = randint(740, 910) 
        ranposy = randint(85, 665)
        counter3 += 15
        colorblueadd = float(i) + counter3
        ball = Circle(Point(ranposx, ranposy), xpos)
        ball.setFill(color_rgb(0, 0, colorblueadd))
        ball.draw(window)

        
while True:
    currentPos = ball.getCenter()
    if(currentPos.getY() >= 85): yspeed = -yspeed
    if(currentPos.getY() <= 665): yspeed = -yspeed
    if(currentPos.getX() >= 740): xspeed = -xspeed
    if(currentPos.getX() <= 910): xspeed = -xspeed
    ball.move(xspeed, yspeed)
    currentPos2 = ball2.getCenter()
    if(currentPos2.getY() >= 60): yspeed2 = -yspeed2
    if(currentPos2.getY() <= 690): yspeed2 = -yspeed2
    if(currentPos2.getX() >= 60): xspeed2 = -xspeed2
    if(currentPos2.getX() <= 240): xspeed2 = -xspeed2
    ball2.move(xspeed2, yspeed2)
    currentPos3 = ball3.getCenter()
    if(currentPos3.getY() >= 40): yspeed3 = -yspeed3
    if(currentPos3.getY() <= 710): yspeed3 = -yspeed3
    if(currentPos3.getX() >= 390): xspeed3 = -xspeed3
    if(currentPos3.getX() <= 510): xspeed3 = -xspeed3
    ball3.move(xspeed3, yspeed3)
        
window.getMouse()