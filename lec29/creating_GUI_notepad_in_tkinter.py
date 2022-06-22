import os
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename

def newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    textArea.delete(1.0, END)

def openfile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textArea.delete(1.0, END)
        f = open(file, "rt")
        textArea.insert(1.0, f.read())
        f.close()

def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if file == "":
            file = None
        else:
            #save as a new file
            f = open(file, "wt")
            f.write(textArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
    else:
        #save the file
        f = open(file, "wt")
        f.write(textArea.get(1.0, END))
        f.close()

def quitapp():
    root.destroy()

def cut():
    textArea.event_generate(("<<Cut>>"))

def copy():
    textArea.event_generate(("<<Copy>>"))

def paste():
    textArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad", "Notepad By CodeWithHarry/RandomBuggy")

if __name__ == "__main__":
    root = Tk()
    root.title("Simple Notepad")
    root.geometry("445x355")
    #root.wm_iconbitmap("1.ico")

    #create textarea
    textArea = Text(root, font="FiraCode-Regular 12")
    textArea.pack(expand=True, fill=BOTH)
    file = None

    #create menubar
    menuBar = Menu(root)
    #file menu starts
    fileMenu = Menu(menuBar, tearoff=0)
    #open new file
    fileMenu.add_command(label="New", command=newfile)
    #open existing file
    fileMenu.add_command(label="Open", command=openfile)
    #save current file
    fileMenu.add_command(label="Save", command=savefile)
    #add a separator
    fileMenu.add_separator()
    #exit the editor
    fileMenu.add_command(label="Exit", command=quitapp)
    #add fileMenu as cascade to menuBar
    menuBar.add_cascade(label="File", menu=fileMenu)
    #file menu ends

    #edit menu starts
    editMenu = Menu(menuBar, tearoff=0)
    #add cut, copy and paste feature
    editMenu.add_command(label="Cut", command=cut)
    editMenu.add_command(label="Copy", command=copy)
    editMenu.add_command(label="Paste", command=paste)

    menuBar.add_cascade(label="Edit", menu=editMenu)
    #edit menu ends

    #help menu starts
    helpMenu = Menu(menuBar, tearoff=0)
    helpMenu.add_command(label="About Notepad", command=about)
    menuBar.add_cascade(label="Help", command=helpMenu)
    #help menu ends
    root.config(menu=menuBar)
    #adding scroll bar
    scrollBar = Scrollbar(textArea)
    scrollBar.pack(side=RIGHT, fill=Y)
    scrollBar.config(command=textArea.yview)
    textArea.config(yscrollcommand=scrollBar.set)
    #scroll bar done
    root.mainloop()
