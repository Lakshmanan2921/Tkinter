from tkcalendar import *
from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("DatePicker")
win.iconbitmap("js icon.ico")


def date_picker():
    def my_calender():
        messagebox.showinfo("Date picker", cal.get_date())
    top = Toplevel(win)
    top.geometry("300x300")
    top.title("Date picker")
    top.iconbitmap("js icon.ico")
    cal = Calendar(top, selectmode='day', year=2023, month=12, day=8, date_pattern="dd/MM/yyyy")
    cal.pack(fill='both', expand=True)
    button = Button(top, text="Submit", command=my_calender, bd=4, padx=10, pady=10, bg="#F8EFBA", fg="#2C3A47")
    button.pack(pady=10)

w = 400
h = 400
sw = win.winfo_screenwidth()
sh = win.winfo_screenheight()
x = (sw/2)-(w/2)
y = (sh/2)-(h/2)
win.geometry("%dx%d+%d+%d" % (w, h, x, y))

# Button
button = Button(win, text="Calender",padx=10, pady=10, bd=2, bg="#27ae60",
                fg="#ecf0f1",command=date_picker,
                activebackground="yellow",
                activeforeground="red", font=("Arial", 15,  "bold"), relief="ridge"
                )
button.pack(pady=20)

win.mainloop()


