from turtle import Turtle

import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.shapesize(1, 1)
        self.x_move = random.randint(1, 10)
        self.y_move = random.randint(1, 10)
        self.move_speed = 0.02

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.increase_speed()

    def bounce_x(self):
        self.x_move *= -1
        self.increase_speed()

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.01
        self.bounce_x()

    def increase_speed(self):
        self.move_speed *= 0.9
