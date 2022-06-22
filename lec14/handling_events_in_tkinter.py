from tkinter import *

def harry(event):
    print(f"You have clicked on pixel {event.x}, {event.y}")

root = Tk()

root.title("Events in Tkinter")
root.geometry("644x344")

widget = Button(root, text="Please Click Me")
widget.pack()

widget.bind("<Button-1>", harry)
widget.bind("<Double-1>", quit)

root.mainloop()
