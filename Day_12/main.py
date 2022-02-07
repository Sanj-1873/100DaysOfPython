from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


# Create board 
line = Turtle()
line.color("white")
line.penup()
line.goto(0,300)
line.right(90)
line.pendown()

for make_board in range(600):
    if make_board % 2 == 0:
        line.pendown()
        line.forward(10)
        
    else:
        line.penup()
        line.forward(20)



player_1 = Paddle(350,0)
player_2 = Paddle(-350, 0)
ball = Ball()


# Start game
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    if(ball.ycor() > 290 or ball.ycor() < -290 ):
        ball.bounce()
        ball.move_ball()
    else:
        ball.move_ball()
    screen.listen()
    screen.onkey(player_1.up,"Up")
    screen.onkey(player_1.down, "Down")
    screen.onkey(player_2.up,"w")
    screen.onkey(player_2.down, "s")
    screen.update()


screen.update()    

screen.exitonclick()