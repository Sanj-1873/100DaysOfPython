from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Pong")
# screen.tracer(0)

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



# screen.update()    

screen.exitonclick()