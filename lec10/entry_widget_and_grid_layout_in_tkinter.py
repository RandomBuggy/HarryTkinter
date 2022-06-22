from tkinter import *

def getvals():
    print(f"The value of username is {uservalue.get()}")
    print(f"The value of password is {password.get()}")

root = Tk()

root.geometry("745x432")

user = Label(root, text="username")
password = Label(root, text="password")
user.grid()
password.grid(row=1)

#variable class in tkinter
#BooleanVar, DoubleVar, StringVar, IntVar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(root, text="Submit", command=getvals).grid()

root.mainloop()
