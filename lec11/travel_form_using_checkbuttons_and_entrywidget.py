from tkinter import *
root = Tk()

def getvals():
    print("It Works!")

root.geometry("644x144")
Label(root, text="Welcome to Harry Travels", font="FiraCode-Regular 14 bold", pady=15).grid(row=0, column=3)

name = Label(root, text="Name")
phone = Label(root, text="phone")
gender = Label(root, text="gender")
emergency = Label(root, text="Emergency Contact")
paymentmode = Label(root, text="Payment Mode")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)

namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()

nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymentmodeentry = Entry(root, textvariable=paymentmodevalue)

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)

foodservice = Checkbutton(root, text="Want to prebook your meals?", variable=foodservicevalue)

foodservice.grid(row=6, column=3)

Button(root, text="Submit to Harry Travels", command=getvals).grid(row=7, column=3)

root.mainloop()
