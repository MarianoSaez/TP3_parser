from lexer import Token


class Node(Token):
    def __init__(self, value, cat, childs=[]):
        super().__init__(cat, value)
        self.childs = childs
    
    def printTree(self, root, level=0):
        print("\t" * level, root.value)
        for child in root.childs:
            self.printTree(child, level + 1)
    #tree = Node(..., children=[Node(...., ...), Node(...,....)] # See end of the article for a bigger structure that is used for the examples in this article.

    def evaluate(self, acc=0):
        if self.cat == "E":
            # Nodo T
            t_node = self.childs[0].evaluate()
            # Nodo N
            n_node = self.childs[1].evaluate(t_node)
            # Retornar el total que acumula el nodo E
            return n_node

        elif self.cat == "N":
            if len(self.childs) == 0:
                return acc
            t_node = self.childs[1].evaluate()
            if self.childs[0].cat == "+":
                n_node = self.childs[2].evaluate(acc + t_node)
            else:
                n_node = self.childs[2].evaluate(acc - t_node)
            return n_node

        elif self.cat == "T":
            if self.childs[0].cat == "i":
                return self.childs[0].value
            else:
                return self.childs[1].evaluate()




if __name__ == "__main__":
    lista2 = [Node(2, 2, []), Node(3, 3, [])]
    lista1 = [Node(1, 1, lista2), Node(4, 4, [])]
    tree = Node(0, 0, lista1)
    tree.printTree(tree)

    n1 = Node(0, 0)
    n2 = Node(1, 0)
    n3 = Node(2, 0)
    n4 = Node(3, 0)
    n5 = Node(4, 0)
    n6 = Node(5, 0)
    n7 = Node(6, 0)

        
    