import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

play = Player()
car=CarManager()
score=Scoreboard()
screen.listen()
screen.onkeypress(play.up,"w")
screen.onkeypress(play.down,"s")
screen.onkeypress(play.left,"a")
screen.onkeypress(play.right,"d")


game_is_on = True
while game_is_on:
    screen.update()

    car.create_car()
    car.move_car()
    for i in car.all_cars:
        if i.distance(play)<20:
            game_is_on=False
            score.game_over()

    if play.finish():
        car.level_up()
        score.update_score()



screen.exitonclick()