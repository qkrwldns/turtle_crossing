from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 1
        self.goto(-200, 250)
        self.write(f"Level:{self.score}", align="center", font=FONT)

    def up_score(self):
        self.clear()
        self.score += 1
        self.write(f"Level:{self.score}", align="center", font=FONT)

    def know_game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"     Game Over \nyour final Level is {self.score}", align="center", font=FONT)
