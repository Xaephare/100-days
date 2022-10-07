import pandas


data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}

input = input("Enter the word: ").upper()
phonetic_output = [nato_dict[letter] for letter in input]
print(phonetic_output)
