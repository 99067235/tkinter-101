import tkinter as tk
from tkinter.ttk import Label
import random
import tkinter
import time

window = tk.Tk()
window.configure(bg= "white")
window.geometry("500x500")
window.title("Grabbelton")
txtVar = tkinter.StringVar(value="Klik op de knop om te grabbelen.")
TextLabel = tkinter.Label(window,textvariable=txtVar).pack()

def grabbelen():
    clicks = 0
    randomChoice = random.choice(items)
    items.remove(randomChoice)
    clicks += 1
    txtVar.set(f"Gefeliciteerd! Je hebt een {randomChoice} gegrabbelt!")
    lengte = len(items)
    if lengte == 0:
        txtVar.set("Helaas de grabbelton is leeg, druk op 'close' om de window te sluiten")
        window.configure(bg= "black")
        button.destroy()
        button2 = tk.Button(text= "Close", command = close)
        button2.pack(padx= 100, pady= 100  )
    else:
        pass

def close():
    clicks = 0
    clicks += 1
    if clicks == 1:
        window.destroy()





button = tk.Button(text= "Grabbelen", command= grabbelen)
button.pack(padx= 100, pady= 100)

items = ["aap", "stukje kaas", "drop veter zonder dropsmaak", "schoen", "rickroll", "autoband"]

window.mainloop()