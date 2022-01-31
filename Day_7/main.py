import turtle
from turtle import Turtle, Screen
from random import randrange

turtle.colormode(255)

timmy = Turtle()

timmy.shape("turtle")
timmy.color("green")

# Drawing a square 
for side in range(4):
    timmy.forward(100)
    timmy.left(90.0)
turtle.resetscreen()

#Draw a dashed line
for dashed in range(100):
    if dashed % 2 == 0:
        timmy.penup()
    else:
        timmy.pendown()
    timmy.forward(5)
turtle.resetscreen()

# Many shapes
for shape in range(3,11):   
    angle = 360 / shape
    for side in range(shape):
        timmy.pencolor(randrange(255),randrange(255),randrange(255))   
        timmy.forward(100)
        timmy.right(angle)
turtle.resetscreen()

# Random walk
timmy.width(10)
for walk in range(1000):
    timmy.forward(10)
    timmy.pencolor(randrange(255),randrange(255),randrange(255))
    direction = randrange(10000)
    if direction % 2 == 0:
        timmy.right(90)
    else:
        timmy.left(90)


screen = Screen()
screen.exitonclick()