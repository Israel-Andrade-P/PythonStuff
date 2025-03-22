from turtle import Screen
from paddle import Paddle
from  ball import Ball
from scoreboard import Scoreboard
import time

WIDTH = 700
HEIGHT = 500

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle1 = Paddle((330, 0))
paddle2 = Paddle((-330, 0))
ball = Ball()
scoreboard = Scoreboard()

def game_loop():
    is_game_on = True

    while is_game_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()
        #Check wall collision
        if ball.ycor() > 240 or ball.ycor() < -240:
            ball.bounce_y()

        if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
            ball.bounce_x()

        if ball.xcor() > 380:
            ball.reset_position() 
            scoreboard.l_point()

        if ball.xcor() < -380:
            ball.reset_position() 
            scoreboard.r_point()
               
           


screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")

game_loop()






screen.exitonclick()