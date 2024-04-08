import turtle
import random

STARTING_X = 280

turtle.colormode(255)


class Cars:
    def __init__(self):
        self.cars = []
        self.starting_y = random.randint(-280, 280)
        car = turtle.Turtle()
        car.shape("square")
        car.shapesize(stretch_len=2, stretch_wid=1)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        car.color(r, g, b)
        car.penup()
        car.goto(STARTING_X, self.starting_y)
        self.cars.append(car)
        self.y = self.starting_y

    def create_car(self):
        y_new = random.randint(-280, 280)
        if self.y - y_new > 15 or y_new - self.y >15:
            car = turtle.Turtle()
            car.shape("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            car.color(r, g, b)
            car.penup()
            car.goto(STARTING_X, y_new)
            self.cars.append(car)
        else:
            if self.y - y_new < 15:
                while((self.y - y_new) < 15):
                    y_new -= 2
            if y_new - self.y < 15:
                while(y_new - self.y < 15):
                    y_new += 2
            car = turtle.Turtle()
            car.shape("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            car.color(r, g, b)
            car.penup()
            car.goto(STARTING_X, y_new)
            self.cars.append(car)
        self.y = y_new

    def move(self):
        for i in self.cars:
            new_x = i.xcor() - 20
            i.goto(new_x, i.ycor())



