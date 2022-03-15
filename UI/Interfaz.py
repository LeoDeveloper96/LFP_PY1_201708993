import tkinter as tk
from tkinter import *
from tkinter import ttk
import os


def analizar():
    pass


def cargar():
    pass


def opElegida(event):
    pass


def crearInterfaz():
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

    combo = ttk.Combobox(root, values=opciones)
    combo.current(0)
    combo.bind("<<ComboBoxSelected>>", opElegida)
    combo.pack(pady=10)
    # creo el text area
    texto_analizar = Text(root, width=100, height=40)
    texto_analizar.pack(pady=40)
    # creo los botones
    boton_frame = Frame(root)
    boton_frame.pack()
    boton_cargar = Button(boton_frame, text="Analizar", command=analizar)
    boton_cargar.grid(row=0, column=0)
    boton_cargar = Button(boton_frame, text="Cargar", command=cargar)
    boton_cargar.grid(row=0, column=1, padx=10)
    root.mainloop()

