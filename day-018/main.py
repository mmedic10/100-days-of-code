import turtle
from turtle import Turtle, Screen
from random import choice,random,randint

timm = Turtle()
timm.shape("turtle")
timm.color("red")
turtle.colormode(255)

# Tkinter es una libreria que nos ayuda a grear interfaces de usuarios tambien conocido como GUI

#timm.forward(100)
#timm.right(90)
#timm.forward(100)


def square_turtle(steps):
    for i in range(4):
        timm.forward(steps)
        timm.right(90)

def move_and_draw(steps):
    pen_draw =True
    for i in range(50):
        timm.forward(steps)
        if pen_draw:
            timm.pendown()
            pen_draw=False
        else:
            timm.penup()
            pen_draw=True


def figure_angule():
    colors = ["blue","red","brown","black","cyan","green","orange","yellow","magenta","salmon"]
    for i in range(3,11):
        angule = 360/i
        for j in range(i):
            timm.forward(50)
            timm.right(angule)
        timm.pencolor(choice(colors))


def turtle_random_walk():
    colors = ["blue", "red", "brown", "black", "cyan", "green", "orange", "yellow", "magenta", "salmon"]
    direction =[0,90,180,270]
    for _ in range(200):
        angulo = choice(direction)
        timm.speed(randint(1,10))
        timm.width(randint(1,10))
        timm.pencolor(random_color())
        timm.setheading(angulo)
        timm.forward(30)


def random_color():
    r = randint(0,255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r,g,b)
    return random_color


timm.speed(0)

def draw_spirograph(size_of_graph):
    for _ in range(int(360/size_of_graph)):
        timm.color(random_color())
        timm.circle(100)
        timm.right(size_of_graph)



turtle_random_walk()


screen = Screen()
screen.exitonclick()