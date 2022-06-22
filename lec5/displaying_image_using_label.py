from tkinter import *
#pip install pillow
from PIL import Image, ImageTk

root = Tk()
#image is also a widget but non-interactive

root.geometry("1280x720")
#for jpg images supporting
#image = Image.open("image.jpg")
#photo = ImageTk.PhotoImage(image)
photo = PhotoImage(file="1.png")
label = Label(image=photo)
label.pack()
root.mainloop()
