import tkinter as tk
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}


# -------------- GET WORD --------------------------------#
try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("./data/jp_vocab.csv")    
finally:
    jp_words = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(jp_words)
    canvas.itemconfig(language_text, text="Japanese", fill="black")
    canvas.itemconfig(word_text, text=current_card["Japanese"], fill="black")
    canvas.itemconfig(canvas_img, image=front_img)

    flip_timer = window.after(3000, func=flip_card)

    
def flip_card():
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_img, image=back_img)


def is_known():
    jp_words.remove(current_card)
    data = pd.DataFrame(jp_words)
    data.to_csv("./data/words_to_learn.csv")
    next_card()



# --------------------- UI SETUP ------------------------#
window = tk.Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = tk.Canvas(width=800, height=526)
front_img = tk.PhotoImage(file="./images/card_front.png")
back_img = tk.PhotoImage(file="./images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

language_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

check_img = tk.PhotoImage(file="./images/right.png")
check_btn = tk.Button(image=check_img, highlightthickness=0, command=is_known)
check_btn.grid(row=1, column=1)
x_img = tk.PhotoImage(file="./images/wrong.png")
x_btn = tk.Button(image=x_img, highlightthickness=0, command=next_card)
x_btn.grid(row=1, column=0)

next_card()

window.mainloop()
