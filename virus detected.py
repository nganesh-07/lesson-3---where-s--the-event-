from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

# function for displaying warning message - this will be called once the button is clicked
def msg():
    messagebox.showwarning("Alert!", "Virus found.")

# adding button widget to window
button = Button(root, text="Scan for virus", command=msg)
button.place(x=40, y=80)

root.mainloop()