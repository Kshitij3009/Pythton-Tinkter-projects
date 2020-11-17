# Importing Modules
from tkinter import *
from time import strftime

root = Tk()  # Creates tkinter_files window
root.title("Digital Computer Clock")  # Adds title to tkinter_files window

# Function used to display time on the label
def time():
    string = strftime("%H:%M:%S %p")
    lbl.config(text = string)
    lbl.after(1000, time)

# Styling the label widget which displays the clock
lbl = Label(root, font = ("arial", 160, "bold"),bg="black",fg="white")

# Pack method in tkinter_files packs widgets into rows or columns. Positions label
lbl.pack(anchor = "center",fill = "both",expand=1)

time()  # Time function is called

mainloop()   # Runs the application program
