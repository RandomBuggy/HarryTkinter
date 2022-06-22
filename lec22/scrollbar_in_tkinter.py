from tkinter import *

root = Tk()
root.geometry("544x344")
root.title("Scroll Bar Tutorial")

#for connecting scroll bar to a widget
#1. widget(yscrollcommand = scrollbar.set())
#2. scrollbar.config(command=widget.yview)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

lbx = Listbox(root, yscrollcommand = scrollbar.set)

for i in range(1, 501):
    lbx.insert(END, f"Item {i}")
lbx.pack(fill=BOTH, padx=25)

scrollbar.config(command = lbx.yview)

root.mainloop()
