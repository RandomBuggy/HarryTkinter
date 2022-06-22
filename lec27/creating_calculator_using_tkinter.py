from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"
                screen.update()
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("345x800")
root.title("Simple Calculator")

scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvariable=scvalue, font="FiraCode-Retina 40 bold")
screen.pack(fill=X, padx=10, pady=10)

f = Frame(root, bg="grey")
b = Button(root, text="9", padx=28, pady=18, font="FiraCode-Retina 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(root, text="8", padx=28, pady=18, font="FiraCode-Retina 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(root, text="7", padx=28, pady=18, font="FiraCode-Retina 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.grid(row=1, column=1)

f2 = Frame(root, bg="grey")
b = Button(root, text="6", padx=28, pady=18, font="FiraCode-Retina 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(root, text="5", padx=28, pady=18, font="FiraCode-Retina 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(root, text="4", padx=28, pady=18, font="FiraCode-Retina 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f2.grid(row=2, column=1)

f3 = Frame(root, bg="grey")
b = Button(root, text="3", padx=28, pady=18, font="FiraCode-Retina 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(root, text="2", padx=28, pady=18, font="FiraCode-Retina 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(root, text="1", padx=28, pady=18, font="FiraCode-Retina 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f3.grid(row=3, column=1)

f4 = Frame(root, bg="grey")
b = Button(root, text="0", padx=28, pady=18, font="FiraCode-Retina 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(root, text="+", padx=28, pady=18, font="FiraCode-Retina 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(root, text="-", padx=28, pady=18, font="FiraCode-Retina 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f4.grid(row=4, column=1)

f5 = Frame(root, bg="grey")
b = Button(root, text="*", padx=28, pady=18, font="FiraCode-Retina 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(root, text="/", padx=28, pady=18, font="FiraCode-Retina 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(root, text="%", padx=28, pady=18, font="FiraCode-Retina 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f5.grid(row=5, column=1)

f6 = Frame(root, bg="grey")
b = Button(root, text="=", padx=28, pady=18, font="FiraCode-Retina 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(root, text="C", padx=28, pady=18, font="FiraCode-Retina 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(root, text="=", padx=28, pady=18, font="FiraCode-Retina 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f6.grid(row=6, column=1)

root.mainloop()
