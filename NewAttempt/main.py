#!/usr/bin/env python

## IMPORT STATEMENTS

import matplotlib
matplotlib.use('TkAgg') 

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tkinter import *
import tkinter.ttk as ttk
import math
# from tkinter import *
# from tkinter.ttk import *

## READING JSON DATA

def main():

	global attribute_list, attribute_lists, attribute_list_length, attribute_sets, lists, sets, area_counts, version_counts, hostname_dictionary

	sample_data = pd.read_json("SBHSData.json")

	attribute_list = ['area', 'version', 'uptime', 'hostname']
	attribute_lists = {'area': [], 'version': [], 'uptime': [], 'hostname': []}
	attribute_sets = {'area': set(), 'version': set(), 'uptime': set(), 'hostname': set()}

	for i in attribute_lists.keys():
		attribute_lists[i] = list(sample_data[i])
		attribute_sets[i] = set(sample_data[i])	

	lists = list(attribute_lists.values())
	sets = list(attribute_sets.values())

	uptime_list, uptime_set = [], set()
	for i in sample_data.uptime:
		try: 
			uptime_list.append(int(i))
			uptime_set.add(int(i))
		except:
			pass
	
	lists[2] = uptime_list
	sets[2] = uptime_set

	area_counts = sample_data['area'].value_counts()
	version_counts = sample_data['version'].value_counts()

	# print(sample_data.describe())

	# NEARLY DOUBLES RUNTIME!!
	# version_per_area_counts = {x:dict() for x in attribute_sets['area']}
	version_per_area_counts = {x:dict() for x in attribute_sets['area']}
	data_as_list = [sample_data.iloc[x] for x in range(len(attribute_lists['area']))]

	# print(data_as_list)

	# FIX THIS LATTTTTTERRRR
	# for i in data_as_list:

		# if i[0] in version_per_area_counts:
		# 	version_per_area_counts[i[0]][i[2]] += 1
		# else:
		# 	version_per_area_counts[i[0]] = dict()

	# data_as_list = sample_data.values.tolist()
	# for area in version_per_area_counts:
	# 	version_per_area_counts[area] = dict()
	# 	for i in data_as_list:
	# 		if data_as_list[0] == area:
	# 			if data_as_list[entry][3] in version_per_area_counts[area]:
	# 				version_per_area_counts[area][data_as_list[entry][3]] = version_per_area_counts[area][data_as_list[entry][3]] + 1
	# 			else:
	# 				version_per_area_counts[area][data_as_list[entry][3]] = 0	
					# data_as_list2 = sample_data.values.tolist()
	for area in version_per_area_counts:
		for entry in range(len(data_as_list)):
			if data_as_list[entry][0] == area:
				if data_as_list[entry][3] in version_per_area_counts[area]:
					version_per_area_counts[area][data_as_list[entry][3]] = version_per_area_counts[area][data_as_list[entry][3]] + 1
				else:
					version_per_area_counts[area][data_as_list[entry][3]] = 0

	hostname_dictionary = {}				
	# data = list(sample_data.iloc)
	for i in range(len(attribute_lists['hostname'])):
		hostname_dictionary[attribute_lists['hostname'][i]] = list(sample_data.iloc[i])
	# for i in sample_data.hostname:
	# 	print(i)
	# print()
	# print()			
	# print(hostname_dictionary)						
	gui()

	# print(lists[2])

	# print(version_per_area_counts)

	# sample_data = pd.read_json("SBHSData.json")

	# attribute_list = ['area', 'version', 'uptime', 'hostname']
	# attribute_list_length = len(attribute_list)

	# # Change both of these lists to dictionaries
	# lists = [[],] * attribute_list_length
	# sets = [set(),] * attribute_list_length

	# for i in range(attribute_list_length):
	# 	lists[i] = list(sample_data[attribute_list[i]])
	# 	sets[i] = set(sample_data[attribute_list[i]])

	# versions_in_area = {}

	# uptime_list, uptime_set = [], set()
	# for i in sample_data.uptime:
	# 	try: 
	# 		uptime_list.append(int(i))
	# 		uptime_set.add(int(i))
	# 	except:
	# 		uptime_list.append(0)
	
	# lists[2] = uptime_list
	# sets[2] = uptime_set

## DRAWING GUI

def gui():

	global sets, lists

	window = Tk()
	window.title("Bloomberg SBHSData JSON Project")
	window.geometry('680x320')
	# window.configure(padx=20, pady=20)

	frame = Frame(window)
	frame.pack(fill='both', expand=True, padx=20, pady=20)

	text_frame = Frame(frame)
	text_frame.place(in_=frame, relwidth=.4, relheight=1, relx=.6)

	Grid.rowconfigure(text_frame, 1, weight=1)
	Grid.columnconfigure(text_frame, 0, weight=1)

	global statistics_text
	intro_text = StringVar()
	intro_text.set('This application is able to parse JSON data and create charts and graphs. \nUse the tabs and options to choose which data to show and click the filter button')
	intro = Label(text_frame, textvariable=intro_text, fg="white", wraplength=200, font=("San Francisco", 14))
	intro.grid(row=2, sticky='nsew', ipadx=10, ipady=10)
	statistics_text = StringVar()
	Label(text_frame, text='Statistics', fg="white", font=("San Francisco", 18), background='#4b86b4').grid(row=0, pady=(20, 5))
	statistics = Label(text_frame, textvariable=statistics_text, fg="white", font=("San Francisco", 14))
	statistics.grid(row=1, sticky='n')

	options_frame = Frame(frame)
	options_frame.place(in_=frame, relwidth=.6, relheight=1)

	Grid.rowconfigure(options_frame, 0, weight=1)
	Grid.columnconfigure(options_frame, 0, weight=1)

	notebook = ttk.Notebook(options_frame)

	# AREA FRAME
	area_frame = Frame(options_frame)
	area_frame.grid(row=0, column=0, sticky='nswe')

	radio_button_frame = Frame(area_frame)
	radio_button_frame.pack(pady=15)

	radio_button_choice = StringVar()
	radio_button_choice.set('area')

	# def radio_button():
	# 	print('radiobutton changed')

	Radiobutton(radio_button_frame, variable=radio_button_choice, text='area', value='area').pack(side='left')
	Radiobutton(radio_button_frame, variable=radio_button_choice, text='version', value='version').pack(side='left')
	Radiobutton(radio_button_frame, variable=radio_button_choice, text='uptime', value='uptime').pack(side='left')
	Radiobutton(radio_button_frame, variable=radio_button_choice, text='hostname', value='hostname').pack(side='left')

	# radio_label = Label(area_frame, textvariable=radio_button_choice)
	# radio_label.pack()

	# VERSION FRAME
	version_frame = Frame(options_frame)
	version_frame.grid(row=0, column=0, sticky='nswe')

	# Label(version_frame, text='version').pack()

	# UPTIME FRAME
	uptime_frame = Frame(options_frame)
	uptime_frame.grid(row=0, column=0, sticky='nswe')

	# Label(uptime_frame, text='Enter Range:').pack()

	# HOSTNAME FRAME
	hostname_frame = Frame(options_frame)
	hostname_frame.grid(row=0, column=0, sticky='nswe')

	hostname_inner_frame = Frame(hostname_frame)
	hostname_inner_frame.place(in_=hostname_frame, relx=.5, rely=.45, anchor='center')
	Label(hostname_inner_frame, text='Enter Hostname').pack()
	hostname = Entry(hostname_inner_frame)
	hostname.pack()

	# Label(hostname_frame, text='hostname').pack()

	notebook.add(area_frame, text='area')
	notebook.add(version_frame, text='version')
	notebook.add(uptime_frame, text='uptime')
	notebook.add(hostname_frame, text='hostname')

	# global current_configuration
	# current_configuration = {}
	# def configuration(event):
	# 	global current_configuration
	# 	print('tab changed')
	# 	print(current_configuration)
	# 	current_configuration = {} 
	# 	# current_configuration['tab'] = notebook.tab(notebook.select(), "text")
	# 	# current_configuration['filter_option'] = 

	def filter_options():
		dependent, independent = notebook.tab(notebook.select(), "text"), radio_button_choice.get()
		def absolute_value(val):
			global lists
			return '%1.1f%% [%s]'%(float(val), str(math.floor(len(lists[0]) * float(val) / 100)))
		# print(dependent, independent)
		if dependent == 'area':
			if independent == 'area':
		# 		#figure out what this does
				plt.pie(area_counts.values, labels=area_counts.keys(), pctdistance=0.65, labeldistance=1.2, autopct=absolute_value)
			# elif independent == 'version':
		# 		print('pie chart')
		# 	elif independent == 'uptime':
		# 		print('histogram')
			elif independent == 'hostname':
				plt.hist(lists[2], [x for x in range(0, len(lists[2]), 150)], histtype='bar')
			plt.show()
		if dependent == 'version':
			plt.pie(version_counts.values, labels=version_counts.keys(), autopct='%1.1f%%')
			# plt.tight_layout()
			plt.show()
			print('version')	
		if dependent == 'uptime':
			print('uptime')				
		if dependent == 'hostname':
			global hostname_dictionary
			if hostname.get() in hostname_dictionary:
				hostname_attributes = hostname_dictionary[hostname.get()]
				statistics_text.set('Area: %s\n Version: %s\n Uptime: %s' %(hostname_attributes[0], hostname_attributes[3], hostname_attributes[2]))
			else:
				statistics_text.set('Hostname could not be found')

	# notebook.bind('<<NotebookTabChanged>>', configuration)b

	notebook.pack(fill='both', expand=True)	

	# filter_button = Button(options_frame, command=lambda: filter_options(notebook.tab(notebook.select(), "text"), radio_button_choice.get(), statistics='hello'), text="Filter")
	filter_button = Button(options_frame, command=filter_options, text="Filter")
	filter_button.pack(pady=20)

	style = ttk.Style()

	style.theme_create( "yummy", settings={
	        "TNotebook": {"background": 'green'}} )

	# style.theme_use("yummy")

	window.configure(background='#2a4d69')
	text_frame.configure(background='#4b86b4')
	statistics.configure(background='#4b86b4')
	intro.configure(background='#63ace5')
	options_frame.configure(background='#19486e')

	window.mainloop()

	# TODO create a dictionary (or other data structure) to hold configuration data
	# Or create a class and instantiate it and update the state, possibly make this function a class
	# Python isn't really used for OOP (I think), so maybe stay away from that paradigm


	# window.configure(background='red')

	# index = IntVar() 

	# global options_frame, button, color_list

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

	# frame = Frame(window)
	# # frame.configure(background='orange')
	# frame.pack(fill='both', expand=True)

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

	# notebook = Notebook(frame)

	# # AREA FRAME
	# options_frame_container = Frame(frame)
	# options_frame = Frame(options_frame_container)
	# Grid.rowconfigure(options_frame, 2, weight=1)
	# Grid.columnconfigure(options_frame, 0, weight=1)
	# Label(options_frame, text='Select Filter:').grid(row=0)
	# # area_uptime_frame
	# def uptime_options():
	# 	area_uptime_frame = Frame(options_frame)
	# 	Label(frame, text='Select Areas:').grid(row=1)
	# 	vars = []
	# 	for attribute in sets[0]:
	# 		var = BooleanVar()
	# 		Checkbutton(frame, text=attribute, variable=var).grid(row=2, sticky='nsew')
	# 		vars.append(var)
	# 	frame.grid(row=2, sticky='nswe')
	# index = IntVar()
	# radio_buttons_frame = Frame(options_frame)
	# radio_buttons_frame.grid(row=1)
	# # selected_areas = 
	# Radiobutton(radio_buttons_frame, variable=index, text='area', value=0).pack(side='left')
	# Radiobutton(radio_buttons_frame, variable=index, text='version', value=1).pack(side='left')
	# Radiobutton(radio_buttons_frame, variable=index, command=uptime_options, text='uptime', value=2).pack(side='left')
	# Radiobutton(radio_buttons_frame, variable=index, text='hostname', value=3).pack(side='left')
	# # button = Button(options_frame, text="Submit", command=lambda: parse_options([var.get() for var in vars]))
	# button = Button(options_frame, text="Submit", command=lambda: parse_options('area', attribute_list[index.get()], ))
	# button.grid(row=4)

	# # VERSION FRAME
	# version_frame = Frame(frame)
	# Label(version_frame, text='version').pack()
	# Button(version_frame, text="Submit", command=lambda: print('version')).pack()

	# # UPTIME FRAME
	# uptime_frame = Frame(frame)
	# Label(uptime_frame, text='uptime').pack()
	# Button(uptime_frame, text="Submit", command=lambda: print('uptime')).pack()

	# # HOSTNAME FRAME
	# hostname_frame = Frame(frame)
	# Label(hostname_frame, text='hostname').pack()
	# Button(hostname_frame, text="Submit", command=lambda: print('hostname')).pack()
			
	# notebook.add(options_frame_container, text='area')
	# notebook.add(version_frame, text='version')
	# notebook.add(uptime_frame, text='uptime')
	# notebook.add(hostname_frame, text='hostname')

	# def testfunc():
	# 	print('test successful')

	# notebook.pack(fill='both', expand=True)

	# options_frame.pack(fill='both', expand=True)


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

## PARSE GUI OPTIONS

# def filter_options(dependent, independent, statistics):
# 	global lists, attribute_sets, area_counts, statistics_text
# 	statistics_text.set(notebook.tab(notebook.select(), "text"))
# 	if dependent == 'area':
# 		if independent == 'area':
# 			#figure out what this does
# 			plt.pie(area_counts.values, labels=area_counts.keys(), autopct='%1.1f%%')
# 		elif independent == 'version':
# 			print('pie chart')
# 		elif independent == 'uptime':
# 			print('histogram')
# 		elif independent == 'hostname':
# 			plt.hist(lists[2], [x for x in range(0, len(lists[2]), 150)], histtype='bar')
# 	plt.show()
	# plot(index)

## DRAW PLOT

# def plot(index):

# 	global lists

# 	plt.hist(lists[2], [x for x in range(0, len(lists[2]), 150)], histtype='bar')

# 	plt.show()

main()