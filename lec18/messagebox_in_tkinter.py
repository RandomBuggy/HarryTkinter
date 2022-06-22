from tkinter import *
import tkinter.messagebox as Tmsg

def myfunc():
    print("I am a very good and cute function")
    Tmsg.showinfo(title="MessageBox", message="own dialogue box")

def Help():
    print("I will help you")
    Tmsg.askquestion("gjfgddd", "do you do???")
    Tmsg.askretrycancel("ask retry", "do this!!")

root = Tk()
root.geometry("733x566")
root.title("Hey There!!!")

mymenu = Menu(root)
mymenu.add_command(label="File", command=myfunc)
mymenu.add_command(label="Exit", command=quit)
mymenu.config()

#yourmenubar = Menu(root)
#m1 = Menu(yourmenubar, tearoff=0)
#m1.add_command(label="New Project", command=myfunc)
#m1.add_command(label="Save", command=myfunc)
#m1.add_separator()
#m1.add_command(label="Save As", command=myfunc)
#m1.add_command(label="Print", command=myfunc)
m3 = Menu(mymenu, tearoff=0)
m3.add_command(label="Help", command=Help)
mymenu.add_cascade(label="Help", menu=m3)

root.config(menu=mymenu)
mymenu.add_cascade(label="File", menu=m3)

root.mainloop()
