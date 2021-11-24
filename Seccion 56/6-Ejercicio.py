import tkinter as tk
from tkinter import Widget, ttk, messagebox, Menu
from tkinter.constants import *
import sys

# VentanaLogin extiende tk.Tk


class VentanaLogin(tk.Tk):

    def __init__(self):
        # super().__init_() inicia un objeto de tipo tk.Tk
        super().__init__()

        self.geometry('300x200')
        self.title('Login')
        self.resizable(0, 0)

        # configuracion de la ventana
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        # llamando a metodo restringido
        self._crear_widgets()

    def _crear_widgets(self):
        lbl_user = ttk.Label(self, text='Usuario: ')
        lbl_password = ttk.Label(self, text='Password: ',)

        self.lbl_data = ttk.Label(text=f'''
        USUARIO: ... \nCONTRASEÑA: ...
        ''', justify=tk.LEFT)

        self.input1 = ttk.Entry(self,  justify=tk.LEFT)
        self.input2 = ttk.Entry(self,  justify=tk.LEFT, show="*")
        btn1 = ttk.Button(text='Login', command=self._btn1_click)

        # GRIDS
        lbl_user.grid(column=0, row=0, padx=0, pady=5, sticky=tk.E)
        lbl_password.grid(column=0, row=1, padx=0, pady=5, sticky=tk.E)

        self.input1.grid(column=1, row=0, padx=10, pady=5, sticky="WE")
        self.input2.grid(column=1, row=1, padx=10, pady=5, sticky="WE")

        btn1.grid(column=0, row=2, padx=5, pady=5, columnspan=2, sticky="N")

        self.lbl_data.grid(row=3, column=0, columnspan=2, sticky="W")

    def _btn1_click(self):
        entrada_user = self.input1.get()
        entrada_password = self.input2.get()
        self.input1.delete(0, tk.END)
        self.input1.insert(0, '')
        self.input2.delete(0, tk.END)
        self.input2.insert(0, '')
        self.lbl_data.config(
            text=f'''
            USUARIO: {entrada_user} \nCONTRASEÑA: {entrada_password}''')
        self.input1.focus()
        if entrada_user == 'admin' and entrada_password == 'admin':
            messagebox.showinfo('info', 'admin logueado correctamente')
        else:
            messagebox.showerror('Error', 'User o password incorrecto')


if __name__ == '__main__':
    # ============= mainloop
    login_ventana = VentanaLogin()

    login_ventana.mainloop()
