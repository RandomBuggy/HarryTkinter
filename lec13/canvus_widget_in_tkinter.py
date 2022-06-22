from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("My GUI")

canvas_widget = Canvas(root, width=canvas_width, height=canvas_height)
canvas_widget.pack()

#co-ordinate x1, y1 to x2, y2
canvas_widget.create_line(0, 0, 800, 400, fill="red")
canvas_widget.create_line(0, 400, 800, 0, fill="red")

#co-ordinate top-left to bottom-right
canvas_widget.create_rectangle(25, 30, 700, 300, fill="green")
#center of the canvas
canvas_widget.create_text(400, 200, text="Python")
#co-ordinate top-lelf to bottom-right where inside oval will be fitted
canvas_widget.create_oval(344, 233, 244, 355)

root.mainloop()
