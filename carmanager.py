from turtle import Turtle
import random

STARTING_MOVE_DISTANCE = 5
COLOR = ["orange", "purple", "green", "blue"]


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        # Create a car only when number is == 1, otherwise the number of spawn cars in the screen will be too much.
        if random_chance == 1:
            new_car = Turtle()
            new_car.color(random.choice(COLOR))
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            random_y = random.randint(-350, 350)
            new_car.goto(380, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
