from tkinter import *
from tkinter import ttk

# declarando metodo


def mostrar_datos():
    ttk.Label(frm, text="MOSTRANDO DATOS DESDE METODO").grid(column=0, row=1)


root = Tk()
root.geometry('600x600')
root.title('Hello World')
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Button(frm, text="print something",
           command=mostrar_datos).grid(column=2, row=0)

root.mainloop()
