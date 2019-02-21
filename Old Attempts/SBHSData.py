# 1. Read in json file from pandas 
# 2. Draw new UI from 
import matplotlib
matplotlib.use('TkAgg') 

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# import tkinter

# window = tkinter.Tk()
# window.title("This is the title of the app")
# window.geometry('350x200')

# label = tkinter.Label(window, text = "Hello World!").pack()
# btn = tkinter.Button(window, text="Click Me").pack()
# window.mainloop()

import tkinter as tk 

window = tk.Tk()
window.title("This is the title of the app")
window.geometry('300x200')

number = 0

def clicked():
	global number
	label.configure(text="Button was clicked %d times" % number)
	number = number + 1

label = tk.Label(window, text = "Hello World!")
button = tk.Button(window, text="Click Me", command=clicked)

string = tk.StringVar()

radio_set = tk.Frame(window)
radio_set.pack()

a = Radiobutton(frame, text='a', variable=var, value='a').pack(side='left')
b = Radiobutton(frame, text='b', variable=var, value='b').pack(side='left')
c = Radiobutton(frame, text='c', variable=var, value='c').pack(side='left')
d = Radiobutton(frame, text='d', variable=var, value='d').pack(side='left')

label.pack()
button.pack()

window.mainloop()


# from tkinter import *
# window = Tk()
# window.title("Welcome to LikeGeeks app")
# window.geometry('350x200')
# lbl = Label(window, text="Hello")
# lbl.grid(column=0, row=0)
# btn = Button(window, text="Click Me")
# btn.grid(column=1, row=0)
# window.mainloop()

# sample_data = pd.read_json("SBHSData.json")

# y = [x for x in range(0, len(uptime), 50)]
# uptime = list(map(int, uptime))
# uptime = uptime.astype('int64')
# try: 

# x = np.array(sample_data.uptime)
# x.tolist()
# x = sample_data.select('uptime')
# x = pd.Series(sample_data.uptime).astype(intvalues
# print(x[0] + x[1])
# uptime = []
# for i in list(sample_data.uptime):
# 	try:
# 		uptime.append(int(i))
# 	except:
# 		pass

# try: 
# 	uptime = []
# 	for i in sample_data.uptime:
# 		uptime.append(int(i))
# except:
# 	pass

# print(uptime)

# print(sample_data.uptime.dtype())


# result = results = [int(i) if i for i in results]

# except:
# 	pass
 
# plt.hist(uptime, len(uptime) // 50)
# plt.hist(uptime, (max(uptime) - min(uptime)) // 100)

# plt.hist(uptime, [x for x in range(0, len(uptime), 50)])

# plt.show()