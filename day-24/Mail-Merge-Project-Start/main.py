with open('Input/Names/invited_names.txt') as names:
    content = names.read()
    name_list = content.split('\n')

with open('Input/Letters/starting_letter.txt') as letter:
    content = letter.read()
    for name in name_list:
        new_letter = content.replace("[name]", name)
        file_name = f"Output/ReadyToSend/letter_to_{name}.txt"
        with open(file_name, 'w') as final:
            final.write(new_letter)
