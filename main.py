#!/usr/bin/env python

## IMPORT STATEMENTS

import matplotlib
matplotlib.use('TkAgg') 

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
from tkinter import *
import tkinter.ttk as ttk

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

	version_per_area_counts = {x:dict() for x in attribute_sets['area']}
	data_as_list = [sample_data.iloc[x] for x in range(len(attribute_lists['area']))]

	for area in version_per_area_counts:
		for entry in range(len(data_as_list)):
			if data_as_list[entry][0] == area:
				if data_as_list[entry][3] in version_per_area_counts[area]:
					version_per_area_counts[area][data_as_list[entry][3]] = version_per_area_counts[area][data_as_list[entry][3]] + 1
				else:
					version_per_area_counts[area][data_as_list[entry][3]] = 0			

	hostname_dictionary = {}				
	for i in range(len(attribute_lists['hostname'])):
		hostname_dictionary[attribute_lists['hostname'][i]] = list(sample_data.iloc[i])

	gui()

## DRAWING GUI

def gui():

	global sets, lists

	window = Tk()
	window.title("Bloomberg SBHSData JSON Project")
	window.geometry('680x320')

	frame = Frame(window)
	frame.pack(fill='both', expand=True, padx=20, pady=20)

	text_frame = Frame(frame)
	text_frame.place(in_=frame, relwidth=.4, relheight=1, relx=.6)

	Grid.rowconfigure(text_frame, 1, weight=1)
	Grid.columnconfigure(text_frame, 0, weight=1)

	global information_text, version_selected

	intro_text = StringVar()
	intro_text.set('This application is able to parse JSON data and create charts and graphs. \nUse the tabs and options to choose which data to show and click the filter button')
	intro = Label(text_frame, textvariable=intro_text, fg="white", wraplength=200, font=("San Francisco", 14))
	intro.grid(row=2, sticky='nsew', ipadx=10, ipady=10)

	information_text = StringVar()
	information_title = Label(text_frame, text='Information', fg="white", font=("San Francisco", 18))
	information_title.grid(row=0, sticky='nsew', ipady=5)
	information = Label(text_frame, textvariable=information_text, fg="white", font=("San Francisco", 14))
	information.grid(row=1, sticky='n', pady=10)

	options_frame = Frame(frame)
	options_frame.place(in_=frame, relwidth=.575, relheight=1)

	Grid.rowconfigure(options_frame, 0, weight=1)
	Grid.columnconfigure(options_frame, 0, weight=1)

	notebook = ttk.Notebook(options_frame)

	# AREA FRAME
	area_frame = Frame(options_frame)
	area_frame.grid(row=0, column=0, sticky='nswe')

	Grid.rowconfigure(area_frame, 0, weight=1)
	Grid.columnconfigure(area_frame, 0, weight=1)

	radio_button_frame = Frame(area_frame)
	radio_button_frame.grid(pady=15)

	radio_button_choice = StringVar()
	radio_button_choice.set('area')

	Radiobutton(radio_button_frame, variable=radio_button_choice, text='area', value='area').pack(side='left')
	Radiobutton(radio_button_frame, variable=radio_button_choice, text='version', value='version').pack(side='left')
	Radiobutton(radio_button_frame, variable=radio_button_choice, text='uptime', value='uptime').pack(side='left')
	Radiobutton(radio_button_frame, variable=radio_button_choice, text='hostname', value='hostname').pack(side='left')

	# VERSION FRAME
	version_frame = Frame(options_frame)
	version_frame.grid(row=0, column=0, sticky='nswe')

	Grid.rowconfigure(version_frame, 0, weight=1)
	Grid.columnconfigure(version_frame, 0, weight=1)

	version_selected = StringVar()

	version_inner_frame = Frame(version_frame)
	version_inner_frame.place(in_=version_frame, relx=.5, rely=.45, anchor='center')

	# Label(version_inner_frame, text='Choose Version').grid()

	# version_options = OptionMenu(version_inner_frame, version_selected, *list(attribute_sets['version']))
	# version_options.grid()

	# UPTIME FRAME
	uptime_frame = Frame(options_frame)
	uptime_frame.grid(row=0, column=0, sticky='nswe')

	# HOSTNAME FRAME
	hostname_frame = Frame(options_frame)
	hostname_frame.grid(row=0, column=0, sticky='nswe')

	hostname_inner_frame = Frame(hostname_frame)
	hostname_inner_frame.place(in_=hostname_frame, relx=.5, rely=.45, anchor='center')
	Label(hostname_inner_frame, text='Enter Hostname').pack()
	hostname = Entry(hostname_inner_frame)
	hostname.pack()

	notebook.add(area_frame, text='area')
	notebook.add(version_frame, text='version')
	notebook.add(uptime_frame, text='uptime')
	notebook.add(hostname_frame, text='hostname')

	def filter_options():

		dependent, independent = notebook.tab(notebook.select(), "text"), radio_button_choice.get()
		def absolute_value(val):
			global lists
			return '%1.1f%% [%s]'%(float(val), str(math.floor(len(lists[0]) * float(val) / 100)))
		if dependent == 'area':
			if independent == 'area':
				plt.pie(area_counts.values, labels=area_counts.keys(), pctdistance=0.65, labeldistance=1.2, autopct=absolute_value)
				plt.show()
		if dependent == 'version':
			plt.pie(version_counts.values, labels=version_counts.keys(), autopct='`%1.1f%%')
			plt.show()	
		if dependent == 'uptime':	
			plt.hist(lists[2], [x for x in range(0, len(lists[2]), 150)], histtype='bar')
			plt.show()			
		if dependent == 'hostname':
			global hostname_dictionary
			if not hostname.get() == '':
				if hostname.get() in hostname_dictionary:
					hostname_attributes = hostname_dictionary[hostname.get()]
					information_text.set('Area: %s\n Version: %s\n Uptime: %s' %(hostname_attributes[0], hostname_attributes[3], hostname_attributes[2]))
				else:
					information_text.set('Hostname could not be found')

	notebook.pack(fill='both', expand=True)	

	filter_button = Button(options_frame, command=filter_options, text="Filter")
	filter_button.pack(pady=20)

	window.configure(background='#2a4d69')
	frame.configure(background='#2a4d69')
	text_frame.configure(background='#4b86b4')
	information.configure(background='#4b86b4')
	intro.configure(background='#63ace5')
	information_title.configure(background='#19486e')
	options_frame.configure(background='#19486e')

	window.mainloop()

main()