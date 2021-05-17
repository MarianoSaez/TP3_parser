class Pila:
    def __init__(self):
        self.items = []
    
    def estaVacia(self):  # verificar si la pila está vacía
        return self.items == []
    
    def insertar(self, item):  # inserta elemento en la pila (cima)
        self.items.append(item)
   
    def extraer(self):  # extrae elemento de la pila (cima)
        return self.items.pop()
   
    def inspeccionar(self):  # devuelve el elemento de la cima de la pila
        return self.items[len(self.items)-1]
    
    def tamano(self): #devuelve el tamaño de la pila
        return len(self.items)

    def contenido(self): #devuelve el tamaño de la pila
        return (self.items)
