from tkinter import *

root = Tk()

#logic here

#geometry means width X height of the window
root.geometry("1180x720")
# atleast size of the window width, height
root.minsize(200, 100)
#atmost size of the window width, height
root.maxsize(600, 300)
#label is user-non-interactive widget
shakib = Label(text="shakib is a good boy")
shakib.pack()
root.mainloop()
