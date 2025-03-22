from turtle import Turtle

PADDLE_SPEED = 40

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.create_paddle()


    def create_paddle(self):
            self.shape("square")
            self.penup()
            self.shapesize(stretch_wid=5, stretch_len=1)
            self.color("white")
            self.goto(self.position)
            
    def up(self):
         new_ycor = self.ycor() + PADDLE_SPEED
         self.goto(self.xcor(), new_ycor) 

    def down(self):
         new_ycor = self.ycor() - PADDLE_SPEED
         self.goto(self.xcor(), new_ycor)           
            
