from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.score_board_left()
        self.score_board_right()

    def score_board_left(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-390, 375)
        self.write(f"{self.score_left}", False, align="center", font=("Courier", 50, "bold"))

    def score_board_right(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(390, 375)
        self.write(f"{self.score_right}", False, align="center", font=("Courier", 50, "bold"))

    def left_score(self):
        self.score_left += 1
        self.clear()
        self.score_board_left()
        self.score_board_right()

    def right_score(self):
        self.score_right += 1
        self.clear()
        self.score_board_right()
        self.score_board_left()
