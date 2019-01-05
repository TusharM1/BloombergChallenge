from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Bloomberg SBHSData JSON Project")
window.geometry('640x480')
window.configure(padx=20, pady=20)

# style.configure('My.TFrame', background='green')

frame = Frame(window)
frame.pack(fill='both', expand=True)

# Grid.rowconfigure(frame, 1, weight=1)
# Grid.columnconfigure(frame, 0, weight=1)

notebook = Notebook(frame)

style = Style(window)
style.map('My,TFrame', background=[("active", "green")])

area_frame = Frame(frame, style='My.TFrame')
# area_frame.grid(sticky='nsew')

area_options = Frame(area_frame)
Grid.rowconfigure(area_options, 2, weight=1)
Grid.columnconfigure(area_options, 0, weight=1)
Label(area_options, text='Select Filter:').grid(row=0, pady=20)

# def uptime_options():
# 	area_uptime_frame = Frame(area_options)
# 	Label(frame, text='Select Areas:').grid(row=1)
# 	vars = []
# 	for attribute in sets[0]:
# 		var = BooleanVar()
# 		Checkbutton(frame, text=attribute, variable=var).grid(row=2, sticky='nsew')
# 		vars.append(var)
# 	frame.grid(row=2, sticky='nswe')	
index = IntVar()

radio_buttons_frame = Frame(area_options)
radio_buttons_frame.grid(row=1)

global area_uptime_frame 

def area_radio_buttons():
	pass
	# if index.get() == 2:
	# 	Grid.rowconfigure(area_options, 2, weight=1)
	# 	area_uptime_frame.grid(row=2, sticky='nsew')
	# else:
	# 	Grid.rowconfigure(area_options, 2, weight=0)
	# 	area_uptime_frame.grid_forget()
		# print('not')
# # selected_areas = 
Radiobutton(radio_buttons_frame, variable=index, command=area_radio_buttons, text='area', value=0).pack(side='left')
Radiobutton(radio_buttons_frame, variable=index, command=area_radio_buttons, text='version', value=1).pack(side='left')
Radiobutton(radio_buttons_frame, variable=index, command=area_radio_buttons, text='uptime', value=2).pack(side='left')
Radiobutton(radio_buttons_frame, variable=index, command=area_radio_buttons, text='hostname', value=3).pack(side='left')		
# # button = Button(area_options, text="Submit", command=lambda: parse_options([var.get() for var in vars]))
# button = Button(area_options, text="Submit", command=lambda: parse_options('area', attribute_list[index.get()], ))

style = Style(area_options)

# style.configure('BW.TLabel', background='orange')

# area_uptime_frame = Frame(area_options, style='BW.TLabel')
# area_uptime_frame.grid(row=2, sticky='nsew')

button = Button(area_options, text="Submit", command=lambda: print('submit'))
button.grid(row=3, pady=20)	

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

notebook.add(area_frame, text='area')
# notebook.add(version_frame, text='version')
# notebook.add(uptime_frame, text='uptime')
# notebook.add(hostname_frame, text='hostname')

# def testfunc():
# 	print('test successful')

notebook.pack(fill='both', expand=True)	

window.mainloop()