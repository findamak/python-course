#  TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

import pandas

# Create dataframe from CSV.
nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

# Using dictionary comprehension together with iterrows to create a new dictionary.
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
nato_dict = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter a word: ").upper()

# List comprehension keyword method
# [new_item for item in list]
user_input_list = [nato_dict[key] for key in user_input]
print(user_input_list)

