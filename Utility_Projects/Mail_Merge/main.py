#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

PLACEHOLDER = "[name]"

with open("/Users/Notebook/Python/Mail_Merge/Mail Merge Project Start/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    
        

with open("/Users/Notebook/Python/Mail_Merge/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    
for name in names:
    stripped_name = name.strip()
    updated_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
    with open(f"/Users/Notebook/Python/Mail_Merge/Mail Merge Project Start/Output/ReadyToSend/inv_{stripped_name}.txt", "w") as f:
        f.write(updated_letter)
    
    






    


    
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp