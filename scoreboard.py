from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.score = 0
        with open("data.txt", "r") as f:
            self.high_score = int(f.read())
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center",
                   font=("Arial", 24, "normal"))

    def score_update(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as f:
                f.write(f"{self.high_score}")

        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center",
                   font=("Arial", 24, "normal"))

    def score_reset(self):
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center",
                   font=("Arial", 24, "normal"))
