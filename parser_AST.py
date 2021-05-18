from pila import Pila
from lexer import Lexer
from tree import Node

# Gramatica libre de contexto implementada
# E ::= TN
# N ::= +TN | -TN | e
# T ::= i | (E)

# Simbolos terminales y $
terminales = ["i", "+", "-", "(", ")", "$"]

# No terminales
no_terminales = ["E", "N", "T"]

# Formato para impresion
espacios = 60

# Tabla de analisis sintactico
# Por motivos de implementacion se decidio utilizar caracteres
# simples. Por lo tanto E' se define como N. E' = N.
tabla = [["TN", "", "", "TN", "", ""],
         ["", "+TN", "-TN", "", "e", "e"],
         ["i", "", "", "(E)", "", ""]]

class Parser:
    def __init__(self, token_stream, tabla, terminales, no_terminales):
        self.token_stream = token_stream
        self.entrada = token_stream
        self.entrada2 = self.generate_entrada(token_stream).split()
        self.pila = Pila()
        self.terminales = terminales
        self.no_terminales = no_terminales
        self.tabla = tabla
        self.parse_tree = Node("E", "NoTerm")

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
        self.pila.insertar(Node("$", "$"))
        self.pila.insertar(Node("NoTerm", "E"))

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

    def parse(self):
        root = None
        print(self.pila.contenido(), " "*(espacios-len(str(self.pila.contenido()))), self.entrada2)
        for simbolo_entrada in self.entrada:
            tope_pila = self.pila.inspeccionar()

            while tope_pila.cat != simbolo_entrada.cat:

                # Determinar celda en la tabla
                columna = self.obtener_columna(simbolo_entrada.cat)
                fila = self.obtener_fila(tope_pila.cat)
                celda = self.tabla[fila][columna]

                # Reemplazar no terminal en el tope de la pila
                # por el cuerpo de la produccion que le
                # corresponde
                if celda == "":
                    print(f"celda: tabla[{fila}][{columna}] esta vacia")
                    raise ValueError('Error Sintactico')
                else:
                    p = self.pila.extraer()
                    children = list()
                    if p.cat == "E" and root == None:
                        root = p

                    for i in celda:
                        if i != "e":
                            if i in self.terminales:
                                new_node = Node(simbolo_entrada.value, i)
                            else:
                                new_node = Node("NoTerm", i)
                            children.append(new_node)

                    p.childs = children

                    for i in reversed(children):
                        self.pila.insertar(i)
                
                tope_pila = self.pila.inspeccionar()


                print(self.pila.contenido(), " "*(espacios-len(str(self.pila.contenido()))), self.entrada2)
            if tope_pila.cat == "$" and simbolo_entrada.cat == "$":
                break


            # En este punto es seguro que los simbolos en el tope de
            # la pila son iguales

            self.entrada2.pop(0)
            self.pila.extraer()
            # print(self.pila.contenido(), " "*(espacios-len(str(self.pila.contenido()))), self.entrada2)

        return root

if __name__ == "__main__":
    token_stream = Lexer('10+2-(3-2)').get_token_stream()
    parser = Parser(token_stream, tabla, terminales, no_terminales)
    root = parser.parse()
    print(root.evaluate())
