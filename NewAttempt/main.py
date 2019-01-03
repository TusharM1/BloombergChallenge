#!/usr/bin/env python

## IMPORT STATEMENTS

import matplotlib
matplotlib.use('TkAgg') 

import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk

## READING JSON DATA

def main():

	global attribute_list, lists, sets

	sample_data = pd.read_json("SBHSData.json")

	attribute_list = list(sample_data)
	attribute_list_length = len(attribute_list)

	lists = [[],] * attribute_list_length
	sets = [set(),] * attribute_list_length

	for i in range(attribute_list_length):
		lists[i] = list(sample_data[attribute_list[i]])
		sets[i] = set(sample_data[attribute_list[i]])

	uptime_list, uptime_set = [], set()
	for i in sample_data.uptime:
		try: 
			uptime_list.append(int(i))
			uptime_set.add(int(i))
		except:
			pass
	
	lists[2] = uptime_list
	sets[2] = uptime_set

	gui()

## DRAWING GUI

def gui():

	global sets, lists

	# TODO create a dictionary (or other data structure) to hold configuration data
	# Or create a class and instantiate it and update the state, possibly make this function a class
	# Python isn't really used for OOP (I think), so maybe stay away from that paradigm

	window = tk.Tk()
	window.title("Bloomberg SBHSData JSON Project")
	window.geometry('640x480')
	window.configure(padx=20, pady=20)

	index = tk.IntVar() 

	global options_frame, button

	def change_frame():
		global options_frame, attribute_list, button
		button.forget()
		options_frame.forget()
		options_frame = tk.Frame(window)
		options_frame.configure(background='orange')
		options_frame.pack(fill='both', expand=True, padx=20, pady=20)
		tk.Label(options_frame, text=attribute_list[index.get()]).pack()
		button.pack()

	radio_buttons = tk.Frame(window)
	radio_buttons.pack()

	options_frame = tk.Frame(window)
	button = tk.Button(window, text="Sumbit", command=lambda: parse_options(index.get()))
	button.pack()

	tk.Radiobutton(radio_buttons, text='area', variable=index, command=change_frame, value=0).pack(side='left')
	tk.Radiobutton(radio_buttons, text='version', variable=index, command=change_frame, value=1).pack(side='left')
	tk.Radiobutton(radio_buttons, text='uptime', variable=index, command=change_frame, value=2).pack(side='left')
	tk.Radiobutton(radio_buttons, text='hostname', variable=index, command=change_frame, value=3).pack(side='left')

	change_frame()

	# string = tk.StringVar()
	# name_frame = tk.Frame(window)
	# name_frame.pack()
	# name = tk.Entry(name_frame, textvariable=string).pack()

	window.mainloop()

## PARSE GUI OPTIONS

def parse_options(index):

	print(index)

	plot(index)

## DRAW PLOT

def plot(index):

	global lists

	plt.hist(lists[2], [x for x in range(0, len(lists[2]), 150)], histtype='bar')

	plt.show()

main()