import random

placeholder = ""
guess = ""
guess_list = []
hangman_limbs = ["Right leg", "Left leg", "Right arm" ,"Left arm" ,"Torso" , "Head", "You're clear"]

words = ["unicorn", "ogre", "dragon", "chimaera", "platypus"]
word = random.choice(words)

lives = 6

for letter in range(len(word)):
    placeholder += "_"
print(placeholder)    

while True:
    print(f"{lives} / 6 LIVES LEFT")
    while True:
        guess = input("Guess a letter: ").lower()
        if guess_list.__contains__(guess):
            print("You've already guessed that letter! Try again")
            continue
        else:
            guess_list.append(guess)
            break

    display = ""

    for i in range(len(word)):
        if guess_list.__contains__(word[i]):
            display += word[i]
        else:    
            display += "_"    

    if guess not in word:
        lives -= 1
        print(f"You've guessed {guess}, that's not in there, you lose a life")
        if lives == 0:
            print(f"**********IT WAS: {word} YOU LOSE**************************")
            break 
              
    print(display) 
    print(hangman_limbs[lives])

    if "_" not in display:
        print("******************YOU WIN**************************")
        break
    
