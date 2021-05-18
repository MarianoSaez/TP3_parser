import re

class Lexer:
    def __init__(self, string):
        self.token_stream = self.tokenize(string)

    def tokenize(self, string):
        stream = list()
        numbers = re.findall(r'[0-9]+', string)
        string = re.sub(r'[0-9]+', '?', string)
        for i in range(len(string)):
            if re.match(r'\?', string[i]):
                stream.append(Token('i', numbers.pop(0)))
            elif re.match(r'\+', string[i]):
                stream.append(Token('+', string[i]))
            elif re.match(r'\-', string[i]):
                stream.append(Token('-', string[i]))
            elif re.match(r'\(', string[i]):
                stream.append(Token('(', string[i]))
            elif re.match(r'\)', string[i]):
                stream.append(Token(')', string[i]))
            elif re.match(r'\$', string[i]):
                stream.append(Token('$', string[i]))
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
        try:
            self.value = int(value)
        except Exception:
            self.value = value


    def __repr__(self):
        if self.value == "NoTerm":
            return str(f"{self.value}")
        else:
            return str(f"{self.cat}")



if __name__ == '__main__':
    l = Lexer('3+2-2-(1-3)$')
    print(l.get_token_stream())