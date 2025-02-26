import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    return random.choice(cards)

def calculate_score(cards_list):
    if sum(cards_list) == 21 and len(cards_list) == 2:
        return 0
    
    if 11 in cards_list and sum(cards_list) > 21:
        cards_list.remove(11)
        cards_list.append(1)

    return sum(cards_list)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has Blackjack"
    elif u_score == 0:
        return "Win, with Blackjack"
    elif u_score > 21:
        return "You went over, you lose"
    elif c_score > 21:
        return "Computer went over, you win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"      

def play_game():
    player_cards = []
    computer_cards = []
    player_score = -1
    computer_score = -1

    for _ in range(2):
        computer_cards.append(deal_card())
        player_cards.append(deal_card())

    while True:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"Your cards: {player_cards}, current score: {player_score}")

        print(f"Computer's first card: {computer_cards[0]}")

        if  player_score == 0 or computer_score == 0 or player_score > 21:
            break
        else:
            answer = input("Type y to get another card or type n to pass: ")
            if answer == "y":
                player_cards.append(deal_card())
            else:
                break

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(player_score, computer_score))

while input("Do you want to play a game of Blackjack? y/n: ") == "y":
    play_game()

print("Bye!")    


