from tkinter import *
import pandas as pd
import random as rd

BACKGROUND_COLOR = "#B1DDC6"

# --------------------------------- WORD DICTIONARY -------------------------------------
df = pd.read_csv('data/french_words.csv')
word_dictionary = df.to_dict(orient='records')

# --------------------------------- FLASH CARD MECHANISM -------------------------------------

def new_card():
    current_card = rd.choice(word_dictionary)
    canvas.itemconfig(flash_title, text="French")
    canvas.itemconfig(flash_word, text=f"{current_card['French']}")

# --------------------------------- UI -------------------------------------
# --------------------------------- UI -------------------------------------

window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')
canvas.create_image(400, 263, image=card_front)
flash_title = canvas.create_text(400, 150, text="", font=('Courier', 30, 'italic'))
flash_word = canvas.create_text(400, 263, text="", font=('Courier', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=3)

check_img = PhotoImage(file='./images/right.png')
x_img = PhotoImage(file='./images/wrong.png')

check_button = Button(image=check_img, highlightthickness=0, command=new_card)
check_button.grid(column=2, row=1)

x_button = Button(image=x_img, highlightthickness=0, command=new_card)
x_button.grid(column=0, row=1)



new_card()

window.mainloop()
