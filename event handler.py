from tkinter import *

window = Tk()
window.title("event handler")
window.geometry("100x100")

# event handler for keypress
def handle_keypress(event):
    """Print the character associated to the key that's been pressed."""
    print(event.char)

# bind keypress event to handle_keypress function
window.bind("<Key>", handle_keypress)

# event handler for button click
def handle_click(event):
    print("Button was clicked")

button = Button(text="Click me.")
button.pack()

# bind click event to handle_click
button.bind("<Button-1>", handle_click)

window.mainloop()