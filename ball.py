from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.reset()

    def reset(self):
        self.start_co_cords = random.choice(((300, 179), (-300, 179)))
        if self.start_co_cords == (300, 179):
            self.x_modifier = -3
        else:
            self.x_modifier = 3
        self.y_modifier = -4
        self.goto(self.start_co_cords)
        self.side_bounce_register = False
        self.bounce_register = False


    def move(self, left_paddle, right_paddle):

        #detect collision with wall
        if self.bounce_register:
            self.is_ball_clear_of_wall()
        elif self.ycor() >= 280 or self.ycor() <= -280:
            self.bounce_y()
        else:
        #detect collision with paddle
            if self.xcor() == 330 and self.distance(right_paddle) <= 60:
                self.bounce_x(right_paddle)

            elif self.xcor() == -330 and self.distance(left_paddle) <= 60:
                self.bounce_x(left_paddle)

            else:
                #detect collision with side of paddle
                if self.xcor() > 330 and self.distance(right_paddle) < 62:
                    if self.side_bounce_register == False:
                        self.prevent_clipping(right_paddle)
                        self.side_bounce(right_paddle)
                    else:
                        self.bounce_y(rebound_energy_loss=False)


                elif self.xcor() < -330 and self.distance(left_paddle) < 62:
                    if self.side_bounce_register == False:
                        self.prevent_clipping(left_paddle)
                        self.side_bounce(left_paddle)
                    else:
                        self.bounce_y(rebound_energy_loss=False)




        self.goto(self.xcor() + self.x_modifier, self.ycor() + self.y_modifier)

    def bounce_y(self, rebound_energy_loss=True):

        if self.y_modifier > 1 and rebound_energy_loss:
            self.y_modifier -= 1

        self.y_modifier *= -1

        if self.y_modifier > 1 and rebound_energy_loss:
            self.y_modifier -= 1



        print(self.y_modifier)
        self.bounce_register = True


    def bounce_x(self, paddle):
        if paddle.move_status == "up":
            self.y_modifier += 4
        elif paddle.move_status == "down":
            self.y_modifier -= 4

        self.x_modifier *= -1


    def side_bounce(self, paddle):
        if paddle.move_status == "up" and self.ycor() > paddle.ycor():
            self.bounce_y(rebound_energy_loss=False)
            self.y_modifier = 5
        elif paddle.move_status == "down" and self.ycor() < paddle.ycor():
            self.y_modifier = -5
            self.bounce_y(rebound_energy_loss=False)
        else:
            self.bounce_y(rebound_energy_loss=False)

        self.side_bounce_register = True

    def prevent_clipping(self, paddle):
        if self.ycor() > paddle.ycor():
            self.goto(self.xcor(), paddle.ycor() + 62)
            print("clipping prevented")
        else:
            self.goto(self.xcor(), paddle.ycor() - 62)
            print("clipping prevented")




    def is_ball_clear_of_wall(self):
        if self.ycor() < 280 or self.ycor() > -280:
            self.bounce_register = False

        else:

            pass


    def random_number(self):
        return 1 if random.random() < 0.5 else -1






