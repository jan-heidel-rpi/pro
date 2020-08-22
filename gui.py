from tkinter import *
import sys


def erster():
    mywin = Tk()
    label = Label(mywin, text='hello')
    label2 = Label(mywin, text='pierre')
    label.pack()
    label2.pack()
    mywin.mainloop()


if __name__ == '__main__':
    try:
        erster()
    except:
        sys.exit(0)
