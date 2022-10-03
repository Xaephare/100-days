import tkinter as tk


def convert():
    miles = float(miles_input.get())
    km = round(miles * 1.609344, 1)
    conversion_result.config(text=km)


# Window
window = tk.Tk()
window.title("Mile to Km Converter")
window.config(padx=40, pady=30)

# Labels
miles_label = tk.Label(text="Miles")
km_label = tk.Label(text="Km")
conversion_result = tk.Label(text=0)
is_equal_label = tk.Label(text="is equal to")

miles_label.grid(column=2, row=0)
km_label.grid(column=2, row=1)
conversion_result.grid(column=1, row=1)
is_equal_label.grid(column=0, row=1)

# Buttons
calc_button = tk.Button(text="Calculate", command=convert)
calc_button.grid(column=1, row=2)

# Entries
miles_input = tk.Entry()
miles_input.grid(column=1, row=0)
miles_input.config(width=13)

window.mainloop()
