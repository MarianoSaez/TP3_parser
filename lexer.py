import re

class Lexer:
    def __init__(self, string):
        self.token_stream = self.tokenize(string)

    def tokenize(self, string):
        stream = list()
        for i in string:
            if re.match(r'[0-9]+', i):
                stream.append(Token('i', i))
            elif re.match(r'\+', i):
                stream.append(Token('+', i))
            elif re.match(r'\-', i):
                stream.append(Token('-', i))
            elif re.match(r'\(', i):
                stream.append(Token('(', i))
            elif re.match(r'\)', i):
                stream.append(Token(')', i))
            elif re.match(r'\$', i):
                stream.append(Token('$', i))
            else:
                raise ValueError('Error Lexico')
            
        if stream[len(stream) - 1].cat != "$":
            stream.append(Token("$", "$"))
        return stream

    def get_token_stream(self):
        return self.token_stream

class Token:
    def __init__(self, cat, value):
        self.cat = cat
        self.value = value

    def __repr__(self):
        return str(f"{self.cat} : {self.value}")


if __name__ == '__main__':
    l = Lexer('3+2-2-(1-3)$')
    print(l.get_token_stream())