from tkinter import *

root = Tk()
root.geometry("450x250")
root.title("More Tips Tricks And Functions")
root.wm_iconbitmap("1.ico")
root.configure(background="green")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"{width}x{height}")
Button(root, text="Close", command=root.destroy).pack()
root.mainloop()
