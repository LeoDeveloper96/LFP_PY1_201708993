import tkinter as tk
import webbrowser
from io import open
from tkinter import *
from tkinter import ttk, filedialog
import os
from Analizador.AnalizadorScript import AnalizadorLexico


class Interfaz:
    analizador = AnalizadorLexico()
    contenido = ""

    def cadenaError(self):
        cadena_temp = ""
        for error in self.analizador.listaErrores:
            cadena_temp += "<tr><td>"+str(error.descripcion)+"</td><td>"+str(error.linea)+"</td><td>"+str(error.columna)+"</td></tr>\n"
        return cadena_temp

    def cadenaTokens(self):
        cadena_temp = ""
        for token in self.analizador.listaTokens:
            cadena_temp += "<tr><td>"+str(token.lexema)+"</td><td>"+str(token.linea)+"</td><td>"+str(token.columna)+"</td></tr>\n"
        return cadena_temp

    def exportarReporteTokens(self):
        dir = os.getcwd()
        archivo = open(dir+"\\Modelos\\ModeloTokens.html", "r")
        modelo = archivo.read()
        archivo.close()
        pagina_resultado = open(dir+"\\Modelos\\tokens.html", "w+")
        indice = modelo.index("</table>")
        cadena = self.cadenaTokens()
        nuevo_contenido = ""
        nuevo_contenido += modelo[0:indice] + cadena[0] + modelo[indice:len(modelo)]
        indice2 = nuevo_contenido.rindex("</table>")
        nuevo_contenido = nuevo_contenido[:indice2] + cadena[1:] + nuevo_contenido[indice2:]
        pagina_resultado.write(nuevo_contenido)
        webbrowser.open_new_tab(dir+"\\Modelos\\tokens.html")

    def exportarReporteErrores(self):
        dir = os.getcwd()
        archivo = open(dir + "\\Modelos\\ModeloErrores.html", "r")
        modelo = archivo.read()
        archivo.close()
        pagina_resultado = open(dir + "\\Modelos\\errores.html", "w+")
        indice = modelo.index("</table>")
        cadena = self.cadenaError()
        nuevo_contenido = ""
        nuevo_contenido += modelo[0:indice] + cadena[0] + modelo[indice:len(modelo)]
        indice2 = nuevo_contenido.rindex("</table>")
        nuevo_contenido = nuevo_contenido[:indice2] + cadena[1:] + nuevo_contenido[indice2:]
        pagina_resultado.write(nuevo_contenido)
        webbrowser.open_new_tab(dir + "\\Modelos\\errores.html")

    def abrirArchivo(self, nombre):
        dir = os.getcwd()
        webbrowser.open_new_tab(dir + "\\Manuales\\"+nombre)

    def opElegida(self, event):
        if self.clicked.get() == "Reporte de tokens":
            self.exportarReporteTokens()
        elif self.clicked.get() == "Reporte de errores":
            self.exportarReporteErrores()
        elif self.clicked.get() == "Manual técnico":
            self.abrirArchivo("Manual técnico.pdf")
        elif self.clicked.get() == "Manual de usuario":
            self.abrirArchivo("Manual de usuario.pdf")

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
        self.clicked = StringVar()
        self.clicked.set(opciones[0])
        self.combo = OptionMenu(root, self.clicked, *opciones, command=self.opElegida)
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
        self.crearFormulario()

    def crearFormulario(self):
        dir = os.getcwd()
        archivo = open(dir + "\\Modelos\\Formulario.html", "r")
        modelo = archivo.read()
        archivo.close()
        pagina_resultado = open(dir + "\\Modelos\\form.html", "w+")
        indice = modelo.index("</form>")
        cadena = "AA"
        # aqui  mi logica para crear el formulario
        #
        nuevo_contenido = ""
        nuevo_contenido += modelo[0:indice] + cadena[0] + modelo[indice:len(modelo)]
        indice2 = nuevo_contenido.rindex("</form>")
        nuevo_contenido = nuevo_contenido[:indice2] + cadena[1:] + nuevo_contenido[indice2:]
        pagina_resultado.write(nuevo_contenido)
        webbrowser.open_new_tab(dir + "\\Modelos\\form.html")

    def cargarArchivo(self):
        ruta = os.getcwd() + "\\Archivos Entrada"
        nombre_archivo = filedialog.askopenfilename(initialdir="ruta", title="Seleccionar un archivo",
                                                    filetypes=(("texto", "*.form"), ("todos", "*.*")))
        try:
            archivo = open(nombre_archivo, "r")
            self.contenido += archivo.read()
            self.texto_analizar.insert('1.0', self.contenido)
        except FileNotFoundError:
            print("archivo no encontrado")
