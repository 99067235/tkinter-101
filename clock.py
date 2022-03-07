import tkinter as tk
from datetime import datetime
import time
import threading



window = tk.Tk()
window.configure(bg= "black")
window.geometry("500x500")


timer= tk.StringVar(value= "loading")


box1 = tk.Label(
    window,
    text="TIMER:",
    bg="black",
    fg="white",
    font=("Courier", 44)
)

box1.pack(
    ipadx=10,
    ipady=10
)

box2 = tk.Label(
    window,
    textvariable= timer,
    bg="black",
    fg="white",
    font=("Courier", 44)
)

box2.pack(
    ipadx=10,
    ipady=10
)

def clock():
    global timer
    i = 0
    while i < 1:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        timer.set(current_time)
        time.sleep(1)


threading.Timer(1.0, clock).start()

window.mainloop()


