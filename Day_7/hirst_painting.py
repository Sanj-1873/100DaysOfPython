import colorgram
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
screen = Screen()
screen_size = screen.screensize()
x_start_position = 0.0 
y_start_position = 0.0 
hirst = Turtle()
hirst.penup()

hirst.setpos((x_start_position, y_start_position))


#Create color palette
colors = colorgram.extract('image.jpg', 20)
palette = []
for color in colors:
    rgb_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
    palette.append(rgb_tuple)


# Draw

for dots in range(10):
    for dot in range(10):
        hirst.pendown()
        hirst.dot(20, random.choice(palette))
        hirst.penup()
        hirst.forward(40)

    hirst.setx(0.0)
    hirst.right(90)
    
    hirst.forward(40)
    hirst.left(90)





screen.exitonclick()



