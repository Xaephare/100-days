from tkinter import *
import pandas as pd
import random as rd
import pandas.errors

BACKGROUND_COLOR = "#B1DDC6"

# --------------------------------- WORD DICTIONARY ------------------------------
try:
    df = pd.read_csv('data/to_learn.csv')
except FileNotFoundError:
    df = pd.read_csv('data/french_words.csv')
except pandas.errors.EmptyDataError:
    df = pd.read_csv('data/french_words.csv')
finally:
    word_dictionary = df.to_dict(orient='records')
# --------------------------------- NEW CARD -------------------------------------

current_card = {}


def remove_from_list():
    try:
        word_dictionary.remove(current_card)
    except ValueError:
        pass
    finally:
        to_learn_df = pd.DataFrame.from_dict(word_dictionary)
        to_learn_df.to_csv('data/to_learn.csv', index=False)
        new_card()


def new_card():
    global current_card, timer
    window.after_cancel(timer)
    try:
        current_card = rd.choice(word_dictionary)
    except IndexError:
        canvas.itemconfig(flash_card, image=card_front)
        canvas.itemconfig(flash_title, text="You've finished", fill='black')
        canvas.itemconfig(flash_word, text="Well Done!", fill='black')
    else:
        canvas.itemconfig(flash_card, image=card_front)
        canvas.itemconfig(flash_title, text="French", fill='black')
        canvas.itemconfig(flash_word, text=f"{current_card['French']}", fill='black')
        timer = window.after(3000, flip_card, current_card)


def flip_card(old_card):
    canvas.itemconfig(flash_card, image=card_back)
    canvas.itemconfig(flash_title, text="English", fill='white')
    canvas.itemconfig(flash_word, text=f"{old_card['English']}", fill='white')


# --------------------------------- UI -------------------------------------

window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, flip_card, current_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')
flash_card = canvas.create_image(400, 263, image=card_front)
flash_title = canvas.create_text(400, 150, text="", font=('Courier', 30, 'italic'))
flash_word = canvas.create_text(400, 263, text="", font=('Courier', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=3)

check_img = PhotoImage(file='./images/right.png')
x_img = PhotoImage(file='./images/wrong.png')

check_button = Button(image=check_img, highlightthickness=0, command=remove_from_list)
check_button.grid(column=2, row=1)

x_button = Button(image=x_img, highlightthickness=0, command=new_card)
x_button.grid(column=0, row=1)

new_card()

window.mainloop()
