#! /Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import time, tkinter

window=tkinter.Tk()
label=tkinter.Label(master=window, text='time of day: ' + time.asctime())

label.pack()
window.mainloop()