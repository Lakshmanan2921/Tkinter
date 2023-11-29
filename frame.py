from tkinter import *

root = Tk()
root.title("Frames")

frame = Frame(root)
frame.pack()

frame1 = Frame(root)
frame1.pack(side=LEFT)

frame2 = Frame(root)
frame2.pack(side=RIGHT)

name = Label(frame, text="frame on toop")
name.pack()

b1 = Button(frame1, text="button1", bg="pink", fg="white")
b1.pack()
b2 = Button(frame1, text="button2", bg="sky blue", fg="white")
b2.pack()

b3 = Button(frame2, text="button3", bg="purple", fg="white")
b3.pack()

b4 = Button(frame2, text="button4", bg="light green", fg="white")
b4.pack()

root.mainloop()