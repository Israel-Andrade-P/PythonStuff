bidders = {}

while True:
    name = input("What is your name: ")
    bid_amount = int(input("What is your bid: $"))
    bidders[name] = bid_amount
    
    answer = input("Are there any other bidders? (yes | no)\n").lower()
    if answer == "no":
        break
    print("\n" * 100)

def get_highest_bidder(bidding_dictionary):
    highest_amount = 0
    
    winner = max(bidding_dictionary, key=bidding_dictionary.get)

    return winner

    '''
    for key in bidding_dictionary:
        if bidding_dictionary[key] > highest_amount:
            highest_amount = bidding_dictionary[key]
            winner = key
    return winner, highest_amount    
    '''    

winner = get_highest_bidder(bidders)

print(f"The winner is {winner}, with bid amount ${bidders[winner]}")    