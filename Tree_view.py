from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Window_Center import *
from tkinter import *


Tkinter_File(800, 600, "FileDialog")
global sno
sno = 1


def add_Record():
    if E_Name.get() != "" and E_Add.get() != "" and E_Con.get() != "" and E_mail.get() != "":

        my_Tree.insert("", index="end", iid=sno, values=(sno, E_Name.get(), E_Add.get(), E_Con.get(), E_mail.get()))

        E_Name.delete(0, END), E_Add.delete(0, END), E_Con.delete(0, END), E_mail.delete(0, END)
    else:
        messagebox.showinfo("Message", "Please fill all the Field")


def select_Record():
    E_Name.delete(0, END), E_Add.delete(0, END), E_Con.delete(0, END), E_mail.delete(0, END)
    selected = my_Tree.focus()
    values = my_Tree.item(selected, "values")
    E_Name.insert(0, values[1]), E_Add.insert(0, values[2])
    E_Con.insert(0, values[3]), E_mail.insert(0, values[4])


def Update_Record():
    if E_Name.get() != "" and E_Add.get() != "" and E_Con.get() != "" and E_mail.get() != "":
        no = my_Tree.focus()[0]
        my_Tree.item(no, values=(no, E_Name.get(), E_Add.get(), E_Con.get(), E_mail.get()))

        E_Name.delete(0, END), E_Add.delete(0, END), E_Con.delete(0, END), E_mail.delete(0, END)
    else:
        messagebox.showinfo("Message", "Please fill all the Field")


def delete_Record():
    record = my_Tree.selection()[0]
    my_Tree.delete(record)
    E_Name.delete(0, END), E_Add.delete(0, END), E_Con.delete(0, END), E_mail.delete(0, END)


def delete_many():
    record = my_Tree.selection()
    for data in record:
        my_Tree.delete(data)


def delete_all():
    for record in my_Tree.get_children():
        my_Tree.delete(record)


My_frame = Frame(win)
My_frame.pack()

# Name
Name = Label(My_frame, text="Name:", font=("Courier New", 15, "bold"), pady=5)
Name.grid(row=1, column=0, sticky=E)

E_Name = Entry(My_frame, font=("Helvetica", 10, "bold"))
E_Name.grid(row=1, column=1)

# Address
Add = Label(My_frame, text="Address:", font=("Courier New", 15, "bold"), pady=5)
Add.grid(row=2, column=0, sticky=E)

E_Add = Entry(My_frame, font=("Helvetica", 10, "bold"))
E_Add.grid(row=2, column=1)

# Contact
Con = Label(My_frame, text="Contact:", font=("Courier New", 15, "bold"), pady=5)
Con.grid(row=3, column=0, sticky=E)

E_Con = Entry(My_frame, font=("Helvetica", 10, "bold"))
E_Con.grid(row=3, column=1)

# Email
Email = Label(My_frame, text="Email:", font=("Courier New", 15, "bold"), pady=5)
Email.grid(row=4, column=0, sticky=E)

E_mail = Entry(My_frame, font=("Helvetica", 10, "bold"))
E_mail.grid(row=4, column=1)

button_frame = Frame(win)
button_frame.pack()

# Add Record
button_Add = Button(button_frame, text="Add Record", bg="#7bed9f", font=("Arial", 10, "bold"), command=add_Record)
button_Add.grid(row=1, column=0, padx=5, pady=10)

# Select Record
button_Select = Button(button_frame, text="Select Record", bg="#ffa502", font=("Arial", 10, "bold"),
                       command=select_Record)
button_Select.grid(row=1, column=1, padx=5, pady=10)

# Update Record
button_Up = Button(button_frame, text="Update Record", bg="#5352ed", font=("Arial", 10, "bold"), command=Update_Record)
button_Up.grid(row=1, column=2, padx=5, pady=10)

# Delete Record
button_del = Button(button_frame, text="Delete Record", bg="#ff4757", font=("Arial", 10, "bold"), command=delete_Record)
button_del.grid(row=1, column=3, padx=5, pady=10)

# Delete Many
button_D_many = Button(button_frame, text="Delete Many", bg="#747d8c", font=("Arial", 10, "bold"), command=delete_many)
button_D_many.grid(row=1, column=4, padx=5, pady=10)

# Delete all
button_d_all = Button(button_frame, text="Delete Many", bg="#747d8c", font=("Arial", 10, "bold"), command=delete_all)
button_d_all.grid(row=1, column=5, padx=5, pady=10)

my_Tree = ttk.Treeview(win)
my_Tree['columns'] = ('S.No', "Name", "Address", "Contact", "Mail")

my_Tree.column("#0", width=0, stretch=NO)
my_Tree.column('#1', width=50)
my_Tree.column('#2', width=80)
my_Tree.column('#3', width=80)
my_Tree.column('#4', width=80)
my_Tree.column('#5', width=80)

my_Tree.heading('#0', text="")
my_Tree.heading('#1', text="S.NO")
my_Tree.heading('#2', text="NAME")
my_Tree.heading('#3', text="ADDRESS")
my_Tree.heading('#4', text="CONTACT")
my_Tree.heading('#5', text="MAIL")

datas = [
    ["laks", "pndm", "9943177752", "laks@gmail.com"],
    ["anu", "pndm", "9139916624", "anulaks@gmail.com"],
    ["vani", "pndm", "8870909510", "vanic@gmail.com"]
]
for data in datas:
    my_Tree.insert("", index="end", iid=sno, values=(sno, data[0], data[1], data[2], data[3]))
    sno += 1


# my_Tree.insert("",index=0,values=(1,"amma", "slam", "192480","afgs2gamil.com"))
def my_bind(e):
    select_Record()


my_Tree.bind("<ButtonRelease-1>", my_bind)

my_Tree.pack(fill=X)

win.mainloop()
