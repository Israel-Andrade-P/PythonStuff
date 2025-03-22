from turtle import Turtle

ALIGMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as h_score:
            self.high_score = int(h_score.read())
        self.penup()
        self.color("white")
        self.setpos(0, 265)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGMENT, font=FONT)    

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", "w") as h_score:
                h_score.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()        

    #def game_over_text(self):
      #  self.setpos(0, 0)
       # self.write("GAME OVER", move=False, align=ALIGMENT, font=FONT)    
        
        