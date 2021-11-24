import tkinter as tk
from tkinter import Widget, ttk, messagebox, scrolledtext

root = tk.Tk()
root.geometry('600x400')
root.title('componentes')


def mk_tabulador1(ctrl_tabulador):
    tabulador1 = ttk.Frame(ctrl_tabulador)
    ctrl_tabulador.add(tabulador1, text='tabulador 1')
    input1 = ttk.Entry(tabulador1, width=30)
    input1.grid(row=0, column=0)
    lbl1 = ttk.Label(tabulador1, text='etiqueta')
    lbl1.grid(row=0, column=1)


def mk_tabulador2(ctrl_tabulador):

    def enviarscrolledtext():
        # 1.0 because => line.column
        value = scroll.get('1.0', tk.END)
        messagebox.showinfo('title', value)

    contenido = 'Titulo del frame tabulador 2'
    tabulador2 = ttk.LabelFrame(ctrl_tabulador, text=contenido)

    ctrl_tabulador.add(tabulador2, text='tabulador 2')
    boton = ttk.Button(tabulador2, text='enviar', command=enviarscrolledtext)
    boton.grid(row=1, column=0)

    scroll = scrolledtext.ScrolledText(
        tabulador2, width=60, height=10, wrap=tk.WORD)
    scroll.insert('insert', 'Introduce texto aquí')
    # tk.INSERT == 'insert'
    scroll.grid(row=0, column=0)


def mk_tabulador3(ctrl_tabuldor):
    tab3 = ttk.Frame(ctrl_tabuldor)
    ctrl_tabuldor.add(tab3, text="tab3")

    lista_pares = [x+1 for x in range(10) if x % 2 == 1]
    datalist = ttk.Combobox(tab3, values=lista_pares, takefocus=0)
    datalist.grid(column=0, row=0)

    btn_combo = ttk.Button(tab3, text='ver result',
                           command=lambda: messagebox.showinfo('seleccionaste', f'seleccionaste {datalist.get()}'))

    btn_combo.grid(row=1, column=0)


def crear_tabs():
    """
    EL CTRL TABULADOR USA PACK DENTRO DEL ROOT
    LOS ELEMENTOS DENTRO DE LOS TABULADORES PUEDEN /Y LLEVAN/ GRID

    SE SEPARA LA CREACION DE TABULADORES EN 2 METODOS QUE RECIBEN EL OBJETO PADRE CONTROL TABULADOR COMO PARAMETRO
    """
    ctrl_tabulador = ttk.Notebook(root)
    ctrl_tabulador.pack(fill='both')
    # =====TABULADOR 1======
    mk_tabulador1(ctrl_tabulador)
    # =====TABULADOR 2======
    mk_tabulador2(ctrl_tabulador)
    # =====TABULADOR 3======
    mk_tabulador3(ctrl_tabulador)


# comenzando procesos
crear_tabs()
root.mainloop()
