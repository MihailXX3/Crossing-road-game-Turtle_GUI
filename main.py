from turtle import Screen
from crossing_turtle import CrossingTurtle
from scoreboard import Scoreboard
from carmanager import CarManager
import time
# Importing screen and set up the screen.
# Importing crossing_turtle, scoreboard, carmanager and time.
# Activate the key to respond.
screen = Screen()
screen.tracer(0)
scoreboard = Scoreboard()
car_manager = CarManager()
turtle = CrossingTurtle()
screen.listen()
screen.title("CROSSING ROAD GAME")
screen.setup(800, 800)
# The turtle should go only upward.
screen.onkey(turtle.go_up, "Up")

game_on = True
while game_on:
    # While game_on car should be generate and move.
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    # When turtle reach the border, go back to the start position and change to the upper level.
    if turtle.ycor() >= 390:
        scoreboard.num_level += 1
        turtle.refresh()
        scoreboard.scoreboard_place()
    # If car touch the turtle, then the game should stop and print "Game over!".
    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
