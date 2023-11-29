from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Button")
root.iconbitmap("js icon.ico")

def fun():
    #print(1)
    #messagebox.showinfo("Hello", "Red button clicked")
    label = Label(root,text="red button clicked")
    label.pack()


button = Button(root, text="Click",
                height=4, width=8,
                padx=50,
                pady=5,
                bd=6,
                bg="gray",
                fg="green",
                command=fun,
                activebackground="yellow",
                activeforeground="red",
                font="Arial",
                relief="ridge"
                )
button.pack()
root.mainloop()
