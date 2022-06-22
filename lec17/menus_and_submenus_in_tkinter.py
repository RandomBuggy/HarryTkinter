from tkinter import *

def myfunc():
    print("I am a very good and cute function")

root = Tk()
root.geometry("733x566")
root.title("Hey There!!!")

mymenu = Menu(root)
mymenu.add_command(label="File", command=myfunc)
mymenu.add_command(label="Exit", command=quit)
mymenu.config()

yourmenubar = Menu(root)
m1 = Menu(yourmenubar, tearoff=0)
m1.add_command(label="New Project", command=myfunc)
m1.add_command(label="Save", command=myfunc)
m1.add_separator()
m1.add_command(label="Save As", command=myfunc)
m1.add_command(label="Print", command=myfunc)

root.config(menu=yourmenubar)
yourmenubar.add_cascade(label="File", menu=m1)
root.mainloop()
