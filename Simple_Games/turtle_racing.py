import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ["red", "green", "blue", "orange", "yellow", "black", "purple", "brown", "cyan"]

def get_number_of_racers():
    while True:  
        racers = input("Enter the number of racers (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 10:
                break
            else:
                print("Please pick a number between 2 - 10")
        else:
            print("Please pick a number")
    return racers   

def race(colors):
    turtles = create_turles(colors)    

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


def create_turles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) +1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles    
       
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")         

racers = get_number_of_racers()   
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(f"The winner is the turtle with color: {winner}")
time.sleep(5)




