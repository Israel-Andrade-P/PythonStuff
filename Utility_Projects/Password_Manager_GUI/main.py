import tkinter as tk
from tkinter import messagebox
from random import choice, randint, shuffle
import json
#import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in  range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)
    
    password = "".join(password_list)
    password_entry.insert(0, password)    
    #pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def create_or_append_file(data):
    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email":email,
            "password":password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                    message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it ok to save?")

        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)    
            except FileNotFoundError:
                 create_or_append_file(new_data)
            else:
                data.update(new_data)
                create_or_append_file(data)  
            finally:
                website_entry.delete(0, tk.END)    
                email_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)

# --------------------------- FIND PASSWORD -------------------------------#

def find_password():
    website = website_entry.get()     
    try:
        with open("data.json", "r") as data_file:
                data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="File doesn't exist")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email:{email}\nPassword:{password}")
        else:
            messagebox.showerror(title="Error", message=f"{website} hasn't been registered yet")    
                           
# ---------------------------- UI SETUP ------------------------------- #
screen = tk.Tk()
screen.title("Password Manager")
screen.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
pm_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pm_img)
canvas.grid(row=0, column=1)

#LABELS
website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = tk.Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0)

#ENTRIES
website_entry = tk.Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = tk.Entry(width=39)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1)

#BUTTONS
gen_password_btn = tk.Button(text="Generate Password", command=generate_password)
gen_password_btn.grid(row=3, column=2)
add_btn = tk.Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2)
search_btn = tk.Button(text="Search", width=14, command=find_password)
search_btn.grid(row=1, column=2)

screen.mainloop()