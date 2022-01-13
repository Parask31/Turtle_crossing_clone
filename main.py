import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()

screen.onkeypress(fun=player.move_up, key="Up")


game_is_on = True

while game_is_on:

    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_car()

    # Detecting collision with the car
    for cars in car.all_car:
        if cars.distance(player) < 20:
            game_is_on = False

    # Detect successful crossing
    if player.ycor() > 280:
        player.go_to_start()
        car.level_up()
        score.update_lvl()
        score.scoreboard()


screen.exitonclick()
