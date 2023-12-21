from Window_Center import *
from tkinter import filedialog
from PIL import Image, ImageTk

Tkinter_File(500, 500, "FileDialog")

def file():
    global myImage
    file = filedialog.askopenfilename(initialdir="D:/", title="Select File", filetypes=(("PNG Files", "*.png"), ("JPG File", "*.jpg"), ("JPEG Files", "*.jpeg"), ("All Files", "*.*")))


    image = Image.open(file)
    resized =image.resize((250, 300))
    myImage = ImageTk.PhotoImage(resized)

    image_label = Label(win,image=myImage,width=250,height=300)
    image_label.pack()


bt_file = Button(win,text="Open File", command=file, bd=3,bg="#ED4C67", fg="#ffffff", font=("Verdana", 15, "bold"))
bt_file.pack(pady=30)
win.mainloop()