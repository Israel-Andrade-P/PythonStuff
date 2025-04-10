import turtle as t
import pandas as pd

screen = t.Screen()
screen.title("U.S States Game")
image = "../blank_states_img.gif"
screen.addshape(image)
t.shape(image)

data = pd.read_csv("../50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)} / 50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("../states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t2 = t.Turtle()
        t2.penup()
        t2.hideturtle()
        state_data = data[data.state == answer_state]
        t2.goto(state_data.x.item(), state_data.y.item())
        t2.write(answer_state, move=False, align="center", font=("Courier", 8, "normal"))
        
    