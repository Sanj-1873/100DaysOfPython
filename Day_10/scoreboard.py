from turtle import Turtle
SCOREBOARD_POSITION = (0, 270)
SCOREBOARD_FONT = ("Arial", 15, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.color("white")
        # self.high_score = 10
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.goto(SCOREBOARD_POSITION)
        self.write("SCORE : {}  High Score: {}".format(self.score, self.high_score),False, align="center", font=SCOREBOARD_FONT)




    def update_scoreboard(self):
        self.clear()
        self.write("Score : {} High Score: {}".format(self.score, self.high_score),False, align=ALIGNMENT, font=SCOREBOARD_FONT)

    def reset(self): 
        if self.score >  self.high_score:
            with open("data.txt", mode="w") as data:
                data.write(str(self.score))
            self.high_score = self.score

        self.score = 0 
        self.update_scoreboard()
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0) 
    #     self.write("GAME OVER", False, align=ALIGNMENT, font=SCOREBOARD_FONT)