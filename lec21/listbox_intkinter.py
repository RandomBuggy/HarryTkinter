from tkinter import *

def item():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i += 1

i = 0
root = Tk()
root.geometry("440x344")
root.title("ListBox Tutorial")

lbx = Listbox(root)
lbx.pack()

Button(root, text="Add Item", command=item).pack()

root.mainloop()
