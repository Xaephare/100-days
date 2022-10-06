from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    with open('data.txt', 'a') as data:
        data.write(f"{website} | {username} | {password}\n")
    website_entry.delete(0, 'end')
    username_entry.delete(0, 'end')
    username_entry.insert(0, "youremail@email.com")
    password_entry.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
mypass_logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=mypass_logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Text boxes
website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky='EW')
website_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2, sticky='EW')
username_entry.insert(0, "youremail@email.com")

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky='EW')

# Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3, sticky='EW')

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky='EW')

window.mainloop()
