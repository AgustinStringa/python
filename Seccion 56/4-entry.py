import tkinter as tk
from tkinter import ttk, messagebox, Menu
from tkinter.constants import *
import sys


def crear_menu():

    def salir():
        root.quit()
        root.destroy()
        sys.exit()
    # creando el menu principal
    menu_principal = Menu(root)

    # creando los submenus
    submenu_archivo = Menu(menu_principal, tearoff=0)
    submenu_edicion = Menu(menu_principal, tearoff=0)
    submenu_salir = Menu(menu_principal, tearoff=0)

    # agregando comandos y separadores
    submenu_archivo.add_command(label='Nuevo')
    submenu_archivo.add_separator()
    submenu_archivo.add_command(label='Salir')
    submenu_edicion.add_command(label='Editar')
    submenu_salir.add_command(label='Salir', command=salir)

    # agregando submenus al principal
    menu_principal.add_cascade(menu=submenu_archivo, label='Archivo')
    menu_principal.add_cascade(menu=submenu_edicion, label='Edicion')
    menu_principal.add_cascade(menu=submenu_salir, label='Salir')

    # añadiendo a la ventana el menu
    root.config(menu=menu_principal)


def btn1_click():
    guardado = True
    entrada_name = input1.get()
    entrada_lastname = input2.get()
    input1.delete(0, tk.END)
    input1.insert(0, '')
    input2.delete(0, tk.END)
    input2.insert(0, '')
    lbl_data.config(
        text=f'''
ENTRADA NOMBRE: {entrada_name} \nENTRADA APELLIDO: {entrada_lastname}
        ''')
    input1.focus()
    if guardado:
        messagebox.showinfo('info', 'Guardado correctamente')
    else:
        messagebox.showerror('Error', 'No se ha podido guardar')


root = tk.Tk()
root.geometry('600x400')
root.title('Entry component')


lbl_name = ttk.Label(text='nombre')
lbl_last_name = ttk.Label(text='apellido')

lbl_data = ttk.Label()


input1 = ttk.Entry(root, width=20, justify=tk.LEFT)
input2 = ttk.Entry(root, width=20, justify=tk.LEFT)

# show="*"
# state = tk.DISABLED / tk.NORMAL /readonly
btn1 = ttk.Button(text='submit', command=btn1_click)

#input1.insert(0, 'introduce una cadena')


# GRIDS
lbl_name.grid(column=0, row=0, padx=5, pady=5,)
lbl_last_name.grid(column=0, row=1, padx=5, pady=5, )

input1.grid(column=1, row=0, padx=5, pady=5, sticky="N")
input2.grid(column=1, row=1, padx=5, pady=5, sticky="N")

btn1.grid(column=2, row=1, padx=5, pady=5)

lbl_data.grid(row=2, column=0)

crear_menu()
root.mainloop()
