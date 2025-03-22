alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def caesar(direction: str, original_text: str, shift_amount: int):
    cypher_message = ""

    for letter in original_text:
        if not alphabet.__contains__(letter):
            cypher_message += letter
        else :
            if direction == "encode":
                shifted_position = alphabet.index(letter) + shift_amount
            else:
                shifted_position = alphabet.index(letter) - shift_amount    
 
            shifted_position %= len(alphabet)
            cypher_message += alphabet[shifted_position]   
    print(f"Your {direction}d message is: {cypher_message}")
   
while True:
    direction = input("Type encode to encrypt, type decode to decrypt:\n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n").lower())
    caesar(direction, text, shift)
    answer = input("Type 'yes' if you want to go again, otherwise type 'no': \n").lower()
    if answer == "no":
        print("Thanks for supporting, come again!")
        break   


    

