from tkinter import *

def print_var(*args):
    print (root.getvar(name=args[0]))

root = Tk()

var = StringVar()
var.trace('w', print_var)

frame = Frame(root)

a = Radiobutton(frame, text='a', variable=var, value='a').pack(side='left')
b = Radiobutton(frame, text='b', variable=var, value='b').pack(side='left')
c = Radiobutton(frame, text='c', variable=var, value='c').pack(side='left')
d = Radiobutton(frame, text='d', variable=var, value='d').pack(side='left')

frame.pack()

root.mainloop()