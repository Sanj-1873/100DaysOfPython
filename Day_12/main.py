from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from board import Board
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
board = Board()
board.update_scoreboard()
# Start game
game_is_on = True

move_speed = 0.1
count = 0 
while game_is_on:
    time.sleep(move_speed)
    
    screen.update()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()


    if ball.distance(player_1) < 50 and ball.xcor() > 320 or ball.distance(player_2) < 50 and ball.xcor() < -320:
        print("ball collision")
        ball.paddle_collision()
        count +=1

    if ball.xcor() > 380:
        print("missed it!")
        ball.reset_ball()
        board.player_2_point()
        board.update_scoreboard()
        move_speed = 0.1
        count = 0

    if ball.xcor() < -380:
        print("missed it!")
        ball.reset_ball()
        board.player_1_point()
        board.update_scoreboard()
        move_speed = 0.1
        count = 0
        
    if count == 3 and move_speed > 0:
        move_speed = move_speed - 0.01
        count = 0

    ball.move_ball()
    screen.listen()
    screen.onkey(player_1.up,"Up")
    screen.onkey(player_1.down, "Down")
    screen.onkey(player_2.up,"w")
    screen.onkey(player_2.down, "s")



screen.update()    

screen.exitonclick()