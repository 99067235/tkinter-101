from cgitb import text
import tkinter as tk
import time
from tkinter.tix import TEXT
from typing import Text


window = tk.Tk()
window.configure(bg= "black")
window.geometry("500x500")


uren = 0
minuten = 0
seconden = 0

timer = uren, ":", minuten, ":", seconden



box1 = tk.Label(
    window,
    text="TIMER:",
    bg="black",
    fg="white",
)

box1.pack(
    ipadx=10,
    ipady=10
)

box2 = tk.Label(
    window,
    text=timer,
    bg="black",
    fg="white",
)

box2.pack(
    ipadx=10,
    ipady=10
)

window.mainloop()

def secondenTimer():
    i = 0
    global seconden, minuten    
    for i in range(59):
        time.sleep(1)
        seconden += 1
        
    time.sleep(1)
    seconden = 0
    minuten += 1
    print(uren, ":", minuten, ":", seconden)
    secondenTimer()

secondenTimer()