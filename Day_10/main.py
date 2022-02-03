from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = []
starting_point = [0,-20,-40]
for snake_pos in range(3):
    body = Turtle(shape="square")
    body.color("white")
    body.penup()
    body.goto(x=starting_point[snake_pos], y=0)
    snake.append(body)
    screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(snake)-1, 0, -1):
        new_x = snake[seg_num - 1].xcor()
        new_y = snake[seg_num - 1].ycor()
        snake[seg_num].goto(new_x, new_y)
    
    snake[0].forward(20)

screen.exitonclick()