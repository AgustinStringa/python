import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from time import sleep


class VentanaComponentes(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry('600x400')
        self.title('componentes')

        self._crear_tabs()
        self.mainloop()

    def _mk_tabulador1(self):
        tabulador1 = ttk.Frame(self.ctrl_tabulador)
        self.ctrl_tabulador.add(tabulador1, text='tabulador 1')
        input1 = ttk.Entry(tabulador1, width=30)
        input1.grid(row=0, column=0)
        lbl1 = ttk.Label(tabulador1, text='etiqueta')
        lbl1.grid(row=0, column=1)

    def _mk_tabulador2(self):

        def enviarscrolledtext():
            # 1.0 because => line.column
            value = scroll.get('1.0', tk.END)
            messagebox.showinfo('title', value)

        contenido = 'Titulo del frame tabulador 2'
        tabulador2 = ttk.LabelFrame(self.ctrl_tabulador, text=contenido)

        self.ctrl_tabulador.add(tabulador2, text='tabulador 2')
        boton = ttk.Button(tabulador2, text='enviar',
                           command=enviarscrolledtext)
        boton.grid(row=1, column=0)

        scroll = scrolledtext.ScrolledText(
            tabulador2, width=60, height=10, wrap=tk.WORD)
        scroll.insert('insert', 'Introduce texto aquí')
        # tk.INSERT == 'insert'
        scroll.grid(row=0, column=0)

    def _mk_tabulador3(self):
        tab3 = ttk.Frame(self.ctrl_tabulador)
        self.ctrl_tabulador.add(tab3, text="tab3")

        lista_pares = [x+1 for x in range(10) if x % 2 == 1]
        datalist = ttk.Combobox(tab3, values=lista_pares, takefocus=0)
        datalist.grid(column=0, row=0)

        btn_combo = ttk.Button(tab3, text='ver result',
                               command=lambda: messagebox.showinfo('seleccionaste', f'seleccionaste {datalist.get()}'))

        btn_combo.grid(row=1, column=0)

    def _mk_tabulador4(self):
        tab4 = ttk.Frame(self.ctrl_tabulador)
        self.ctrl_tabulador.add(tab4, text="tab4")
        # creando progressbar
        barra = ttk.Progressbar(tab4, orient='horizontal', length=550)
        barra.grid(row=0, column=0)

        for e in range(0, 101):
            sleep(0.05)
            barra['value'] = e
            barra.update()
        #barra['value'] = 50
        # codigo para manejar la barra de progreso
        # barra.start()
        #root.after('3000', barra.stop)

    def _crear_tabs(self):
        """
        EL CTRL TABULADOR USA PACK DENTRO DEL ROOT
        LOS ELEMENTOS DENTRO DE LOS TABULADORES PUEDEN /Y LLEVAN/ GRID

        SE SEPARA LA CREACION DE TABULADORES EN 2 METODOS QUE RECIBEN EL OBJETO PADRE CONTROL TABULADOR COMO PARAMETRO
        """
        self.ctrl_tabulador = ttk.Notebook(self)
        self.ctrl_tabulador.pack(fill='both')
        # =====TABULADOR 1======
        self._mk_tabulador1()
        # =====TABULADOR 2======
        self._mk_tabulador2()
        # =====TABULADOR 3======
        self._mk_tabulador3()
        # =====TABULADOR 4======
        self._mk_tabulador4()


# FUERA DE LA DECLARACION DE LA CLASE

if __name__ == '__main__':
    mi_ventana = VentanaComponentes()
