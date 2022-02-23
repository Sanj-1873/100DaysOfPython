from turtle import Turtle

class States(Turtle):
    def __init__(self, state_name, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x_cor, y_cor)
        self.write(state_name, align="center")