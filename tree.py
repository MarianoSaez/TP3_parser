from lexer import Token


class Node(Token):
    def __init__(self, value, cat, childs=[]):
        super().__init__(cat, value)
        self.childs = childs


    
        
    