from tkinter import *

win = Tk()
win.title("Menu_Bar")
win.iconbitmap("js icon.ico")
win.geometry("500x500")


def New():
    file_win = Toplevel(win)
    file_win.geometry("400x400")
    file_win.config(bg="#2c3e50")
    label = Label(file_win, text="New Page", bg="#3498db", fg="White",
                  padx=30, pady=5, font=("Times", 25, "bold"))
    label.pack(fill=X)
    button = Button(file_win, text="Click", height=2, width=4, bd=6, bg="gray", fg="green", command=file_win.destroy,
                    activebackground="yellow",
                    activeforeground="red",
                    font="Arial",
                    relief="ridge"
                    )
    button.pack()


def open():
    file_win = Toplevel(win)
    file_win.geometry("400x400")
    file_win.config(bg="#2c3e50")
    label = Label(file_win, text="Open", bg="#3498db", fg="White",
                  padx=30, pady=5, font=("Times", 25, "bold"))
    label.pack(fill=X)


menubar = Menu(win)
# File Menu
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=New)
file_menu.add_command(label="Open", command=open)
file_menu.add_separator()
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=win.destroy)
menubar.add_cascade(label="File", menu=file_menu)

# Edit Menu
edit_menu = Menu(menubar, tearoff=0)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_separator()
edit_menu.add_command(label="Exit")
menubar.add_cascade(label="Edit", menu=edit_menu)

win.config(menu=menubar)
win.mainloop()
