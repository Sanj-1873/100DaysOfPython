import time
from turtle import Screen
from player import Player
from car_manager import CarManager
import random
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height= 600)
screen.tracer(0)



player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_turtle, "Up")

game_is_on = True
count = 1
car_list = []
while game_is_on:
    time.sleep(0.1)
    screen.update()
    count = count +1

    if count % 6 == 0  :
        car = CarManager(random.randrange(-250,300))
        car_list.append(car)

    for moving_car in car_list:
        moving_car.move_car()
        if player.distance(moving_car) < 20: 
            # print("game over")
            scoreboard.game_over()
            game_is_on = False 
            break 
    
            print("collision")


