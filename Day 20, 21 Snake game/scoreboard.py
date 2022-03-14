from turtle import *
score = 0

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,280)
        self.update()

    def update(self):
        self.write(f"score = {score}", False, align="center", font=("times new roman", 12, "bold"))

    def increase_score(self):
        global score
        score += 1
        self.clear()
        self.update()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER", False, align="center", font=("arial", 18, "bold"))
        self.goto(0,-20)
        self.write(f"your final score was {score}", align ="center", font = ("arial",12,"normal"))