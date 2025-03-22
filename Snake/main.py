from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

WIDTH = 600
HEIGHT = 600

screen = Screen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

def start_game():
    is_game_on = True
    while is_game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        
        if snake.head.distance(food) < 15:
            snake.extend()
            food.respawn()
            scoreboard.increase_score()
            
        # Check wall collision
        if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -290:
            scoreboard.reset_score()
            snake.reset_pos()
            

        # Check body collision
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
               scoreboard.reset_score()
               snake.reset_pos()
            
                
            
screen.setup(WIDTH, HEIGHT)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
         
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

start_game()

screen.exitonclick()


