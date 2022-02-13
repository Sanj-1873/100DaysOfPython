COLORS = ["red", "orange", "yellow", "green", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random
class CarManager(Turtle ):
    def __init__(self, y_pos):
        self.y_pos = y_pos
        super().__init__()
        self.penup()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.goto(300, self.y_pos)
       
    def move_car(self):
        self.backward(10)
        
        