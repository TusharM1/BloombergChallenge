from tkinter import *
     
# class Checkbar(Frame):
#     def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
#         Frame.__init__(self, parent)
#         self.vars = []
#         var = IntVar()
#         for pick in picks:
#             chk = Checkbutton(self, text=pick, variable=var)
#             chk.pack(side=side, anchor=anchor, expand=YES)
#             self.vars.append(var)
#     def state(self):
#         return [var.get() for var in self.vars]  

root = Tk()
# checkBoxBar = Checkbar(root, ['A', 'B', 'C', 'D'])

checkbox = Frame(root)

vars = []
picks = ['A', 'B', 'C', 'D']
for pick in picks:
    var = BooleanVar()
    chk = Checkbutton(checkbox, text=pick, variable=var)
    chk.pack(side=LEFT, anchor=W, expand=YES)
    vars.append(var)

checkbox.pack(side=TOP,  fill=X)
checkbox.config(relief=GROOVE, bd=2)

def allstates(): 
   print([var.get() for var in vars])

Button(root, text='Peek', command=allstates).pack(side=RIGHT)
root.mainloop()