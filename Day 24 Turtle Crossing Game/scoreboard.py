from turtle import Turtle
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()      # works even when the super bracket is kept empty
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 270)
        self.write_score()

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write_score()

    def write_score(self):
        self.write(f"level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!!!", align="center", font =("arial", 26, "bold"))
        self.goto(0,-30)
        self.write(f"Your final level was: {self.level}", align="center", font=FONT)