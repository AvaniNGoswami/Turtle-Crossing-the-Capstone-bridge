from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-270,270)
        self.hideturtle()
        self.level = 1
        self.write(f"Level : {self.level}",24)

    def incre_level(self):
        self.clear()
        self.goto(-270, 270)
        self.level += 1
        self.write(f"Level : {self.level}", 24)

    def game_over(self):
        self.clear()
        self.goto(-25,0)
        self.write(f"GAME OVER \nYOU REACHED LEVEL : {self.level}", 24)

    def level_over(self):
        self.clear()
        self.goto(-25, 0)
        self.write("CONGRATULATIONS GAME IS OVER \nYOU HAVE COMPLETED ALL THE LEVELS", 24)

