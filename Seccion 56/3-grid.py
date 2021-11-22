
import tkinter as tk
from tkinter import ttk
from tkinter.constants import *

variable = 50

root = tk.Tk()
root.geometry('600x400')
root.title('GRID en tkinter')

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=5)

root.columnconfigure(0, weight=3)
root.columnconfigure(1, weight=7)


#color = tk.colorchooser.askcolor()


# anteriormente se uso pack para agregr elementos
# ahora se usará grid


def click_btn1():
    global variable
    variable += 1
    print(variable)


def click_btn4():
    btn4.config(fg="blue", relief=tk.GROOVE, bg="#cccccc")


btn1 = ttk.Button(root, text="nuevo boton",
                  command=click_btn1)
btn1.grid(row=0, column=0, sticky='NSWE')

# con el sig method obtengo las config del elemento
print(btn1.configure().keys())
# print(btn1.configure().values())


btn2 = ttk.Button(root, text="boton 2",
                  command=click_btn1)
btn2.grid(row=1, column=0, sticky='NSWE')
# columnspan=2, rowspan=3


btn3 = ttk.Button(root, text="boton 3")
btn3.grid(row=0, column=1, sticky='NSWE', ipadx=10, ipady=10, padx=15, pady=15)

# btn 4 fue declarado con tk, en lugar de ttk
# por defecto, los de ttk son mas visibles
# tk es personalizable
btn4 = tk.Button(root, text="boton 4", command=click_btn4,
                 activebackground="#FFF000")
btn4.grid(row=1, column=1, sticky="NW", ipadx=10, ipady=10, padx=15, pady=15)
print(btn4.configure().keys())

lbl = tk.Label(text=f"{variable}", bg="white", fg="blue")
lbl.grid(row=2, column=0)


root.mainloop()


# cuando llamo a grid, con NSWE "ocupo todo el espacio disponible"

# la prop columnconfigure de los elementos de tipo root, pueden accederse desde los components cuando se usa grid
# de la forma:  width=30
