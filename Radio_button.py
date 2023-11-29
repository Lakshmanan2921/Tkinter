from tkinter import *
from tkinter import messagebox


win = Tk()
win.title("Radio_button")
win.iconbitmap("js icon.ico")
win.config(bg="#487eb0")
win.geometry("500x400")

def sumt():
    if gender.get() == 1:
        data = male.cget("text")
        messagebox.showinfo("selected", data)
    elif gender.get() == 2:
        data = female.cget("text")
        messagebox.showinfo("selected", data)
    elif gender.get() == 3:
        data = other.cget("text")
        messagebox.showinfo("selected", data)


# label
label = Label(win, text="Checkbutton_Demo", bg="#00a8ff", fg="#f5f6fa",
              padx=30, pady=5, font=("Times", 25, "bold"))
label.pack(fill=X)

gender = IntVar()
male = Radiobutton(win,text="Male",variable=gender, value=1, bg="#487eb0",
                   font=("times", 15, "bold"))
female = Radiobutton(win,text="Female",variable=gender, value=2, bg="#487eb0",
                   font=("times", 15, "bold"))
other = Radiobutton(win,text="Other's",variable=gender, value=3, bg="#487eb0",
                   font=("times", 15, "bold"))

sunbt = Button(win, text="Submit", bg="#f5f6fa", fg="#0097e6",
               font=("Times", 15, "bold"),  padx=10, pady=5,
               command=sumt, relief=RIDGE, bd=8)

# Radio_button placing
male.place(x=50, y=60)
female.place(x=200, y=60)
other.place(x=350, y=60)
# submit & clear Button placing
sunbt.place(x=200, y=150)

win.mainloop()
