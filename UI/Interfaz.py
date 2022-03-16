import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog
import os
from Analizador.AnalizadorScript import AnalizadorLexico


class Interfaz:
    analizador = AnalizadorLexico()
    contenido = ""

    def opElegida(self):
        if self.combo.get() == "Reporte de tokens":
            self.reportetTokens()
        elif self.combo.get() == "Reporte de errores":
            self.reporteErrores()

    def reportetTokens(self):
        pass

    def reporteErrores(self):
        pass

    def crearInterfaz(self):
        root = tk.Tk()
        root.geometry("1200x800")
        root.configure(background='#263D42')
        # creo el combo box del menu de reportes
        opciones = ["Reportes",
                    "Reporte de tokens",
                    "Reporte de errores",
                    "Manual de usuario",
                    "Manual técnico",
                    ]

        self.combo = ttk.Combobox(root, values=opciones)
        self.combo.current(0)
        self.combo.bind("<<ComboBoxSelected>>", self.opElegida)
        self.combo.pack(pady=10)
        # creo el text area
        self.texto_analizar = Text(root, width=100, height=40)
        self.texto_analizar.pack(pady=40)

        # creo los botones
        boton_frame = Frame(root)
        boton_frame.pack()
        self.boton_cargar = Button(boton_frame, text="Analizar", command=self.analizarClick)
        self.boton_cargar.grid(row=0, column=0)
        self.boton_cargar = Button(boton_frame, text="Cargar", command=self.cargarArchivo)
        self.boton_cargar.grid(row=0, column=1, padx=10)
        root.mainloop()

    def analizarClick(self):
        self.analizador.analizar(self.contenido)

    def cargarArchivo(self):
        nombre_archivo = filedialog.askopenfilename(initialdir="/", title="Seleccionar un archivo",
                                                    filetypes=(("texto", "*.form"), ("todos", "*.*")))
        try:
            archivo = open(nombre_archivo, "r")
            self.contenido += archivo.read()
            self.texto_analizar.insert('1.0', self.contenido)
        except FileNotFoundError:
            print("archivo no encontrado")
