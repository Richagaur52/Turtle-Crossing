import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen=Screen()
screen.setup(width=600,height=600)
screen.tracer(0)


player=Player()
car=CarManager()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(player.go_up,"Up")
screen.onkey(player.go_left,"l")
screen.onkey(player.go_right,"k")

game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_car()

    for car1 in car.all_cars:
        if car1.distance(player)<20:
            game_is_on=False
            scoreboard.game_over()

    if player.is_complete() == True:
        player.go_to_start()
        car.car_speed_increase()
        scoreboard.increase_level()



screen.exitonclick()