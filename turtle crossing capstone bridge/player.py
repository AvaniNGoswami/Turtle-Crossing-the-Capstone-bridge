from turtle import Turtle

STARTING_X = 0
STARTING_Y = -285

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(STARTING_X, STARTING_Y)
        self.shape("turtle")
        self.left(90)

    def move(self):
        new_y = self.ycor()+10
        self.goto(0,new_y)

    def redirect(self):
        self.goto(STARTING_X, STARTING_Y)