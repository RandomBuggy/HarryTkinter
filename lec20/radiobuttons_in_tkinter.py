from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("650x344")
root.title("RadioButton Tutorial")

def order():
    tmsg.showinfo("Order Received!!", f"We have received your order for {var.get()}. Thanks for Ordering")

var = StringVar()
var.set("none")

Label(root, text="what would you like to have?", font="FiraCode-Regular 19 bold", justify=LEFT, padx=14).pack()

Radiobutton(root, text="Dosa", padx=14, variable=var, value="dosa").pack()
Radiobutton(root, text="Idly", padx=14, variable=var, value="idly").pack()
Radiobutton(root, text="Paratha", padx=14, variable=var, value="paratha").pack()
Radiobutton(root, text="Samosa", padx=14, variable=var, value="samosa").pack()

Button(root, text="Order Now!", command=order).pack()

root.mainloop()
