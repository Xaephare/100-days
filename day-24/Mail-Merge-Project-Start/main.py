with open('Input/Names/invited_names.txt') as names:
    content = names.read()
    name_list = content.split('\n')

with open('Input/Letters/starting_letter.txt') as letter:
    content = letter.read()
    for name in name_list:
        new_letter = content.replace("[name]", name)
        with open(f"Output/ReadyToSend/letter_to_{name}.txt", 'w') as final:
            final.write(new_letter)
