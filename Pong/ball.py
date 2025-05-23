from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def increase_speed(self):
        self.x_move += 1
        self.y_move += 1    

    def bounce_y(self):
         self.y_move *= -1 

    def bounce_x(self):
        self.x_move *= -1   
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()