from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Check_button")
root.iconbitmap("js icon.ico")
root.geometry("500x400")
root.config(bg="#00a8ff")


def submit():
    if c1.get() == 1:
        val = chk1.cget("text")
        messagebox.showinfo("message", val)
    if (c2.get() == 1):
        val = chk2.cget("text")
        messagebox.showinfo("message", val)
    if (c3.get() == 1):
        val = chk3.cget("text")
        messagebox.showinfo("message", val)


def clear():
    chk1.deselect()
    chk2.deselect()
    chk3.deselect()
    messagebox.showinfo("clear", "the check buttons are deselect")


c1 = IntVar()
c2 = IntVar()
c3 = IntVar()
label = Label(root, text="Checkbutton_Demo", bg="#e84118", fg="White",
              padx=30, pady=5, font=("Times", 25, "bold"))
label.pack(fill=X)

chk1 = Checkbutton(root, text="Dosa", variable=c1, onvalue=1, offvalue=0, bg="#00a8ff")
chk2 = Checkbutton(root, text="Idle", variable=c2, onvalue=1, offvalue=0, bg="#00a8ff")
chk3 = Checkbutton(root, text="Rise", variable=c3, onvalue=1, offvalue=0, bg="#00a8ff")

chk1.pack()
chk2.pack()
chk3.pack()

btnsub = Button(root, text="submit", bg="#05c46b", fg="white", pady=10, padx=30, width=10,
                font=("times", 15, "bold"), command=submit)
btnclr = Button(root, text="clear", bg="#f53b57", fg="white", pady=10, padx=30, width=10,
                font=("times", 15, "bold"), command=clear)

btnsub.pack()
btnclr.pack()

root.mainloop()
