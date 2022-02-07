from turtle import Turtle, Screen
screen = Screen()

MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.penup()
        self.color("white")
        screen.register_shape("rectangle",((0,0),(0,100),(20,100),(20,0)))
        self.shape("rectangle")
        self.left(90)
        self.goto(x=x_pos, y=y_pos)

    def up(self):
        self.forward(MOVE_DISTANCE)
    
    def down(self):
        self.backward(MOVE_DISTANCE)