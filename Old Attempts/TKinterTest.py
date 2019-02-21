import tkinter as tk

window = tk.Tk()
window.title("Bloomberg SBHSData JSON Project")
window.geometry('640x480')

window.configure(background='red')

frame = tk.Frame(window)
frame.configure(background='orange')
frame.pack(fill='both', expand=True, padx=20, pady=20)

# CONFIGURE WEIGHTING FROM PARENT!!!!!!!!!!!!
tk.Grid.rowconfigure(frame, 1, weight=1)
tk.Grid.columnconfigure(frame, 0, weight=1)

tk.Label(frame, text='hello').grid(row=0, pady=20)
frame2 = tk.Frame(frame, background='yellow')
frame2.grid(row=1)
# frame2.rowconfigure(0, weight=1)
tk.Grid.rowconfigure(frame2, 0, weight=1)
tk.Button(frame, text='goodbye').grid(row=2, pady=20)

# frame3 = tk.Frame(frame2)
# frame3.pack(fill='both', expand=True)

# tk.Entry(frame3).pack()
# tk.Entry(frame2).pack()


# frame1 = tk.Frame(frame)
# frame1.configure(background='yellow')
# # frame2.grid(sticky='nsew', row=0, column=0)
# # frame2.grid_rowconfigure(0, weight=1)
# # fra1e2.grid_columnconfigure(0, weight=1)
# frame1.pack(side='left', fill='both', expand=True, padx=(20,10), pady=20)

# frame3 = tk.Frame(frame1)
# frame3.configure(background='green')
# # frame3.grid(sticky='nsew', row=0, column=1)
# # frame3.grid_rowconfigure(0, weight=1)
# # frame3.grid_columnconfigure(1, weight=1)
# frame3.pack(side='left', fill='both', expand=True, padx=(10,20), pady=20)

window.mainloop()

from tkinter import *

# root = Tk()
# root.configure(background='red')

# content = Frame(root)
# content.configure(background='orange')
# frame = Frame(content, borderwidth=5, width=200, height=100)
# frame.configure(background="green")
# namelbl = Label(content, text="Name")
# name = Entry(content)

# onevar = BooleanVar()
# twovar = BooleanVar()
# threevar = BooleanVar()
# onevar.set(True)
# twovar.set(False)
# threevar.set(True)

# one = Checkbutton(content, text="One", variable=onevar, onvalue=True)
# two = Checkbutton(content, text="Two", variable=twovar, onvalue=True)
# three = Checkbutton(content, text="Three", variable=threevar, onvalue=True)
# ok = Button(content, text="Okay")
# cancel = Button(content, text="Cancel")

# content.grid(column=0, row=0, sticky='nsew')
# frame.grid(column=0, row=0, columnspan=3, rowspan=2)
# namelbl.grid(column=3, row=0, columnspan=2)
# name.grid(column=3, row=1, columnspan=2)
# one.grid(column=0, row=3)
# two.grid(column=1, row=3)
# three.grid(column=2, row=3)
# ok.grid(column=3, row=3)
# cancel.grid(column=4, row=3)

# # Grid.rowconfigure(content, weight=1, index=0)
# # Grid.columnconfigure(content, weight=1, index=0)

# content.grid_columnconfigure(index=0, weight=1)
# content.grid_rowconfigure(index=0, weight=1)

# root.mainloop()

# root = Tk()
# root.grid_columnconfigure(1,weight=1) # the text and entry frames column
# root.grid_rowconfigure(0,weight=1) # all frames row
# root.configure(background='red')

# # frame = Frame(root)
# # frame.grid(row=0, column=0, sticky="nswe")

# frame1 = Frame(root)
# frame1.configure(background='green')
# frame1.grid(row=0, column=0, sticky="nswe")
# frame1.grid_columnconfigure(0,weight=1) # the entry and text widgets column
# frame1.grid_rowconfigure(1,weight=1) # the text widgets row

# # button1 = Button(buttonframe, text='one', width=8)
# # button1.grid(row=0, column=0, sticky='nswe')
# # button2 = Button(buttonframe, text='two', width=8)
# # button2.grid(row=1, column=0, sticky='nswe')

# frame2 = Frame(frame1)
# frame2.grid(row=0, column=0, sticky='nswe')

# frame3 = Frame(frame1)
# frame3.grid(row=1, column=0, sticky='news')

# root.geometry("300x400")
# root.mainloop()