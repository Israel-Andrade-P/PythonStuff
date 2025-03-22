import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(turtle.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars() 
    
    for car in car_manager.cars:
        if car.distance(turtle) < 20:
            scoreboard.game_over()
            game_is_on = False
            break

    if turtle.is_at_finish_line():
        turtle.reset_pos()
        car_manager.increase_speed()  
        scoreboard.pass_level()  

screen.exitonclick()

    
