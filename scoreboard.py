from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.num_level = 1
        self.scoreboard_place()

    def scoreboard_place(self):
        self.clear()
        self.goto(-300, 360)
        self.write(f"Level:{self.num_level}", align="right", font=("Courier", 16, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align="center", font=("Courier", 26, "normal"))
