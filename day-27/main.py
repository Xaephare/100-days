from tkinter import *


def button_clicked():
    user_text = entry.get()
    label.config(text=user_text)


window = Tk()
window.title("First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
label = Label(text="I am a Label", font=('Arial', 24))
label["text"] = "Something else"
label.config(text="Something else")
label.grid(column=0, row=0)
label.config(padx=50, pady=50)

# Button
button = Button(text="Click Me", command=button_clicked)
button2 = Button(text="Second Button")
button.grid(column=1, row=1)
button2.grid(column=2, row=0)

# Entry
entry = Entry(width=20)
print(entry.get())
entry.grid(column=3, row=2)

window.mainloop()
