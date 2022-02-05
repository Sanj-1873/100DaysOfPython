from turtle import Turtle
SCOREBOARD_POSITION = (0, 270)
SCOREBOARD_FONT = ("Arial", 15, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self, score):
        self.score = score
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(SCOREBOARD_POSITION)
        self.write("SCORE : {}".format(score),False, align="center", font=SCOREBOARD_FONT)

    def refresh(self, score):
        self.clear()
        self.write("Score : {}".format(score),False, align=ALIGNMENT, font=SCOREBOARD_FONT)
        
        
        