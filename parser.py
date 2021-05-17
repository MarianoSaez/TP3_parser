from pila import Pila
from lexer import Lexer
from tree import Node

# Gramatica libre de contexto implementada

# Simbolos terminales y $
terminales = ["i", "+", "-", "(", ")", "$"]

# No terminales
no_terminales = ["E", "N", "T"]

# Formato para impresion
espacios = 30


# Tabla de analisis sintactico
# Por motivos de implementacion se decidio utilizar caracteres
# simples. Por lo tanto E' se define como N. E' = N.
tabla = [["TN", "", "", "TN", "", ""],
         ["", "+TN", "-TN", "", "e", "e"],
         ["i", "", "", "(E)", "", ""]]

class Parser:
    def __init__(self, token_stream, tabla, terminales, no_terminales):
        self.token_stream = token_stream
        self.entrada = self.generate_entrada(token_stream).split()
        self.entrada2 = self.entrada.copy()
        self.pila = Pila()
        self.terminales = terminales
        self.no_terminales = no_terminales
        self.tabla = tabla
        self.parse_tree = Node(None, None)

    def generate_entrada(self, token_stream: list):
        string = ""
        for i in token_stream:
            string += f"{i.cat} "
        return string

    @property
    def pila(self):
        return self._pila

    # Setea el estado inicial de la pila
    @pila.setter
    def pila(self, value):
        self._pila = value
        self.pila.insertar("$")
        self.pila.insertar("E")

    # Obtener fila para entrar en la tabla de analisis
    # sintactico
    def obtener_fila(self, no_terminal):
        for i in range(len(self.no_terminales)):
            if no_terminal == self.no_terminales[i]:
                return i

    # Obtener columna para entrar en la tabla de analisis
    # sintactico
    def obtener_columna(self, simbolo_entrada):
        for i in range(len(self.terminales)):
            if simbolo_entrada == self.terminales[i]:
                return i

    def add_node(self, symbol, parent):
        pass

    def parse(self):                
        print(self.pila.contenido(), " "*(espacios-len(str(self.pila.contenido()))), self.entrada2)
        for simbolo_entrada in self.entrada:
            tope_pila = self.pila.inspeccionar()

            while tope_pila != simbolo_entrada:
                # Determinar celda en la tabla
                columna = self.obtener_columna(simbolo_entrada)
                fila = self.obtener_fila(tope_pila)
                celda = self.tabla[fila][columna]

                # Reemplazar no terminal en el tope de la pila
                # por el cuerpo de la produccion que le 
                # corresponde
                if celda == "":
                    print(f"celda: tabla[{fila}][{columna}] esta vacia")
                    raise ValueError('Error Sintactico')
                else:
                    self.pila.extraer()
                    for i in reversed(celda):
                        if i != "e":
                            self.pila.insertar(i)

                tope_pila = self.pila.inspeccionar()

                print(self.pila.contenido(), " "*(espacios-len(str(self.pila.contenido()))), self.entrada2)

            # En este punto es seguro que los simbolos en el tope de
            # la pila son iguales

            self.entrada2.pop(0)
            self.pila.extraer()
            print(self.pila.contenido(), " "*(espacios-len(str(self.pila.contenido()))), self.entrada2)
        print("Correcto sintacticamente!")

if __name__ == "__main__":
    token_stream = Lexer('3+2-1-(9-8)').get_token_stream()
    parser = Parser(token_stream, tabla, terminales, no_terminales)
    parser.parse()