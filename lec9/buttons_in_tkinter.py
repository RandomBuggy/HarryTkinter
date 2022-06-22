from tkinter import *

def hello():
    print("Hello Tkinter Buttons")

root = Tk()
root.geometry("1280x720")

frame = Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

button1 = Button(frame, fg="red", text="Print Now", command=hello)
button1.pack(side=LEFT, padx=12)
button2 = Button(frame, fg="red", text="Print Now", command=hello)
button2.pack(side=LEFT, padx=12)
button3 = Button(frame, fg="red", text="Print Now", command=hello)
button3.pack(side=LEFT, padx=12)
button4 = Button(frame, fg="red", text="Print Now", command=hello)
button4.pack(side=LEFT, padx=12)

root.mainloop()
