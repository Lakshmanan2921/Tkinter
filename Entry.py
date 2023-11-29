from tkinter import *
from tkinter import messagebox
win = Tk()
win.title("Entry")
win.iconbitmap("js icon.ico")
win.geometry("800x400")


def summit():
     n = entry.get()
     messagebox.showinfo("summit", n)
def clear():
    entry.delete(0, END)
    entry2.delete(0, END)



name = Label(win,text="Name:", font=("Arial",15))
name.place(x=50, y=60)
entry = Entry(win, width=15,bg="#F8EFBA",bd=5,fg="#3B3B98",font=("Time", 15), highlightcolor="#2C3A47",highlightbackground="#EAB543",    insertbackground="#D6A2E8")
entry.place(x=160, y=60)

# Entry Widget
password = Label(win, text="Password:", font=("Arial",15))
password.place(x=50,y=100)
entry2 = Entry(win, width=15,bg="#F8EFBA", bd=5,fg="#3B3B98",font=("Time", 15),highlightcolor="#2C3A47",highlightbackground="#EAB543",insertbackground="#D6A2E8",show="*")
entry2.place(x=160,y=100)

# Button widget

button = Button(win, text="Click",bg="#8c7ae6",fg="green", command=summit,activebackground="yellow", activeforeground="red",font="Arial",
                relief="ridge")

button.place(x=200, y=200)

button2 = Button(win, text="Click",bg="#8c7ae6",fg="green", command=clear,activebackground="yellow", activeforeground="red",font="Arial",
                relief="ridge")

button2.place(x=300, y=200)
win.mainloop()
