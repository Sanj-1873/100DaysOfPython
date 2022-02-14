import time
from turtle import Screen
from player import Player
from car_manager import CarManager
import random
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height= 600)
screen.tracer(0)


level_number = 1
player = Player()
scoreboard = Scoreboard(level_number)

screen.listen()
screen.onkey(player.move_turtle, "Up")

game_is_on = True
count = 1
car_list = []
move_speed = 0.1

while game_is_on:
    time.sleep(move_speed)
    screen.update()
    count = count +1

    if count % 6 == 0  :
        car = CarManager(random.randrange(-250,300))
        car_list.append(car)

    for moving_car in car_list:
        moving_car.move_car()
        if player.distance(moving_car) < 20: 
            # print("game over")
            
            game_is_on = False 
            scoreboard.game_over() 
    
            print("collision")

    # Detect level up 
    if player.ycor() > 290:
        player = Player()
        level_number = level_number + 1 
        scoreboard.reset_screen()
        scoreboard = Scoreboard(level_number)
        move_speed = move_speed - 0.01
        screen.listen()
        screen.onkey(player.move_turtle, "Up")



