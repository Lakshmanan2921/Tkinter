from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("List_box")
win.geometry("500x400")
win.iconbitmap("js icon.ico")
win.config(bg="#16a085")


def sumbit():
    data = txtData.get()
    list_box.insert(END, data)


def select():
    data = list_box.get(ANCHOR)
    messagebox.showinfo("Selected", data)


def update():
    if (txtData.get() != ""):
        update_id = list_box.index(ANCHOR)
        update_txt_data = txtData.get()
        list_box.delete(ANCHOR)
        list_box.insert(update_id, update_txt_data)
        txtData.delete(0, END)
    else:
        messagebox.showinfo("UPDATE", "Could you place select any option")


def delete():
    list_box.delete(ANCHOR)
    txtData.delete(0, END)


def clearall():
    for item in reversed(list_box.curselection()):
        list_box.delete(item)



label = Label(win, text="List_box", bg="#1289A7", fg="White",
              padx=30, pady=5, font=("Times", 25, "bold"))
label.pack(fill=X)

mdata = StringVar()
txtData = Entry(win, width=30, textvariable=mdata,bd=3)
txtData.pack(pady=10)

list_box = Listbox(win, width=25, height=10, selectmode=EXTENDED, bd=5)
list_box.pack(pady=10)

# list_box.bind("<<ListboxSelect>>", List_bind)

sumbit_button = Button(win, text="Submit", padx=25, pady=10, bg="#C4E538", fg="#1B1464",
                       font=("Times", 10, "bold"), command=sumbit)
sumbit_button.place(x=50, y=120)
select_button = Button(win, text="Select", padx=28, pady=10, bg="#2980b9", fg="#ecf0f1",
                       font=("Times", 10, "bold"), command=select)
select_button.place(x=50, y=200)

update_button = Button(win, text="Update", padx=25, pady=10, bg="#ecf0f1", fg="#2c3e50",
                       font=("Times", 10, "bold"), command=update)
update_button.place(x=350, y=120)

delete_button = Button(win, text="Delete", padx=25, pady=10, bg="#e74c3c", fg="#ecf0f1",
                       font=("Times", 10, "bold"), command=delete)
delete_button.place(x=350, y=200)
Clear_button = Button(win, text="ClearAll", padx=20, pady=10, bg="#e74c3c", fg="#ecf0f1",
                      font=("Times", 13, "bold"), command=clearall)
Clear_button.place(x=190, y=290)

win.mainloop()
