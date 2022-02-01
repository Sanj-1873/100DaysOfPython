from turtle import Turtle, Screen
import turtle
tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_clockwise():
    tim.right(5)
    # tim.forward(5)

def move_counterclockwise():
    tim.left(5)
    # tim.backward(5)

def reset():
    turtle.resetscreen()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="a", fun=move_counterclockwise)
screen.onkey(key="c", fun=reset)
screen.exitonclick()