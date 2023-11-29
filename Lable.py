from tkinter import *


win = Tk()
win.title("Button")
win.iconbitmap("js icon.ico")


# Label
label = Label(win, text="<Welcome to  our page>", bg="#192a56", bd=5,
              fg="#f5f6fa", padx=40, pady=10,
              relief=GROOVE
              )
label.pack()

win.mainloop()

