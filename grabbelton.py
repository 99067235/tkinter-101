import tkinter as tk
from tkinter.ttk import Label
import random
import tkinter

window = tk.Tk()
window.configure(bg= "white")
window.geometry("500x500")
txtVar = tkinter.StringVar(value="Klik op de knop om te grabbelen.")
TextLabel = tkinter.Label(window,textvariable=txtVar).pack()

def grabbelen():
    clicks = 0
    randomChoice = random.choice(items)
    clicks += 1
    txtVar.set(f"Gefeliciteerd! Je hebt een {randomChoice} gegrabbelt!")

        

button = tk.Button(text= "Grabbelen", command= grabbelen)
button.pack(padx= 100, pady= 100)

items = ["aap", "stukje kaas", "drop veter zonder dropsmaak", "schoen", "rickroll", "autoband"]

window.mainloop()