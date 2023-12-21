import time
from tkinter import *
from tkinter import ttk


win = Tk()
win.title("Progress_Bar")
win.iconbitmap("js icon.ico")
win.geometry("500x250")


def start():
        # progress['value'] += 20

        progress.start(30)

        #for i in range(5):
            #progress['value'] += 10
            #win.update_idletasks()
            #time.sleep(2)


def stop():
    progress.stop()



progress = ttk.Progressbar(win, orient=HORIZONTAL, length=400)
progress.pack(pady=50)

button_start = Button(win, text="Start",command=start, bd=5, bg="#6ab04c", fg="#130f40",font=("times", 15, "bold"))
button_start.pack(pady=10)
button_stop = Button(win, text="Stop",command=stop,bd=5, bg="#eb4d4b", fg="#130f40",font=("times", 15, "bold"))
button_stop.pack(pady=10)


win.mainloop()
