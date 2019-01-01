#!/usr/bin/env python

import pandas as pd
import tkinter as tk

## READING JSON DATA

sample_data = pd.read_json("SBHSData.json")

attribute_list = list(sample_data)
attribute_list_length = len(attribute_list)

sets = [set(),] * attribute_list_length
lists = [[],] * attribute_list_length

for i in range(attribute_list_length):
	lists[i] = list(sample_data[attribute_list[i]])
	sets[i] = set(sample_data[attribute_list[i]])

# print(sets, "\n\n\n", lists)

## DRAWING GUI

window = tk.Tk()
window.title("Bloomberg SBHSData JSON Project")
window.geometry('640x480')

index = tk.IntVar()

def clicked():
	print(index.get())
	print(lists[index.get()])

radio_set = tk.Frame(window)

radio_area = tk.Radiobutton(radio_set, text='area', variable=index, value=0, command=clicked).pack(side='left')
radio_version = tk.Radiobutton(radio_set, text='version', variable=index, value=1, command=clicked).pack(side='left')
radio_uptime = tk.Radiobutton(radio_set, text='uptime', variable=index, value=2, command=clicked).pack(side='left')
radio_hostname = tk.Radiobutton(radio_set, text='hostname', variable=index, value=3, command=clicked).pack(side='left')

radio_set.pack()

def sumbit():
	

button = tk.Button(window, text="Click Me", command=submit).pack()

window.mainloop()

## 