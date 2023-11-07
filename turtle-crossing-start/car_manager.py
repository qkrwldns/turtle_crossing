from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def make_more_car(self):
        ran_car = random.randint(1,6)
        if ran_car == 1:
            car = Turtle(shape="square")
            car.penup()
            car.shapesize(1, 2)
            car.color(COLORS[random.randint(0, len(COLORS) - 1)])
            car.goto(300, random.randint(-250, 250))
            self.cars.append(car)

    def move_car(self):
        for i in self.cars:
            i.backward(self.car_speed)

    def up_speed(self):
        self.car_speed += MOVE_INCREMENT

