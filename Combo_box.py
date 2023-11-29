from tkinter import *
from tkinter import ttk

win = Tk()
win.title("Combo_box")
win.geometry("500x500")
win.iconbitmap("js icon.ico")
# Tittle Label
label = Label(win, text="Checkbutton_Demo", bg="#D980FA", fg="#EE5A24",
              padx=30, pady=10, font=("Times", 25, "bold"))
label.pack(fill=X)

# Combo Box
c_box = ttk.Combobox(win, width=25)
c_box.pack(padx=30)

win.mainloop()
