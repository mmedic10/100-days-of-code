import colorgram
import turtle
from turtle import Turtle, Screen
from random import choice,random,randint

turtle.screensize(canvwidth=20, canvheight=20)

timm = Turtle()
timm.pensize(10)
turtle.colormode(255)


colors_pic = colorgram.extract('pic.jpg',25)
colores = []
rgb = []
for color in colors_pic:
    rgb = []
    for i in color.rgb:
        rgb.append(i)
    colores.append(tuple(rgb))




def move_and_draw():
    timm.hideturtle()
    pos_x = -200
    pos_y = -200
    for _ in range(10):
        timm.teleport(pos_x,pos_y)
        for _ in range(10):
            timm.dot(20, choice(colores))
            timm.penup()
            timm.forward(50)
            timm.pendown()
        pos_y+=50


move_and_draw()
screen = Screen()
screen.exitonclick()