from lexer import Lexer
from  parser_AST import Parser, terminales, no_terminales, tabla
# from  parser_simple import Parser, terminales, no_terminales, tabla
from calculate import calculate

print("Herramienta de analisis sintactico LL(1) para expresiones aritmeticas")
print("======== Actualmente se solo se soportan operaciones de + ; - ; () ========")
string = input("\nIngrese una cadena para evaluar: ")
token_stream = Lexer(string).get_token_stream()
tree = Parser(token_stream, tabla, terminales, no_terminales).parse()
print(f"\n\nResultado: {tree.evaluate()}\n")
print("===========================================================================")