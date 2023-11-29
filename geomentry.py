from tkinter import *

win = Tk()
win.title("Geometry")
'''frame = Frame(win, bg="light green", width=200, height=100)
frame.pack(fill=BOTH, side=LEFT, expand=True)

frame2 = Frame(win, bg="red", width=200, height=100)
frame2.pack(fill=BOTH, side=RIGHT, expand=True)'''

'''name = Label(win, text="Name")
name.grid(row=0, column=0)
e1 = Entry(win)
e1.grid(row=0, column=1, ipadx=5, ipady=5,padx=5, pady=5)

password = Label(win, text="password")
password.grid(row=2, column=0)
e2 = Entry(win)
e2.grid(row=2, column=1, ipadx=5, ipady=5,padx=5, pady=5)

button = Button(win, text="Submit")
button.grid(row=4, column=0)'''

button = Button(win, text="place1", bg="sky blue")
button.place(x=90, y=50)

button2 = Button(win, text="button2", bg="green")
button2.place(x=50, y=80)

win.mainloop()