FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, level_number):
        super().__init__()
        self.clear()
        self.level_number = level_number
        self.penup()
        self.hideturtle()
        self.goto(-240, 250)
        self.write("Level:{}".format(self.level_number), font = FONT)

    def game_over(self):
        self.clear()
        self.write("GAME OVER!", font= FONT)
    
    def reset_screen(self):
        self.clear()

