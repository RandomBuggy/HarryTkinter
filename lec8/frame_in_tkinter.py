from tkinter import *
root = Tk()
root.geometry("633x433")

#frame are just like div tag in html, it make many segment inside a window
frame1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
frame1.pack(side=LEFT, fill="y")
frame2 = Frame(root, bg="grey", borderwidth=8, relief= SUNKEN)
frame2.pack(side=TOP, fill="x")
label1 = Label(frame1, text="Project Tkinter")
label1.pack(pady=142)
label2 = Label(frame2, text="welcome to sublime text", font="FiraCode-Regular 14 underline", fg="red")
label2.pack()
root.mainloop()
