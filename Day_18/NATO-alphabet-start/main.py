student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass
    # print(key)
    # print(value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
df = pandas.read_csv("nato_phonetic_alphabet.csv")

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # print("Index {}".format(index))
    # print(" Row \n {} \n end of row".format(row.score))
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
# print(df)

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
# dict_df =  {df['letter']:df['code'] for (index, row) in df.iterrows}

NATO_dict = { row.letter: row.code for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("What is your name?")
user_word = user_word.upper()
phonetic_code = []
for letter in user_word:
    phonetic_code.append(NATO_dict[letter])

print("The phonetic conversion is: {}".format(phonetic_code))
