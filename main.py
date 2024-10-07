from turtle import Turtle, Screen

from score import Score

from paddle import Paddle

from ball import Ball

import random
import time

screen = Screen()
screen.listen()
screen.tracer(0)  # <- does not show animation when tracer is 0, once screen.update is omitted
# it will update everything that has happened in the backend

score = Score()
ball = Ball()
paddle_left = Paddle((-870, 0))
paddle_right = Paddle((870, 0))

screen.setup(1800, 900)
screen.bgcolor("black")

screen.onkeypress(key="w", fun=paddle_left.go_up)
screen.onkeypress(key="s", fun=paddle_left.go_down)
screen.onkeypress(key="Up", fun=paddle_right.go_up)
screen.onkeypress(key="Down", fun=paddle_right.go_down)

coords = 0
for _ in range(20):
    line = Turtle()
    line.shapesize(.3, .3)
    line.color("white")
    line.shape("square")
    line.penup()
    line.sety(-430 + coords)
    coords += 45

start = True
while start:
    time.sleep(ball.move_speed)
    screen.update()  # <- in a while loop so that everytime something changed in the graphics
    # it will update the screen, for example the moving of paddle going up and down
    ball.move_ball()

    # ball bounce on upper wall
    if ball.ycor() > 420 or ball.ycor() < - 420:
        ball.bounce_y()

    # ball bounce with paddle
    if ball.distance(paddle_right) < 100 and ball.xcor() > 860 or ball.distance(
            paddle_left) < 100 and ball.xcor() < -860:
        ball.bounce_x()

    # pass right wall, left paddle score
    if ball.xcor() > 870:
        score.left_score()
        ball.reset_position()

    if ball.xcor() < -870:
        score.right_score()
        ball.reset_position()

screen.exitonclick()
