from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.score = 0
        self.write(f"Score: {self.score}", align="center",
                   font=("Arial", 24, "normal"))

    def score_update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center",
                   font=("Arial", 24, "normal"))
