import pandas as pd

data = pd.read_csv("/Users/Notebook/Data_Science/NATO-alphabet-start/nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
answer = input("Type in a word: ").upper()

output_list = [nato_dict[letter] for letter in answer]

print(output_list)


