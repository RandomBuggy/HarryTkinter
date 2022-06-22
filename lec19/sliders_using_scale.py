from tkinter import *
import tkinter.messagebox as Tmsg

root = Tk()
root.geometry("1280x720")
root.title("Slider Using Scale")

#myslider = Scale(root, from_ = 0, to = 100)
#myslider.pack()

def getdollar():
    print(f"we have credited {myslider2.get()} dollars to your bank account")
    Tmsg.showinfo("Transaction Info", f"we have credited {myslider2.get()} dollars to your bank account successfully")

Label(root, text="How many Dollars do you want???").pack()
myslider2 = Scale(root, from_ = 0, to = 500, orient = HORIZONTAL, tickinterval=100)
myslider2.set(350)
myslider2.pack()
Button(root, text="Get Dollars!!", command=getdollar).pack()

root.mainloop()
