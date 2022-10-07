import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def convert_phonetic():
    user_input = input("Enter the word: ").upper()

    try:
        phonetic_output = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry only letters in the alphabet please.")
        convert_phonetic()
    else:
        print(phonetic_output)


convert_phonetic()
