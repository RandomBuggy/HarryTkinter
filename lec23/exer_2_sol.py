from tkinter import *

def update():
    root.geometry(f"{width.get()}x{height.get()}")

root = Tk()
root.geometry("544x344")
root.title("Exercise 2 Solution")

width = StringVar()
height = StringVar()

Entry(root, textvariable=width).pack()
Entry(root, textvariable=height).pack()

Button(root, text="Apply", command=update).pack()

root.mainloop()
