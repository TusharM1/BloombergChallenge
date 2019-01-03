from tkinter import *

window = Tk()
window.title("Bloomberg SBHSData JSON Project")
window.geometry('640x480')

string = StringVar()

def clicked():
	print(string.get())

radio_set = Frame(window)

radio_area = Radiobutton(radio_set, text='area', variable=string, value='area', command=clicked).pack(side='left')
radio_version = Radiobutton(radio_set, text='version', variable=string, value='version', command=clicked).pack(side='left')
radio_uptime = Radiobutton(radio_set, text='uptime', variable=string, value='uptime', command=clicked).pack(side='left')
radio_hostname = Radiobutton(radio_set, text='hostname', variable=string, value='hostname', command=clicked).pack(side='left')

radio_set.pack()

window.mainloop()