from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()

screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
starting_point = [-120,-75,-30,10,50,90]

racers = []
for racer in range(6):
    player = Turtle(shape="turtle")
    player.color(colors[racer])
    player.penup()
    player.goto(x=-230, y=starting_point[racer])
    
    racers.append(player)

print(racers)

if user_bet:
    is_race_on = True

winner = []

while is_race_on:
    for turtle in racers:
        if turtle.xcor() >= 230:
            winner.append(turtle.color())
            if winner[0][0] == user_bet:
                print("You win!\n The winner is {}".format(winner[0][0]))
            else:
                print("You lose.\n The winner is {}".format(winner[0][0]))
            is_race_on = False
            break
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()