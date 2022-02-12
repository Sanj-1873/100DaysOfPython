from turtle import Turtle, Screen
# screen = Screen()

MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.penup()
        self.color("white")
        # screen.register_shape("rectangle",((0,0),(0,100),(20,100),(20,0)))
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        # self.left(90)
        self.goto(x=x_pos, y=y_pos)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)