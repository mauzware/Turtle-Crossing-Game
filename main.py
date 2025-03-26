import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


jerry = Player()
car_manager = CarManager()
score = Scoreboard()
screen.listen()
screen.onkey(jerry.move_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(jerry) < 20:
            game_is_on = False
            score.game_over()

    if jerry.ycor() > 280:
        jerry.reset_player()
        score.level_increase()
        car_manager.speed_up()

screen.exitonclick()
