import tkinter as tk
from tkinter import ttk
from tkinter.constants import *


def btn1_click():
    # print(type(variable_input1)) # <class 'tkinter.StringVar'>
    if(variable_input1.get()):
        print(variable_input1.get())


def btn2_click():
    variable_input1.set('valor default')
    if(variable_input1.get()):
        print(variable_input1.get())


root = tk.Tk()
root.geometry('600x400')
root.title('GRID en tkinter')

variable_input1 = tk.StringVar(value='')
input1 = ttk.Entry(root, width=20, justify=tk.LEFT,
                   textvariable=variable_input1)

btn1 = ttk.Button(text='submit', command=btn1_click)
btn2 = ttk.Button(text='valor default', command=btn2_click)


input1.grid(column=0, row=0, padx=5, pady=5)
btn1.grid(column=2, row=0, padx=5, pady=5)
btn2.grid(column=3, row=0, padx=5, pady=5)


root.mainloop()
