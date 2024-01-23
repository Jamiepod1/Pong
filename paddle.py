from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, start_co_ords):
        super().__init__()
        self.start_co_ords = start_co_ords
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.score = 0
        self.reset()
        self.move_status = "still"
        self.move_register_timer = 1



    def reset(self):
        self.goto(self.start_co_ords[0], self.start_co_ords[1])

    def reset_move_register_timer(self):
        if self.move_register_timer > 0:
            self.move_register_timer -= 1
        else:
            self.move_status = "still"

    def up(self):
        current_y = self.ycor()
        if current_y < 240 and self.move_register_timer == 0:
            self.setposition(self.xcor(), current_y + 50)
            self.move_status = "up"
            self.move_register_timer = 15

    def down(self):
        current_y = self.ycor()
        if current_y > -240 and self.move_register_timer == 0:
            self.setposition(self.xcor(), current_y - 50)
            self.move_status = "down"
            self.move_register_timer = 15

    def update_score(self):
        self.score += 1
