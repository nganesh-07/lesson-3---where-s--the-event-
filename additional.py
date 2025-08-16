import tkinter as tk

def fahrenheit2celsius():
    """Convert the value for Fahrenheit to Celsius and insert the result into lbl_result."""
    fahrenheit = ent_temperature.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

# create fahrenheit entry frame with an Entry - widget and label in it as well
frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

# layout temp entry and label in frm_entry using the .grid() geometry manager
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

# create conversion button and result display label
btn_convert = tk.Button(
    master=window,
    text="-->",
    command=fahrenheit2celsius
)
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

# setup the layout using the .grid() geometry manager
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

window.mainloop()