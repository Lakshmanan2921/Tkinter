from tkinter import *
from tkinter import ttk
from tkinter import messagebox

win = Tk()
win.title("Combo_box")
win.geometry("800x400")
win.iconbitmap("js icon.ico")



def boxclick(get_msg):
    msg = c_box.get()
    msg2 =c_box2.get()
    msg3 = c_box3.get()
    msg4 = En.get()
    if En.get() != "":
        messagebox.showinfo("Message","Name: "+msg4+" "+"Gender: "+msg2)
        if c_box3.get() == "YES":
           messagebox.showinfo("Message", msg3+" I want to join "+msg)
        elif c_box3.get() == "NO":
           messagebox.showinfo("Message",  msg3 + " Not interested")
    else:
        messagebox.showwarning("Message", "Fill the Name")





# Tittle Label

name = Label(win, text="Name: ",bg="#706fd3",fg="#f7f1e3",font=("times",10,"bold"), padx=20)
name.place(x=400,y=90)
label = Label(win, text="Checkbutton_Demo", bg="#FFC312", fg="#0652DD",
              padx=30, pady=10, font=("Times", 25, "bold"))
label.pack(fill=X)
curses = Label(win, text="Curses: ",bg="#706fd3",fg="#f7f1e3",font=("times",15,"bold"), padx=20)
curses.place(x=75, y=90)

gender = Label(win, text="Gender:",bg="#706fd3",fg="#f7f1e3",font=("times",15,"bold"), padx=20)
gender.place(x=75, y=150)

YN = Label(win, text="Decision:", bg="#706fd3", fg="#f7f1e3",font=("times",15,"bold"), padx=20)
YN.place(x=75, y=200)
# Entry
En = Entry(win,bg="#ecf0f1",fg="#2c3e50")
En.place(x=490,y=90)
# Combo Box
options = ["C", "C++", "Java", "Python"]
c_box = ttk.Combobox(win, width=15, state="readonly", values=options)
c_box.current(0)
c_box.place(x=200, y=90)

c_box2 = ttk.Combobox(win, width=15, state="readonly")
c_box2['values'] = ("Male", "Female", "other")
c_box2.current(2)
c_box2.place(x=200, y=150)

c_box3 = ttk.Combobox(win, width=15, state="readonly")
c_box3['values'] = ("YES", "NO")
c_box3.current(0)
c_box3.place(x=200, y=200)
c_box3.bind("<<ComboboxSelected>>", boxclick)


win.mainloop()
