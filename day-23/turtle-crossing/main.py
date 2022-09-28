import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.move, 'space')

game_speed = 0.1
game_is_on = True
while game_is_on:
    time.sleep(game_speed)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect successful crossing
    if player.ycor() > 290:
        player.reset()
        car_manager.level_up()
        scoreboard.level_up()

screen.exitonclick()
