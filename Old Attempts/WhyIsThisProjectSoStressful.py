import tknter as tk
from tknter import ttk

window = Tk()
window.title("Bloomberg SBHSData JSON Project")
window.geometry('640x480')

# window.configure(background='red')

frame = Frame(window)
# frame.configure(background='orange')
frame.pack(fill='both', expand=True, padx=20, pady=20)

area_left_frame = Frame(frame)
# area_left_frame.configure(background='yellow')
area_left_frame.place(in_=frame, relwidth=.6, relheight=1)

Grid.rowconfigure(area_left_frame, 0, weight=1)
Grid.columnconfigure(area_left_frame, 0, weight=1)

notebook = Notebook(area_left_frame)

tab_frame = Frame(area_left_frame)
# tab_frame.configure(background='lime')
tab_frame.grid(row=0, column=0, sticky='nswe')

notebook.add(tab_frame, text='area')

radio_button_frame = Frame(tab_frame)
# radio_button_frame.configure(background='brown')
radio_button_frame.pack()

Radiobutton(radio_button_frame, text='area', value=0).pack(side='left')
Radiobutton(radio_button_frame, text='version', value=1).pack(side='left')
Radiobutton(radio_button_frame, text='uptime', value=2).pack(side='left')
Radiobutton(radio_button_frame, text='hostname', value=3).pack(side='left')

area_right_frame = Frame(frame)
# area_right_frame.configure(background='aqua')
area_right_frame.place(in_=frame, relwidth=.4, relheight=1, relx=0.6)

notebook.pack(fill='both', expand=True)	

button = Button(area_left_frame, text="Sumbit")
button.pack(pady=20)

window.mainloop()




# import nter as tk
# from nter import ttk

# window = Tk()
# window.title("Bloomberg SBHSData JSON Project")
# window.geometry('640x480')

# window.configure(background='red')

# frame = Frame(window)
# frame.configure(background='orange')
# frame.pack(fill='both', expand=True, padx=20, pady=20)

# # Grid.rowconfigure(frame, 0, weight=1)
# # Grid.columnconfigure(frame, 0, weight=3)
# # Grid.columnconfigure(frame, 1, weight=2)

# area_left_frame = Frame(frame, background='yellow')
# # USE STICKY FOR EXPANDING FRAME!!!!!!!!!!!!!
# # area_left_frame.grid(column=0, sticky='nswe')
# # area_left_frame.pack(side='left', fill='y')
# area_left_frame.place(in_=frame, relwidth=.6, relheight=1)

# Grid.rowconfigure(area_left_frame, 0, weight=1)
# Grid.columnconfigure(area_left_frame, 0, weight=1)
# # Grid.columnconfigure(area_left_frame, 1, weight=2)

# notebook = tNotebook(area_left_frame)

# tab_frame = Frame(area_left_frame, background='lime')
# tab_frame.grid(row=0, column=0, sticky='nswe')
# # tab_frame.grid(row=0, column=0, sticky='nswe')

# # Grid.rowconfigure(tab_frame, 0, weight=1)
# # Grid.columnconfigure(tab_frame, 0, weight=1)

# notebook.add(tab_frame, text='area')

# radio_button_frame = Frame(tab_frame, background='brown')
# radio_button_frame.pack()

# # # Label(tab_frame, text='texthebfuwebfuwbefuwebf').pack()

# Radiobutton(radio_button_frame, text='area', value=0).pack(side='left')
# Radiobutton(radio_button_frame, text='version', value=1).pack(side='left')
# Radiobutton(radio_button_frame, text='uptime', value=2).pack(side='left')
# Radiobutton(radio_button_frame, text='hostname', value=3).pack(side='left')

# area_right_frame = Frame(frame, background='aqua')
# # area_right_frame.grid(row=0, column=1, sticky='nswe')
# # area_right_frame.pack(fill='both', expand=True, side='left')
# area_right_frame.place(in_=frame, relwidth=.4, relheight=1, relx=0.6)

# # notebook.grid(row=0, column=0, sticky='nswe')
# notebook.pack(fill='both', expand=True)	

# button = Button(area_left_frame, text="Sumbit")
# # button.grid(row=2, pady=20)
# button.pack(pady=20)

# # CONFIGURE WEIGHTING FROM PARENT!!!!!!!!!!!!

# # button = Button(window, text="Sumbit", command=lambda: parse_options(index.get()))

# # Label(frame, text='hello').grid(row=0, pady=20)

# # Grid.rowconfigure(area_left_frame, 0, weight=1)
# # Grid.columnconfigure(area_left_frame, 0, weight=1)

# # Grid.rowconfigure(tab_frame, 0, weight=1)
# # Grid.columnconfigure(tab_frame, 0, weight=1)

# # tab_frame.grid(row=0)

# # Grid.rowconfigure(tab_frame, 0, weight=1)
# # Grid.columnconfigure(tab_frame, 0, weight=1)

# # Label(frame, text='goodbye').grid(row=2, pady=20)

# window.mainloop()