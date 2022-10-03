import tkinter as tk

window = tk.Tk()
window.title("First GUI Program")
window.minsize(width=500, height=300)

# Label

label = tk.Label(text="I am a Label", font=('Arial', 24))
label.pack()



window.mainloop()
