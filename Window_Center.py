from tkinter import *

win = Tk()


def Tkinter_File(width, height, title):
    win.title(title)
    win.iconbitmap("js icon.ico")
    w = width
    h = height
    sw = win.winfo_screenwidth()
    sh = win.winfo_screenheight()
    x = (sw / 2) - (w / 2)
    y = (sh / 2) - (h / 2)
    win.geometry("%dx%d+%d+%d" % (w, h, x, y))
