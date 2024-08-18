from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.goto(-280,240)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.score=self.score+1
        self.clear()
        self.write(f"Level:{self.score}",font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=(FONT))



