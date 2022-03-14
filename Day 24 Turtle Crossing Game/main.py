import time
from turtle import *
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.go_up)
screen.onkey(key="Down", fun=player.go_down)

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    # detecting collision with car
    for car in car_manager.all_cars:
        if player.distance(car) <= 20:
            # print("collide")
            scoreboard.game_over()
            game_on = False

    # detecting successful crossing

    # if player.ycor() >= player.FINISH_LINE_Y:
    if player.is_at_finshline():
        # print("success")
        scoreboard.increase_level()     # to increase level
        player.go_to_start()            # to set it again to start line
        car_manager.level_up()          # to increase car speed




screen.exitonclick()