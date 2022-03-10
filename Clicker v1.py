import tkinter as tk
import tkinter
from tkinter import *

root = tk.Tk()
root.configure(bg="grey")
root.geometry("500x500")
root.title("clicker")

root.counter = 0

def color():
    if root.counter == 0:
        root.configure(bg= "grey")
    elif root.counter < 0:
        root.configure(bg= "red")
    else:
        root.configure(bg="green")

### optellen
def up():
    root.counter += 1
    Mylabel['text'] = str(root.counter)
    color()
        

### aftellen
def down():
    root.counter -= 1
    Mylabel['text'] = str(root.counter)
    color()
    
### button optellen
b = Button(root, text="Up", height=2, width=30, command=up)
b.pack()

### label getal
Mylabel = Label(root, text="0", height=2, width=30  )
Mylabel.pack()

### button aftellen
b = Button(root, text="Down", height=2, width=30, command=down)
b.pack()




root.mainloop()