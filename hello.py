import tkinter as tk

window = tk.Tk()

window.title("Hello")
window.configure(bg="black")
window.geometry("200x200")

box1 = tk.Label(
    window,
    text="""Hello
    tkinter!""",
    bg="blue",
    fg="white"
)

box1.pack(
    ipadx=50,
    ipady=50
)

window.mainloop()