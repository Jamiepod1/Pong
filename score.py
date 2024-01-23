from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()



    def update(self, left_score, right_score):
        self.clear()
        self.goto(-40, 240)
        self.write(arg=left_score, align="center", font=("Verdana", 50, "normal"))
        self.goto(40, 240)
        self.write(arg=right_score, align="center", font=("Verdana", 50, "normal"))
        self.goto(0, -250)
        self.write(arg="|\n\n|\n\n|\n\n|\n\n|\n\n|", align="center", font=("Verdana", 50, "normal"))

