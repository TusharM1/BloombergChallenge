from tkinter import *
from tkinter.ttk import *

parent = Tk()

n = Notebook(parent)
f1 = Frame(n)   # first page, which would get widgets gridded into it
f2 = Frame(n)   # second page
n.add(f1, text='One')
n.add(f2, text='Two')

parent.mainloop()

