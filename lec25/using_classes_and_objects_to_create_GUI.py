from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("744x377")
        self.title("GUI With Class And Objects")

    def statusbar(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusBar = Label(self, textvariable=self.var, relief=SUNKEN, anchor="w").pack(side=BOTTOM, fill=X)
    def createbutton(self, text):
        Button(text=text, command=self.click).pack()

    def click(self):
        print("Button Clicked")

if __name__ == "__main__":
    window = GUI()
    window.statusbar()
    window.createbutton("Click Me")
    window.mainloop()
