#!/usr/bin/env python

## IMPORT STATEMENTS

import matplotlib
matplotlib.use('TkAgg') 

import matplotlib.pyplot as plt
import pandas as pd
from tkinter import *
from tkinter.ttk import *

## READING JSON DATA

def main():

	global attribute_list, attribute_list_length, lists, sets

	sample_data = pd.read_json("SBHSData.json")

	attribute_list = ['area', 'version', 'uptime', 'hostname']
	attribute_list_length = len(attribute_list)

	# Change both of these lists to dictionaries
	lists = [[],] * attribute_list_length
	sets = [set(),] * attribute_list_length

	for i in range(attribute_list_length):
		lists[i] = list(sample_data[attribute_list[i]])
		sets[i] = set(sample_data[attribute_list[i]])

	versions_in_area = {}

	uptime_list, uptime_set = [], set()
	for i in sample_data.uptime:
		try: 
			uptime_list.append(int(i))
			uptime_set.add(int(i))
		except:
			uptime_list.append(0)
	
	lists[2] = uptime_list
	sets[2] = uptime_set

	gui()

## DRAWING GUI

def gui():

	global sets, lists

	# TODO create a dictionary (or other data structure) to hold configuration data
	# Or create a class and instantiate it and update the state, possibly make this function a class
	# Python isn't really used for OOP (I think), so maybe stay away from that paradigm

	window = Tk()
	window.title("Bloomberg SBHSData JSON Project")
	window.geometry('640x480')
	window.configure(padx=20, pady=20)
	# window.configure(background='red')

	# index = IntVar() 

	global options_frame, button, color_list

	# color_list = ['green', 'red', 'blue', 'purple']
	# def change_frame():
	# 	print(notebook.tab(notebook.select(), 'text'))
		# global options_frame, button
		# current_option = attribute_list[index.get()]

		# if current_option == 'area':
		# 	options_frame[].grid_forget()
		# 	options_frame = Frame(frame)
		# 	# options_frame.configure(background='green')

		# 	Label(options_frame, text='Select Areas:').pack()

		# 	def print_options():
		# 		print([var.get() for var in vars])

		# 	vars = []
		# 	for attribute in attribute_list:
		# 		var = BooleanVar()
		# 		Checkbutton(options_frame, text=attribute, variable=var).pack()
		# 		vars.append(var)

		# 	options_frame.grid(row=1, sticky='nswe')

		# 	button.grid_forget()
		# 	button = Button(frame, text="Submit", command=print_options)
		# 	button.grid(row=2, pady=20)
		# 	# print(ersion)
		# else:
		# 	options_frame.grid_forget()
		# 	options_frame = Frame(frame)
		# 	# options_frame.configure(background='red')
		# 	options_frame.grid(row=1, sticky='nswe')

		# 	button.grid_forget()
		# 	button = Button(frame, text="Submit", command=lambda: print("Submit"))
		# 	button.grid(row=2, pady=20)
		# pass

		# options_frame.forget()
		# # options_frame = Frame(frame)
		# options_frame.configure(background=color_list[index.get()].format())
		# options_frame.grid(row=1)
		# print(attribute_list[index.get()])

	frame = Frame(window)
	# frame.configure(background='orange')
	frame.pack(fill='both', expand=True)

	Grid.rowconfigure(frame, 1, weight=1)
	Grid.columnconfigure(frame, 0, weight=1)

	# radio_buttons_frame = Frame(frame)
	# radio_buttons_frame.grid(row=0, pady=20)

	# Radiobutton(radio_buttons_frame, variable=index, command=change_frame, text='area', value=0).pack(side='left')
	# Radiobutton(radio_buttons_frame, variable=index, command=change_frame, text='version', value=1).pack(side='left')
	# Radiobutton(radio_buttons_frame, variable=index, command=change_frame, text='uptime', value=2).pack(side='left')
	# Radiobutton(radio_buttons_frame, variable=index, command=change_frame, text='hostname', value=3).pack(side='left')

	# options_frame = [Frame(frame), ] * attribute_list_length
	# options_frame.grid(row=1, sticky='nswe')

	# REALLY NEED TO REDO THIS PART
	# options_frame = []

	notebook = Notebook(frame)

	# AREA FRAME
	area_frame = Frame(frame)
	Grid.rowconfigure(area_frame, 2, weight=1)
	Grid.columnconfigure(area_frame, 0, weight=1)
	Label(area_frame, text='Select Filter:').grid(row=0)
	def uptime_options():
		frame = Frame(area_frame)
		Label(frame, text='Select Areas:').grid(row=1)
		vars = []
		for attribute in sets[0]:
			var = BooleanVar()
			Checkbutton(frame, text=attribute, variable=var).grid(row=2, sticky='nsew')
			vars.append(var)
		frame.grid(row=2, sticky='nswe')	
	index = IntVar()	
	radio_buttons_frame = Frame(area_frame)
	radio_buttons_frame.grid(row=1)
	# selected_areas = 
	Radiobutton(radio_buttons_frame, variable=index, text='area', value=0).pack(side='left')
	Radiobutton(radio_buttons_frame, variable=index, text='version', value=1).pack(side='left')
	Radiobutton(radio_buttons_frame, variable=index, command=uptime_options, text='uptime', value=2).pack(side='left')
	Radiobutton(radio_buttons_frame, variable=index, text='hostname', value=3).pack(side='left')		
	# button = Button(area_frame, text="Submit", command=lambda: parse_options([var.get() for var in vars]))
	button = Button(area_frame, text="Submit", command=lambda: parse_options('area', attribute_list[index.get()], ))
	button.grid(row=4)	

	# VERSION FRAME
	version_frame = Frame(frame)
	Label(version_frame, text='version').pack()
	Button(version_frame, text="Submit", command=lambda: print('version')).pack()

	# UPTIME FRAME
	uptime_frame = Frame(frame)
	Label(uptime_frame, text='uptime').pack()
	Button(uptime_frame, text="Submit", command=lambda: print('uptime')).pack()

	# HOSTNAME FRAME
	hostname_frame = Frame(frame)
	Label(hostname_frame, text='hostname').pack()	
	Button(hostname_frame, text="Submit", command=lambda: print('hostname')).pack()
			
	notebook.add(area_frame, text='area')
	notebook.add(version_frame, text='version')
	notebook.add(uptime_frame, text='uptime')
	notebook.add(hostname_frame, text='hostname')

	def testfunc():
		print('test successful')

	notebook.pack(fill='both', expand=True)	
	notebook.bind('<2>', testfunc)
	# area_frame.pack(fill='both', expand=True)


	# for i in range(attribute_list_length):
		# option_frame = Frame(frame)
		# options_frame.append(option_frame)
	# notebook.tab(notebook.select(), 'text')		
		# print(attribute_list[i])

	# notebook.grid(row=0)

	# Grid.rowconfigure(options_frame, 0, weight=1)
	# Grid.columnconfigure(options_frame, 0, weight=3)
	# Grid.columnconfigure(options_frame, 1, weight=2)

	# frame3 = Frame(options_frame)
	# # frame3.configure(background='lime')
	# frame3.grid(row=0, column=0, sticky='nswe')

	# frame4 = Frame(options_frame)
	# # frame4.configure(background='aqua')
	# frame4.grid(row=0, column=1, sticky='nswe')

	# button = Button(frame, text="Submit", command=lambda: print("Submit"))
	# # button.grid(row=2, pady=20)
	# button.pack()

	# change_frame()

	window.mainloop()

## PARSE GUI OPTIONS

def parse_options(dependent, independent, selected_areas=None):
	global lists
	print(dependent, independent)
	if dependent == 'area':
		if independent == 'area':
			print('pie chart')
		elif independent == 'version':
			print('pie chart')
		elif independent == 'uptime':	
			print('histogram')
		elif independent == 'hostname':
			plt.hist(lists[2], [x for x in range(0, len(lists[2]), 150)], histtype='bar')	
	plt.show()		
	# plot(index)

## DRAW PLOT

# def plot(index):

# 	global lists

# 	plt.hist(lists[2], [x for x in range(0, len(lists[2]), 150)], histtype='bar')

# 	plt.show()

main()