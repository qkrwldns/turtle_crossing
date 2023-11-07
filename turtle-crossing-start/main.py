import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(tim.move,"Up")

make_car = 0
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # make_car += 1
    car.make_more_car()
    car.move_car()
    if tim.ycor() >= 280:
        tim.goto(0,-280)
        car.up_speed()
        score.up_score()

    for each_car in car.cars:
        if tim.distance(each_car) < 20:
            score.know_game_over()
            game_is_on = False

    # if tim.distance(car.head) <= 20:
    #     game_is_on = False

screen.exitonclick()


