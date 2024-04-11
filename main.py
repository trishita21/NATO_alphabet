import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

phonetic_dict = { row.letter : row.code for (index, row) in data.iterrows()}
#print(phonetic_dict)

# Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ")

phonetic = [ phonetic_dict[letter.upper()] for letter in word ]
print("The phonetic representation of the word is : ")
print(phonetic)