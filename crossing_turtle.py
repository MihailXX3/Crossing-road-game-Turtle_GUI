from turtle import Turtle


class CrossingTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red", "green")
        self.penup()
        self.setheading(90)
        self.goto(0, -380)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def refresh(self):
        self.goto(0, -380)
