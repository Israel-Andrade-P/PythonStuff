from art import logo
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def get_number():
    return randint(1, 100)


def get_guess():
    while True:
        guess = input("Guess a number between 1 - 100: ")
        if guess.isdigit():
            return int(guess)
        else:
            print(f"{guess} is not a valid number. Try again")   

def set_difficulty():
    answer = input("Type the difficulty you want to play (easy - hard): ")
    if answer == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def compare(rand_num,  u_guess):
    if u_guess > rand_num:
            print("Too high!  Try again")
    elif u_guess < rand_num:
            print("Too low! Try again")
    else:
        print(f"Correct! It was {rand_num}")


def play_game(number):
    print(logo)
    attempts = 0
    guess = 0
    print("Welcome to Guessing Number The Game!")

    attempts = set_difficulty()

    while guess != number:
        print(f"You have {attempts} attempts remaining to guess the number")

        guess = get_guess()
        attempts -= 1

        compare(number, guess)

        if attempts <= 0:
            print(f"You've run out of attempts! Number was: {number}")
            break

play_game(get_number())        







