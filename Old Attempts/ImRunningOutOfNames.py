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

radio_button_frame = tk.Frame(frame)
radio_button_frame.grid(row=0, padx=20, pady=20)

tk.Radiobutton(radio_button_frame, text='area', value=0).pack(side='left')
tk.Radiobutton(radio_button_frame, text='version', value=1).pack(side='left')
tk.Radiobutton(radio_button_frame, text='uptime', value=2).pack(side='left')
tk.Radiobutton(radio_button_frame, text='hostname', value=3).pack(side='left')

# button = tk.Button(window, text="Sumbit", command=lambda: parse_options(index.get()))

# tk.Label(frame, text='hello').grid(row=0, pady=20)

frame2 = tk.Frame(frame, background='yellow')
# USE STICKY FOR EXPANDING FRAME!!!!!!!!!!!!!
frame2.grid(row=1, sticky='nswe')

tk.Grid.rowconfigure(frame2, 0, weight=1)
tk.Grid.columnconfigure(frame2, 0, weight=3)
tk.Grid.columnconfigure(frame2, 1, weight=2)

frame3 = tk.Frame(frame2, background='lime')
frame3.grid(row=0, column=0, sticky='nswe')

frame4 = tk.Frame(frame2, background='aqua')
frame4.grid(row=0, column=1, sticky='nswe')

button = tk.Button(frame, text="Sumbit")
button.grid(row=2, pady=20)

# frame3.grid(row=0)

# tk.Grid.rowconfigure(frame3, 0, weight=1)
# tk.Grid.columnconfigure(frame3, 0, weight=1)

# tk.Label(frame, text='goodbye').grid(row=2, pady=20)

window.mainloop()