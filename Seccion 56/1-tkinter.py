
try:

    import tkinter as tk
    from tkinter import ttk
    import sys
    import os

    # metodo para el btn1

    def click_btn1():
        print('haciendo click')
        btnClick.config(text='boton clickado')
        boton2 = ttk.Button(root, text="boton agregado")
        boton2.pack()

    root = tk.Tk()
    # print(type(root)) # <class 'tkinter.Tk'>
    root.geometry('600x400')
    root.title('ventana de programa')

    # INTENTANDO CON UN .ICO
    #root.iconbitmap('C:\CURSOS\python\Seccion 56\\resources\py.ico')

    # ruta relativa - funciona solo en vscode
    # root.iconbitmap('../../resources/py.ico')

    # CODIGO SIN ERRORES - FUNCIONA EJECUTANDO DESDE FUERA
    #img = tk.PhotoImage(file='C:\CURSOS\python\Seccion 56\\resources\py.gif')
    #root.tk.call('wm', 'iconphoto', root._w, img)

    # CREANDO RUTAS RELATIVAS CON SYS Y OS
    root.iconbitmap(os.path.join(sys.path[0], ' \\resources\py.ico'))

    # img = tk.PhotoImage(
    #    file=os.path.join(sys.path[0], " \\resources\py.gif"))
    #root.tk.call('wm', 'iconphoto', root._w, img)

    # haciendo un boton
    btnClick = ttk.Button(root, text="click me outta me", command=click_btn1)
    btnClick.pack()

    root.mainloop()
    # input()
except Exception as e:
    print(e)
    print(type(e))
    # input()
