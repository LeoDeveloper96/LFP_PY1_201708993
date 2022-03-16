from Analizador.TokenScript import Token
from Analizador.ErrorScript import Error
from prettytable import PrettyTable
import re


class AnalizadorLexico:

    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
        self.linea = 1
        self.columna = 1
        self.buffer = ''
        self.estado = "A"
        self.i = 0

    def agregar_token(self, caracter, token, linea, columna):
        self.listaTokens.append(Token(caracter, token, linea, columna))
        self.buffer = ''

    def agregar_error(self, caracter, linea, columna):
        self.listaErrores.append(Error('Caracter ' + caracter + ' no reconocido en el lenguaje.', linea, columna))

    def estadoA(self, caracter):
        if caracter == '[':
            self.buffer += caracter
            self.columna += 1
            self.estado = "B"
        elif caracter == ']':
            self.buffer += caracter
            self.columna += 1
            self.estado = "C"
        elif caracter == '<':
            self.buffer += caracter
            self.columna += 1
            self.estado = "D"
        elif caracter == '>':
            self.buffer += caracter
            self.columna += 1
            self.estado = "E"
        elif caracter == ',':
            self.buffer += caracter
            self.columna += 1
            self.estado = "F"
        elif caracter == ':':
            self.buffer += caracter
            self.columna += 1
            self.estado = "G"
        elif caracter == '~':
            self.buffer += caracter
            self.columna += 1
            self.estado = "H"
        elif caracter == '\"':
            self.buffer += caracter
            self.columna += 1
            self.estado = "I"
        elif caracter == '\'':
            self.buffer += caracter
            self.columna += 1
            self.estado = "M"
        #     palabra reservada
        elif caracter.isalpha():
            self.buffer += caracter
            self.columna += 1
            self.estado = "L"
        elif caracter == '\n':
            self.linea += 1
            self.columna = 1
        elif caracter in ['\t', ' ']:
            self.columna += 1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer, self.linea, self.columna)
            self.buffer = ''
            self.columna += 1

    def analizar(self, cadena):
        self.listaTokens = []
        self.listaErrores = []
        # recorrer caracter por caracter
        self.i = 0
        while self.i < len(cadena):
            if self.estado == "A":
                self.estadoA(cadena[self.i])
            elif self.estado == "B":
                self.estadoB(cadena[self.i])
            elif self.estado == "C":
                self.estadoC(cadena[self.i])
            elif self.estado == "D":
                self.estadoD(cadena[self.i])
            elif self.estado == "E":
                self.estadoE(cadena[self.i])
            elif self.estado == "F":
                self.estadoF(cadena[self.i])
            elif self.estado == "G":
                self.estadoG(cadena[self.i])
            elif self.estado == "H":
                self.estadoH(cadena[self.i])
            elif self.estado == "I":
                self.estadoI(cadena[self.i])
            elif self.estado == "J":
                self.estadoJ(cadena[self.i])
            elif self.estado == "K":
                self.estadoK(cadena[self.i])
            elif self.estado == "L":
                self.estadoL(cadena[self.i])
            elif self.estado == "M":
                self.estadoM(cadena[self.i])
            elif self.estado == "N":
                self.estadoN(cadena[self.i])
            elif self.estado == "O":
                self.estadoO(cadena[self.i])
            self.i += 1
        self.impErrores()
        self.impTokens()

    def estadoB(self, caracter):
        self.agregar_token(self.buffer, 'corchete izquierdo', self.linea, self.columna)
        # El i = -1 indica que regreso al caracter anterior para empezar a leer desde ahi
        self.i -= 1
        self.estado = "A"

    def estadoC(self, caracter):
        self.agregar_token(self.buffer, 'corchete derecho', self.linea, self.columna)
        self.i -= 1
        self.estado = "A"

    def estadoD(self, caracter):
        self.agregar_token(self.buffer, 'menor que', self.linea, self.columna)
        self.i -= 1
        self.estado = "A"

    def estadoE(self, caracter):
        self.agregar_token(self.buffer, 'mayor que', self.linea, self.columna)
        self.i -= 1
        self.estado = "A"

    def estadoF(self, caracter):
        self.agregar_token(self.buffer, 'coma', self.linea, self.columna)
        self.i -= 1
        self.estado = "A"

    def estadoG(self, caracter):
        self.agregar_token(self.buffer, 'dos puntos', self.linea, self.columna)
        self.i -= 1
        self.estado = "A"

    def estadoH(self, caracter):
        if caracter == ">":
            self.buffer += caracter
            self.columna += 1
        else:
            self.agregar_token(self.buffer, 'Símbolo especial', self.linea, self.columna)
            self.estado = "A"
            self.i -= 1

    def estadoI(self, caracter):
        if caracter != "\"":
            self.buffer += caracter
            self.columna += 1
            self.estado = "K"
        else:
            self.estado = "A"
            self.agregar_error(self.buffer, self.linea, self.columna)
            self.i -= 1
            self.buffer = ''

    def estadoJ(self, caracter):
        if caracter != "\"":
            self.buffer += caracter
            self.columna += 1
        else:
            self.buffer += caracter
            self.agregar_token(self.buffer, 'identificador', self.linea, self.columna)
            self.estado = "K"

    def estadoK(self, caracter):
        self.estado = "A"
        self.i -= 1

    def estadoL(self, caracter):
        if caracter.isalpha():
            self.buffer += caracter
            self.columna += 1
        else:
            if re.search("formulario|tipo|valor|fondo|valores|evento",
                         self.buffer.lower()):
                self.agregar_token(self.buffer, 'reservada', self.linea, self.columna)
                self.estado = "A"
                self.i -= 1
            else:
                self.agregar_error(self.buffer, self.linea, self.columna)
                self.estado = "A"
                self.i -= 1
                self.buffer = ''

    def estadoM(self, caracter):
        if caracter != "\'":
            self.buffer += caracter
            self.columna += 1
            self.estado = "N"
        else:
            self.estado = "A"
            self.agregar_error(self.buffer, self.linea, self.columna)
            self.i -= 1
            self.buffer = ''

    def estadoN(self, caracter):
        if caracter != "\'":
            self.buffer += caracter
            self.columna += 1
        else:
            self.buffer += caracter
            self.agregar_token(self.buffer, 'identificador', self.linea, self.columna)
            self.estado = "O"

    def estadoO(self, caracter):
        self.estado = "A"
        self.i -= 1

    # imprimeTokens
    def impTokens(self):
        x = PrettyTable()
        x.field_names = ["Lexema", "Token", "Fila", "Columna"]
        for i in self.listaTokens:
            x.add_row(i.enviarData())
        print(x)

    # imprimeErrores
    def impErrores(self):
        x = PrettyTable()
        x.field_names = ["Descripcion", "Fila", "Columna"]
        if len(self.listaErrores) == 0:
            print('No hay errores')
        else:
            for i in self.listaErrores:
                x.add_row(i.enviarData())
            print(x)
