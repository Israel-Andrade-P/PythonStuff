import random

print("Welcome to the Password Generator")

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
symbols = ["!", "@", "#", "$", "%", "&", "*", "(", ")", "=", "+", "-"]

nr_lettes = int(input("How many letters do you want?"))
nr_nums = int(input("How many digits?"))
nr_syms = int(input("How many special characters?"))

password = []

for _ in range(0, nr_lettes):
    password.append(random.choice(chars))

for _ in range(0, nr_nums):
    password.append(random.choice(numbers))

for _ in range(0, nr_syms):
    password.append(random.choice(symbols))

random.shuffle(password)    

final_password = ""

for char in password:
    if type(char) == int:
        char = str(char)
    final_password += char

print(f"Your password is: {final_password}")