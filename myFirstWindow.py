from tkinter import *
import tkinter as tk
import time


counter = 1
counter2 = 2000
width = 100
height = 100
Kleuren = ['white', 'yellow', 'orange', 'red', 'purple', 'black']

def uitbreiden():
    global counter, width, height
    window.configure(bg=(Kleuren[counter]))        # pakt steeds de volgende kleur uit de lijst
    window.geometry("{}x{}".format(width, height)) # veranderd de grootte van de window
    print(counter + 1)                             # print het getal

    if counter == 5:
        window.after(2000, window.destroy)


    counter += 1
    width += 50
    height += 50

window = tk.Tk()
window.title("my first window")
window.geometry("50x50")

print("1")
for i in range(5):
    window.after(counter2, uitbreiden)
    counter2 += 2000

window.mainloop()
print("BOOM!!!")