from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 70, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.lscore = 0
        self.rscore = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 220)
        self.write(self.lscore, align=ALIGNMENT, font=FONT)
        self.goto(100, 220)
        self.write(self.rscore, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.lscore += 1
        self.update_scoreboard()

    def r_point(self):
        self.rscore += 1
        self.update_scoreboard()