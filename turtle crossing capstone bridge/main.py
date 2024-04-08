from turtle import Screen
from player import Player
from cars import Cars
import time
from scoreboard import Scoreboard

screen = Screen()
player = Player()
cars = Cars()
scoreboard = Scoreboard()

screen.setup(600,600)
screen.title("Turtle Crossing Capstone Bridge")
screen.listen()
screen.onkey(key="Up", fun=player.move)
screen.tracer(0)

game_is_on = True
count = 0
level = 1
speed = 0.1

while game_is_on:
    screen.update()
    time.sleep(speed)
    count += 1
    cars.move()
    if count % 6 == 0:
        cars.create_car()
    for i in cars.cars:
        if player.distance(i) < 15:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor()>280:
        level += 1
        speed = speed - 0.025
        player.redirect()
        scoreboard.incre_level()
    if level > 3:
        game_is_on = False
        scoreboard.level_over()


screen.exitonclick()