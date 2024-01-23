from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

screen = Screen()
screen.setup(width=1000, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(left_paddle.up, "q")
screen.onkey(left_paddle.down, "a")
screen.onkey(right_paddle.up, "p")
screen.onkey(right_paddle.down, ";")

#scoreboard.update(left_paddle.score, right_paddle.score, left_paddle, right_paddle)
#ball.move(left_paddle, right_paddle)
#ball.goto(370, left_paddle.ycor() + 60)
#print(ball.distance(left_paddle))
#screen.update()


game_is_on = True
while game_is_on:
    update = False
    scoreboard.update(left_paddle.score, right_paddle.score)
    ball.move(left_paddle, right_paddle)

    if ball.xcor() > 600:
       left_paddle.score += 1
       update = True

    elif ball.xcor() < -600:
        right_paddle.score += 1
        update = True

    if update:
        ball.reset()
        scoreboard.update(left_paddle.score, right_paddle.score)
        update = False


    left_paddle.reset_move_register_timer()
    right_paddle.reset_move_register_timer()
    time.sleep(0.001)
    screen.update()

screen.exitonclick()
