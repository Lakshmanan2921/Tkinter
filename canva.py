from tkinter import *

win = Tk()
win.title("canvas")

ca = Canvas(win, width=400, height=400, bg="brown")
ca.pack()

ca.create_line(0, 200, 400, 200)


win.mainloop()
